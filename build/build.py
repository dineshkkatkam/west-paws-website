#!/usr/bin/env python3
"""Builds the static West Paws site into ../ (index.html, about.html, ...).
Edit content.py for text/data, then run:  python3 build/build.py"""
import os, html, datetime
from content import *

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://www.westpaws.in"  # TODO: replace with the real domain once purchased
E = html.escape

def ic(name):
    p = {
     "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
     "wa": '<path d="M3 21l1.65-3.8A9 9 0 1 1 8 20.3L3 21"/><path d="M9 10a.5.5 0 0 0 1 0V9a.5.5 0 0 0-1 0v1a5 5 0 0 0 5 5h1a.5.5 0 0 0 0-1h-1a.5.5 0 0 0 0 1"/>',
     "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
     "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
     "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/>',
     "fb": '<path d="M15 3h-2.5A3.5 3.5 0 0 0 9 6.5V10H6v4h3v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h2z"/>',
     "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
     "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
     "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
     "steth": '<path d="M6 3v6a4 4 0 0 0 8 0V3"/><path d="M10 13v2a5 5 0 0 0 10 0v-2"/><circle cx="20" cy="11" r="2"/>',
     "syringe": '<path d="m18 2 4 4M17 7l-9.5 9.5L4 17l.5-3.5L14 4zM2 22l5-5M11 7l6 6M9 9l2 2"/>',
     "pill": '<rect x="2.5" y="8.5" width="19" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="m8.5 8.5 7 7"/>',
     "scalpel": '<path d="M3 21 14 10l3 3L8 21z"/><path d="m14 10 6-6a2 2 0 0 1 0 3l-3 6"/>',
     "bone": '<path d="M7 10a2.5 2.5 0 1 1-2-4 2.5 2.5 0 1 1 4 2l6 6a2.5 2.5 0 1 1 2 4 2.5 2.5 0 1 1-4-2z"/>',
     "xray": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 6v12M8 8h8M7 11h10M8 14h8"/>',
     "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
     "heart": '<path d="M3 12h4l2-4 3 8 2-4h7"/>',
     "wave": '<path d="M3 12c2-6 4-6 6 0s4 6 6 0 4-6 6 0"/>',
     "bed": '<path d="M3 18V8M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/>',
     "tooth": '<path d="M7 3c-2 0-4 2-4 5 0 4 2 5 2.5 9 .3 2.5 1.5 4 2.5 4s1.5-2 2-4.5c.3-1 .7-1.5 2-1.5s1.7.5 2 1.5c.5 2.5 1 4.5 2 4.5s2.2-1.5 2.5-4C19 13 21 12 21 8c0-3-2-5-4-5-2 0-3 1-5 1S9 3 7 3z"/>',
     "baby": '<circle cx="12" cy="8" r="4"/><path d="M5 21a7 7 0 0 1 14 0"/>',
     "bath": '<path d="M4 12h16v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM6 12V5a2 2 0 0 1 4 0"/>',
     "bag": '<path d="M5 8h14l-1 13H6z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
     "worm": '<path d="M4 16c3 0 3-4 6-4s3 4 6 4 3-4 4-4"/><circle cx="20" cy="12" r="1"/>',
     "paw": '<circle cx="6" cy="10" r="2"/><circle cx="10" cy="6" r="2"/><circle cx="14" cy="6" r="2"/><circle cx="18" cy="10" r="2"/><path d="M8 17c0-3 2-5 4-5s4 2 4 5a2.5 2.5 0 0 1-4 2 2.5 2.5 0 0 1-4-2z"/>',
     "dog": '<path d="M5 10 3 6l4 1 2-2h5l2 2 4-1-2 4v5a5 5 0 0 1-5 5h-4a5 5 0 0 1-5-5z"/><circle cx="10" cy="11" r=".6" fill="currentColor"/><circle cx="14" cy="11" r=".6" fill="currentColor"/><path d="M11 15h2"/>',
     "cat": '<path d="M5 3l3 4h8l3-4v9a7 7 0 0 1-14 0z"/><circle cx="10" cy="11" r=".6" fill="currentColor"/><circle cx="14" cy="11" r=".6" fill="currentColor"/><path d="M12 14v1M9 15l-4 1M15 15l4 1"/>',
     "bird": '<path d="M16 7h.01M3 20l7-3c5-2 8-5 8-10a3 3 0 0 0-6 0c0 3-2 5-5 6l-4 1z"/><path d="m18 7 3 1-3 1"/>',
     "rabbit": '<path d="M9 9C8 5 8 2 9.5 2S12 5 12 9M15 9c1-4 1-7-.5-7S12 5 12 9"/><circle cx="12" cy="15" r="6"/>',
     "cow": '<path d="M5 6 2 4M19 6l3-2"/><path d="M6 6h12v7a6 6 0 0 1-12 0z"/><ellipse cx="12" cy="16" rx="4" ry="2.5"/>',
     "award": '<circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/>',
     "book": '<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3"/><path d="M20 4v14h-7"/>',
     "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
     "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
     "nav": '<path d="m3 11 18-8-8 18-2-8z"/>',
     "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
     "ext": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    }[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

NAV = [("index.html","Home"),("about.html","Dr. Rajavardan"),("services.html","Services"),("reviews.html","Reviews & Cases"),("visit.html","Visit & Contact")]

def head(title, desc, page):
    url = SITE_URL + "/" + ("" if page == "index.html" else page)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/img/og-image.jpg">
<meta name="theme-color" content="#164834">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<!-- ===== MARKETING TAGS =====
  1) Meta Pixel: replace YOUR_PIXEL_ID and uncomment.
  <script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','YOUR_PIXEL_ID');fbq('track','PageView');</script>
  2) Google Analytics 4: replace G-XXXXXXX and uncomment.
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-XXXXXXX');</script>
  Call / WhatsApp clicks are already reported as "Contact" events (see js/main.js) once either tag is enabled.
