const {chromium}=require('playwright');
const R=process.env.BASIS||'file://'+require('path').resolve(__dirname,'..')+'/';
const cases={
'4ab-nawi/k1-5a-elektromagnet/aufgaben.html':[
 ['a3','theta','240 A',1],['a3','theta','240',1],['a3','theta','Θ = 600 · 0,4 A = 240 A',1],['a3','theta','0,24 kA',1],['a3','theta','240 Ampere',1],['a3','theta','240 V',0],['a3','theta','250',0],['a3','theta','24 A',0],
 ['a3','h','2000 A/m',1],['a3','h','2 kA/m',1],['a3','h','H = 240 A / 0,12 m = 2.000 A/m',1],['a3','h','2000',1],['a3','h','2000 A',0],['a3','h','2000 Am',0],['a3','h','2000 A pro m',1],
 ['a12','a','0,0004 m²',1],['a12','a','4 cm²',1],['a12','a','0,0004 m2',1],['a12','a','4*10^-4 m^2',1],['a12','a','4 cm2 = 0,0004 m²',1],['a12','a','0,04 m²',0],
 ['a12','b','1,5 T',1],['a12','b','1500 mT',1],['a12','b','1,5 Tesla',1],['a12','b','1,5 Vs/m²',1],['a12','b','1,5',1],['a12','b','1,5 A',0],['a12','b','15 T',0],['a12','b','B = 0,0006 Wb / 0,0004 m² = 1,5 T',1],
 ['a18','n','600',1],['a18','n','600 Windungen',1],['a18','n','N = 300 A / 0,5 A = 600',1],['a18','n','60',0],
 ['a18','h','6000 A/m',1],['a18','h','6 kA/m',1],
 ['a4','t','Der Fluss pro Fläche, gemessen in Tesla',1],['a4','t','Feldlinien pro Quadratmeter',0],['a4','t','Anzahl der Feldlinien Φ pro m2 in T',1],
 ['a5','t','Der Draht wird abgelenkt durch die Lorentzkraft',1],['a5','t','Er wird abgelenkt',0],['a5','t','es entsteht eine Kraft, Lorentz-Kraft',1],['a5','t','nichts',0],
 ['a7','t','Der Motor bleibt stehen',1],['a7','t','er dreht sich nicht weiter, weil die Stromrichtung nicht umgepolt wird',1],['a7','t','schneller',0],
 ['a1','t','Windungszahl, Stromstärke, Eisenkern und Länge der Spule',1],['a1','t','Windungen, Strom, Eisen, Spulenlaenge',1],['a1','t','Windungen und Strom',0],['a1','t','Windungszal, Stromstärke, Eisenkern, kürzere Spule',1],
 ['a16','risiken','Lieferengpässe und hohe Preise',1],['a16','risiken','Abhängigkeit von China',0],['a16','risiken','Wir sind abhängig und die Preise steigen',1],
 ['a13','warum','Man kann ihn abschalten, dann fällt das Metall runter',1],['a13','liegen','Alu und Kupfer',1],['a13','liegen','Aluminium',1],['a13','liegen','Eisen',0],
 ['a15','t','Der Magnet zieht Metall an, Gegenstände fliegen',1],
 ],
'3bk-pbgw/k1-3-epochen/aufgaben.html':[
 ['a1','jued','5787',1],['a1','jued','5.787',1],['a1','jued','Jahr 5787',1],['a1','jued','5786',0],
 ['a3','caesar','2069',1],['a3','caesar','2.069 Jahre',1],['a3','caesar','2 069',1],['a3','caesar','2070',0],['a3','oetzi','5325',1],['a3','oetzi','5.325',1],
 ['a11','tag','7',1],['a11','tag','der 7.',1],['a11','tag','07',1],['a11','tag','8',0],
 ['a11','zeit','06:30',1],['a11','zeit','6.30 Uhr',1],['a11','zeit','0630',1],['a11','zeit','6 Uhr 30',1],['a11','zeit','7:30',0],
 ['a11','dzg','182145BOKT26',1],['a11','dzg','182145B OKT 26',1],['a11','dzg','182145B OKT 2026',1],['a11','dzg','182145B Oktober 2026',1],['a11','dzg','182145AOKT26',0],
 ['a12','anz','17',1],['a12','anz','17 mal',1],['a12','anz','16',0],
 ['a14','tage','11',1],['a14','tage','ca. 11 Tage',1],['a14','proz','3,1',1],['a14','proz','3,1 %',1],['a14','proz','3 %',1],['a14','proz','3.1%',1],['a14','proz','5',0],
 ['a10','oe1','Staatsvertrag 1955',1],['a10','oe1','Staatsvertrag',0],['a10','oe2','EU Beitritt 1995',1],
 ['a5','warum','Das julianische Jahr war zu lang',1],['a5','warum','keine ahnung',0],
 ['a9','begr','Erster Weltkrieg 1914 und Fall der Mauer 1989',1],
 ['a15','2024','Das wurde abgelehnt',1],['a15','2024','abgelent',1],['a15','2024','Ja, angenommen',0],
 ],
'3bk-pbgw/k1-2-faelschung/aufgaben.html':[
 ['a3','gruende','Geld und Exklusivität',1],['a3','gruende','1. Die Auflage sollte steigen. 2. Konkurrenz und Zeitdruck',1],['a3','gruende','Sie hatten Angst vor der Konkurrenz',0],['a3','gruende','Sie waren nett',0],
 ['a2','besser','Die Gutachter hätten Originale aus dem Archiv nehmen müssen',1],['a2','besser','Weitere unabhängige Prüfung',1],
 ['a4','stelle','Das Wort Aufheller bzw. Weißmacher',1],
 ['a5','fragen','Wer hat das geschickt? Stimmt der Inhalt? Wem nützt das?',1],['a5','fragen','Wer ist der Absender',0],['a5','tun','Nicht weiterleiten',1],['a5','tun','Ich suche eine zweite Quelle',1],
 ['a6','dafuer','Eine Fälschung ist auch eine Quelle',1],['a6','dagegen','Gefahr von Missbrauch',1],
 ],
'3ab-nawi/k2-3a-ernaehrung/aufgaben.html':[
 ['a3','spaetzle','ovo-lakto und Pescetarier',1],['a3','spaetzle','lakto-ovo, pesc.',1],['a3','spaetzle','vegan',0],
 ['a3','gummi','keine',1],['a3','gummi','niemand',1],['a3','gummi','alle',0],['a3','forelle','Pescetarier',1],['a3','forelle','Pescetarierer',1],['a3','honig','alle außer vegan: lakto, ovo, ovolakto, Pesc.',1],
 ['a1','lisa','Kein Alkohol, nicht für zwei essen',1],['a1','lisa','kein Alkohol',1],['a1','lisa','nur Pommes essen',0],
 ['a1','opa','Mehr trinken, auch ohne Durst',1],['a1','tim','Frühstück essen und Wasser statt Cola',1],
 ],
'2ak-pbgw/k1-grundrechte/aufgaben.html':[
 ['a9','proz','82,8 %',1],['a9','proz','83%',1],['a9','proz','82.8',1],['a9','proz','80',0],['a9','alter','78',1],['a9','alter','78 Jahre',1],['a9','oe','7',1],
 ['a1','jahre','733',1],['a1','jahre','733 Jahre',1],['a1','jahre','7330',0],['a4','jahr','2018',1],
 ['a3','drei','Weltregierung, Weltpolizei, Weltgericht',1],['a3','drei','Keine Regierung, keine Polizei, kein Gericht',1],['a3','drei','Regierung, Polizei',0],
 ['a3','weich','Öffentlich anprangern',1],['a3','weich','Druck auf die Regierung',1],
 ['a10','wen','Zivilisten',1],['a10','wen','Zivilbevölkerung und Gefangene',1],['a10','wen','Soldaten',0],['a11','nobel','Navi Pillay',1],['a11','nobel','Pilay',1],
 ],
};

