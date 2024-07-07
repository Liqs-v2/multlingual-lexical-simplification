import numpy as np

'''
original_data = germaneval_data_provider.GermanEvalDataProvider().provide_data_as_numpy_array()
dataset = original_data[:5]


messages = [
            {"role": "user", "content": "kreiere ein neues Dataset mit 5 Sätzen für lexical simplification."},
            {"role": "assistant", "content": str(dataset.tolist())},
            {"role": "user", "content": "kreiere ein neues Dataset mit 30 Sätzen für lexical simplification."},
            ]
'''
def get_dataset():
    data = [
    [np.str_('Die Politiker haben eine Entscheidung getroffen, die das Leben der Bürger wesentlich verbessern wird'), 
     np.str_('verbessern'), 8, 
     {1: ['aufbessern', 'erhöhen', 'optimieren', 'steigern', 'aufwerten'], 2: ['entwickeln', 'weiterentwickeln', 'vorantreiben', 'vorwärts bringen']}],
     
    [np.str_('Die Schüler müssen ihre Hausaufgaben rechtzeitig abgeben, um gute Noten zu erhalten'), 
     np.str_('erhalten'), 8, 
     {1: ['bekommen', 'erzielen', 'erlangen', 'erreichen', 'ernten'], 2: ['bewahren', 'behalten', 'aufbewahren', 'konservieren']}],
     
    [np.str_('Die Firma plant, innovative Technologien einzuführen, um im Markt wettbewerbsfähig zu bleiben'), 
     np.str_('wettbewerbsfähig'), 14, 
     {1: ['konkurrenzfähig'], 2: ['wettbewerbsstark', 'marktrelevant', 'leistungsstark', 'marktdurchsetzungsfähig']}],
     
    [np.str_('Die Sportler trainieren hart, um bei den Olympischen Spielen eine Medaille zu gewinnen'), 
     np.str_('gewinnen'), 7, 
     {1: ['sichern', 'ergattern', 'holen', 'erringen'], 2: ['erzielen', 'erreichen', 'erlangen', 'bekommen']}],
     
    [np.str_('Die Unternehmen müssen sich auf dem Markt behaupten, um langfristig erfolgreich zu sein'), 
     np.str_('erfolgreich'), 10, 
     {1: ['erfolgreich'], 2: ['gewinnbringend', 'ertragreich', 'profitabel', 'erfolgreich']}],
     
    [np.str_('Die Regierung hat Maßnahmen ergriffen, um die Umwelt zu schützen und die Luftqualität zu verbessern'), 
     np.str_('verbessern'), 8, 
     {1: ['aufbessern', 'erhöhen', 'optimieren', 'steigern', 'aufwerten'], 2: ['entwickeln', 'weiterentwickeln', 'vorantreiben', 'vorwärts bringen']}],
   
    [np.str_('Die Krankenschwester betreut die Patienten mit Empathie und professioneller Fürsorge'), 
     np.str_('betreut'), 7, 
     {1: ['pflegt', 'sorgt für', 'begleitet', 'versorgt'], 2: ['leitet', 'managt', 'koordiniert', 'verwaltet']}],
     
    [np.str_('Die Eltern ermutigen ihre Kinder, ihre Träume zu verfolgen und ihr Bestes zu geben'), 
     np.str_('ermutigen'), 9, 
     {1: ['anfeuern', 'beflügeln', 'unterstützen', 'stärken', 'ermutigen'], 2: ['anregen', 'motivieren', 'inspirieren', 'aufmuntern']}],
     
    [np.str_('Der Professor erklärt das komplizierte Thema auf verständliche Weise, damit die Studenten es besser verstehen'), 
     np.str_('besser verstehen'), 15, 
     {1: ['leichter begreifen'], 2: ['klarer erfassen', 'deutlicher verstehen', 'einfacher nachvollziehen', 'verständlicher erklären']}],

    [np.str_('Die Präsidentin gab eine Rede vor einer großen Menschenmenge'), 
     np.str_('Rede'), 
     2, 
     {1: ['Ansage'], 2: ['Ansprache', 'Vortrag', 'Statement', 'Äußerung']}],
     
    [np.str_('Der Fußballspieler schoss ein Tor und jubelte anschließend'), 
     np.str_('Jubelte'), 
     1, 
     {1: ['freute sich'], 2: ['feierte', 'johlte', 'jauchzte']}],
     
    [np.str_('Die Studenten nahmen an einer Demonstration gegen den Klimawandel teil'), 
     np.str_('Demonstration'), 
     2, 
     {1: ['Protest'], 2: ['Kundgebung', 'Aktion', 'Aufmarsch']}],
     
    [np.str_('Die Polizei nahm den Dieb fest und brachte ihn zur Polizeistation'), 
     np.str_('Festnehmen'), 
     2, 
     {1: ['Verhaften'], 2: ['Inhaftieren', 'Festschreiben', 'Einkerkern']}],
     
    [np.str_('Das Paar verlobte sich nach fünf Jahren Beziehung'), 
     np.str_('Verloben'), 
     2, 
     {1: ['sich verloben'], 2: ['eine Verlobung eingehen', 'sich verbinden', 'sich vermählen']}],
     
    [np.str_('Die Krankenschwester pflegte den Patienten mit großer Sorgfalt'), 
     np.str_('pflegte'), 
     2, 
     {1: ['sorgte für'], 2: ['versorgte', 'betreute', 'begleitete']}],
     
    [np.str_('Der Lehrer lobte die Schüler für ihre gute Arbeit'), 
     np.str_('lobte'), 
     2, 
     {1: ['pries'], 2: ['anerkennend', 'belobigte', 'hervorhob']}],
     
    [np.str_('Die Köchin kochte ein köstliches Abendessen für ihre Familie'), 
     np.str_('köstliches'), 
     1, 
     {1: ['lecker'], 2: ['delikat', 'schmackhaft', 'kulinarisch']}],
     
    [np.str_('Der Arzt verschrieb dem Patienten Medikamente gegen die Grippe'), 
     np.str_('Medikamente'), 
     3, 
     {1: ['Arzneimittel'], 2: ['Heilmittel', 'Medizin', 'Präparat']}],
     
    [np.str_('Die Feuerwehr löschte den Brand in der Fabrik'), 
     np.str_('löschte'), 
     2, 
     {1: ['bekämpfte'], 2: ['auslöschte', 'erstickte', 'ausbrannte']}],
     
    [np.str_('Die Konferenz wurde aufgrund der aktuellen Situation online abgehalten'), 
     np.str_('abgehalten'), 
     5, 
     {1: ['durchgeführt'], 2: ['abgehalten', 'organisiert', 'veranstaltet']}],
     
    [np.str_('Die Lehrer bemühen sich, ihren Schülern ein interessantes Unterrichtserlebnis zu bieten'), 
     np.str_('Unterrichtserlebnis'), 
     15, 
     {1: ['Schulunterricht'], 2: ['Lernerfahrung', 'Bildungserfahrung', 'Schulbildungserfahrung']}],
     
    [np.str_('Die Studenten arbeiten hart, um gute Noten zu bekommen'), 
     np.str_('Noten'), 
     5, 
     {1: ['Bewertungen'], 2: ['GPA', 'Abschlussnoten', 'Leistungsbewertungen']}],
     
    [np.str_('Die Kinder spielen fröhlich im Park und genießen die Sonne'), 
     np.str_('fröhlich'), 
     8, 
     {1: ['glücklich'], 2: ['freudig', 'ausgelassen', 'lustig', 'heiter']}],
     
    [np.str_('Der Vater brachte seinem Sohn bei, wie man Fahrrad fährt'), 
     np.str_('brachte bei'), 
     10, 
     {1: ['lehrte'], 2: ['vermittelte', 'instruierte', 'erklärte', 'zeigte']}],
     
    [np.str_('Die Blumen blühen im Frühling in allen Farben'), 
     np.str_('blühen'), 
     6, 
     {1: ['erblühen'], 2: ['aufblühen', 'erwachen', 'erstrahlen']}],
     
    [np.str_('Das Buch, das ich gelesen habe, war sehr spannend und fesselnd'), 
     np.str_('spannend'), 
     7, 
     {1: ['aufregend'], 2: ['packend', 'faszinierend', 'mitreißend', 'mit Spannung']}],
     
    [np.str_('Die Flugreise dauerte lange, aber die Aussicht aus dem Flugzeugfenster war atemberaubend'), 
     np.str_('atemberaubend'), 
     12, 
     {1: ['beeindruckend'], 2: ['faszinierend', 'spektakulär', 'grandios', 'berauschend']}],
     
    [np.str_('Die Wissenschaftler erforschen die Tiefen des Ozeans, um mehr über das marine Leben zu erfahren'), 
     np.str_('Tiefen des Ozeans'), 
     18, 
     {1: ['Meeresgrund'], 2: ['ozeanische Tiefen', 'Unterwasserwelten', 'Marinemilieu']}],
     
    [np.str_('Die Polizei nahm den Verdächtigen fest und brachte ihn ins Gefängnis'), 
     np.str_('nahm fest'), 
     8, 
     {1: ['verhaftete'], 2: ['festnahm', 'in Gewahrsam nahm', 'dingfest machte']}],
     
    [np.str_('Die Geschwister stritten sich oft, aber am Ende des Tages waren sie wieder versöhnt'), 
     np.str_('wieder versöhnt'), 
     13, 
     {1: ['wieder versöhnt'], 2: ['sich wieder vertragen', 'die Differenzen beigelegt', 'die Streitigkeiten bereinigt']}],
     
    [np.str_('Das Musikfestival zog Tausende von Besuchern an, die die verschiedenen Bands und Künstler genießen wollten'), 
     np.str_('Besucher'), 
     8, 
     {1: ['Gäste'], 2: ['Festivalteilnehmer', 'Zuschauer', 'Konzertgänger']}],
     
    [np.str_('Die Arbeiter streiken für bessere Arbeitsbedingungen und höhere Löhne'), 
     np.str_('Arbeitsbedingungen'), 
     17, 
     {1: ['Arbeitsumstände'], 2: ['Berufsbedingungen', 'Tätigkeitsbedingungen', 'Arbeitsverhältnisse']}],
     
    [np.str_('Das neue Restaurant bietet eine Vielzahl von kulinarischen Köstlichkeiten an'), 
     np.str_('kulinarischen Köstlichkeiten'), 
     20, 
     {1: ['Essensspezialitäten'], 2: ['delikate Speisen', 'Gourmetgerichte', 'Feinschmeckerkost', 'Spezialitäten']}],
     
    [np.str_('Die Wanderer genossen die unberührte Natur und die frische Luft der Berge'), 
     np.str_('unberührte Natur'), 
     13, 
     {1: ['ungestörte Natur'], 2: ['naturbelassene Umgebung', 'natürliche Wildnis', 'intakte Natur']}],
     
    [np.str_('Die Schüler übten fleißig für ihre Abschlussprüfungen, um gute Noten zu erhalten'), 
     np.str_('Abschlussprüfungen'), 
     17, 
     {1: ['Finalprüfungen'], 2: ['Abschlussklausuren', 'Schlussprüfungen', 'Endexamen']}],
     
    [np.str_('Das Unternehmen hat eine neue Technologie eingeführt, um die Effizienz seiner Produktionsprozesse zu verbessern'), 
     np.str_('Effizienz'), 
     8, 
     {1: ['Leistungsfähigkeit'], 2: ['Wirksamkeit', 'Effektivität', 'Produktivität']}],
     
    [np.str_('Die Regierung setzt sich für den Umweltschutz ein und fördert nachhaltige Entwicklungsprojekte'), 
     np.str_('nachhaltige Entwicklungsprojekte'), 
     25, 
     {1: ['langfristige Entwicklungsprojekte'], 
      2: ['umweltfreundliche Projekte', 'zukunftsorientierte Projekte', 'nachhaltige Vorhaben']}],
     
    [np.str_('Die Freiwilligen halfen bei der Verteilung von Lebensmitteln an Bedürftige in der Gemeinde'), 
     np.str_('an Bedürftige'), 
     12, 
     {1: ['an Bedürftige'], 2: ['an hilfsbedürftige Menschen', 'an Bedürftige Personen', 'an Bedürftigen']}],
     
    [np.str_('Die Forscher entdeckten eine neue Spezies im Amazonas-Dschungel, die zuvor unbekannt war'), 
     np.str_('zuvor unbekannt'), 
     14, 
     {1: ['bisher unbekannt'], 2: ['vorher unbekannt', 'früher unbekannt', 'bislang unbekannt']}],

     [np.str_('Die Regierung plant einen Rückgang der Arbeitslosenquote durch neue Maßnahmen'), 
     np.str_('Rückgang'), 
     5, 
     {1: ['Abnahme', 'Verminderung', 'Senkung']}],
     
    [np.str_('Die Schüler müssen für die Prüfung hart lernen, um gute Noten zu bekommen'), 
     np.str_('hart'), 
     3, 
     {1: ['intensiv', 'fleißig', 'ausgiebig']}],
     
    [np.str_('Die Firma plant, ihre Produktion zu erweitern, um mehr Produkte herzustellen'), 
     np.str_('erweitern'), 
     4, 
     {1: ['vergrößern', 'ausbauen', 'erhöhen']}],
     
    [np.str_('Die Wissenschaftler haben eine Entdeckung gemacht, die ihr Verständnis des Universums verändert hat'), 
     np.str_('Entdeckung'), 
     10, 
     {1: ['Fund', 'Erkenntnis', 'Neufund']}],
     
    [np.str_('Der Patient benötigt eine Operation, um sein Problem zu lösen'), 
     np.str_('Operation'), 
     9, 
     {1: ['Eingriff', 'OP', 'Chirurgie']}],
     
    [np.str_('Der Lehrer verwendet verschiedene Methoden, um den Schülern den Lernstoff näherzubringen'), 
     np.str_('Methoden'), 
     7, 
     {1: ['Techniken', 'Verfahren', 'Ansätze']}],
     
    [np.str_('Die Streikenden fordern eine Erhöhung ihrer Gehälter, um ihre Lebenshaltungskosten decken zu können'), 
     np.str_('Erhöhung'), 
     8, 
     {1: ['Anstieg', 'Steigerung', 'Zunahme']}],
     
    [np.str_('Die Forscher haben eine neue Theorie entwickelt, um das Phänomen zu erklären'), 
     np.str_('Theorie'), 
     6, 
     {1: ['Hypothese', 'Modell', 'Ansatz']}],
     
    [np.str_('Der Künstler malt ein Bild, das seine Emotionen ausdrückt'), 
     np.str_('Emotionen'), 
     10, 
     {1: ['Gefühle', 'Empfindungen', 'Stimmungen']}],
     
    [np.str_('Die Firma plant, neue Produkte auf den Markt zu bringen, um ihre Umsätze zu steigern'), 
     np.str_('steigern'), 
     8, 
     {1: ['erhöhen', 'vergrößern', 'anstreben']}],
     
    [np.str_('Die Krankenschwester pflegt den Patienten nach der Operation, um seine Genesung zu unterstützen'), 
     np.str_('Genesung'), 
     8, 
     {1: ['Heilung', 'Wiederherstellung', 'Regeneration']}],
     
    [np.str_('Der Chef lobt die Mitarbeiter für ihre hervorragende Leistung bei der letzten Präsentation'), 
     np.str_('hervorragende'), 
     11, 
     {1: ['ausgezeichnete', 'herausragende', 'exzellente']}],
     
    [np.str_('Der Coach motiviert das Team, um ihre Leistung im nächsten Spiel zu verbessern'), 
     np.str_('Leistung'), 
     7, 
     {1: ['Performance', 'Darbietung', 'Output']}],
     
    [np.str_('Die Lehrerin lobt die Schüler für ihre gute Zusammenarbeit bei der Gruppenarbeit'), 
     np.str_('Zusammenarbeit'), 
     14, 
     {1: ['Kooperation', 'Teamarbeit', 'Kollaboration']}],
     
    [np.str_('Der Autor hat ein Buch über sein Leben geschrieben, das sehr erfolgreich wurde'), 
     np.str_('erfolgreich'), 
     9, 
     {1: ['erfolgsvoll', 'erfolgreich verlaufen', 'glänzend']}],
     
    [np.str_('Die Firma investiert in neue Technologien, um wettbewerbsfähig zu bleiben'), 
     np.str_('wettbewerbsfähig'), 
     14, 
     {1: ['konkurrenzfähig', 'leistungsfähig', 'markttauglich']}],
     
    [np.str_('Der Auszubildende lernt verschiedene Fähigkeiten, um in seinem Beruf erfolgreich zu sein'), 
     np.str_('Erfolg'), 
     6, 
     {1: ['Gelingen', 'Erfolgserlebnis', 'glücklicher Ausgang']}],
     
    [np.str_('Der Musiker komponiert ein neues Lied, das seine künstlerische Kreativität zeigt'), 
     np.str_('Kreativität'), 
     11, 
     {1: ['Schöpferkraft', 'Gestaltungsfreude', 'Fantasie']}],
     
    [np.str_('Die Schüler arbeiten gemeinsam an einem Projekt, um die Aufgabe zu bewältigen'), 
     np.str_('bewältigen'), 
     10, 
     {1: ['meistern', 'schaffen', 'handhaben']}],
     
    [np.str_('Die Fabrik optimiert ihre Produktionsprozesse, um effizienter zu arbeiten'), 
     np.str_('optimiert'), 
     10, 
     {1: ['verbessert', 'perfektioniert', 'steigert die Effizienz']}],
     
    [np.str_('Die Regierung hat beschlossen, die Steuern zu senken, um die Wirtschaft anzukurbeln'), 
     np.str_('anzukurbeln'), 
     11, 
     {1: ['anzuheizen', 'voranzutreiben', 'in Fahrt zu bringen']}],
     
    [np.str_('Der Wissenschaftler entdeckt eine neue Spezies, die bislang unbekannt war'), 
     np.str_('entdeckt'), 
     8, 
     {1: ['aufgespürt', 'gefunden', 'ausfindig gemacht']}],
     
    [np.str_('Die Politiker diskutieren Maßnahmen zur Verbesserung des Bildungssystems'), 
     np.str_('Verbesserung'), 
     12, 
     {1: ['Verbesserungsmaßnahmen', 'Optimierung', 'Fortschritt']}],
     
    [np.str_('Die Krankenschwester kümmert sich um die Patienten, um ihre Genesung zu beschleunigen'), 
     np.str_('beschleunigen'), 
     13, 
     {1: ['vorantreiben', 'schneller machen', 'Speed-up']}],
     
    [np.str_('Die Veranstalter planen ein neues Event, um das Interesse der Besucher zu wecken'), 
     np.str_('Interesse'), 
     9, 
     {1: ['Aufmerksamkeit', 'Neugier', 'Begeisterung']}],
     
    [np.str_('Die Forscher führen Experimente durch, um neue Erkenntnisse zu gewinnen'), 
     np.str_('Erkenntnisse'), 
     11, 
     {1: ['Erkenntnisgewinn', 'Forschungsergebnisse', 'Einsichten']}],
     
    [np.str_('Die Schüler arbeiten hart an ihren Projekten, um gute Noten zu erhalten'), 
     np.str_('hart'), 
     3, 
     {1: ['intensiv', 'fleißig', 'ausgiebig']}],
     
    [np.str_('Der Künstler malt ein Bild, das seine Gefühle widerspiegelt'), 
     np.str_('Gefühle'), 
     7, 
     {1: ['Emotionen', 'Empfindungen', 'Stimmungen']}],
     
    [np.str_('Die Forscher haben eine neue Theorie entwickelt, um das Phänomen zu erklären'), 
     np.str_('Theorie'), 
     6, 
     {1: ['Hypothese', 'Modell', 'Ansatz']}],
     
    [np.str_('Die Firma plant, neue Produkte auf den Markt zu bringen, um ihre Umsätze zu steigern'), 
     np.str_('steigern'), 
     8, 
     {1: ['erhöhen', 'vergrößern', 'anstreben']}],
     
    [np.str_('Die Krankenschwester pflegt den Patienten nach der Operation, um seine Genesung zu unterstützen'), 
     np.str_('Genesung'), 
     8, 
     {1: ['Heilung', 'Wiederherstellung', 'Regeneration']}],



#original_data = germaneval_data_provider.GermanEvalDataProvider().provide_data_as_numpy_array()
#dataset = original_data[7:21]


    [np.str_('Die Schüler freuten sich über den Ausflug ins Naturkundemuseum, wo sie viele interessante Fossilien und Dinosaurierskelette sehen konnten'), 
     np.str_('Fossilien'), 
     5, 
     {1: ['Versteinerungen', 'Urfossilien'], 2: ['alte Überreste', 'ausgegrabene Überreste', 'prähistorische Funde']}],
    
    [np.str_('Die Lehrerin erklärte den Schülern geduldig die komplizierten mathematischen Formeln, bis alle sie verstanden haben'), 
     np.str_('mathematischen Formeln'), 
     7, 
     {1: ['Rechenausdrücke', 'Berechnungsvorschriften'], 2: ['Zahlenformeln', 'Mathegleichungen', 'Rechenregeln']}],
    
    [np.str_('Der Gärtner pflanzte die bunten Blumen im Garten, um eine fröhliche und lebhafte Atmosphäre zu schaffen'), 
     np.str_('bunten Blumen'), 
     3, 
     {1: ['farbenfrohe Blumen'], 2: ['vielfarbige Blüten']}],
    
    [np.str_('Die Straßen waren nach dem starken Regen überschwemmt und die Autofahrer mussten langsam und vorsichtig fahren'), 
     np.str_('überschwemmt'), 
     7, 
     {1: ['überflutet', 'unter Wasser stehend'], 2: ['überfließend', 'überbordend', 'übergebend']}],
    
    [np.str_('Die Katze kletterte geschickt auf den Baum, um einen besseren Überblick über den Garten zu bekommen'), 
     np.str_('geschickt'), 
     5, 
     {1: ['gewandt', 'geschmeidig'], 2: ['geschickt handelnd', 'routiniert', 'gekonnt']}],
    
    [np.str_('Die Modedesignerin entwarf eine neuartige Kollektion von Kleidungsstücken, die viele Menschen begeisterte'), 
     np.str_('neuartige Kollektion'), 
     10, 
     {1: ['innovative Auswahl', 'frische Kollektion'], 2: ['ungewöhnliche Zusammenstellung', 'originelle Serie', 'kreative Sammlung']}],
    
    [np.str_('Das Konzert der berühmten Band war ein voller Erfolg und die Zuschauer waren begeistert von der Musik'), 
     np.str_('berühmten Band'), 
     4, 
     {1: ['bekannten Gruppe'], 2: ['populären Band', 'renommierten Ensemble']}],
    
    [np.str_('Die Schriftstellerin gewann einen renommierten Literaturpreis für ihr neuestes Buch, das von Kritikern hochgelobt wurde'), 
     np.str_('renommierten Literaturpreis'), 
     10, 
     {1: ['angesehenen Buchauszeichnung', 'bekannten Schriftstellerpreis'], 2: ['gefeierten Autorenpreis', 'angesehenen Literaturaward', 'geschätzten Bücherpreis']}],
    
    [np.str_('Die Maschine arbeitete effizient und zuverlässig, was die Produktivität des Unternehmens steigerte'), 
     np.str_('effizient und zuverlässig'), 
     8, 
     {1: ['effektiv und verlässlich'], 2: ['leistungsfähig und stabil', 'wirkungsvoll und sicher']}],
    
    [np.str_('Die Kinder spielten ausgelassen im Garten und hatten dabei viel Spaß und Freude'), 
     np.str_('ausgelassen'), 
     3, 
     {1: ['fröhlich'], 2: ['lustig', 'heiter', 'ausgelassen fröhlich']}],
    
    [np.str_('Die Forscher entdeckten eine neue Art von Bakterien in der Tiefsee, die bisher unbekannt war'), 
     np.str_('neue Art von Bakterien'), 
     6, 
     {1: ['unbekannte Bakterienart', 'neuartige Bakteriengattung'], 2: ['frische Bakterienform', 'überraschende Bakterienspezies']}],
    
    [np.str_('Die Astronauten schwebten schwerelos im Weltraum und genossen den Blick auf die Erde von oben'), 
     np.str_('schwerelos'), 
     7, 
     {1: ['gravitationslos', 'ohne Gewicht'], 2: ['leichtfrei', 'gewichtsfrei', 'ohne Schwere']}],
    
    [np.str_('Die Krankenschwester kümmerte sich liebevoll um die Patienten und sorgte dafür, dass es ihnen an nichts fehlte'), 
     np.str_('liebevoll'), 
     3, 
     {1: ['herzlich'], 2: ['fürsorglich', 'zärtlich', 'liebevoll sorgend']}],
    
    [np.str_('Der Architekt entwarf ein modernes Gebäude mit einer innovativen und futuristischen Gestaltung'), 
     np.str_('futuristischen Gestaltung'), 
     7, 
     {1: ['zukunftsweisenden Design', 'visionären Aufbau'], 2: ['fortschrittlichen Stil', 'zukunftsgerichteten Entwurf']}],
    
    [np.str_('Die Wissenschaftler untersuchten die Auswirkungen des Klimawandels auf die Umwelt und fanden alarmierende Ergebnisse'), 
     np.str_('alarmierende Ergebnisse'), 
     5, 
     {1: ['besorgniserregende Resultate', 'beunruhigende Erkenntnisse'], 2: ['beunruhigende Resultate', 'erschreckende Informationen']}],
    
    [np.str_('Die Künstlerin malte ein beeindruckendes Gemälde, das die Betrachter in seinen Bann zog'), 
     np.str_('beeindruckendes Gemälde'), 
     6, 
     {1: ['imposantes Kunstwerk', 'eindrucksvolles Bild'], 2: ['grandioses Gemälde', 'beeindruckende Malerei']}],
    
    [np.str_('Der Musiker komponierte eine melodische Symphonie, die die Herzen der Zuhörer berührte'), 
     np.str_('melodische Symphonie'), 
     5, 
     {1: ['harmonische Musikstück', 'wohlklingende Komposition'], 2: ['melodiöse Orchestermusik', 'harmonische Symphonie']}],
    
    [np.str_('Der Regisseur drehte einen aufwendigen Film mit spektakulären Effekten und anspruchsvollen Kulissen'), 
     np.str_('aufwendigen Film'), 
     7, 
     {1: ['kostspieligen Streifen', 'aufwändigen Kinofilm'], 2: ['anspruchsvollen Film', 'elaborierten Spielfilm']}],
    
    [np.str_('Das Festival lockte zahlreiche Besucher an, die die vielfältigen Veranstaltungen und Darbietungen genossen'), 
     np.str_('vielfältigen Veranstaltungen'), 
     5, 
     {1: ['abwechslungsreiche Events', 'bunte Veranstaltungen'], 2: ['diverse Vorführungen', 'verschiedene Aufführungen']}],
    
    [np.str_('Die Tänzerinnen führten eine zauberhafte Ballettvorstellung auf, die das Publikum begeisterte'), 
     np.str_('zauberhafte Ballettvorstellung'), 
     6, 
     {1: ['magische Tanzdarbietung', 'verzaubernde Ballettaufführung'], 2: ['zauberhafte Ballettdarbietung', 'märchenhafte Tanzvorführung']}],
    
    [np.str_('Der Zauberer zeigte atemberaubende Tricks und Illusionen, die die Zuschauer faszinierten'), 
     np.str_('atemberaubende Tricks'), 
     7, 
     {1: ['beeindruckende Tricks', 'verblüffende Illusionen'], 2: ['faszinierende Zaubertricks', 'sensationelle Zaubereien']}],
    
    [np.str_('Die Köchin kochte ein köstliches Gericht mit frischen Zutaten, das allen Gästen vorzüglich schmeckte'), 
     np.str_('köstliches Gericht'), 
     7, 
     {1: ['delikates Gericht', 'feines Essen'], 2: ['schmackhaftes Menü', 'exquisite Speise']}],
    
    [np.str_('Die Reisenden erkundeten abenteuerliche Orte und erlebten aufregende Abenteuer während ihrer Reise'), 
     np.str_('abenteuerliche Orte'), 
     5, 
     {1: ['spannende Orte', 'aufregende Locations'], 2: ['abenteuerliche Gegenden', 'aufregende Landschaften']}],
    
    [np.str_('Der Arzt untersuchte den Patienten gründlich und stellte schließlich die Diagnose einer schweren Erkrankung'), 
     np.str_('schweren Erkrankung'), 
     8, 
     {1: ['schwerwiegenden Krankheit', 'ernsten Leiden'], 2: ['kritischen Gesundheitszustand', 'bedrohliches Leiden']}],
    
    [np.str_('Die Forscher entwickelten eine bahnbrechende Technologie, die die gesamte Branche revolutionieren könnte'), 
     np.str_('bahnbrechende Technologie'), 
     7, 
     {1: ['wegweisende Innovation', 'visionäre Technik'], 2: ['revolutionäre Erfindung', 'innovative Methode']}],
    
    [np.str_('Die Lehrerin lobte die Schüler für ihre hervorragenden Leistungen und ermunterte sie, weiterhin ihr Bestes zu geben'), 
     np.str_('hervorragenden Leistungen'), 
     6, 
     {1: ['exzellenten Erfolgen', 'herausragenden Leistungen'], 2: ['spitzenmäßigen Leistungen', 'überragenden Ergebnissen']}],
    
    [np.str_('Die Eltern feierten den Geburtstag ihres Sohnes mit einer fröhlichen Party und einer großen Torte'), 
     np.str_('fröhlichen Party'), 
     3, 
     {1: ['lustigen Feier'], 2: ['ausgelassenen Fest', 'heiteren Zusammenkunft']}],

#dataset = original_data[23:33]

    [np.str_('Das Mädchen spielt im Garten mit einem bunten Ball'), 
     np.str_('spielt'), 
     4, 
     {1: ['toben', 'amüsieren', 'unterhalten', 'den Ball bewegen', 'sich amüsieren', 'Ball spielen', 'herumtollen']}],
    
    [np.str_('Der alte Mann zieht sich warme Kleidung an, bevor er nach draußen geht'), 
     np.str_('anziehen'), 
     7, 
     {1: ['sich kleiden', 'bekleiden', 'Kleidung tragen', 'Kleidung anlegen', 'sich anziehen', 'Kleidung anziehen']}],
    
    [np.str_('Die Katze schläft auf dem gemütlichen Sofa'), 
     np.str_('schläft'), 
     5, 
     {1: ['ruht', 'döst', 'traumt', 'schläft', 'dämmert', 'ruht sich aus']}],
    
    [np.str_('Der Junge isst gerne Eis in der heißen Sommersonne'), 
     np.str_('isst'), 
     4, 
     {1: ['sich ernähren', 'speisen', 'naschen', 'Eis essen', 'verzehren', 'sich sättigen']}],
    
    [np.str_('Die Familie plant einen Ausflug in den nahe gelegenen Park'), 
     np.str_('plant'), 
     6, 
     {1: ['überlegt', 'vorbereitet', 'plant', 'sich vorbereiten', 'organisiert', 'plant vor']}],
    
    [np.str_('Die Blumen blühen im Frühling in vielen verschiedenen Farben'), 
     np.str_('blühen'), 
     6, 
     {1: ['erblühen', 'blühend', 'aufblühen', 'sich entfalten', 'aufgehen', 'blühen']}],
    
    [np.str_('Der Schüler lernt für die bevorstehende Prüfung'), 
     np.str_('lernt'), 
     5, 
     {1: ['studiert', 'lernt', 'übt', 'sich vorbereitet', 'Wissen aneignen']}],
    
    [np.str_('Die Vögel singen fröhlich in den Bäumen'), 
     np.str_('singen'), 
     6, 
     {1: ['trällern', 'zwitschern', 'piepen', 'singend', 'fröhlich singen', 'Liedchen trällern']}],
    
    [np.str_('Die Sonne scheint hell am wolkenlosen Himmel'), 
     np.str_('scheint'), 
     5, 
     {1: ['leuchtet', 'glänzt', 'strahlt', 'scheint', 'hell scheinen', 'sich zeigen']}],
    
    [np.str_('Die Kinder spielen im Sandkasten und bauen eine Burg'), 
     np.str_('spielen'), 
     6, 
     {1: ['tollen', 'spielen', 'sich vergnügen', 'sich unterhalten', 'sich amüsieren', 'spielen']}],
    
    [np.str_('Der Hund bellt fröhlich, als er seinen Besitzer sieht'), 
     np.str_('bellt'), 
     4, 
     {1: ['kläffen', 'bellen', 'jaulen', 'freudig bellen', 'fröhlich bellen', 'freudig kläffen']}],
    
    [np.str_('Die Frau fährt mit dem Fahrrad zur Arbeit'), 
     np.str_('fährt'), 
     5, 
     {1: ['bewegt sich', 'reist', 'fährt', 'sich fortbewegen', 'mit dem Fahrrad unterwegs sein', 'fahren']}],
    
    [np.str_('Der Mann läuft im Park und genießt die frische Luft'), 
     np.str_('läuft'), 
     5, 
     {1: ['rennt', 'spaziert', 'geht', 'läuft', 'sich bewegen', 'läuft herum']}],
    
    [np.str_('Die Kinder lachen laut, während sie im Garten spielen'), 
     np.str_('lachen'), 
     5, 
     {1: ['kichern', 'fröhlich sein', 'herzlich lachen', 'lachen', 'spaß haben', 'lachen']}],
    
    [np.str_('Der Apfelbaum trägt im Herbst viele reife Früchte'), 
     np.str_('trägt'), 
     6, 
     {1: ['produziert', 'erzeugt', 'hervorbringen', 'tragen', 'Früchte hervorbringen', 'ernten']}],
    
    [np.str_('Der Lehrer erklärt den Schülern das neue Thema'), 
     np.str_('erklärt'), 
     7, 
     {1: ['darlegt', 'interpretiert', 'erläutert', 'erklären', 'beschreiben', 'verdeutlichen']}],
    
    [np.str_('Der Künstler malt ein Bild auf der Leinwand'), 
     np.str_('malt'), 
     4, 
     {1: ['künstlerisch gestalten', 'malen', 'zeichnen', 'Kunst schaffen', 'ausmalen', 'kreativ gestalten']}],
    
    [np.str_('Die Katze jagt die Maus über die Wiese'), 
     np.str_('jagt'), 
     5, 
     {1: ['verfolgt', 'hetzt', 'jagt', 'jagen', 'nachjagen', 'hinterherjagen']}],
    
    [np.str_('Der Autofahrer hupt, um die anderen Verkehrsteilnehmer zu warnen'), 
     np.str_('hupt'), 
     4, 
     {1: ['signalisiert', 'tutet', 'hupt', 'sich bemerkbar machen', 'warnen', 'signal geben']}],
    
    [np.str_('Die Bäume rauschen im Wind'), 
     np.str_('rauschen'), 
     5, 
     {1: ['flüstern', 'säuseln', 'plätschern', 'sanft rauschen', 'rauschen', 'wehen']}],
    
    [np.str_('Die Eule ruft in der Nacht'), 
     np.str_('ruft'), 
     4, 
     {1: ['schreit', 'tönt', 'ruft', 'rufen', 'wimmern', 'schallen']}],
    
    [np.str_('Die Biene summt fleißig um die Blumen herum'), 
     np.str_('summt'), 
     5, 
     {1: ['sirrt', 'summt', 'brummt', 'summen', 'fließig summen', 'beschwirrt']}],
    
    [np.str_('Die Kinder rennen fröhlich umher und spielen Fangen'), 
     np.str_('rennen'), 
     5, 
     {1: ['rasen', 'schnell laufen', 'sausen', 'sich bewegen', 'fröhlich rennen', 'umher rennen']}],
    
    [np.str_('Der Regen prasselt gegen das Fenster'), 
     np.str_('prasselt'), 
     7, 
     {1: ['trommeln', 'klopfen', 'stürmen', 'hageln', 'prasseln', 'donnern']}],
    
    [np.str_('Die Katze schleicht sich leise an die Maus heran'), 
     np.str_('schleicht'), 
     5, 
     {1: ['pirscht', 'schleicht sich', 'sich anschleichen', 'still schleichen', 'leise schleichen', 'sich heranschleichen']}],
    
    [np.str_('Der Vogel zwitschert im Baum'), 
     np.str_('zwitschert'), 
     6, 
     {1: ['trillert', 'zwitschert', 'piept', 'Vogelzwitschern', 'fröhlich zwitschern', 'singt']}],
    
    [np.str_('Die Sonne geht langsam unter und taucht den Himmel in warme Farben'), 
     np.str_('geht unter'), 
     9, 
     {1: ['versinkt', 'sinken', 'verschwinden', 'untergehen', 'sich senken', 'verschwinden']}],
    
    [np.str_('Der Gärtner gießt die Blumen im Beet'), 
     np.str_('gießt'), 
     5, 
     {1: ['wässert', 'bewässert', 'gießen', 'bewässern', 'Blumen gießen', 'sich um die Pflanzen kümmern']}],
    
    [np.str_('Der Koch würzt das Essen mit verschiedenen Kräutern'), 
     np.str_('würzt'), 
     6, 
     {1: ['verfeinert', 'assoziiert', 'aromatisierend', 'würzen', 'mit Gewürzen versehen', 'verwürzen']}],
    
    [np.str_('Die Wolken ziehen schnell über den Himmel'), 
     np.str_('ziehen'), 
     5, 
     {1: ['wander', 'fliegen', 'ziehen', 'bewegen', 'sich bewegen', 'weiterziehen']}],
    
    [np.str_('Die Kinder baden im kalten See und plantschen fröhlich im Wasser'), 
     np.str_('plantschen'), 
     7, 
     {1: ['plantschen', 'planschen', 'plantschen', 'sich vergnügen', 'Im Wasser spielen', 'sich amüsieren', 'herumtollen']}],
    
    [np.str_('Der Wanderer erklimmt den steilen Berg'), 
     np.str_('erklimmt'), 
     7, 
     {1: ['besteigt', 'ersteigt', 'hinaufklettern', 'erklimmen', 'den Berg erklimmen', 'sich erheben']}],

#dataset = original_data[33:43]

    [np.str_('Die Katze streicht um die Beine ihres Besitzers und miaut lautstark'), 
     np.str_('miaut'), 
     8, 
     {1: ['macht miau', 'laut miauen', 'miauen'], 2: ['macht Geräusche', 'Töne von sich geben', 'miauen']}],
    
    [np.str_('Er trank einen großen Schluck aus der Flasche'), 
     np.str_('Schluck'), 
     1, 
     {1: ['Trinken', 'Zug', 'Sippen'], 2: ['Trinken', 'Zug', 'Sippen']}],
    
    [np.str_('Die Vögel zwitschern fröhlich in den Bäumen'), 
     np.str_('zwitschern'), 
     4, 
     {1: ['pfeifen', 'flöten'], 2: ['machen Vogelgeräusche', 'Vogelrufe von sich geben']}],
    
    [np.str_('Das Baby lachte laut und strahlte vor Freude'), 
     np.str_('strahlte'), 
     3, 
     {1: ['glänzte', 'leuchtete'], 2: ['ausstrahlen', 'freudig sein', 'glücklich sein']}],
    
    [np.str_("Die Sonne scheint hell am Himmel und wärmt die Menschen"), 
     np.str_('scheint'), 
     3, 
     {1: ['leuchtet', 'strahlt'], 2: ['lichten', 'helle Lichtemission haben']}],
    
    [np.str_('Die Blumen blühen bunt im Garten'), 
     np.str_('blühen'), 
     2, 
     {1: ['aufblühen', 'florieren'], 2: ['wachsen und blühen', 'blühend sein']}],
    
    [np.str_('Der Wind weht stark und lässt die Blätter rascheln'), 
     np.str_('weht'), 
     2, 
     {1: ['bläst'], 2: ['stürmisch blasen', 'Luftbewegung erzeugen']}],
    
    [np.str_('Das Wasser plätschert leise im Bach'), 
     np.str_('plätschert'), 
     3, 
     {1: ['rauscht', 'säuselt'], 2: ['leise fließt', 'sanft fließt']}],
    
    [np.str_('Der Hahn kräht früh am Morgen'), 
     np.str_('kräht'), 
     2, 
     {1: ['gackert'], 2: ['Hahnenruf lassen hören', 'rufen']}],
    
    [np.str_('Die Sterne funkeln hell am Nachthimmel'), 
     np.str_('funkeln'), 
     3, 
     {1: ['glitzern', 'schimmern'], 2: ['leuchten', 'strahlen']}],
    
    [np.str_('Der Regen prasselt laut auf das Dach'), 
     np.str_('prasselt'), 
     3, 
     {1: ['trommelt', 'peitscht'], 2: ['stark regnet', 'regnet laut']}],
    
    [np.str_('Der Baum spendet angenehmen Schatten'), 
     np.str_('spendet'), 
     2, 
     {1: ['gibt', 'gewährt'], 2: ['schattet', 'Schatten spenden']}],
    
    [np.str_('Die Kinder spielen fröhlich im Garten'), 
     np.str_('spielen'), 
     2, 
     {1: ['tollen', 'herumtoben'], 2: ['Spaß haben', 'fröhlich sein']}],
    
    [np.str_('Der Postbote läutet an der Tür und übergibt einen Brief'), 
     np.str_('läutet'), 
     3, 
     {1: ['klingelt', 'ruft'], 2: ['Türklingel betätigen', 'klingeln']}],
    
    [np.str_('Die Lampe leuchtet hell im Zimmer'), 
     np.str_('leuchtet'), 
     2, 
     {1: ['strahlt', 'scheint'], 2: ['hell sein', 'Licht ausstrahlen']}],
    
    [np.str_('Die Katze schnurrt zufrieden auf dem Schoß ihres Besitzers'), 
     np.str_('schnurrt'), 
     4, 
     {1: ['maunzt', 'brummt'], 2: ['gibt Schnurrlaute von sich', 'sich wohlfühlen']}],
    
    [np.str_('Der Zug rattert laut auf den Schienen'), 
     np.str_('rattert'), 
     2, 
     {1: ['klappert', 'poltert'], 2: ['Geräusch machen', 'laut fahren']}],
    
    [np.str_('Die Musik erklingt laut aus den Lautsprechern'), 
     np.str_('erklingt'), 
     3, 
     {1: ['klingt', 'ertönt'], 2: ['hörbar sein', 'Musik spielen']}],
    
    [np.str_('Der Hund bellt laut vor Freude'), 
     np.str_('bellt'), 
     2, 
     {1: ['kläfft'], 2: ['freudig bellen', 'Hundelaute von sich geben']}],
    
    [np.str_('Die Tür quietscht beim Öffnen'), 
     np.str_('quietscht'), 
     3, 
     {1: ['knarzt', 'kreischt'], 2: ['Geräusch machen', 'quietschend sein']}],

    ###dataset = original_data[43:53]

    [np.str_("Sie gewann das Rennen mit einer beeindruckenden Zeit"), 
     np.str_('beeindruckend'), 
     7, 
     {1: ['imponierend', 'eindrucksvoll'], 2: ['bewundernswert', 'beeindruckend', 'erstaunlich', 'fantastisch', 'fabelhaft']}],
    
    [np.str_("Der Film erhielt großes Lob von Kritikern und Publikum gleichermaßen"), 
     np.str_('gleichermaßen'), 
     10, 
     {1: ['ebenso', 'genauso'], 2: ['gleichermaßen', 'in gleicher Weise', 'ebenfalls', 'auch']}],
    
    [np.str_('Der Autor hat eine faszinierende Geschichte über die Erkundung des Weltraums geschrieben'), 
     np.str_('faszinierend'), 
     10, 
     {1: ['beeindruckend', 'spannend'], 2: ['interessant', 'aufregend', 'faszinierend', 'packend', 'faszinierend']}],
    
    [np.str_('Die Veranstaltung zog eine große Menschenmenge an'), 
     np.str_('Menschenmenge'), 
     10, 
     {1: ['Menschenansammlung', 'Menge an Menschen'], 2: ['Crowd', 'Zuschauerschaft', 'Publikum']}],
    
    [np.str_('Das Projekt wurde mit umfangreichen Kostenüberschreitungen fertiggestellt'), 
     np.str_('Kostenüberschreitungen'), 
     8, 
     {1: ['Kostenerhöhung'], 2: ['Überschreitung des Budgets', 'Ausgabenüberschreitung']}],
    
    [np.str_('Wir haben eine umfassende Lösung für das Problem entwickelt'), 
     np.str_('umfassende'), 
     7, 
     {1: ['vollständige', 'ganzheitliche'], 2: ['ausführliche', 'umfassende', 'weitreichende']}],
    
    [np.str_('Die Präsentation war fesselnd und informativ zugleich'), 
     np.str_('fesselnd'), 
     7, 
     {1: ['packend', 'spannend'], 2: ['fesselnd', 'einnehmend', 'faszinierend']}],
    
    [np.str_('Seine Leistungen bei der Arbeit sind außergewöhnlich'), 
     np.str_('außergewöhnlich'), 
     14, 
     {1: ['besonders', 'herausragend'], 2: ['ungewöhnlich', 'außerordentlich', 'außergewöhnlich', 'einzigartig', 'bemerkenswert']}],
    
    [np.str_('Der Gewinn des Teams war immens'), 
     np.str_('immens'), 
     6, 
     {1: ['enorm', 'riesig'], 2: ['gewaltig', 'immens', 'überwältigend']}],
    
    [np.str_('Die Veränderungen haben einen deutlichen Rückgang der Umweltverschmutzung bewirkt'), 
     np.str_('deutlichen'), 
     9, 
     {1: ['klaren', 'erkennbaren'], 2: ['deutlichen', 'spürbaren', 'merklichen', 'wesentlichen']}],
    
    [np.str_('Der erfolgreiche Abschluss des Projekts wurde mit Begeisterung aufgenommen'), 
     np.str_('Begeisterung'), 
     13, 
     {1: ['Freude', 'Euphorie'], 2: ['Enthusiasmus', 'Faszination', 'Begeisterung', 'Leidenschaft', 'Feuereifer']}],
    
    [np.str_("Seine professionelle Arbeit wurde von allen Kollegen geschätzt"), 
     np.str_('geschätzt'), 
     9, 
     {1: ['anerkannt', 'gewürdigt'], 2: ['geschätzt', 'respektiert', 'hochgeachtet', 'geachtet']}],
    
    [np.str_("Das Unternehmen hat sich an die veränderten Marktbedingungen angepasst"), 
     np.str_('veränderten'), 
     10, 
     {1: ['neuen', 'modifizierten'], 2: ['veränderten', 'angepassten', 'adaptierten']}],
    
    [np.str_("Die Diskussion über den Einsatz erneuerbarer Energien wurde angeregt"), 
     np.str_('angeregt'), 
     8, 
     {1: ['ausgelöst', 'belebt'], 2: ['angeregt', 'beflügelt', 'stimuliert']}],
    
    [np.str_("Die Zusammenarbeit zwischen den Teams war vorbildlich"), 
     np.str_('vorbildlich'), 
     12, 
     {1: ['beispielhaft', 'hervorragend'], 2: ['vorbildlich', 'exemplarisch', 'mustergültig']}],
    
    [np.str_("Seine emotionalen Reaktionen waren überwältigend"), 
     np.str_('überwältigend'), 
     12, 
     {1: ['erdrückend', 'übermächtig'], 2: ['überwältigend', 'überwältigend', 'überragend', 'überwältigend']}],
    
    [np.str_("Die Schauspielerin erntete enormes Lob für ihre Darstellung"), 
     np.str_('enormes'), 
     6, 
     {1: ['riesiges', 'gewaltiges'], 2: ['enormes', 'überwältigendes', 'erhebliches']}],
    
    [np.str_("Seine Bemühungen zeigten ein beeindruckendes Ergebnis"), 
     np.str_('beeindruckendes'), 
     14, 
     {1: ['imponierendes', 'eindrucksvolles'], 2: ['bewundertes', 'beeindruckendes', 'fantastisches']}],

     ###dataset = original_data[53:63]

    [np.str_('Das Mädchen spielte fröhlich im Park'), 
     np.str_('fröhlich'), 
     7, 
     {1: ['glücklich', 'fröhlich und munter', 'freudig'], 
      2: ['ausgelassen', 'lebhaft', 'heiter', 'vergnügt']}],
    
    [np.str_('Der alte Mann war sehr müde und schlief sofort ein, als er ins Bett ging'), 
     np.str_('müde'), 
     5, 
     {1: ['erschöpft', 'abgespannt', 'schlapp'], 
      2: ['ermattet', 'schläfrig', 'verbraucht', 'kraftlos']}],
    
    [np.str_('Der laute Lärm des Verkehrs störte die Ruhe der kleinen Stadt'), 
     np.str_('Ruhe'), 
     5, 
     {1: ['Stille', 'Frieden', 'Gelassenheit'], 
      2: ['Tranquillität', 'Stille', 'Entspannung', 'Harmonie']}],
    
    [np.str_('Die Kinder hatten einen lustigen Tag im Freizeitpark'), 
     np.str_('lustigen'), 
     7, 
     {1: ['spaßigen', 'unterhaltsamen', 'vergnüglichen'], 
      2: ['amüsanten', 'lustvollen', 'humorvollen', 'freudigen']}],
    
    [np.str_('Der Abenteurer trotzte den Gefahren und erlebte spannende Abenteuer'), 
     np.str_('spannende'), 
     9, 
     {1: ['aufregende', 'packende', 'faszinierende'], 
      2: ['fesselnde', 'interessante', 'aufregende', 'nervenaufreibende']}],
    
    [np.str_('Der heftige Sturm riss die heruntergefallenen Blätter mit sich'), 
     np.str_('heftige'), 
     7, 
     {1: ['starke', 'kräftige', 'wilde'], 
      2: ['intensive', 'unkontrollierbare', 'gewaltige', 'rasante']}],

    
    [np.str_('Die schüchterne Katze versteckte sich hinter dem Sofa, als Besuch kam'), 
     np.str_('schüchterne'), 
     10, 
     {1: ['ängstliche', 'verschüchterte', 'zurückhaltende'], 
      2: ['unsichere', 'scheue', 'ängstliche', 'zaghafte']}],
    
    [np.str_('Das knisternde Feuer im Kamin verbreitete eine angenehme Wärme im Raum'), 
     np.str_('angenehme'), 
     8, 
     {1: ['wohlige', 'bequeme', 'warme'], 
      2: ['genüssliche', 'erfreuliche', 'behagliche', 'gemütliche']}],
    
    [np.str_('Die bunten Blumen blühten prächtig in dem Garten'), 
     np.str_('prächtig'), 
     8, 
     {1: ['farbenfroh'], 
      2: ['prachtvoll', 'üppig', 'opulent', 'prächtig blühend']}],
    
    [np.str_('Der kleine Junge war begeistert, als er das Geschenk öffnete'), 
     np.str_('begeistert'), 
     9, 
     {1: ['aufgeregt', 'freudig überrascht', 'erfreut'], 
      2: ['enthusiastisch', 'voller Euphorie', 'hocherfreut', 'vor Begeisterung funkensprühend']}],
    
    [np.str_('Die Melodie des Liedes war so melodisch, dass alle dazu tanzten'), 
     np.str_('melodisch'), 
     8, 
     {1: ['harmonisch', 'wohlklingend', 'schön klingend'], 
      2: ['tonvoll', 'stimmig', 'melodisch klingend', 'elegant']}],
    
    [np.str_('Der klare Himmel war mit unzähligen funkelnden Sternen übersät'), 
     np.str_('klare'), 
     5, 
     {1: ['reine', 'rein'], 
      2: ['klar verständlich', 'offensichtlich', 'klar strukturiert', 'transparent']}],
    
    [np.str_('Die friedliche Szene am See inspirierte den Maler zu einem Gemälde'), 
     np.str_('friedliche'), 
     9, 
     {1: ['ruhige', 'harmonische', 'idyllische'], 
      2: ['besinnliche', 'entspannte', 'heitere', 'sanfte']}],

    ##dataset = original_data[63:73]

    [np.str_('Die Teilnehmer der Studie wurden gebeten, anhand von Fragebögen ihre Meinungen und Einstellungen zu verschiedenen Themen zu äußern'), 
     np.str_('Teilnehmer'), 
     4, 
     {1: ['Beteiligte', 'Mitwirkende', 'Personen']}],
    
    [np.str_('Es ist wichtig, regelmäßig Sport zu treiben, um die Gesundheit und das Wohlbefinden zu fördern'), 
     np.str_('regelmäßig'), 
     4, 
     {1: ['oft', 'ständig', 'kontinuierlich']}],
    
    [np.str_('Die Mitarbeiter wurden gebeten, ihre Arbeitszeiten zu dokumentieren und mögliche Überstunden zu vermerken'), 
     np.str_('Überstunden'), 
     4, 
     {1: ['Mehrarbeit', 'Zusatzstunden', 'Extrastunden']}],
    
    [np.str_('Das Unternehmen plant, neue Produkte auf den Markt zu bringen, um seine Umsätze zu steigern'), 
     np.str_('Umsätze'), 
     4, 
     {1: ['Einnahmen', 'Gewinne', 'Erlöse']}],
    
    [np.str_('Die Schüler wurden gebeten, einen Aufsatz über ihr Lieblingsthema zu schreiben und dabei ihre Kreativität auszudrücken'), 
     np.str_('Kreativität'), 
     4, 
     {1: ['Innovationskraft', 'Einfallsreichtum', 'Schöpferkraft']}],
    
    [np.str_('Unsere Firma legt großen Wert auf eine positive Arbeitsatmosphäre und gegenseitiges Vertrauen zwischen den Mitarbeitern'), 
     np.str_('gegenseitiges'), 
     4, 
     {1: ['beidseitiges', 'wechselseitiges', 'wechselseitig']}],
    
    [np.str_('Es ist sinnvoll, sich regelmäßig fortzubilden und neue Kenntnisse zu erwerben, um beruflich erfolgreich zu sein'), 
     np.str_('fortzubilden'), 
     4, 
     {1: ['weiterzubilden', 'sich weiterbilden', 'fortzusetzen']}],
    
    [np.str_('Um Konflikte zu vermeiden, ist es wichtig, offen und ehrlich miteinander zu kommunizieren'), 
     np.str_('wichtig'), 
     4, 
     {1: ['bedeutsam', 'essentiell', 'relevant']}],
    
    [np.str_('Die Regierung plant, Maßnahmen zur Verbesserung der Luftqualität in stark belasteten Regionen zu ergreifen'), 
     np.str_('Maßnahmen'), 
     4, 
     {1: ['Schritte', 'Handlungen', 'Aktionen']}],
    
    [np.str_('Die Jugendlichen wurden ermutigt, sich ehrenamtlich zu engagieren und soziale Verantwortung zu übernehmen'), 
     np.str_('ehrenamtlich'), 
     4, 
     {1: ['unentgeltlich', 'freiwillig', 'ehrenvoll']}],
    
    [np.str_('Die Schule legt großen Wert darauf, individuelle Stärken und Talente der Schüler zu fördern und zu entwickeln'), 
     np.str_('individuelle'), 
     4, 
     {1: ['persönliche', 'eigene', 'einzigartige']}],
    
    [np.str_('Es ist ratsam, sich gesund zu ernähren und ausreichend zu bewegen, um die körperliche Fitness zu verbessern'), 
     np.str_('ratsam'), 
     4, 
     {1: ['empfehlenswert', 'zu empfehlen', 'angebracht']}],
    
    [np.str_('Die Forscher konnten im Rahmen ihrer Studie interessante Erkenntnisse zu diesem Thema gewinnen'), 
     np.str_('Erkenntnisse'), 
     4, 
     {1: ['Ergebnisse', 'Funde', 'Forschungsergebnisse']}],
    
    [np.str_('Es ist wichtig, Umweltschutzmaßnahmen zu unterstützen und sich für den Erhalt der Natur einzusetzen'), 
     np.str_('Umweltschutzmaßnahmen'), 
     4, 
     {1: ['Naturschutzmaßnahmen', 'Umweltschutzaktivitäten', 'Schutzmaßnahmen für die Umwelt']}],
    
    [np.str_('Die Mitarbeiter wurden ermutigt, konstruktives Feedback zu geben und Vorschläge zur Verbesserung des Arbeitsklimas einzubringen'), 
     np.str_('konstruktives'), 
     4, 
     {1: ['aufbauendes', 'positives', 'hilfreiches']}],
    
    [np.str_('Es ist wichtig, sich regelmäßig Zeit für Entspannung und Erholung zu nehmen, um Stress vorzubeugen'), 
     np.str_('vorzubeugen'), 
     4, 
     {1: ['zu vermeiden', 'zu verhindern', 'abzuwenden']}],
    
    [np.str_('Die Schüler wurden ermutigt, an einem Austauschprogramm teilzunehmen, um andere Kulturen kennenzulernen'), 
     np.str_('Austauschprogramm'), 
     4, 
     {1: ['Wechselprogramm', 'Programm zum Kulturaustausch', 'Kulturaustauschprogramm']}],
    
    [np.str_('Die Veranstaltung war gut organisiert und bot den Teilnehmern interessante Einblicke in aktuelle Forschungsthemen'), 
     np.str_('Einblicke'), 
     4, 
     {1: ['Einblick', 'Überblick', 'Eindrücke']}],
    
    [np.str_('Es ist wichtig, sich in schwierigen Situationen resilient zu zeigen und Herausforderungen aktiv anzugehen'), 
     np.str_('resilient'), 
     4, 
     {1: ['widerstandsfähig', 'belastbar', 'robust']}],
    
    [np.str_('Die Mitarbeiter wurden gebeten, sich aktiv an der Planung und Umsetzung neuer Projekte zu beteiligen'), 
     np.str_('beteiligen'), 
     4, 
     {1: ['mitwirken', 'sich einbringen', 'teilnehmen']}],
    
    [np.str_('Die Jugendlichen wurden ermutigt, ihre individuellen Interessen und Hobbys zu entdecken und zu verfolgen'), 
     np.str_('individuellen'), 
     4, 
     {1: ['persönlichen', 'eigenen', 'einzigartigen']}],
    
    [np.str_('Die Forscher konnten mithilfe moderner Technologien neue Erkenntnisse in ihrem Fachgebiet gewinnen'), 
     np.str_('Erkenntnisse'), 
     4, 
     {1: ['Ergebnisse', 'Funde', 'Forschungsergebnisse']}],
    
    [np.str_('Es ist wichtig, sich regelmäßig weiterzubilden und neue Fähigkeiten zu erlangen, um beruflich erfolgreich zu sein'), 
     np.str_('weiterzubilden'), 
     4, 
     {1: ['sich fortzubilden', 'weiterzuführen', 'sich weiterbilden']}],
    
    [np.str_('Die Gemeinde setzt sich aktiv für Umweltschutzprojekte ein und engagiert sich für nachhaltige Maßnahmen'), 
     np.str_('nachhaltige'), 
     4, 
     {1: ['langfristige', 'zukunftsorientierte', 'dauerhafte']}],
    
    [np.str_('Die Mitarbeiter wurden dazu ermutigt, konstruktive Kritik anzubringen und Verbesserungsvorschläge zu unterbreiten'), 
     np.str_('konstruktive'), 
     4, 
     {1: ['aufbauende', 'hilfreiche', 'positive']}],
    
    [np.str_('Es ist wichtig, regelmäßig Sport zu treiben, um die eigene Gesundheit und Fitness zu erhalten'), 
     np.str_('regelmäßig'), 
     4, 
     {1: ['häufig', 'kontinuierlich', 'ständig']}],
    
    [np.str_('Die Schüler wurden ermutigt, ihre Fähigkeiten und Talente durch kreative Projekte weiterzuentwickeln'), 
     np.str_('Fähigkeiten'), 
     4, 
     {1: ['Kompetenzen', 'Qualifikationen', 'Fertigkeiten']}],
    
    [np.str_('Es ist sinnvoll, sich regelmäßig Zeit für Entspannung und Erholung zu gönnen, um den Alltagsstress zu bewältigen'), 
     np.str_('bewältigen'), 
     4, 
     {1: ['zu meistern', 'zu überwinden', 'zu bewältigen']}],
    
    [np.str_('Die Mitarbeiter wurden dazu angehalten, respektvoll miteinander umzugehen und einen harmonischen Arbeitsplatz zu schaffen'), 
     np.str_('harmonischen'), 
     4, 
     {1: ['ausgeglichenen', 'ausgewogenen', 'stimmigen']}],
    
    [np.str_('Die Schüler wurden ermutigt, ihre individuellen Stärken und Fähigkeiten zu entdecken und weiterzuentwickeln'), 
     np.str_('individuellen'), 
     4, 
     {1: ['persönlichen', 'eigenen', 'einzigartigen']}],
    
    [np.str_('Es ist wichtig, sich gesund zu ernähren und ausreichend zu bewegen, um die körperliche Gesundheit zu erhalten'), 
     np.str_('Gesundheit'), 
     4, 
     {1: ['Wohlbefinden', 'Fitness', 'wohlergehen']}],

     ###dataset = original_data[73:83]

    [np.str_('Das Haus steht in Flammen und die Feuerwehr ist bereits auf dem Weg'), 
     np.str_('Flammen'), 
     4, 
     {1: ['Brand', 'Feuer', 'Inferno', 'Licht'], 2: ['Hitze', 'Gefahr', 'Katastrophe']}],
    
    [np.str_('Der Student hat eine umfangreiche Bibliographie für seine Abschlussarbeit zusammengestellt'), 
     np.str_('Bibliographie'), 
     2, 
     {1: ['Literaturliste'], 2: ['Quellenverzeichnis', 'Bibliothek']}],
    
    [np.str_('Die Sonne scheint hell am Himmel und die Vögel zwitschern fröhlich in den Bäumen'), 
     np.str_('zwitschern'), 
     3, 
     {1: ['singen', 'piepen', 'zwitschern', 'trällern'], 2: ['Lärm machen', 'Töne machen']}],
    
    [np.str_('Der Schüler hat eine gute Note in Mathematik bekommen und ist stolz auf seine Leistung'), 
     np.str_('Note'), 
     3, 
     {1: ['Bewertung', 'Zensur'], 2: ['Punktzahl', 'Ergebnis', 'Bewertung']}],
    
    [np.str_('Die Familie verbrachte den Tag gemeinsam im Park und genoss das schöne Wetter'), 
     np.str_('verbrachte'), 
     7, 
     {1: ['aufhalten', 'bleiben', 'wohnen', 'bleiben'], 2: ['verweilen', 'aufhalten', 'da verbringen', 'Zeit verbringen']}],
    
    [np.str_('Der Arzt diagnostizierte eine leichte Grippe und riet zur Bettruhe und ausreichend Flüssigkeitszufuhr'), 
     np.str_('diagnostizierte'), 
     6, 
     {1: ['feststellen', 'bestimmen', 'erkennen', 'identifizieren'], 2: ['Erkennen', 'feststellen', 'benennen']}],
    
    [np.str_('Die Kinder spielten fröhlich im Garten und bauten Sandburgen am Strand'), 
     np.str_('Sandburgen'), 
     2, 
     {1: ['Sandburg', 'Sandspielzeug'], 2: ['Burg aus Sand', 'Spielsand']}],
    
    [np.str_('Die Katze saß gemütlich auf dem Sofa und beobachtete die Vögel im Garten'), 
     np.str_('beobachtete'), 
     4, 
     {1: ['betrachtete', 'sah', 'verfolgte', 'belauschte'], 2: ['anschauen', 'betrachten', 'blicken', 'folgen']}],
    
    [np.str_('Die Blumen blühen bunt im Garten und verbreiten einen angenehmen Duft'), 
     np.str_('verbreiten'), 
     2, 
     {1: ['ausstrahlen'], 2: ['Aussenden', 'vermitteln', 'ausgeben']}],
    
    [np.str_('Der Koch bereitete ein leckeres Abendessen zu und überraschte seine Gäste mit einer besonderen Spezialität'), 
     np.str_('bereitete zu'), 
     5, 
     {1: ['zubereiten', 'kochen', 'machen', 'zubereiten'], 2: ['kochen', 'küchen', 'errichten', 'erreiten']}],
    
    [np.str_('Die Uhr tickte leise im Raum und die Zeit verging langsam'), 
     np.str_('verging'), 
     8, 
     {1: ['verrann', 'vergeudet', 'verstreichet', 'verrausched'], 2: ['sich bewegen', 'fortgehen', 'zu Ende gehen', 'verlaufen']}],
    
    [np.str_('Die Polizei ermittelte die Ursache des Unfalls und befragte Zeugen'), 
     np.str_('ermittelte'), 
     8, 
     {1: ['suchte', 'aufklären', 'nachforschte', 'recherchierte'], 2: ['bestimmen', 'entwickeln', 'entdecken', 'ermitteln']}],
    
    [np.str_('Der Maler vollendete sein Kunstwerk und war zufrieden mit dem Ergebnis'), 
     np.str_('vollendete'), 
     5, 
     {1: ['beendete', 'abschloss', 'vollendete', 'vervollständigte'], 2: ['beendigen', 'vollbringen', 'abschließen', 'schließen']}],
    
    [np.str_('Die Gäste tranken fröhlich Champagner und feierten bis spät in die Nacht'), 
     np.str_('tranken'), 
     4, 
     {1: ['konsumierten', 'genossen', 'schlürften', 'desgleichen'], 2: ['saufen', 'rauchen', 'trinken', 'schlucken']}],
    
    [np.str_('Der Musiker spielte virtuos auf seiner Geige und begeisterte das Publikum'), 
     np.str_('begeisterte'), 
     3, 
     {1: ['faszinierte', 'entzückte', 'berührte', 'packte'], 2: ['erfreute', 'entzückte', 'faszinierte', 'beeindruckte']}],
    
    [np.str_('Die Sonne ging langsam unter und tauchte den Himmel in warmes Licht'), 
     np.str_('unter'), 
     6, 
     {1: ['hinunter', 'tief', 'nach unten', 'in']}],
    
    [np.str_('Die Schüler lösten gemeinsam die knifflige Matheaufgabe und waren stolz auf ihre Leistung'), 
     np.str_('knifflig'), 
     4, 
     {1: ['schwierig', 'rätselhaft', 'kompliziert', 'heikel'], 2: ['anspruchsvoll', 'schwer', 'schwierig', 'durchdacht']}],
    
    [np.str_('Der Künstler malte ein farbenfrohes Bild und brachte damit Leben in den Raum'), 
     np.str_('farbenfrohes'), 
     7, 
     {1: ['bunt', 'farbenprächtig', 'leuchtend', 'coloriert'], 2: ['farbig', 'farbkraft', 'koloriert', 'rundum']}],
    
    [np.str_('Der Hund bellte laut vor Freude, als sein Herrchen nach Hause kam'), 
     np.str_('bellte'), 
     3, 
     {1: ['wuffte', 'kläffte', 'gab laut'], 2: ['heulte', 'winselte', 'kläffte', 'schrie']}],
    
    [np.str_('Der Lehrer lobte die Fleiß der Schüler und ermutigte sie, weiterhin hart zu arbeiten'), 
     np.str_('Fleiß'), 
     2, 
     {1: ['Emsigkeit'], 2: ['Fleiß', 'Anstrengung', 'Arbeitsverhalten']}],
    
    [np.str_('Die Taube flog elegant über die Dächer und landete auf einem Baum'), 
     np.str_('elegant'), 
     3, 
     {1: ['stilvoll', 'anmutig', 'fein', 'geschmackvoll'], 2: ['schick', 'edel', 'schön', 'gepflegt']}],
    
    [np.str_('Die Kinder spielten fröhlich im Park und saßen gemeinsam auf der Schaukel'), 
     np.str_('Schaukel'), 
     4, 
     {1: ['wiege'], 2: ['Rutsche', 'Karussell', 'Klettergerüst', 'Schaukel']}],
    
    [np.str_('Der Bäcker backte frische Brötchen und verkaufte sie direkt aus dem Ofen'), 
     np.str_('frische Brötchen'), 
     3, 
     {1: ['Köstlichkeiten', 'Backwaren', 'Brot', 'Gebäck'], 2: ['Semmeln', 'Gebäck', 'Brötchen', 'Kringerl']}],
    
    [np.str_('Die Maus huschte schnell durch das Gras und verschwand im Mauseloch'), 
     np.str_('huschte'), 
     5, 
     {1: ['huschte eilig', 'huschte flink', 'huschte rasch', 'huschte pfeilschnell'], 
      2: ['eilig laufen', 'schnell gehen', 'rasch laufen', 'flink rennen']}],
    
    [np.str_('Die Eltern erfreuten sich an der Gesellschaft ihrer Kinder und genossen die Familienzeit'), 
     np.str_('erfreuten'), 
     2, 
     {1: ['freuten'], 2: ['erfreuen', 'sich freuen', 'begeistern']}],
    
    [np.str_('Der Fahrradfahrer fuhr gemütlich durch den Wald und genoss die Ruhe der Natur'), 
     np.str_('gemütlich'), 
     3, 
     {1: ['entspannt', 'ruhig', 'behaglich', 'bequem'], 2: ['angenehm', 'entspannend', 'behaglich', 'bequem']}],
    
    [np.str_('Die Reisenden machten eine Pause an der Raststätte und gönnten sich eine Tasse Kaffee'), 
     np.str_('Raststätte'), 
     6, 
     {1: ['Rastplatz', 'Rasthof', 'Rasthaus', 'Autohof'], 
      2: ['Parkplatz', 'Autohof', 'Tankstelle', 'Rastplatz']}],
    
    [np.str_('Der Jogger lief flott durch den Park und genoss die frische Luft'), 
     np.str_('flott'), 
     5, 
     {1: ['schnell', 'zügig', 'rasant', 'fix'], 2: ['fix', 'rasch', 'schnell', 'zügig']}],
    
    [np.str_('Der Clown zauberte ein Lächeln auf die Gesichter der Kinder und sorgte für gute Laune im Zirkuszelt'), 
     np.str_('zauberte'), 
     4, 
     {1: ['brachte hervor', 'erschuf', 'zauberte'], 2: ['zaubern', 'beschwören', 'hexen', 'verzaubern']}],
    
    [np.str_('Die Regentropfen prasselten laut auf das Dach und ließen einen gemütlichen Abend zuhause noch schöner werden'), 
     np.str_('prasselten'), 
     7, 
     {1: ['klapperten', 'schlugen', 'schellten', 'ratterten'], 2: ['regnen', 'stürmen', 'prasseln', 'niedergehen']}],
    
    [np.str_('Der Zauberer führte eine beeindruckende Zaubershow vor und verblüffte sein Publikum'), 
     np.str_('verblüffte'), 
     6, 
     {1: ['erstaunte', 'überraschte', 'verwunderte', 'konstatierte'], 
      2: ['baffte', 'überraschte', 'erstaunte', 'verblüffte']}],
    
    [np.str_('Die Forscher entdeckten eine neue Art von Pflanze und untersuchten sie eingehend'), 
     np.str_('entdeckten'), 
     7, 
     {1: ['aufdeckten', 'aufspürten', 'fanden', 'aufklären'], 2: ['finden', 'erforschen', 'suchen', 'erkunden']}],
    
    [np.str_('Die Eule saß regungslos auf dem Ast und beobachtete das Geschehen im Wald'), 
     np.str_('regungslos'), 
     4, 
     {1: ['still', 'ruhig', 'bewegungslos', 'unbewegt'], 2: ['ruhend', 'bewegungslos', 'starr', 'unbeweglich']}],
    
    [np.str_('Der Künstler malte ein beeindruckendes Porträt und präsentierte es in seiner Ausstellung'), 
     np.str_('beeindruckendes'), 
     7, 
     {1: ['imponierenden', 'ausgezeichneten', 'erstaunlichen', 'bewundernswerten'], 
      2: ['verblüffend', 'staunenswert', 'beeindruckend', 'faszinierend']}],
    
    [np.str_('Die Schmetterlinge flatterten leicht durch den Garten und sorgten für eine zauberhafte Atmosphäre'), 
     np.str_('flatterten'), 
     3, 
     {1: ['flatterten', 'flugten', 'schwirrten', 'stoben'], 2: ['fliegen', 'schwirren', 'stöbern', 'wirbeln']}],

    #dataset = original_data[83:93]
    [np.str_('Die Krankenschwester hat dem Patienten bei der Körperpflege geholfen'), 
     np.str_('Krankenschwester'), 
     3, 
     {1: ['Pflegerin', 'Pflegekraft'], 2: ['Schwester']}],
    
    [np.str_('Der Ingenieur entwarf ein neues Bauprojekt für die Firma'), 
     np.str_('Ingenieur'), 
     5, 
     {1: ['Techniker', 'Konstrukteur'], 2: ['Fachingenieur']}],
    
    [np.str_('Die Lehrerin unterrichtete die Schüler in Mathematik'), 
     np.str_('Lehrerin'), 
     4, 
     {1: ['Pädagogin', 'Erzieherin'], 2: ['Dozentin']}],
    
    [np.str_('Der Polizist nahm den Verbrecher fest und brachte ihn ins Gefängnis'), 
     np.str_('Polizist'), 
     6, 
     {1: ['Beamter', 'Ordnungshüter'], 2: ['Streifenpolizist']}],
    
    [np.str_('Der Architekt plant den Bau eines neuen Wohnkomplexes'), 
     np.str_('Architekt'), 
     5, 
     {1: ['Bauplaner', 'Bauzeichner'], 2: ['Bauingenieur']}],
    
    [np.str_('Der Gastronom eröffnete ein neues Restaurant in der Innenstadt'), 
     np.str_('Gastronom'), 
     2, 
     {1: ['Wirt'], 2: ['Koch']}],
    
    [np.str_('Die Journalistin schrieb einen Artikel über die politische Lage im Land'), 
     np.str_('Journalistin'), 
     4, 
     {1: ['Reporterin', 'Redakteurin'], 2: ['Medienfachfrau']}],
    
    [np.str_('Der Musiker spielte ein Konzert vor einem begeisterten Publikum'), 
     np.str_('Musiker'), 
     3, 
     {1: ['Künstler', 'Instrumentalist'], 2: ['Sänger']}],
    
    [np.str_('Der Feuerwehrmann löschte den Brand im Wohnhaus'), 
     np.str_('Feuerwehrmann'), 
     5, 
     {1: ['Brandbekämpfer', 'Rettungskraft'], 2: ['Löscheinheit']}],
    
    [np.str_('Der Anwalt vertritt seinen Mandanten vor Gericht'), 
     np.str_('Anwalt'), 
     6, 
     {1: ['Rechtsanwalt', 'Jurist'], 2: ['Verteidiger']}],
    
    [np.str_('Die Ärztin diagnostizierte die Krankheit des Patienten und verschrieb Medikamente'), 
     np.str_('Ärztin'), 
     7, 
     {1: ['Medizinerin', 'Doktorin'], 2: ['Gesundheitsexpertin']}],
    
    [np.str_('Die Politikerin hielt eine Rede im Parlament über die aktuelle Gesetzgebung'), 
     np.str_('Politikerin'), 
     4, 
     {1: ['Abgeordnete', 'Parlamentarierin'], 2: ['Staatsfrau']}],
    
    [np.str_('Der Koch bereitete ein köstliches Dinner für seine Gäste zu'), 
     np.str_('Koch'), 
     4, 
     {1: ['Küchenchef', 'Kochkünstler'], 2: ['Gourmet']}],
    
    [np.str_('Der Schauspieler spielte die Hauptrolle in dem neuen Film'), 
     np.str_('Schauspieler'), 
     3, 
     {1: ['Darsteller', 'Künstler'], 2: ['Theaterspieler']}],
    
    [np.str_('Der Lehrer hielt eine interessante Vorlesung über Geschichte'), 
     np.str_('Lehrer'), 
     6, 
     {1: ['Pädagoge', 'Dozent'], 2: ['Unterrichtsexperte']}],
    
    [np.str_('Der Verkäufer beriet die Kunden bei der Auswahl eines neuen Fernsehers'), 
     np.str_('Verkäufer'), 
     4, 
     {1: ['Händler', 'Vertriebsmitarbeiter'], 2: ['Kaufmann']}],
    
    [np.str_('Der Pilot flog das Flugzeug sicher zum Zielflughafen'), 
     np.str_('Pilot'), 
     4, 
     {1: ['Flugkapitän', 'Flugzeugführer'], 2: ['Luftfahrer']}],
    
    [np.str_('Der Maler malte ein beeindruckendes Gemälde auf Leinwand'), 
     np.str_('Maler'), 
     3, 
     {1: ['Künstler', 'Kunstmaler'], 2: ['Bildmacher']}],
    
    [np.str_('Die Bibliothekarin half den Besuchern bei der Suche nach Büchern'), 
     np.str_('Bibliothekarin'), 
     5, 
     {1: ['Büchereianstellerin', 'Mediathekarin'], 2: ['Leseprofi']}],
    
    [np.str_('Der Astronaut flog mit einer Raumkapsel ins Weltall'), 
     np.str_('Astronaut'), 
     5, 
     {1: ['Raumfahrer', 'Weltraumpionier'], 2: ['Kosmonaut']}],
    
    [np.str_('Der Detektiv löste den kniffligen Fall und brachte den Dieb zur Rechenschaft'), 
     np.str_('Detektiv'), 
     7, 
     {1: ['Kriminalist', 'Ermittler'], 2: ['Spürnase']}],
    
    [np.str_('Der Bauer erntete die reifen Früchte auf seinem Feld'), 
     np.str_('Bauer'), 
     3, 
     {1: ['Landwirt', 'Agrarier'], 2: ['Feldbewirtschafter']}],
    
    [np.str_('Der Designer entwarf eine neue Kollektion für die Modenschau'), 
     np.str_('Designer'), 
     4, 
     {1: ['Gestalter', 'Kreateur'], 2: ['Modemacher']}],
    
    [np.str_('Der Sänger sang ein emotionales Lied vor einem begeisterten Publikum'), 
     np.str_('Sänger'), 
     4, 
     {1: ['Vokalist', 'Interpret'], 2: ['Musiker']}],
    
    [np.str_('Der Gärtner pflegte den Garten und pflanzte neue Blumen'), 
     np.str_('Gärtner'), 
     5, 
     {1: ['Gartenfachmann', 'Hausgärtner'], 2: ['Pflanzenfreund']}],
    
    [np.str_('Die Sekretärin typte die Berichte für den Chef'), 
     np.str_('Sekretärin'), 
     2, 
     {1: ['Assistentin'], 2: ['Bürokraft']}],
    
    [np.str_('Der Archäologe grub nach antiken Artefakten in der Ausgrabungsstätte'), 
     np.str_('Archäologe'), 
     4, 
     {1: ['Grabungsforscher', 'Antikenforscher'], 2: ['Kulturhistoriker']}],
    
    [np.str_('Der Handwerker reparierte die defekte Leitung im Haus'), 
     np.str_('Handwerker'), 
     3, 
     {1: ['Handwerksmeister', 'Reparateur'], 2: ['Heimwerker']}],
    
    [np.str_('Der Rennfahrer gewann das Autorennen auf der Rennstrecke'), 
     np.str_('Rennfahrer'), 
     5, 
     {1: ['Rennsportler', 'Wettbewerbsfahrer'], 2: ['Rallyefahrer']}],
    
    [np.str_('Die Tänzerin führte eine elegante Choreografie auf der Bühne vor'), 
     np.str_('Tänzerin'), 
     4, 
     {1: ['Tanzkünstlerin', 'Balletttänzerin'], 2: ['Choreographin']}],
    
    [np.str_('Der Mechaniker reparierte das kaputte Auto in der Werkstatt'), 
     np.str_('Mechaniker'), 
     4, 
     {1: ['Kfz-Techniker', 'Reparaturfachmann'], 2: ['Schrauber']}],
    
    [np.str_('Die Friseurin schneidet die Haare und stylte sie neu'), 
     np.str_('Friseurin'), 
     4, 
     {1: ['Haarstylistin', 'Haarkünstlerin'], 2: ['Coiffeurin']}],

    #dataset = original_data[93:113]
    [np.str_('Die perfekte Inszenierung wird aus Sicht der Nazis nicht einmal dadurch getrübt, dass mit Jesse Owens ein Afroamerikaner erfolgreichster Athlet der Olympischen Spiele wird.'), 
     np.str_('Afroamerikaner'), 
     16, 
     {1: ['Schwarzer'], 2: ['Schwarz-Amerikaner']}],
    
    [np.str_('Athleten müssen hart trainieren, um auf Wettkämpfen erfolgreich zu sein.'), 
     np.str_('Athleten'), 
     0, 
     {1: ['Sportler']}],
    
    [np.str_('Basketball ist ein sehr beliebter Sport in den USA.'), 
     np.str_('Basketball'), 
     8, 
     {1: ['Korbball']}],
    
    [np.str_('Marie ist eine talentierte Tänzerin und macht bei jeder Vorstellung eine großartige Performance.'), 
     np.str_('Performance'), 
     14, 
     {1: ['Vorstellung'], 2: ['Darbietung', 'Aufführung']}],
    
    [np.str_('Der berühmte Maler Vincent van Gogh schuf viele beeindruckende Gemälde.'), 
     np.str_('Gemälde'), 
     9, 
     {1: ['Bild'], 2: ['Kunstwerk']}],
    
    [np.str_('In der Kunstwelt gibt es viele talentierte Künstler, die mit ihren Werken die Menschen begeistern.'), 
     np.str_('Künstler'), 
     9, 
     {1: ['Maler', 'Kunstschaffender'], 2: ['Kunstler']}],
    
    [np.str_('Die Oper ist eine Form der musikalischen Darbietung, die viele Menschen fasziniert.'), 
     np.str_('Oper'), 
     4, 
     {1: ['Opernhaus']}],
    
    [np.str_('In der Schule lernen die Schüler verschiedene Fächer wie Mathematik, Geschichte und Biologie.'), 
     np.str_('Fächer'), 
     3, 
     {1: ['Unterrichtsfächer']}],
    
    [np.str_('Der Lehrer erklärte den Schülern das Thema sehr verständlich, sodass alle es gut nachvollziehen konnten.'), 
     np.str_('Nachvollziehen'), 
     13, 
     {1: ['verstehen'], 2: ['nachempfinden']}],
    
    [np.str_('Die Wissenschaftler führten viele Experimente durch, um neue Erkenntnisse zu gewinnen.'), 
     np.str_('Erkenntnisse'), 
     10, 
     {1: ['Ergebnisse'], 2: ['Entdeckungen']}],
    
    [np.str_('Das Buch enthält viele interessante Informationen über die Geschichte des alten Ägypten.'), 
     np.str_('Informationen'), 
     4, 
     {1: ['Fakten'], 2: ['Details']}],
    
    [np.str_('Die Studenten müssen für ihre Prüfungen viel lernen, um gute Noten zu bekommen.'), 
     np.str_('Noten'), 
     13, 
     {1: ['Bewertungen'], 2: ['Zensuren']}],
    
    [np.str_('Die Reise um die Welt war ein einmaliges Erlebnis, das ich nie vergessen werde.'), 
     np.str_('Erlebnis'), 
     11, 
     {1: ['Erfahrung']}],
    
    [np.str_('Die Entdeckung neuer Planeten im Universum fasziniert viele Astronomen.'), 
     np.str_('Astronomen'), 
     14, 
     {1: ['Himmelskundler'], 2: ['Sterngucker']}],
    
    [np.str_('Die Archäologen fanden bei ihren Ausgrabungen viele historische Artefakte.'), 
     np.str_('Artefakte'), 
     10, 
     {1: ['Fundstücke'], 2: ['Relikte']}],
    
    [np.str_('Das Konzert des berühmten Musikers war ein voller Erfolg und begeisterte das Publikum.'), 
     np.str_('Publikum'), 
     5, 
     {1: ['Zuhörer'], 2: ['Audienz', 'Gäste']}],
    
    [np.str_('Die Politiker diskutierten über wichtige Themen, die die Zukunft des Landes beeinflussen.'), 
     np.str_('Beeinflussen'), 
     10, 
     {1: ['auswirken'], 2: ['beeinträchtigen']}],
    
    [np.str_('Die Schauspielerin erhielt für ihre Darbietung im Theater viel Lob von den Kritikern.'), 
     np.str_('Kritiker'), 
     13, 
     {1: ['Bewerter'], 2: ['Rezensent']}],
    
    [np.str_('Die Forscher haben neue Erkenntnisse über die Auswirkungen des Klimawandels auf die Umwelt gewonnen.'), 
     np.str_('Erkenntnisse'), 
     4, 
     {1: ['Einsichten'], 2: ['Ergebnisse']}],
    
    [np.str_('Der Maler Picasso schuf viele einzigartige Kunstwerke, die bis heute bewundert werden.'), 
     np.str_('Kunstwerke'), 
     9, 
     {1: ['Gemälde'], 2: ['Werke']}],
    
    [np.str_('Die Schüler machten bei der Chemie-Experimente viele interessante Entdeckungen.'), 
     np.str_('Entdeckungen'), 
     6, 
     {1: ['Fundstücke'], 2: ['Funde']}],
    
    [np.str_('Die Jugendlichen verbrachten ihren Sommerurlaub auf einer abenteuerlichen Reise durch Europa.'), 
     np.str_('abenteuerlichen'), 
     8, 
     {1: ['spannenden'], 2: ['aufregenden']}],
    
    [np.str_('Die Veranstaltung war gut organisiert und begeisterte die Besucher durch ihre Vielfalt an Programmpunkten.'), 
     np.str_('Programmpunkten'), 
     8, 
     {1: ['Events'], 2: ['Darbietungen', 'Auftritte']}],
    
    [np.str_('Die Anwältin setzte sich mit großem Engagement für die Rechte ihrer Mandanten ein.'), 
     np.str_('Mandanten'), 
     11, 
     {1: ['Klienten'], 2: ['Kunden']}],
    
    [np.str_('Die Nachrichten berichteten über wichtige Ereignisse aus aller Welt.'), 
     np.str_('Ereignisse'), 
     11, 
     {1: ['Vorkommnisse'], 2: ['Geschehnisse']}],
    
    [np.str_('Die Veranstaltung bot den Gästen eine Vielzahl an Unterhaltungsmöglichkeiten.'), 
     np.str_('Unterhaltungsmöglichkeiten'), 
     14, 
     {1: ['Entertainment'], 2: ['Spaßoptionen']}],
    
    [np.str_('Der Autor schrieb ein faszinierendes Buch über das Leben im Mittelalter.'), 
     np.str_('faszinierendes'), 
     20, 
     {1: ['spannendes'], 2: ['interessantes']}],
    
    [np.str_('Die Forscher untersuchten die Zusammenhänge zwischen Ernährung und Gesundheit.'), 
     np.str_('Zusammenhänge'), 
     11, 
     {1: ['Verbindungen'], 2: ['Beziehungen']}],
    
    [np.str_('Die Veranstaltung bot den Besuchern eine Vielfalt an kulinarischen Leckerbissen.'), 
     np.str_('kulinarischen'), 
     11, 
     {1: ['kulinarischen'], 2: ['Essens-']}],
    
    [np.str_('Der Musiker komponierte eine Melodie, die die Zuhörer tief berührte.'), 
     np.str_('Zuhörer'), 
     12, 
     {1: ['Hörer'], 2: ['Publikum']}],
    
    [np.str_('Die Schauspielerin erhielt für ihre Darstellung im Film viel Anerkennung von den Kritikern.'), 
     np.str_('Anerkennung'), 
     16, 
     {1: ['Lob'], 2: ['Respekt']}],
    
    [np.str_('Die Forscher stellten fest, dass die Temperatur einen direkten Einfluss auf das Wachstum der Pflanzen hat.'), 
     np.str_('Einfluss'), 
     9, 
     {1: ['Wirkung'], 2: ['Auswirkung']}]

    ]

# Convert the list to a numpy array
    return np.array(data, dtype=object)