-->
{SCHEMA}
</head>
<body>
<div class="topbar"><div class="wrap">
  <span class="hide-sm">Small Animal Surgical Centre · Manikonda, Hyderabad</span>
  <span><span class="hide-sm">Mon–Sat 10 AM–9 PM · Sun 10 AM–2 PM · </span>Call <a href="tel:{PHONE_TEL}" data-track="call">{PHONE_DISPLAY}</a></span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="West Paws home">
    <img src="img/logo-green.png" alt="West Paws logo" width="52" height="52">
    <span class="brand-text"><span class="brand-name">WEST PAWS</span><span class="brand-sub">Small Animal Surgical Centre</span></span>
  </a>
  <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="nav" aria-label="Main">
    {''.join(f'<a href="{h}"{" class=\"active\"" if h==page else ""}>{t}</a>' for h,t in NAV)}
    <a class="btn btn-primary" href="tel:{PHONE_TEL}" data-track="call">{ic("phone")} Book a visit</a>
  </nav>
</div></header>
<main>
'''

def footer():
    hrs = "".join(f"<li>{d[:3]}: {h}</li>" for d, h in [("Mon–Sat", HOURS[0][1]), ("Sunday", HOURS[6][1])])
    yr = datetime.date.today().year
    return f'''</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <img src="img/logo-white.png" alt="" width="84" height="84">
      <p>West Paws Small Animal Surgical Centre, led by consultant veterinary surgeon Dr. K. Rajavardan. Surgery, diagnostics and everyday care for pets in Manikonda, Narsingi and Puppalaguda.</p>
      <div class="socials">
        <a href="{INSTA}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a>
        <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp" data-track="whatsapp">{ic("wa")}</a>
        <a href="{GMAPS}" target="_blank" rel="noopener" aria-label="Google Maps">{ic("pin")}</a>
      </div>
    </div>
    <div><h4>Explore</h4><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}<li><a href="camp.html">Pet health camps</a></li></ul></div>
    <div><h4>Hours</h4><ul><li>Mon–Sat: {HOURS[0][1]}</li><li>Sunday: {HOURS[6][1]}</li></ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="tel:{PHONE_TEL}" data-track="call">{PHONE_DISPLAY}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{'<br>'.join(E(l) for l in ADDRESS_LINES)}</li>
    </ul></div>
  </div>
  <div class="wrap foot-bottom"><span>© {yr} West Paws Pet Clinic · Dr. K. Rajavardan, TSVC Reg. No. 01409/2018</span><span>Reviews and case summaries are from our Google listing and Instagram.</span></div>
</footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-track="whatsapp">{ic("wa")}</a>
<div class="mobile-bar"><a href="tel:{PHONE_TEL}" data-track="call">{ic("phone")} Call now</a><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">{ic("wa")} WhatsApp</a></div>
<script src="js/main.js"></script>
</body>
</html>
'''

SCHEMA = f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"VeterinaryCare","name":"West Paws Pet Clinic (Dr. K. Rajavardan)","alternateName":"West Paws Small Animal Surgical Centre",
"url":"{SITE_URL}","telephone":"{PHONE_TEL}","email":"{EMAIL}","image":"{SITE_URL}/img/og-image.jpg",
"address":{{"@type":"PostalAddress","streetAddress":"H. No. 115, Narsingi - Puppalaguda Main Road, near Geethanjali Vedika School, Alkapur Township, Puppalaguda, Manikonda","addressLocality":"Hyderabad","addressRegion":"Telangana","postalCode":"500089","addressCountry":"IN"}},
"geo":{{"@type":"GeoCoordinates","latitude":{LAT},"longitude":{LNG}}},"hasMap":"{GMAPS}","sameAs":["{INSTA}"],
"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"10:00","closes":"21:00"}},{{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"14:00"}}]}}
</script>'''

def cta_band(title="Is your pet unwell, or due for a check-up?", sub="Call or WhatsApp us to book. Walk-ins are welcome during clinic hours."):
    return f'''<section class="section tight"><div class="wrap"><div class="cta-band">
  <div><h2>{title}</h2><p style="margin:0">{sub}</p></div>
  <div class="btn-row"><a class="btn btn-yellow" href="tel:{PHONE_TEL}" data-track="call">{ic("phone")} {PHONE_DISPLAY}</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">{ic("wa")} WhatsApp</a></div>
</div></div></section>'''