/* Gegenbeispiele aus dem Prüfbericht (23.10.2026): diese Antworten dürfen NICHT als richtig gelten (0) bzw. müssen gelten (1) */
const E4='4ab-nawi/k1-5a-elektromagnet/aufgaben.html',F3='3bk-pbgw/k1-2-faelschung/aufgaben.html',EP='3bk-pbgw/k1-3-epochen/aufgaben.html';
cases[E4].push(['a12','b','1000 mT',0],['a12','b','1500 mT',1],['a12','b','1.5e3 mT',1],['a3','theta','240 A ist falsch, richtig sind 24 A',0],['a3','theta','nicht 240 A, sondern 24 A',0],['a3','theta','2,4*10^2 A',1],
 ['a5','t','Es gibt keine Lorentzkraft und der Draht wird nicht abgelenkt.',0],['a5','t','Der Draht wird abgelenkt, die Lorentzkraft wirkt, weil sich die Felder überlagern.',1],
 ['a7','t','Der Motor bleibt nicht stehen, sondern dreht immer weiter.',0],['a7','t','Ohne Kommutator bleibt der Motor stehen, weil der Strom nicht umgepolt wird.',1]);
cases[F3].push(['a3','gruende','Zeitdruck',0],['a3','gruende','Verkaufsgewinn',0],['a3','gruende','Zeitdruck und Verkaufsgewinn',1]);
cases[EP].push(['a10','oe1','1955',0],['a10','oe1','Staatsvertrag 1955',1]);
/* Prüfbericht v4 (23.10.2026) */
cases[E4].push(
 ['a7','t','Die Spule dreht sich nicht weiter.',1],['a7','t','Er kann sich nicht weiterdrehen, weil nicht umgepolt wird.',1],['a7','t','Die Stromrichtung ist egal; der Motor läuft immer weiter.',0],
 ['a7','t','Ohne Kommutator läuft der Motor ohne Kommutator.',0],['a7','t','Die Stromrichtung ändert sich nicht, deshalb bleibt er nach einer halben Umdrehung stehen.',1],['a7','t','Der Strom wird nicht umgepolt.',1],
 ['a12','b','1 T',0],['a12','b','2 T',0],['a12','b','0,002 kT',0],['a12','b','1,5 V s / m²',1],['a12','b','1,50 T',1],
 ['a3','theta','240 A oder 24 A oder 999 A',0],['a3','theta','240 A (oder 0,24 kA)',1],['a3','theta','0.240 kA',1],['a3','theta','2,4 × 10² A',1],['a3','theta','240 A sind nicht falsch',1],['a3','h','2000 A m^-1',1],['a3','h','2000 A / m',1],['a3','h','2.000 A/m',1],
 ['a3','theta','Θ = I · N = 0,4 A · 600 = 240 A',1]);
