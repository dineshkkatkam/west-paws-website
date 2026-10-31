WEST PAWS — STATIC WEBSITE
==========================

Open index.html in any browser to preview. Everything is plain HTML/CSS/JS and works on any static host.

PAGES
  index.html     Home: about, services teaser, doctor, featured cases, reviews, camp, map
  about.html     Dr. K. Rajavardan: credentials, experience, surgical expertise
  services.html  OP by species and all 14 services/facilities
  reviews.html   Google reviews, filterable library of 41 Instagram cases, Instagram embeds
  visit.html     Directions by road, route map, Google Map, contact details, hours
  camp.html      Landing page for health camps (reuse it for Meta ad campaigns)

EDITING CONTENT
  All text, reviews, cases, hours and phone numbers are in build/content.py.
  After editing, run:  python3 build/build.py   (this regenerates the .html files)

BEFORE GOING LIVE
  1. Buy a domain and set SITE_URL in build/build.py (currently https://www.westpaws.in as a placeholder), then rebuild.
  2. Host free on Netlify (drag and drop this folder at app.netlify.com/drop), Cloudflare Pages or GitHub Pages.
  3. Meta Pixel / Google Analytics: paste your IDs into the commented block near the top of head() in build/build.py, uncomment, rebuild.
     Call / WhatsApp / Directions clicks are then tracked automatically as "Contact" conversions.
  4. For ads, link to a specific page with UTM tags, e.g.
     https://yourdomain/camp.html?utm_source=meta&utm_medium=paid&utm_campaign=rabies_camp
  5. Add real photos (doctor portrait, clinic front, OT) to /img and swap them in where useful.
  6. Update GOOGLE_COUNT in content.py every few months.