def stars(n=5): return '<span class="stars" aria-label="5 out of 5 stars">' + "★"*n + "</span>"

def review_card(r):
    initials = "".join(w[0] for w in r["name"].split()[:2])
    return f'''<article class="review"><span class="tag">{E(r["tag"])}</span>{stars()}
<blockquote>“{E(r["text"])}”</blockquote>
<div class="who"><span class="avatar">{initials}</span><span>{E(r["name"])}<small>Google review · {r["when"]}</small></span></div></article>'''

def case_card(c):
    date, cat, title, patient, text, outcome, path = c
    return f'''<article class="case" data-cat="{cat}"><div class="meta"><span class="cat">{CASE_CATS[cat]}</span><span>{date}</span></div>
<h3>{E(title)}</h3><p><b>{E(patient)}.</b> {E(text)}</p><div class="outcome"><b>Outcome:</b> {E(outcome)}</div>
<a class="more" href="https://www.instagram.com/westpaws_petclinic/{path}/" target="_blank" rel="noopener">View on Instagram ↗</a></article>'''

SERVICES = [
    ("steth","General health check-ups","Head-to-tail examinations, weight and diet advice, and senior pet screening."),
    ("syringe","Vaccination","Puppy and kitten schedules, annual boosters and anti-rabies vaccination, with digital reminders."),
    ("worm","Deworming & parasite control","Deworming plans and tick and flea prevention suited to your pet's age and lifestyle."),
    ("scalpel","General & soft tissue surgery","Spay and neuter, tumour removal, hernia repair, pyometra, C-section and wound reconstruction."),
    ("bone","Orthopaedic surgery","Fracture fixation with pins, wires and cross-pinning, FHO for hip dysplasia, and amputations."),
    ("xray","Digital X-ray","In-house digital radiography for fractures, foreign bodies, the chest and the abdomen."),
    ("wave","Ultrasound","Abdominal and pregnancy ultrasound for fast, non-invasive diagnosis."),
    ("heart","ECG","Heart rhythm checks, including pre-anaesthetic screening for older pets."),
    ("drop","Blood & biochemical tests","Complete blood count and organ-function panels to support diagnosis and safer anaesthesia."),
    ("bed","Critical care unit","Monitoring, IV fluids and oxygen support for emergencies, after surgery and for very sick pets."),
    ("tooth","Dental care","Scaling, polishing and extractions to treat bad breath and gum disease."),
    ("baby","Pregnancy diagnosis","Pregnancy confirmation and monitoring by ultrasound, plus whelping advice."),
    ("bath","Grooming & bathing","Medicated and regular baths, nail trims and ear cleaning."),
    ("bag","Pet food & accessories","Prescription and everyday diets, leashes, cones, beds and other essentials in store."),
]
SPECIES = [
    ("dog","Dogs","Puppies to seniors, toy breeds to giants."),
    ("cat","Cats","Gentle, low-stress handling for cats and kittens."),
    ("bird","Birds","Parrots, budgies, lovebirds and other pet birds."),
    ("rabbit","Rabbits & small pets","Rabbits, guinea pigs, hamsters and other small companions."),
    ("cow","Other animals","Calves, goats and other animals. Please call before you visit."),
]

def page_index():
    n_cases = len(CASES)
    feat = [CASES[i] for i in (2, 9, 17)]
    svc = SERVICES[:3] + SERVICES[3:5] + [SERVICES[5]]
    return head("West Paws Pet Clinic | Vet & Pet Surgeon in Manikonda, Narsingi, Hyderabad",
                "West Paws Small Animal Surgical Centre by Dr. K. Rajavardan: vet consultations, vaccination, digital X-ray, ultrasound and orthopaedic and soft tissue surgery near Narsingi and Puppalaguda, Manikonda, Hyderabad.", "index.html") + f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Pet clinic & surgical centre · Manikonda, Hyderabad</span>
    <h1>Expert surgery and <em>everyday care</em> for the pets you love.</h1>
    <p class="lead">West Paws is led by Dr. K. Rajavardan, a consultant soft tissue and orthopaedic veterinary surgeon who was formerly an Assistant Professor of Surgery. Check-ups, vaccinations, digital X-ray, ultrasound and complex surgery are all under one roof on Narsingi–Puppalaguda Road.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="tel:{PHONE_TEL}" data-track="call">{ic("phone")} Call {PHONE_DISPLAY}</a>
      <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">{ic("wa")} Book on WhatsApp</a>
    </div>
    <div class="hero-badges">
      <span class="chip">{ic("scalpel")} Orthopaedic & soft tissue surgery</span>
      <span class="chip">{ic("xray")} Digital X-ray & ultrasound</span>
      <span class="chip">{ic("bed")} Critical care unit</span>
    </div>
  </div>
  <aside class="hero-card">
    <img class="logo" src="img/logo-white.png" alt="" width="150" height="150">
    <div class="rating"><span class="big">{GOOGLE_RATING}</span><span>{stars()}<br><small>{GOOGLE_COUNT} Google reviews</small></span></div>
    <ul>
      <li>{ic("check")} Consultant surgeon who has also taught surgery at a veterinary college</li>
      <li>{ic("check")} Dogs, cats, birds, rabbits and more</li>
      <li>{ic("check")} Open 7 days: Mon–Sat 10 AM–9 PM, Sun 10 AM–2 PM</li>
    </ul>
  </aside>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="stats">
    <div class="stat"><b>{GOOGLE_RATING}★</b><span>Average from {GOOGLE_COUNT} Google reviews</span></div>
    <div class="stat"><b>{n_cases}+</b><span>Surgical cases documented on Instagram</span></div>
    <div class="stat"><b>14</b><span>Services under one roof</span></div>
    <div class="stat"><b>Since 2025</b><span>Caring for pets in Manikonda</span></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">About West Paws</span><h2>A surgical centre that also handles everyday pet care</h2>
  <p class="lead">West Paws opened in February 2025 on Narsingi–Puppalaguda Main Road. Most clinics refer complex cases elsewhere. Here a specialist surgeon handles diagnosis, surgery and recovery in one place: an equipped operation theatre, in-house imaging and lab tests, and a critical care unit.</p></div>
  <div class="grid g3">
    {''.join(f'<div class="card feature"><div class="icon">{ic(i)}</div><h3>{t}</h3><p class="muted">{d}</p></div>' for i,t,d in svc)}
  </div>
  <p style="margin-top:28px"><a class="btn btn-ghost" href="services.html">See all 14 services {ic("arrow")}</a></p>