cases[F3].push(['a3','gruende','Zeitdruck und Konkurrenzdruck',1],['a3','gruende','Gewinn durch höhere Auflage',0],['a3','gruende','Gewinn und Zeitdruck',1]);
cases[EP].push(['a10','oe1','Ereignis 1955',0]);
/* Prüfbericht v6 (24.10.2026) */
cases[E4].push(
 ['a7','t','Die Stromrichtung in der Spule kehrt sich nicht um. Deshalb dreht sich der Motor nicht kontinuierlich weiter.',1],
 ['a7','t','Der Motor dreht sich ohne Kommutator immer weiter, weil die Stromrichtung nicht umgepolt werden muss.',0],
 ['a12','b','1.500 T oder 1,5 T',1],['a12','b','1.500 T oder 1500 mT',1],['a12','b','1,5 V·s·m⁻²',1],['a12','b','1,5 V·s·m^-2',1],
 ['a7','t','Er bleibt stehen, weil der Strom nicht umgepolt werden kann.',1],['a7','t','Die Spule bleibt stehen, statt immer weiter zu laufen.',1],['a7','t','Der Motor läuft einfach immer weiter.',0]);
/* Prüfbericht v7 (24.10.2026): N1 Motor-contra, N2 verworfene Zahl, N3 Einheiten */
cases[E4].push(
 ['a7','t','Der Motor bleibt stehen, egal wie groß die Stromstärke ist.',1],
 ['a7','t','Zunächst läuft er weiter und bleibt dann stehen, weil der Strom nicht umgepolt wird.',1],
 ['a3','theta','Das falsche Ergebnis wäre 240 A. Richtig ist 24 A.',0],
 ['a12','b','1,5 N/(A·m)',1],['a12','b','1,5 kg/(A·s²)',1],['a12','b','1,5 V s m⁻²',1],['a12','b','1,5 V·s·m^(-2)',1],['a12','b','1,5 V·s·m−2',1],
 ['a3','theta','2,4 × 10^+2 A',1],
 /* Gegenproben: ausdrücklich falsche Erklärungen und falsche Dimensionen bleiben falsch */
 ['a7','t','Die Stromrichtung ist egal, der Motor dreht sich einfach weiter.',0],
 ['a7','t','Der Motor läuft einfach weiter, die Polung ist egal.',0],
 ['a7','t','Der Motor läuft immer weiter.',0],
 ['a7','t','Er läuft kurz weiter, dann bleibt er stehen, weil nicht umgepolt wird.',1],
 ['a3','theta','Falsch wäre 24 A. Richtig sind 240 A.',1],
 ['a3','theta','Ein falsches Ergebnis ist 24 A, richtig ist 240 A.',1],
 ['a3','theta','0,4 A bei 600 Windungen = 240 A',1],
 ['a12','b','1,5 N/(A·s)',0],['a12','b','1,5 V·s·m^-1',0],['a12','b','1,5 kg/(A·s)',0],['a12','b','1,5 N / (A · m)',1],['a12','b','1,5 V s m−2',1],
 ['a3','theta','2,4 × 10^-2 A',0],['a3','theta','2,4 x 10² A',1]);
