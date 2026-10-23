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
(async()=>{const b=await chromium.launch();let bad=0,tot=0;
for(const [f,list] of Object.entries(cases)){const p=await b.newPage({viewport:{width:390,height:844}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(R+f);
 for(const [id,key,txt,exp] of list){
  const r=await p.evaluate(([id,key,txt])=>{const t=T.find(x=>x.id===id);S.a[id]=S.a[id]||{};S.a[id][key]=txt;const c=t.chk[key];return checkField(t,key,c).ok;},[id,key,txt]);
  tot++; if(!!r!==!!exp){bad++;console.log('FALSCH',f.split('/')[0],id,key,JSON.stringify(txt),'erwartet',exp,'bekam',r);}
 }
 if(errs.length){console.log('JS-Fehler',f,errs);bad++;}
 await p.close();}
console.log(tot,'Fälle,',bad,'abweichend');await b.close();process.exit(bad?1:0);})();