</div></section>

<section class="section alt"><div class="wrap split">
  <div>
    <span class="eyebrow">Meet the doctor</span>
    <h2>Dr. K. Rajavardan</h2>
    <p class="lead">M.V.Sc in Veterinary Surgery & Radiology. He was formerly Assistant Professor of Surgery at the Teaching Veterinary Hospital, C.V.Sc. Korutla, and now works as a consultant soft tissue and orthopaedic surgeon.</p>
    <p>Pet parents mention the same things in their reviews: he takes time to explain, answers the phone when you are worried, and costs are fair.</p>
    <a class="btn btn-primary" href="about.html">Credentials & experience {ic("arrow")}</a>
  </div>
  <div class="doc-card">
    <div class="monogram">KR</div>
    <h3>Consultant Veterinary Surgeon</h3>
    <ul class="creds">
      <li>{ic("award")} <span>B.V.Sc & A.H. (SVVU)</span></li>
      <li>{ic("book")} <span>M.V.Sc, Veterinary Surgery & Radiology (PVNRTVU)</span></li>
      <li>{ic("scalpel")} <span>Former Asst. Professor of Surgery, TVH, C.V.Sc. Korutla</span></li>
      <li>{ic("shield")} <span>TSVC Reg. No. 01409/2018</span></li>
    </ul>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Recent surgical cases</span><h2>Recent cases from the operation theatre</h2>
  <p class="lead">Dr. Rajavardan posts real cases from the clinic on Instagram. Here are three recent ones.</p></div>
  <div class="grid g3">{''.join(case_card(c) for c in feat)}</div>
  <p style="margin-top:28px"><a class="btn btn-ghost" href="reviews.html#cases">Browse all {n_cases} cases {ic("arrow")}</a></p>
</div></section>

<section class="section alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">What pet parents say</span><h2>Rated {GOOGLE_RATING} on Google by {GOOGLE_COUNT} pet parents</h2></div>
  <div class="grid g3">{''.join(review_card(r) for r in REVIEWS[:3])}</div>
  <p style="margin-top:28px" class="btn-row"><a class="btn btn-ghost" href="reviews.html">Read more reviews {ic("arrow")}</a><a class="btn btn-ghost" href="{GMAPS}" target="_blank" rel="noopener">See all on Google {ic("ext")}</a></p>
</div></section>

<section class="section"><div class="wrap camp">
  <img src="img/rabies-camp-2026.jpg" alt="Free Rabies Camp poster held by West Paws on World Rabies Day, 28 September" loading="lazy" width="1024" height="1536">
  <div>
    <span class="eyebrow">Community camps</span>
    <h2>Free Rabies Camp for World Rabies Day</h2>
    <p class="lead">On 28 September we ran a free camp for pets in the neighbourhood. It offered anti-rabies vaccination, deworming, nail trims and ear cleaning, from 10 AM to 8 PM.</p>
    <p>We run camps like this through the year. Message us on WhatsApp to hear about the next one.</p>
    <div class="btn-row"><a class="btn btn-primary" href="camp.html">About our camps {ic("arrow")}</a><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">{ic("wa")} Notify me</a></div>
  </div>
</div></section>

<section class="section alt"><div class="wrap split">
  <div>
    <span class="eyebrow">Find us</span>
    <h2>On Narsingi–Puppalaguda Road, near Geethanjali Vedika School</h2>
    <p class="lead">{'<br>'.join(E(l) for l in ADDRESS_LINES)}</p>
    <div class="btn-row"><a class="btn btn-primary" href="{DIRECTIONS}" target="_blank" rel="noopener" data-track="directions">{ic("nav")} Get directions</a><a class="btn btn-ghost" href="visit.html">How to reach {ic("arrow")}</a></div>
  </div>
  <div class="map-frame"><iframe src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="West Paws on Google Maps"></iframe></div>