/* Prüfbericht v8 (24.10.2026): V8-01 Einheit in Klammern, V8-02 Leerzeichen/Malpunkt, V8-03 hochgestelltes Plus, V8-04 richtig/falsch ohne Satzzeichen, V8-05 Motor, V8-06 nachgestellte Verneinung */
cases[E4].push(
["a12","b","1500 (mT)",1],["a12","b","1,5 (A)",0],["a3","h","2 (kA/m)",1],["a3","h","2000 (V/m)",0],["a12","b","1500 mT",1],["a12","b","1,5 N/(A·s)",0],
["a3","h","2000 A · m^-1",1],["a3","h","2000 A⋅m⁻¹",1],["a12","b","1,5 kg · s^-2 · A^-1",1],["a12","b","1,5 kg / A / s²",1],["a3","h","2000 A·m^-1",1],["a12","b","1,5 kg/A/s²",1],["a3","h","2000 A · m",0],["a12","b","1,5 kg · s^-1 · A^-1",0],
["a3","theta","2,4 × 10⁺² A",1],["a3","theta","240 × 10⁺¹ A",0],["a3","theta","2,4 × 10² A",1],["a3","theta","240 × 10¹ A",0],["a3","theta","2,4 × 10⁺¹ A",0],
["a3","theta","Richtig sind 240 A falsch sind 24 A",1],["a3","theta","24 A sind falsch 240 A sind richtig",1],["a3","theta","24 A sind falsch. 240 A sind richtig.",1],["a3","theta","240 A sind falsch. 24 A sind richtig.",0],["a3","theta","Richtig sind 24 A falsch sind 240 A",0],["a3","theta","0,4 A bei 600 Windungen = 240 A",1],
["a7","t","Der Motor läuft weiter und kommt schließlich zum Stillstand.",1],["a7","t","Der Motor bleibt stehen, egal in welche Richtung der Strom vorher geflossen ist.",1],["a7","t","Ohne Kommutator ist keine endlose Rotation möglich.",1],["a7","t","Der Motor dreht sich nicht unendlich weiter.",1],
["a7","t","Zunächst läuft er weiter und bleibt dann stehen, weil der Strom nicht umgepolt wird.",1],["a7","t","Die Spule bleibt stehen, egal wie groß die Stromstärke ist.",1],["a7","t","Der Motor läuft immer weiter.",0],["a7","t","Die Stromrichtung ist egal, der Motor dreht sich einfach weiter.",0],
["a7","t","Der Motor stoppt nicht.",0],["a7","t","Der Motor stoppt nie.",0],["a7","t","Der Motor stoppt.",1],["a7","t","Der Motor kommt nicht zum Stillstand.",0],
["a5","t","Der Draht wird abgelenkt, aber nicht durch die Lorentzkraft.",0],["a5","t","Der Draht wird abgelenkt, die Lorentzkraft wirkt, weil sich die Felder überlagern.",1],["a5","t","Es gibt keine Lorentzkraft und der Draht wird nicht abgelenkt.",0],
/* zusätzliche Gegenproben */
["a12","b","1,5 (T)",1],["a3","theta","240 (A)",1],["a3","theta","240 A (oder 0,24 kA)",1],["a3","theta","240 × 10^x A",0],
["a3","theta","Das ist falsch 240 A",0],["a3","theta","Richtig ist 240 A, falsch ist 24 A.",1],["a3","theta","240 A falsch 24 A richtig",1],["a5","t","Der Draht wird abgelenkt durch die Lorentzkraft nicht durch Reibung",1],["a7","t","Kein Stillstand, er dreht sich immer weiter.",0],["a7","t","Der Motor hat keinen Stillstand.",0],["a3","h","2 kA / m",1],["a3","h","5 (Windungen) 2000 A/m",1]);
/* Entscheidung Stephan 24.10.2026: Gleichungen mit ungleichen Seiten sind falsch; Motor: falsche Begründung ist falsch, »Stromrichtung muss gewechselt werden« allein genügt */
cases[E4].push(
 ["a3","theta","240 A = 24 A",0],["a3","theta","24 A = 240 A",0],["a3","theta","Θ = 240 A = 24 A",0],["a3","theta","240 A = 0,240 kA",1],["a3","theta","Θ = 0,4 A · 600 = 240 A",1],["a3","theta","0,4 A · 600 Windungen = 240 A",1],["a3","theta","Θ = I · N = 0,4 A · 600 = 240 A",1],
 ["a12","b","1,5 T = 15 mT",0],["a12","b","1,5 T = 1500 mT",1],["a12","b","B = 0,0006 Wb / 0,0004 m² = 1,5 T",1],["a12","b","B = 1,5 T = 1,5 Vs/m²",1],["a12","a","4 cm² = 0,0004 m²",1],["a3","h","1000 A/m + 1000 A/m = 2000 A/m",1],["a3","h","2 kA/m = 2000 A/m",1],["a3","h","2 kA/m = 200 A/m",0],
 ["a7","t","Der Motor bleibt stehen, obwohl die Stromrichtung ständig umgepolt wird.",0],["a7","t","Der Motor bleibt stehen, weil der Strom zu schwach ist.",0],["a7","t","Die Stromrichtung muss gewechselt werden, egal wie stark der Strom ist.",1],["a7","t","Der Motor bleibt stehen, weil der Strom nicht umgepolt wird.",1],["a7","t","Ohne Kommutator bleibt der Motor stehen, weil keine Umpolung erfolgt.",1]);
