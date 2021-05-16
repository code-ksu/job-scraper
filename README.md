# job-scraper

## stepstone

### job offer page
URL
```
https://www.stepstone.de/stellenangebote--Agiler-IT-Berater-fuer-das-Data-Management-Infrastructure-Team-w-m-d-Frankfurt-am-Main-Deutsche-Bahn-AG--6966789-inline.html?suid=3001cfcc-3179-4c33-a15d-8d88c71a4361&rltr=1_1_25_mb_m_0_0_0
```
- static: https://www.stepstone.de/stellenangebote--
- dynamic SSO component = title + location + employer with removed special chars
- ID: --6966789
- static: -inline.html
- tracking: ?suid=3001cfcc-3179-4c33-a15d-8d88c71a4361&rltr=1_1_25_mb_m_0_0_0

Note the SSO part when requesting and will be filled by the stepstone backend! This allows us to collect titles of already offline offers.