</div></section>
''' + cta_band() + footer()

def page_about():
    areas = [
        ("bone","Orthopaedics","Fracture fixation (IM pins, cerclage wire, cross pinning with K-wires), FHO for hip dysplasia and femoral head fractures, and amputations."),
        ("scalpel","Soft tissue & oncology","Removal of mammary, mast cell, perianal, nasal, testicular and digital tumours, with histopathology to guide follow-up care."),
        ("bed","Abdominal emergencies","GDV (bloat), intestinal and linear foreign bodies, exploratory laparotomy, gastrotomy and enterotomy."),
        ("drop","Urinary surgery","Perineal urethrostomy and its revision, cystotomy for bladder and urethral stones."),
        ("steth","Reproductive surgery","Spay and neuter, pyometra, en-bloc removal of the gravid uterus, and cryptorchid surgery."),
        ("pin","Eye & perineal surgery","Cherry eye correction (pocket technique), enucleation, and perineal hernia repair with mesh."),
    ]
    return head("Dr. K. Rajavardan | Consultant Veterinary Surgeon | West Paws, Hyderabad",
                "Dr. K. Rajavardan: B.V.Sc & A.H., M.V.Sc (Veterinary Surgery & Radiology), former Assistant Professor of Surgery and consultant soft tissue and orthopaedic surgeon at West Paws, Manikonda.", "about.html") + f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Dr. Rajavardan</div>
  <span class="eyebrow">The surgeon behind West Paws</span>
  <h1>Dr. K. Rajavardan</h1>
  <p class="lead">Consultant soft tissue and orthopaedic surgeon. He has trained veterinary surgeons and now operates on Hyderabad's pets.</p>
</div></section>

<section class="section"><div class="wrap split">
  <div class="doc-card">
    <div class="monogram">KR</div>
    <h3>Credentials</h3>
    <ul class="creds">
      <li>{ic("award")} <span><b>B.V.Sc & A.H.</b><br>Sri Venkateswara Veterinary University (SVVU)</span></li>
      <li>{ic("book")} <span><b>M.V.Sc, Veterinary Surgery & Radiology</b><br>P.V. Narsimha Rao Telangana Veterinary University (PVNRTVU)</span></li>
      <li>{ic("scalpel")} <span><b>Former Assistant Professor of Surgery</b><br>Teaching Veterinary Hospital, College of Veterinary Science, Korutla</span></li>
      <li>{ic("steth")} <span><b>Consultant Soft Tissue & Orthopaedic Surgeon</b><br>West Paws, and consultant surgeon to other city hospitals</span></li>
      <li>{ic("shield")} <span><b>Registered Veterinary Practitioner</b><br>Telangana State Veterinary Council, Reg. No. 01409/2018</span></li>
    </ul>
  </div>
  <div>
    <span class="eyebrow">Experience</span>
    <h2>A teacher of surgery, now operating full-time</h2>
    <p>Dr. Rajavardan specialised in veterinary surgery and radiology for his master's degree. He then taught surgery to veterinary students at the Teaching Veterinary Hospital in Korutla, which gave him years of hands-on work on hundreds of clinical cases.</p>
    <p>He opened West Paws in February 2025 as a small animal surgical centre for Manikonda, Narsingi and Puppalaguda. Pet parents get the same standard of surgery and diagnostics as at a teaching hospital, along with time and attention from the doctor himself. Other hospitals in the city also call him in as a consultant surgeon.</p>
    <div class="timeline" style="margin-top:28px">
      <div class="t"><b>B.V.Sc & A.H., SVVU</b><span class="muted">Veterinary degree</span></div>
      <div class="t"><b>M.V.Sc, Surgery & Radiology, PVNRTVU</b><span class="muted">Postgraduate specialisation</span></div>
      <div class="t"><b>Asst. Professor of Surgery, C.V.Sc. Korutla</b><span class="muted">Taught and practised surgery at the teaching hospital</span></div>
      <div class="t"><b>Founded West Paws, Feb 2025</b><span class="muted">Small Animal Surgical Centre, Manikonda</span></div>
    </div>
  </div>
</div></section>

<section class="section alt"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Surgical expertise</span><h2>Procedures he performs regularly</h2>
  <p class="lead">All of these come from cases treated and documented in the last year and a half.</p></div>
  <div class="grid g3">{''.join(f'<div class="card"><div class="icon">{ic(i)}</div><h3>{t}</h3><p class="muted">{d}</p></div>' for i,t,d in areas)}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Critical cases</span><h2>Selected cases</h2></div>
  <div class="grid g3">{''.join(case_card(CASES[i]) for i in (0,2,4,10,17,27))}</div>
  <p style="margin-top:28px"><a class="btn btn-ghost" href="reviews.html#cases">See the full case library {ic("arrow")}</a></p>
</div></section>
''' + cta_band("Want a surgeon's opinion?", "Bring your pet's earlier reports and X-rays. Dr. Rajavardan will go through them with you.") + footer()