/* 2AB K1.3 Stoffumwandlung – Prüfbericht ChatGPT v4 (24.10.2026), Punkt 09: halbe, falsche und verneinte Antworten gelten nicht */
const K13='2ab-nawi/k1-3-reaktionen/aufgaben.html';
cases[K13]=[
 /* N01: kurze Stoffantwort – nur der Stoff Kupfer zählt */
 ['a4','prod','Cu',1],['a4','prod','2 Cu',1],['a4','prod','Kupfer',1],['a4','prod','Cu (Kupfer)',1],['a4','prod','Kupfer (Cu)',1],['a4','prod','cu.',1],['a4','prod','elementares Kupfer',1],['a4','prod','Kupfermetall',1],
 ['a4','prod','Kupferoxid',0],['a4','prod','CuO',0],['a4','prod','Kupfer(II)-oxid',0],['a4','prod','Kupfer oxid',0],['a4','prod','Cu2O',0],
 ['a4','prod','Kupfersulfat',0],['a4','prod','Kupferchlorid',0],['a4','prod','nicht Kupfer, sondern Kohlenstoff',0],['a4','prod','CO2',0],['a4','prod','Kupfer und Kohlenstoffdioxid entstehen',0],
 /* N02: offene Erklärungen bewertet die Lehrkraft – M = Teil ist als manuell gekennzeichnet, gibt kein automatisches »richtig« und keine Punkte */
 ['a5','warum','Innen oxidiert Kupfer, außen fehlt Sauerstoff.','M'],['a5','warum','Sauerstoff gefaltet','M'],['a5','warum','Außen reagiert das heiße Kupfer mit Luftsauerstoff. Zwischen den gefalteten Flächen kommt kaum Luft hin.','M'],
 ['a13','warum','Enzym gekocht','M'],['a13','warum','Die Kartoffel wurde gekocht, aber die Katalase ist weiterhin aktiv.','M'],['a13','warum','Das Enzym wurde durch Hitze nicht zerstört.','M'],['a13','warum','Beim Kochen verändert sich die Form der Katalase; sie verliert dadurch ihre Wirkung.','M'],
 ['a1','warum','Sauerstoff wird freigesetzt; Eisen nimmt keinen Sauerstoff auf.','M'],['a1','warum','Das Eisen nimmt Sauerstoff aus der Luft auf.','M'],
 ['a11','erkl','Aktivierungsenergie wird frei. Danach nimmt das Feuer Wärme auf.','M'],['a11','erkl','Zum Anzünden braucht man Energie. Danach kann die frei werdende Wärme weitere Reaktionen ermöglichen.','M'],
 ['a8','punkt','Öl drauf, weil Wasser fernbleibt','M'],['a15','fehler','kein Filter','M'],['a19','kat','beschleunigt','M'],['a21','warum','teuer','M'],['a22','duenn','Oberfläche','M'],['a23','titel','Plakat','M'],
 /* N02: Stofflisten – nur vollständige positive Nennung */
 ['a21','metalle','Chrom',0],['a21','metalle','Ruthenium, Cobalt, Mangan und Chrom',1],['a21','metalle','Chrom, Mangan, Kobalt, Ruthenium',1],['a21','metalle','Ruthenium, Kobalt, Mangan',0],
 ['a21','metalle','Chrom, Mangan, Kobalt und Ruthenium sind nicht die Metalle.',0],['a21','metalle','Es sind Ruthenium, Kobalt, Mangan und Chrom – Iridium ist nicht dabei.',1],
 ['a22','metalle','Platin',0],['a22','metalle','Platin, Palladium, Rhodium',1],['a22','metalle','Rhodium Palladium Platin',1],['a22','metalle','Platin, Palladium und Rhodium sind falsch.',0],['a22','metalle','Platin, Palladium und Rhodium sind keine Edelmetalle.',0],
 ['a13','gas','Sauerstoff',1],['a13','gas','Wasserstoff',0],
 ['a12','o2','0,32 g',1],['a12','o2','0.32 g',1],['a12','o2','320 mg',1],['a12','o2','0,32 kg',0],['a12','proz','26,7',1],['a12','proz','26,7 %',1],['a17','rgt','20 s',1],['a17','rgt','40 s',0],
 ['a3','ea','2',1],['a3','ea','4',0]];
