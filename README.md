# EPG-Australia

Australia IPTV M3U + XMLTV project.

## TiviMate URLs

M3U:
https://raw.githubusercontent.com/SPS8007/EPG-Australia/main/australia.m3u

EPG:
https://raw.githubusercontent.com/SPS8007/EPG-Australia/main/australia.xml

The EPG XML is refreshed automatically each day from EPG.pw Australia by GitHub Actions.

## Mapping rules

The AU mapping uses Channel DNA rules. Australian Fox Sports channel numbers are treated as authoritative where applicable:

- 500 = FOX Sports News
- 501 = FOX Cricket
- 502 = FOX League
- 503 = FOX Sports 503
- 504 = FOX Footy
- 505 = FOX Sports 505
- 506 = FOX Sports 506
- 507 = FOX Sports More / 507

ESPN Play PPV/event feeds are retained as event streams and are not incorrectly mapped to the permanent ESPN AU channel.

## Daily update

GitHub Actions runs daily at 02:15 UTC and can also be started manually from Actions > Update Australia EPG > Run workflow.
