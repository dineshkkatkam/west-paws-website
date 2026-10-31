# Content for the West Paws website — edit here, then run build.py
PHONE_DISPLAY = "93920 11580"
PHONE_TEL = "+919392011580"
WA = "https://wa.me/919392011580?text=" + "Hi%20West%20Paws%2C%20I%27d%20like%20to%20book%20an%20appointment%20for%20my%20pet."
EMAIL = "westpawspetclinic@gmail.com"
INSTA = "https://www.instagram.com/westpaws_petclinic/"
GMAPS = "https://maps.app.goo.gl/jqcY1hZpUmz1absB8"
LAT, LNG = 17.3947036, 78.3630391
DIRECTIONS = f"https://www.google.com/maps/dir/?api=1&destination={LAT},{LNG}"
MAP_EMBED = f"https://maps.google.com/maps?q={LAT},{LNG}&z=16&output=embed"
ADDRESS_LINES = [
    "H. No. 115, Narsingi – Puppalaguda Main Road",
    "Near Geethanjali Vedika School, Opp. D-Mart Ready",
    "Alkapur Township, Puppalaguda, Manikonda",
    "Hyderabad, Telangana 500089",
]
HOURS = [  # (day, hours)
    ("Monday", "10 AM – 9 PM"), ("Tuesday", "10 AM – 9 PM"), ("Wednesday", "10 AM – 9 PM"),
    ("Thursday", "10 AM – 9 PM"), ("Friday", "10 AM – 9 PM"), ("Saturday", "10 AM – 9 PM"),
    ("Sunday", "10 AM – 2 PM"),
]
GOOGLE_RATING = "5.0"
GOOGLE_COUNT = "117"   # update when the Google count changes

# Real Google reviews (excerpts, lightly trimmed with …). Source: Google Maps listing, Oct 2026.
REVIEWS = [
    dict(name="Manoranjan Kumar S.", tag="Emergency · Pyometra surgery (cat)", when="2026",
         text="My cat recently had a very serious condition and was suffering from pyometra … After reviewing, the way he handled the case was totally different. My cat was safely treated, surgery was done at an almost 5x more affordable rate with full guidance. My cat is recovering well and walking happily again. So grateful to Dr. Rajavardan sir — he really saved my child."),
    dict(name="Aafreen R.", tag="Neutering (cat)", when="2026",
         text="We had neutering surgery done on my male cat and my cat did not face any problem before or after the surgery. The hospital is neat and tidy and the doctor and staff are very friendly and gentle with my cat throughout the procedure. I highly recommend this hospital for all pets."),
    dict(name="Neeraj S.", tag="Allergy diagnosis & vaccination", when="2026",
         text="After being misdiagnosed at another vet, we brought our beloved Pixie to this clinic. The way the doctor took time to examine, answer all our questions and diagnose the allergic issue correctly was commendable. He is also always available to answer questions over the call … We couldn't ask for anything more as first-time pet parents."),
    dict(name="Yashwanth R.", tag="Rescued puppy · wound care", when="2025",
         text="My friends and I adopted a wounded, helpless Indian puppy. Dr. Rajavardhan is kind and welcoming — he checked the puppy thoroughly and explained the wounds and the treatment clearly … It's my first puppy and I had many doubts about raising him in an apartment. He answered all of them and gave me the confidence to raise the puppy."),
    dict(name="Sreeharsha T.", tag="Consultation", when="2026",
         text="The consultation felt really comfortable and thorough, like the doctor took time to listen and understand every concern without rushing. They explained everything in a simple way and handled my pet with so much care."),
]
REVIEW_SNIPPETS = [
    "Best experience at this clinic… Highly recommend this place for your fur babies.",
    "Very friendly doctor with a smile, good treatment at affordable pricing.",
    "Experienced, economical, well maintained and good service.",
]