/* 4AB K2.1–2.3 Schwingungen und Wellen (25.10.2026): Zahlen mit Einheit, Rundung, falsche Dimension, Auswahl als ganze Antwort, offene Erklärungen = M */
const W21='4ab-nawi/k2-1-wellen/aufgaben.html';
cases[W21]=[
 ['a1','amp','3 cm',1],['a1','amp','3',1],['a1','amp','0,03 m',1],['a1','amp','30 mm',1],['a1','amp','A = 3 cm',1],['a1','amp','6 cm',0],['a1','amp','3 s',0],['a1','amp','nicht 3 cm, sondern 6 cm',0],
 ['a1','periode','0,8 s',1],['a1','periode','0.8 s',1],['a1','periode','800 ms',1],['a1','periode','T = 1,0 s - 0,2 s = 0,8 s',1],['a1','periode','1,6 s',0],['a1','periode','0,4 s',0],['a1','periode','0,8 Hz',0],['a1','periode','0,8 m',0],
 ['a1','frequenz','1,25 Hz',1],['a1','frequenz','1,25',1],['a1','frequenz','f = 1 / 0,8 s = 1,25 Hz',1],['a1','frequenz','1,3 Hz',1],['a1','frequenz','0,8 Hz',0],['a1','frequenz','1,25 s',0],['a1','frequenz','12,5 Hz',0],
 ['a3','periode','1,81 s',1],['a3','periode','1,8 s',1],['a3','periode','1.81s',1],['a3','periode','T = 2π · 0,287 s = 1,81 s',1],['a3','periode','2 s',0],['a3','periode','1,81 Hz',0],['a3','periode','0,29 s',0],['a3','periode','11,3 s',0],
 ['a7','schall','0,759 m',1],['a7','schall','0,76 m',1],['a7','schall','75,9 cm',1],['a7','schall','76 cm',1],['a7','schall','λ = 334 : 440 = 0,759 m',1],['a7','schall','0,8 m',0],['a7','schall','1,32 m',0],['a7','schall','0,759 s',0],
 ['a7','meer','20 m/s',1],['a7','meer','20',1],['a7','meer','v = 300 m : 15 s = 20 m/s',1],['a7','meer','4500 m/s',0],['a7','meer','20 m',0],['a7','meer','0,05 m/s',0],
 ['a1','amp','Amplitude – 3 cm',1],['a1','amp','A = −3 cm',0],['a1','amp','−3 cm',0],['a1','amp','–3 cm',0],['a1','periode','T = 1,0 s − 0,2 s = 0,8 s',1],['a1','periode','0,2 s – 1,0 s',0],
 ['a8','summe','1 cm',1],['a8','summe','+1 cm',1],['a8','summe','10 mm',1],['a8','summe','3 cm',0],['a8','summe','-1 cm',0],['a8','summe','1 s',0],
 ['a8','summe','−1 cm',0],['a8','summe','–1 cm',0],['a8','summe','(+2 cm) + (−1 cm) = +1 cm',1],['a8','summe','Die Summe ist +1 cm.',1],['a8','summe','11 cm',0],['a8','summe','(+2 cm) + (−1 cm) = −1 cm',0],
 ['a6','punkt','Die Büroklammer bewegt sich mit dem Puls fort bis ans andere Ende.','M'],['a12','beleg','Teil 3, Stichwort Schall','M'],
 ['a11','funk','6 m',1],['a11','funk','6,0 m',1],['a11','funk','600 cm',1],['a11','funk','λ = 3·10^8 m/s : 5·10^7 Hz = 6 m',1],['a11','funk','60 m',0],['a11','funk','0,6 m',0],['a11','funk','6 Hz',0],
 ['a14','feder','0,628 s',1],['a14','feder','0,63 s',1],['a14','feder','628 ms',1],['a14','feder','0,1 s',0],['a14','feder','6,28 s',0],
 ['a15','periode','1,63 s',1],['a15','periode','1,6 s',1],['a15','periode','32,6 s',0],['a15','periode','1,5 s',0],
 ['a15','grav','9,51 m/s²',1],['a15','grav','9,51 m/s2',1],['a15','grav','9,5 m/s²',1],['a15','grav','g = 9,51 m/s^2',1],['a15','grav','9,81 m/s²',0],['a15','grav','9,51 m/s',0],['a15','grav','9,87 m/s²',0],
 ['a16','gleich','4 cm',1],['a16','gleich','40 mm',1],['a16','gleich','2 cm',0],['a16','gegen','2 cm',1],['a16','gegen','0 cm',0],['a16','gegen','4 cm',0],
 /* Auswahl: nur die ganze richtige Option */
 ['a2','trend','T wird größer',1],['a2','trend','T wird kleiner',0],['a2','trend','T bleibt gleich',0],
 ['a3','laenge','T wird doppelt so groß',1],['a3','laenge','T wird viermal so groß',0],['a3','masse','T bleibt gleich',1],['a3','masse','T wird doppelt so groß',0],
 ['a4','begriff','Resonanz',1],['a4','begriff','Dämpfung',0],
 ['a6','quer','transversal (Querwelle)',1],['a6','quer','longitudinal (Längswelle)',0],['a6','laengs','longitudinal (Längswelle)',1],['a6','laengs','transversal (Querwelle)',0],
 ['a8','danach','laufen beide unverändert weiter',1],['a8','danach','prallen sie voneinander ab',0],
 ['a10','ordnung','Funk → Infrarot → sichtbares Licht → UV → Röntgen',1],['a10','ordnung','Röntgen → UV → sichtbares Licht → Infrarot → Funk',0],['a10','kamera','Infrarot',1],['a10','kamera','Ultraviolett',0],['a10','sonne','Ultraviolett',1],['a10','sonne','Infrarot',0],
 ['a11','kurz','Mikrowellen (Teil der Radiowellen)',1],['a11','kurz','sichtbares Licht',0],['a11','rot','sichtbares Licht (roter Rand)',1],['a11','rot','Mikrowellen',0],['a11','lang','Radiowellen (UKW)',1],['a11','lang','UV',0],
 ['a14','vier','T verdoppelt sich',1],['a14','vier','T bleibt gleich',0],['a17','welle','Gravitationswelle – keine elektromagnetische Welle',1],['a17','welle','Radiowelle',0],
 /* offene Erklärungen und eigene Messwerte: Lehrkraft bewertet (M) – auch wenn das Stichwort passt oder die Aussage falsch ist */
 ['a2','t40','1,27 s','M'],['a2','t40','12,7 s','M'],['a2','t90','1,9 s','M'],['a2','fehler','Reaktionszeit – 10 Schwingungen messen','M'],['a2','fehler','keine','M'],
 ['a4','beob','Im eigenen Takt wurde der Ausschlag am größten.','M'],['a4','beob','Beim schnellsten Takt am größten.','M'],
 ['a4','fahrzeug','Die Feder federt, der Dämpfer wandelt Energie in Wärme um.','M'],['a4','fahrzeug','Der Dämpfer erzeugt Energie.','M'],
 ['a5','partner','Lukas','M'],['a5','check','alle Fragen richtig','M'],
 ['a6','punkt','Die Klammer bleibt am Ort und geht auf und ab, der Puls läuft weiter.','M'],['a6','punkt','Die Klammer läuft mit zum Ende.','M'],
 ['a8','energie','Die Auslenkung ist nur an dieser Stelle null, danach laufen die Wellen weiter.','M'],['a8','energie','Energie wird vernichtet.','M'],
 ['a9','front','Die Einhüllende der Elementarwellen ist die neue Front.','M'],['a12','beleg','Teil 5: nur im Vakuum','M'],['a13','titel','Draußen sicher','M'],
 ['a15','unsicher','Messfehler und Modell','M'],['a17','trennung','Gemessen wurde ein Signal, die Linse ist ein Modell.','M'],['a17','sicherheit','Es ist nur eine Vermutung.','M']];
(async()=>{const b=await chromium.launch(process.env.CHROMIUM?{executablePath:process.env.CHROMIUM}:{});let bad=0,tot=0;
for(const [f,list] of Object.entries(cases)){const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(R+f);
 for(const [id,key,txt,exp] of list){
  const r=await p.evaluate(([id,key,txt])=>{const t=T.find(x=>x.id===id);S.a[id]=S.a[id]||{};S.a[id][key]=txt;const c=t.chk[key];if(c.man){const r=evalTask(t),p=r.parts.find(x=>x.key===key);return p&&p.man&&!(r.ok&&!r.man)?'M':'kein M';}return checkField(t,key,c).ok;},[id,key,txt]);
  tot++; if(exp==='M'?r!=='M':(!!r!==!!exp)){bad++;console.log('FALSCH',f.split('/')[0],id,key,JSON.stringify(txt),'erwartet',exp,'bekam',r);}
 }
 if(errs.length){console.log('JS-Fehler',f,errs);bad++;}
 await p.close();}
console.log(tot,'Fälle,',bad,'abweichend');await b.close();process.exit(bad?1:0);})();
