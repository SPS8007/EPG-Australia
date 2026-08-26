import csv, gzip, io, urllib.request, xml.etree.ElementTree as ET

SOURCE = "https://epg.pw/xmltv/epg_AU.xml"
MAP = "epg-map.csv"
OUT = "australia.xml"

# stable_id -> source EPG ID and canonical name
rows=[]
with open(MAP,encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))

source_to_stable={}
stable_to_name={}
for r in rows:
    sid=r["Stable ID"].strip()
    eid=r["EPG.pw ID"].strip()
    if sid and eid:
        source_to_stable.setdefault(eid,[]).append(sid)
        stable_to_name[sid]=r["Canonical Name"].strip()

req=urllib.request.Request(SOURCE,headers={"User-Agent":"Mozilla/5.0"})
with urllib.request.urlopen(req,timeout=90) as r:
    data=r.read()
if data[:2] == b"\x1f\x8b":
    data=gzip.decompress(data)

root=ET.fromstring(data)

# Replace/duplicate channel definitions.
newroot=ET.Element(root.tag, root.attrib)
mapped_channels=0
mapped_programmes=0

# Preserve XMLTV metadata elements other than channel/programme.
for child in list(root):
    if child.tag not in ("channel","programme"):
        newroot.append(child)

for ch in root.findall("channel"):
    src_id=ch.get("id","")
    targets=source_to_stable.get(src_id,[])
    if not targets:
        continue
    for sid in targets:
        nch=ET.Element("channel", {"id":sid})
        # Use our canonical display name.
        dn=ET.SubElement(nch,"display-name",{"lang":"en"})
        dn.text=stable_to_name.get(sid,"")
        # Preserve logo/icon if supplied.
        icon=ch.find("icon")
        if icon is not None:
            nch.append(ET.fromstring(ET.tostring(icon,encoding="unicode")))
        newroot.append(nch)
        mapped_channels+=1

for p in root.findall("programme"):
    src_id=p.get("channel","")
    targets=source_to_stable.get(src_id,[])
    for sid in targets:
        np=ET.fromstring(ET.tostring(p,encoding="unicode"))
        np.set("channel",sid)
        newroot.append(np)
        mapped_programmes+=1

ET.ElementTree(newroot).write(OUT,encoding="utf-8",xml_declaration=True)

if mapped_channels == 0 or mapped_programmes == 0:
    raise RuntimeError(f"Invalid mapping result: channels={mapped_channels}, programmes={mapped_programmes}")
print(f"Created {OUT}: {mapped_channels} channels, {mapped_programmes} programmes")