# Surgical cases documented on @westpaws_petclinic (newest first)
# cat keys: ortho, onco, abdo, uro, eye, repro, soft
CASES = [
    ("Oct 2026","uro","Revision of a perineal urethrostomy stricture","9-year-old male cat","Presented with anuria, azotemia and urine scalding from a stricture after a perineal urethrostomy done elsewhere two years earlier. Surgically corrected.","Stricture corrected","p/DePRSZvmZYq"),
    ("Sep 2026","onco","High tail amputation for multiple plasma cell tumours","14-year-old male dog","Multiple plasma cell tumours on the tail were removed with a high tail amputation.","Tumours removed","p/DdgCyPaGV2R"),
    ("Aug 2026","abdo","Razor blade removed from stomach and duodenum","6-year-old male Golden Retriever","Swallowed a facial razor blade. Pre-op X-rays located it in the stomach and duodenum, and it was removed by exploratory laparotomy.","Uneventful recovery","p/DcLGIyJmQhv"),
    ("Aug 2026","onco","Anal neoplasia excision","9-year-old male dog","Operated by Dr. Rajavardan as consultant surgeon at Animal Health Hospital. Histopathology confirmed a perianal gland (hepatoid) adenoma.","Uneventful recovery","p/DcNso2fmTTC"),
    ("Jul 2026","ortho","Femur fracture repair after a road accident","6-year-old female Pomeranian, 6 kg","Femoral shaft fracture with a butterfly fragment, repaired by open reduction and internal fixation using an intramedullary pin and cerclage wire.","Anatomic reduction achieved","p/Dahjt1BGe9c"),
    ("May 2026","abdo","Marble stone removed from the intestine","Labrador Retriever","Sudden vomiting and loss of appetite. A hard mass was felt and X-rays showed a foreign body. A large marble stone was removed from the jejunum by enterotomy.","Uneventful recovery","p/DY_lA8OmQNY"),
    ("May 2026","ortho","FHO for hip dysplasia","5-year-old male Labrador Retriever","Severe hind-limb lameness from hip dysplasia. A femoral head and neck ostectomy (FHO) relieved the pain.","Walking without pain","p/DYmbUoRGa1e"),
    ("May 2026","eye","Cherry eye correction","Dog","The prolapsed third-eyelid gland was put back in place, which preserves the gland's tear production.","Gland preserved","p/DYZtnHkmXRN"),
    ("May 2026","uro","Perineal urethrostomy","Male cat","Done to treat a urinary blockage that could not be cleared by catheter and to stop it coming back.","Urinary flow restored","p/DYOsGwumXrx"),
    ("Apr 2026","ortho","FHO for hip dysplasia","2.5-year-old male Golden Retriever","Severely lame with a positive Ortolani sign in the left hind limb. FHO was performed.","Fully walking by day 30, pain-free","p/DXZVIqxGTKn"),
    ("Mar 2026","uro","Bladder and urethral stones plus a retained testis","9-year-old male Shih Tzu","Presented unable to pass urine. Bladder and pelvic urethral stones and an undescended testis were removed through one parapreputial incision.","Both problems treated in one surgery","p/DWI-HqCmS0g"),
    ("Mar 2026","onco","Scrotal ablation for a testicular sarcoma","7-year-old male Bulldog","An enlarged left testicle turned out on histopathology to be a soft tissue sarcoma.","Tumour removed","p/DV-dImtmRMa"),
    ("Mar 2026","eye","Enucleation after a traumatic eye injury","1-year-old Shih Tzu","The eyeball had been pushed out of its socket by trauma, so it was surgically removed.","Pain relieved","p/DVnZb2kGUZz"),
    ("Feb 2026","soft","Perineal hernia repair with mesh","9-year-old intact male Shih Tzu","Repaired by internal obturator transposition with a Prolene mesh.","Hernia repaired","p/DVL0FVxGWZP"),
    ("Jan 2026","ortho","Femur fracture fixation in a cat","1-year-old cat","A supracondylar femoral fracture of the right hind limb was fixed by cross pinning.","Successful fixation","p/DUI9u7lEsur"),
    ("Jan 2026","onco","Mammary tumour removal (mastectomy)","8-year-old Labrador Retriever","The mammary tumour was removed surgically.","Tumour removed","reel/DT2025vkrtY"),
    ("Jan 2026","ortho","FHO for severe hip dysplasia","7-year-old male Labrador Retriever","Femoral head and neck excision for severe hip dysplasia.","Walking without pain","p/DTvDHQLEqW-"),
    ("Jan 2026","ortho","Complex femur fracture repair","1.5-year-old male dog","Complex wedge fracture of the femoral shaft, fixed with cerclage wire and a Steinmann pin.","Running and bearing weight at 6 weeks","p/DTM8Ej0kgrC"),
    ("Jan 2026","onco","Toe amputation for a digital tumour","10-year-old Labrador Retriever","The tumour had invaded the bone of the third toe, so the toe was amputated.","Tumour removed","p/DTDZb8_EmjE"),
    ("Dec 2025","onco","Removal of a growth on the hock","8-year-old male Labrador","A growth on the point of the right hock was removed. Histopathology showed a cutaneous fibroma.","Benign; fully removed","p/DS4aBh7Eslx"),
    ("Dec 2025","eye","Cherry eye correction (pocket technique)","Dog","The prolapsed third-eyelid gland was corrected by the pocket technique.","Gland preserved","p/DSfTr0bkpq-"),
    ("Nov 2025","abdo","Linear foreign body in the stomach and intestine","Persian cat","Removed by exploratory laparotomy with gastrotomy and enterotomy.","Foreign body removed","p/DRcdlBzEpkv"),
    ("Nov 2025","onco","Excision of a large paw tumour","Dog","A large tumour hanging from the underside of the paw was surgically removed.","Mass removed","p/DRSGTnpkuuq"),
    ("Nov 2025","repro","En-bloc removal of the gravid uterus","Dog","Needed because the puppies had died in the womb and the uterus was compromised.","Life-saving surgery","p/DQ6KYcREtvv"),
    ("Nov 2025","repro","Spay surgery","Cat","Routine spay (ovariohysterectomy) done with sterile surgical technique.","Routine recovery","p/DQzLqnxksoH"),
    ("Oct 2025","ortho","FHO for a femoral head fracture","Puppy","FHO for a fracture of the femoral head.","Walking on the leg by day 15","p/DQPLReYEqkV"),
    ("Oct 2025","onco","Scrotal ablation","German Shepherd","Surgical scrotal ablation.","Successful surgery","p/DPdUzzokjYl"),
    ("Sep 2025","repro","Emergency pyometra surgery","7-year-old Siberian Husky","Surgery for a pyometra (infected uterus), a life-threatening condition.","Life-saving surgery","p/DPOnGNkEj1o"),
    ("Sep 2025","abdo","GDV (bloat) correction","Labrador Retriever","Emergency surgical correction of gastric dilatation and volvulus.","Emergency handled","p/DPHFrC8EoT_"),
    ("Sep 2025","onco","Perianal adenoma excision","Dog","Removal of a perianal adenoma, the most common tumour around a dog's anus.","Tumour removed","p/DPEdmvXkp8W"),
    ("Sep 2025","onco","Tumour excision","9-year-old Beagle","Surgical removal of a tumour.","Tumour removed","p/DOqqyLxEl7H"),
    ("Sep 2025","onco","Nasal tumour excision","9-year-old Cocker Spaniel","Surgical excision of a nasal tumour.","Tumour removed","p/DOiKIVLksHh"),
    ("Sep 2025","eye","Transconjunctival enucleation","2-year-old Shih Tzu","Eye removal by the transconjunctival technique.","Pain relieved","p/DOWKMBKktGi"),
    ("Aug 2025","onco","Excision of multiple mast cell tumours","9-year-old male Bullmastiff","Several mast cell tumours were removed (cancer surgery).","Tumours removed","p/DNnYxKzS9cb"),
    ("Aug 2025","repro","Pyometra surgery","Shih Tzu","Surgery for an infected uterus.","Life-saving surgery","p/DNx8H_SZKNa"),
    ("Aug 2025","repro","Pyometra surgery","10-year-old Cocker Spaniel","Surgery for an infected uterus in a senior dog.","Life-saving surgery","p/DNhueqFMDUO"),
    ("Jul 2025","onco","Regional mastectomy","10-year-old German Shepherd","Regional mastectomy for mammary cancer.","Tumour removed","p/DMfh8RJSIoV"),
    ("Jun 2025","ortho","Femur fracture in a kitten","6-month-old female cat","A left femoral supracondylar fracture, stabilised by cross pinning with K-wires.","Walking normally by day 12","p/DLCO6zAyUPi"),
    ("May 2025","repro","Spay surgery in a large dog","Large-breed dog","Spay (ovariohysterectomy) in a large-breed dog.","Routine recovery","reel/DJ1pCQnyn3b"),
    ("Apr 2025","repro","Ovariohysterectomy (spay)","Shih Tzu","Routine spay surgery.","Routine recovery","reel/DIfqPVjychL"),
    ("Mar 2025","onco","Removal of a benign growth on the elbow","Dog","A benign growth on the elbow was removed.","Growth removed","reel/DHsaIVuSzR0"),
]
CASE_CATS = {
    "ortho": "Orthopaedic", "onco": "Tumour & oncology", "abdo": "Abdominal & foreign body",
    "uro": "Urinary", "eye": "Eye", "repro": "Reproductive & pyometra", "soft": "Soft tissue",
}
# Non-graphic Instagram posts to embed as a gallery
IG_EMBEDS = ["p/DGOTpRbyNCx", "p/DGLcToXy1x4", "p/DGPtZrwy9MF", "reel/DI365peSezQ", "reel/DIq_ganyI7R", "p/DHDlRTWyo8v"]
