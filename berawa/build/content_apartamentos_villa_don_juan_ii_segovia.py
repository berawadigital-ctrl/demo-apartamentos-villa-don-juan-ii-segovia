# Contenido de la demo Villa Don Juan II (Segovia) (es/en/fr/de). Hechos de villadonjuanii.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Apartamento Menta','Apartamento Melocotón','Apartamento Fresa'],'en':['Menta apartment','Melocotón apartment','Fresa apartment'],'fr':['Appartement Menta','Appartement Melocotón','Appartement Fresa'],'de':['Apartment Menta','Apartment Melocotón','Apartment Fresa']}
RD={
'es':['Para 2 personas, en dos plantas: dormitorio con cama de matrimonio, sofá-cama para un niño, baño con ducha y loft con salón, comedor y cocina.','Para 4 personas, en dos plantas: dos dormitorios con cama de matrimonio, baño con ducha, sofá-cama para un niño y loft con cocina.','Para 6 personas, en dos plantas: tres dormitorios, dos baños completos, dos sofás-cama para niños y loft con salón, comedor y cocina.'],
'en':['For 2 people, on two floors: bedroom with double bed, sofa bed for a child, bathroom with shower and a loft with living room, dining area and kitchen.','For 4 people, on two floors: two bedrooms with double beds, bathroom with shower, sofa bed for a child and a loft with kitchen.','For 6 people, on two floors: three bedrooms, two full bathrooms, two sofa beds for children and a loft with living room, dining area and kitchen.'],
'fr':['Pour 2 personnes, sur deux niveaux : chambre avec lit double, canapé-lit pour un enfant, salle de bains avec douche et loft avec salon, salle à manger et cuisine.','Pour 4 personnes, sur deux niveaux : deux chambres avec lit double, salle de bains avec douche, canapé-lit pour un enfant et loft avec cuisine.','Pour 6 personnes, sur deux niveaux : trois chambres, deux salles de bains complètes, deux canapés-lits pour enfants et loft avec salon, salle à manger et cuisine.'],
'de':['Für 2 Personen auf zwei Etagen: Schlafzimmer mit Doppelbett, Schlafsofa für ein Kind, Bad mit Dusche und Loft mit Wohnzimmer, Essbereich und Küche.','Für 4 Personen auf zwei Etagen: zwei Schlafzimmer mit Doppelbett, Bad mit Dusche, Schlafsofa für ein Kind und Loft mit Küche.','Für 6 Personen auf zwei Etagen: drei Schlafzimmer, zwei vollständige Bäder, zwei Schlafsofas für Kinder und Loft mit Wohnzimmer, Essbereich und Küche.']}
ART={
'hero':('arches',2011,['#1f2a22','#5d7a4f','#eef2e6','#4a6340','#344833','#151d17']),
'intro':('columns',2012,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25']),
'r1':('hills',2021,['#f2f5ec','#dbe6cc','#9cb784','#6f8c5b','#526b43','#35472c']),
'r2':('arches',2022,['#2b1f1a','#c47a52','#f7e9dd','#9a5a3c','#6e3f2a','#1d1411']),
'r3':('skyline',2023,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25']),
'g1':('skyline',2031,['#1f2a22','#5d7a4f','#eef2e6','#4a6340','#344833','#151d17']),
'g2':('hills',2032,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g3':('arches',2033,['#1f2a22','#6d8a5f','#f1f5ea','#55704a','#3c5236','#151d17']),
'g4':('columns',2034,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Villa Don Juan II · Apartamentos turísticos en Segovia',see_rooms='Ver apartamentos',hero_k='Segovia · Ronda Don Juan II, 3',hero_t='Apartamentos en el corazón de Segovia',hero_s='Junto a la antigua muralla, a pocos metros del Alcázar y de la Catedral, con aparcamiento en la propia finca.',
 intro_t='Un lugar para descansar y disfrutar',intro_p1='Tres apartamentos en dos plantas con vistas a un patio privado ajardinado y al Alcázar de Segovia.',
 intro_p2='Espacios castellanos con trazos de color intenso y líneas contemporáneas, a nueve minutos del Acueducto.',
 stats=['3 apartamentos','De 2 a 6 personas','Parking en la finca','Wifi gratuito'],nav_rooms='Apartamentos',rooms_t='Apartamentos',rooms_s='Todos con cocina completa, calefacción y aire acondicionado, TV, wifi gratuito, ropa de cama y toallas.',
 svcs=['Cocina completa con lavadora y lavavajillas','Jardín y patio privados','Cuna gratis (según disponibilidad)','Parking en la finca (consultar)','Wifi gratuito en toda la villa','Información local y cultural'],
 loc_p='Ronda Don Juan II, 3 · 40003 Segovia. Teléfono: +34 679 00 89 43. Correo: info@villadonjuanii.com.',
 chips=['¿Qué apartamentos tenéis?','¿Tenéis parking?','¿A qué hora es la entrada?','¿Cómo reservo?']),
'en':dict(title='Villa Don Juan II · Holiday apartments in Segovia',see_rooms='See apartments',hero_k='Segovia · Ronda Don Juan II, 3',hero_t='Apartments in the heart of Segovia',hero_s='Beside the old city wall, a few metres from the Alcázar and the Cathedral, with parking on the property.',
 intro_t='A place to rest and enjoy',intro_p1='Three two-floor apartments overlooking a private landscaped patio and the Alcázar of Segovia.',
 intro_p2='Castilian spaces with bold colour and contemporary lines, nine minutes from the Aqueduct.',
 stats=['3 apartments','2 to 6 guests','Parking on site','Free wifi'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='All with a fully equipped kitchen, heating and air conditioning, TV, free wifi, bed linen and towels.',
 svcs=['Full kitchen with washing machine and dishwasher','Private garden and patio','Free cot (subject to availability)','Parking on site (ask)','Free wifi throughout the villa','Local and cultural information'],
 loc_p='Ronda Don Juan II, 3 · 40003 Segovia. Phone: +34 679 00 89 43. Email: info@villadonjuanii.com.',
 chips=['Which apartments do you have?','Do you have parking?','What time is check-in?','How do I book?']),
'fr':dict(title='Villa Don Juan II · Appartements touristiques à Ségovie',see_rooms='Voir les appartements',hero_k='Ségovie · Ronda Don Juan II, 3',hero_t='Des appartements au cœur de Ségovie',hero_s='Le long de l’ancienne muraille, à quelques mètres de l’Alcazar et de la cathédrale, avec parking sur place.',
 intro_t='Un lieu pour se reposer et profiter',intro_p1='Trois appartements sur deux niveaux avec vue sur un patio privé paysager et sur l’Alcazar de Ségovie.',
 intro_p2='Des espaces castillans aux couleurs intenses et aux lignes contemporaines, à neuf minutes de l’aqueduc.',
 stats=['3 appartements','De 2 à 6 personnes','Parking sur place','Wifi gratuit'],nav_rooms='Appartements',rooms_t='Appartements',rooms_s='Tous avec cuisine équipée, chauffage et climatisation, TV, wifi gratuit, linge de lit et serviettes.',
 svcs=['Cuisine équipée avec lave-linge et lave-vaisselle','Jardin et patio privés','Lit bébé gratuit (selon disponibilité)','Parking sur place (à demander)','Wifi gratuit dans toute la villa','Informations locales et culturelles'],
 loc_p='Ronda Don Juan II, 3 · 40003 Ségovie. Téléphone : +34 679 00 89 43. E-mail : info@villadonjuanii.com.',
 chips=['Quels appartements avez-vous ?','Avez-vous un parking ?','À quelle heure est l’arrivée ?','Comment réserver ?']),
'de':dict(title='Villa Don Juan II · Ferienwohnungen in Segovia',see_rooms='Apartments ansehen',hero_k='Segovia · Ronda Don Juan II, 3',hero_t='Apartments im Herzen von Segovia',hero_s='An der alten Stadtmauer, wenige Meter vom Alcázar und der Kathedrale, mit Parkplatz auf dem Grundstück.',
 intro_t='Ein Ort zum Ausruhen und Genießen',intro_p1='Drei zweistöckige Apartments mit Blick auf einen privaten Gartenpatio und den Alcázar von Segovia.',
 intro_p2='Kastilische Räume mit kräftigen Farben und modernen Linien, neun Minuten vom Aquädukt entfernt.',
 stats=['3 Apartments','2 bis 6 Personen','Parkplatz vor Ort','Kostenloses WLAN'],nav_rooms='Apartments',rooms_t='Apartments',rooms_s='Alle mit voll ausgestatteter Küche, Heizung und Klimaanlage, TV, kostenlosem WLAN, Bettwäsche und Handtüchern.',
 svcs=['Küche mit Waschmaschine und Geschirrspüler','Privater Garten und Patio','Kostenloses Babybett (nach Verfügbarkeit)','Parkplatz vor Ort (auf Anfrage)','Kostenloses WLAN in der ganzen Villa','Lokale und kulturelle Informationen'],
 loc_p='Ronda Don Juan II, 3 · 40003 Segovia. Telefon: +34 679 00 89 43. E-Mail: info@villadonjuanii.com.',
 chips=['Welche Apartments gibt es?','Gibt es einen Parkplatz?','Wann ist der Check-in?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://book.octorate.com/octobook/site/reservation/calendar.xhtml?siteKey=526d6e0fb930aaa8a2fa580214f46ee0&lang='
BOOK=dict(mode='engine',url=dict(es=RB+'ES',en=RB+'EN',fr=RB+'FR',de=RB+'DE'))
D=dict(name='Villa Don Juan II',ac='#1f2a22',ac2='#7a3b2e',ac2_a11y='#6e3529',book=BOOK,around=[],foot=FOOT,
 address='Ronda Don Juan II, 3 · 40003 Segovia',phones=['+34 679 00 89 43'],emails=['info@villadonjuanii.com'],maps='Villa Don Juan II, Ronda Don Juan II 3, 40003 Segovia',t=T)
META=dict(repo='demo-apartamentos-villa-don-juan-ii-segovia',name='Villa Don Juan II',legal_name='Esther González Sanz, NIF 03404425B (política de privacidad de su web; autónoma)',registry_ids=['03404425B'],
 url='https://www.villadonjuanii.com/es/apartamentos-turisticos-segovia/',domain='villadonjuanii.com',municipality='Segovia',province='Segovia',sector='apartamentos turísticos en el casco histórico de Segovia',
 read_at='2026-11-02T11:08:00+01:00',created_at='2026-11-02T11:08:00+01:00',built_at='2026-11-02T11:30:00+01:00',audit_date='2026-11-02T11:08:00+01:00',
 rating=dict(value=4.8,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/search/Apartamentos+Turisticos+Villa+Don+Juan+II+Segovia'),
 book=dict(mode='engine',url=RB+'ES',note='motor Octorate (Octobook) incrustado en su web con data-sitekey 526d6e0fb930aaa8a2fa580214f46ee0; su página pública book.octorate.com/octobook/site/reservation/calendar.xhtml?siteKey=…&lang=ES/EN/FR/DE devuelve HTTP 200 con el título «VILLA DON JUAN II» (02/11/2026 11:10).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué apartamentos tenéis?','K01'),('¿Qué tienen los apartamentos?','K02'),('¿Tenéis parking?','K03'),('¿Hay cuna para bebé?','K04'),('¿Tenéis camas supletorias?','K05'),('¿A qué hora es la entrada?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay wifi?','K09'),('¿Tiene jardín?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Está cerca del Acueducto?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which apartments do you have?','K01'),('What do the apartments include?','K02'),('Do you have parking?','K03'),('Is there a baby cot?','K04'),('Do you have extra beds?','K05'),('What time is check-in?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there wifi?','K09'),('Is there a garden?','K10'),('What is your phone number?','K11'),('Is it close to the Aqueduct?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quels appartements avez-vous ?','K01'),('Que comprennent les appartements ?','K02'),('Avez-vous un parking ?','K03'),('Y a-t-il un lit bébé ?','K04'),('Avez-vous des lits d’appoint ?','K05'),('À quelle heure est l’arrivée ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il le wifi ?','K09'),('Y a-t-il un jardin ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Est-ce près de l’aqueduc ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Apartments gibt es?','K01'),('Was bieten die Apartments?','K02'),('Gibt es einen Parkplatz?','K03'),('Gibt es ein Babybett?','K04'),('Haben Sie Zustellbetten?','K05'),('Wann ist der Check-in?','K06'),('Wo liegt die Villa?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es WLAN?','K09'),('Gibt es einen Garten?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Ist es nahe am Aquädukt?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