def page_services():
    return head("Services | Vaccination, X-ray, Ultrasound, Surgery, Grooming | West Paws Hyderabad",
                "All services at West Paws Pet Clinic, Manikonda: consultations for dogs, cats, birds and small pets, vaccination, deworming, digital X-ray, ultrasound, ECG, blood tests, surgery, critical care, dental care, grooming, and pet food and accessories.", "services.html") + f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Services</div>
  <span class="eyebrow">Services & facilities</span>
  <h1>Everything your pet needs, in one place</h1>
  <p class="lead">Consultations, diagnostics, surgery, recovery, grooming and supplies are all available at the clinic.</p>
</div></section>

<section class="section tight" id="op"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Out-patient (OP) consultations</span><h2>Who we see</h2>
  <p class="lead">Walk in during clinic hours, or call or WhatsApp ahead to skip the wait.</p></div>
  <div class="grid g4" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
    {''.join(f'<div class="card feature"><div class="icon">{ic(i)}</div><h3>{t}</h3><p class="muted small">{d}</p></div>' for i,t,d in SPECIES)}
  </div>
</div></section>

<section class="section alt" id="all"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Facilities</span><h2>14 services under one roof</h2></div>
  <div class="grid g3">
    {''.join(f'<div class="card feature" id="s{n}"><div class="icon">{ic(i)}</div><h3>{t}</h3><p class="muted">{d}</p></div>' for n,(i,t,d) in enumerate(SERVICES))}
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div>
    <span class="eyebrow">Surgery at West Paws</span>
    <h2>A proper operation theatre, not a back room</h2>
    <p>Our dedicated operation theatre is set up for sterile procedures, with anaesthetic monitoring and post-operative care in the critical care unit.</p>
    <ul class="ticks">
      <li>{ic("check")} Pre-anaesthetic blood work and ECG when needed</li>
      <li>{ic("check")} Digital X-ray before and after orthopaedic surgery</li>
      <li>{ic("check")} Histopathology for removed tumours</li>
      <li>{ic("check")} Clear written aftercare and follow-up reviews</li>
    </ul>
    <a class="btn btn-primary" href="reviews.html#cases">See real surgical cases {ic("arrow")}</a>
  </div>
  <div class="card">
    <h3>Common procedures</h3>
    <p class="muted">Spay and neuter · Pyometra · Caesarean section · Tumour and lump removal · Mastectomy · Fracture fixation · FHO · Amputation · Foreign body removal · GDV (bloat) · Bladder stones · Perineal urethrostomy · Perineal hernia · Cherry eye · Enucleation · Wound repair</p>
    <div class="notice">For emergencies such as trauma, bloat, or a pet that can't pass urine, <b>call before you set out</b> on <a href="tel:{PHONE_TEL}" data-track="call">{PHONE_DISPLAY}</a> so the team is ready.</div>
  </div>
</div></section>
''' + cta_band() + footer()

def page_reviews():
    filters = '<button class="on" data-f="all">All</button>' + "".join(f'<button data-f="{k}">{v}</button>' for k, v in CASE_CATS.items())
    embeds = "".join(f'<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/westpaws_petclinic/{p}/" data-instgrm-version="14"><a href="https://www.instagram.com/westpaws_petclinic/{p}/" target="_blank" rel="noopener">View this post on Instagram</a></blockquote>' for p in IG_EMBEDS)
    return head("Reviews & Surgical Cases | West Paws Pet Clinic, Hyderabad",
                f"Rated {GOOGLE_RATING} on Google by {GOOGLE_COUNT} pet parents. Read reviews and browse {len(CASES)} real surgical cases treated by Dr. K. Rajavardan at West Paws, Manikonda.", "reviews.html") + f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Reviews & Cases</div>
  <span class="eyebrow">References</span>
  <h1>Reviews from pet parents and real surgical cases</h1>
  <p class="lead">Reviews come from our Google listing. Cases come from Dr. Rajavardan's posts on Instagram.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="gscore">
    <span class="num">{GOOGLE_RATING}</span>
    <div>{stars()}<br><b>{GOOGLE_COUNT} reviews on Google</b><br><span class="muted small">Pet parents mention: experienced surgeon · safe environment · gentle handling · new pet parent support</span></div>
    <div class="btn-row" style="margin-left:auto"><a class="btn btn-primary" href="{GMAPS}" target="_blank" rel="noopener">Read all on Google {ic("ext")}</a><a class="btn btn-ghost" href="{GMAPS}" target="_blank" rel="noopener">{ic("star")} Write a review</a></div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g3">{''.join(review_card(r) for r in REVIEWS)}
    <article class="review"><span class="tag">From the Google review summary</span>{''.join(f'<blockquote style="margin-bottom:12px">“{E(s)}”</blockquote>' for s in REVIEW_SNIPPETS)}<div class="who small muted">Short quotes from the Google review summary</div></article>
  </div>
</div></section>

<section class="section alt" id="cases"><div class="wrap">
  <div class="section-head"><span class="eyebrow">Case library</span><h2>{len(CASES)} surgical cases and counting</h2>
  <p class="lead">Each card summarises a real case. Tap "View on Instagram" for the photos and videos.</p></div>
  <p class="notice" style="margin-bottom:22px">Some posts show surgical photos that a few people may find upsetting. Instagram will warn you before showing them.</p>
  <div class="filters" role="group" aria-label="Filter cases">{filters}</div>
  <div class="grid g3" id="case-grid">{''.join(case_card(c) for c in CASES)}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">@westpaws_petclinic</span><h2>Life at West Paws</h2>
  <p class="lead">Our opening day, our first happy patient, our first bird patients and the operation theatre.</p></div>
  <div class="ig-grid">{embeds}</div>
  <p style="margin-top:28px"><a class="btn btn-primary" href="{INSTA}" target="_blank" rel="noopener">{ic("ig")} Follow on Instagram</a></p>
</div></section>
<script async src="https://www.instagram.com/embed.js"></script>
''' + cta_band() + footer()

