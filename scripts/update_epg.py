import gzip, io, os, urllib.request

URL = "https://epg.pw/xmltv/epg_AU.xml"
OUT = "australia.xml"

req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=60) as r:
    data = r.read()

# Handle either plain XML or gzip content transparently.
if data[:2] == b"\x1f\x8b":
    data = gzip.decompress(data)

if not data.lstrip().startswith(b"<"):
    raise RuntimeError("EPG source did not return XML")

tmp = OUT + ".tmp"
with open(tmp, "wb") as f:
    f.write(data)
os.replace(tmp, OUT)
print(f"Wrote {OUT}: {len(data):,} bytes")
