# EPG-Australia

Stable-ID Australian IPTV playlist and XMLTV EPG.

TiviMate:
- M3U: https://raw.githubusercontent.com/SPS8007/EPG-Australia/main/australia.m3u
- EPG: https://raw.githubusercontent.com/SPS8007/EPG-Australia/main/australia.xml

The GitHub Action downloads the current EPG.pw Australia XMLTV feed daily and transforms its changing source channel IDs into stable AU IDs used by the M3U.

Special rule:
- ESPN PLAY / PPV event feeds are not mapped to the permanent ESPN AU EPG.
- AU Fox Sports channels use the established 500-507 channel-number mapping.