def route_svg():
    # Redrawn from the clinic's visiting-card route map (not to scale)
    return '''<svg viewBox="0 0 560 520" role="img" aria-labelledby="rt"><title id="rt">Route map to West Paws (not to scale)</title>
<g fill="none" stroke="#a9c9b4" stroke-width="16" stroke-linecap="round">
<path d="M70 60V490"/><path d="M200 70V250"/><path d="M200 250H520"/><path d="M380 250V430"/><path d="M70 430H380"/>
</g>
<g fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="8 8"><path d="M70 60V490"/></g>
<path d="M70 430H230" fill="none" stroke="#1d5a41" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 12"/>
<g fill="#fffdf8" stroke="#1d5a41" stroke-width="4"><circle cx="200" cy="70" r="13"/><circle cx="200" cy="250" r="13"/></g>
<path d="M250 285l-22-22" stroke="#a9c9b4" stroke-width="8" stroke-linecap="round"/>
<rect x="395" y="320" width="18" height="18" fill="#a9c9b4"/>
<path d="M380 320h-22M380 360h-22" stroke="#a9c9b4" stroke-width="8"/>
<g transform="translate(230 362)"><rect width="64" height="64" rx="12" fill="#164834"/><path d="M32 18c-7 0-12 5-12 12 0 9 12 18 12 18s12-9 12-18c0-7-5-12-12-12z" fill="#f2c230"/><circle cx="32" cy="30" r="4.5" fill="#164834"/></g>
<g font-family="DM Sans,Arial,sans-serif" font-size="15" fill="#1c2420">
<text x="200" y="45" text-anchor="middle" font-weight="700">Butterfly Circle</text>
<text x="178" y="255" text-anchor="end" font-weight="700">Yoga Circle</text>
<text x="262" y="305">Ganesh Mandapam</text>
<text x="420" y="334">Nethaji Park</text>
<text x="262" y="356" font-weight="800" fill="#164834" font-size="17">WEST PAWS</text>
<text x="40" y="275" transform="rotate(-90 40 275)" text-anchor="middle" font-weight="700">Narsingi – Puppalaguda Road</text>
<text x="88" y="470" font-weight="700">Geethanjali Vedika School</text>
<text x="88" y="488" fill="#5a665f" font-size="13">Opp. D-Mart Ready · High-tension line</text>
</g>
<g font-family="DM Sans,Arial,sans-serif" font-size="12" fill="#5a665f"><text x="70" y="30" text-anchor="middle">↑ Narsingi</text><text x="70" y="512" text-anchor="middle">↓ Puppalaguda / Manikonda</text></g>
</svg>'''

def page_visit():
    rows = "".join(f'<tr data-day="{i}"><td>{d}</td><td>{h}</td></tr>' for i, (d, h) in enumerate(HOURS))
    lm = ["Geethanjali Vedika School", "D-Mart Ready", "High-tension line", "Alkapur Township", "Yoga Circle", "Butterfly Circle", "Ganesh Mandapam", "Nethaji Park"]
    return head("Visit & Contact | How to Reach West Paws Pet Clinic, Manikonda, Hyderabad",
                "Directions, map, timings and contact details for West Paws Pet Clinic, H.No. 115, Narsingi–Puppalaguda Main Road, near Geethanjali Vedika School, Alkapur Township, Manikonda, Hyderabad 500089.", "visit.html") + f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Visit & Contact</div>
  <span class="eyebrow">Visit us</span>
  <h1>How to reach West Paws</h1>
  <p class="lead">We are on Narsingi–Puppalaguda Main Road in Alkapur Township, close to Manikonda, Narsingi, Puppalaguda, Kokapet and Neknampur.</p>
</div></section>

<section class="section tight"><div class="wrap split">
  <div class="map-frame"><iframe src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="West Paws on Google Maps"></iframe></div>
  <div>
    <h2>By road</h2>
    <ol class="steps">
      <li><b>Get onto Narsingi–Puppalaguda Main Road.</b> It runs between Narsingi and Puppalaguda/Manikonda.</li>
      <li><b>Look for Geethanjali Vedika School</b>, opposite D-Mart Ready, near the high-tension power line in Alkapur Township.</li>
      <li><b>Turn into the lane at the school.</b> West Paws is a short way down the lane, on your left.</li>
      <li><b>Coming from Yoga Circle?</b> Head east past Ganesh Mandapam, turn right towards Nethaji Park, then turn right again at the end. West Paws will be on your right.</li>
    </ol>
    <div class="btn-row" style="margin-top:24px"><a class="btn btn-primary" href="{DIRECTIONS}" target="_blank" rel="noopener" data-track="directions">{ic("nav")} Start navigation</a><a class="btn btn-ghost" href="{GMAPS}" target="_blank" rel="noopener">Open in Google Maps {ic("ext")}</a></div>
  </div>
</div></section>

<section class="section alt"><div class="wrap split rev">
  <div class="route">{route_svg()}</div>
  <div>
    <span class="eyebrow">Route map</span>
    <h2>Landmarks to look for</h2>
    <p class="muted">This map is redrawn from our visiting card and is not to scale. Use Google Maps for live navigation.</p>
    <div class="landmarks">{''.join(f'<span class="chip">{ic("pin")} {l}</span>' for l in lm)}</div>
    <p style="margin-top:20px" class="small muted">Plus Code: 99V7+V6 Hyderabad · GPS {LAT:.5f}, {LNG:.5f}</p>
  </div>
</div></section>

<section class="section" id="contact"><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">Contact</span>
    <h2>Get in touch</h2>
    <ul class="contact-list">
      <li><span class="icon">{ic("phone")}</span><span><b>Phone / appointments</b><a href="tel:{PHONE_TEL}" data-track="call">{PHONE_DISPLAY}</a></span></li>
      <li><span class="icon">{ic("wa")}</span><span><b>WhatsApp</b><a href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">Chat with us</a></span></li>
      <li><span class="icon">{ic("mail")}</span><span><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
      <li><span class="icon">{ic("ig")}</span><span><b>Instagram</b><a href="{INSTA}" target="_blank" rel="noopener">@westpaws_petclinic</a></span></li>
      <li><span class="icon">{ic("pin")}</span><span><b>Address</b>{'<br>'.join(E(l) for l in ADDRESS_LINES)}<br><a href="{GMAPS}" target="_blank" rel="noopener">Google Maps listing ↗</a></span></li>
    </ul>
  </div>
  <div class="card">
    <h3>{ic("clock").replace('<svg','<svg style="width:22px;height:22px;vertical-align:-4px;margin-right:6px"')}Clinic hours</h3>
    <table class="hours">{rows}</table>
    <p class="small muted" style="margin-top:16px">For emergencies outside these hours, call {PHONE_DISPLAY} first.</p>
  </div>
</div></section>
''' + cta_band() + footer()

def page_camp():
    return head("Free Pet Health Camps | Rabies Vaccination Camp | West Paws Hyderabad",
                "West Paws runs free pet health camps in Manikonda, including anti-rabies vaccination, deworming, nail trims and ear cleaning. Message us on WhatsApp to hear about the next camp.", "camp.html") + f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Pet health camps</div>
  <span class="eyebrow">Community camps</span>
  <h1>Free pet health camps</h1>
  <p class="lead">Free camps for the neighbourhood's pets, held on awareness days and during the year.</p>
</div></section>
<section class="section tight"><div class="wrap camp">
  <img src="img/rabies-camp-2026.jpg" alt="Free Rabies Camp poster" width="1024" height="1536">
  <div>
    <span class="chip">{ic("cal")} Held on Monday, 28 September · World Rabies Day</span>
    <h2 style="margin-top:16px">Free Rabies Camp</h2>
    <p class="lead">Protect today for a safer tomorrow. The camp offered, at no cost:</p>
    <ul class="ticks">
      <li>{ic("check")} Free anti-rabies vaccine</li>
      <li>{ic("check")} Free deworming</li>
      <li>{ic("check")} Free nail trim</li>
      <li>{ic("check")} Free ear cleaning</li>
    </ul>
    <p>Rabies is almost always fatal but 100% preventable. An annual vaccination protects your pet and your family.</p>
    <div class="btn-row"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener" data-track="whatsapp">{ic("wa")} Tell me about the next camp</a><a class="btn btn-ghost" href="services.html">Vaccination at West Paws {ic("arrow")}</a></div>
  </div>
</div></section>
''' + cta_band("Missed the camp?", "Anti-rabies vaccination is available at the clinic every day.") + footer()

PAGES = {"index.html": page_index, "about.html": page_about, "services.html": page_services,
         "reviews.html": page_reviews, "visit.html": page_visit, "camp.html": page_camp}

if __name__ == "__main__":
    for fn, f in PAGES.items():
        with open(os.path.join(ROOT, fn), "w", encoding="utf-8") as fh:
            fh.write(f().replace("{SCHEMA}", SCHEMA))
        print("built", fn)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                 "".join(f"  <url><loc>{SITE_URL}/{'' if p=='index.html' else p}</loc></url>\n" for p in PAGES) + "</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w") as fh:
        fh.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
