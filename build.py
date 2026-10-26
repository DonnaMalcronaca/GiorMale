# Genera il sito del GiorMale. Per aggiungere un numero: aggiungere un dict in NUMERI (il più recente in cima).
import html, os
NUMERI = [
 {
  "n": 1,
  "slug": "1",
  "data": "Zou, 1511",
  "occhiello": "Cronaca nera",
  "titolo": "Capitan Mutanda rapito dai ricercati!",
  "sommario": "Liberato in fretta e furia dopo l'articolo del Sea Shanty",
  "copertina": "img/n1_prima_pagina.jpg",
  "paragrafi": [
   "Zou, 1511. Brutte notizie per chi crede ancora che i pirati siano gentiluomini incompresi. Nei giorni scorsi Capitan Mutanda, l'alato più elegante del Nuovo Mondo, noto per l'impeccabile mantellina di piume e per una collezione di biancheria che fa invidia alle sartorie di Water Seven, è stato rapito da un gruppo di ricercati. Appena uscito l'ultimo numero del Sea Shanty, i rapitori lo hanno liberato in fretta e furia, senza chiedere un solo Berry.",
   "@@Il giornale dei pirati fa più paura ai pirati che alla Marina.",
   "E già che siamo in tema di Sea Shanty, rispondiamo volentieri al collega. Ci accusa di essere i cattivi? Ebbene sì: siamo stati noi. L'imboscata, le telecamere, il gatto nel fango, la messinscena. Tutto nostro, e ne andiamo fieri. Così cattivi che persino l'autore dell'articolo è venuto a trovarci, ha visto il video e ci ha scritto la colonna sonora. Una serata deliziosa, in ottima compagnia. Peccato che, tra una nota di flauto e l'altra, nessuno sia andato a recuperare l'amico rimasto nel fango. Caro collega, lei non ci ha smascherati: ci ha accompagnati. E con la musica.",
   "Ci accusa anche di lavorare per lo Shichibukai? Indovinato anche stavolta. Lapin Von Juste ha amici, e da oggi sono i più rumorosi dell'isola. Per dimostrarlo, chi ha osato sfidare lo Shichibukai al duello sacro sappia che dovrà prima passare dal Genio del Male in persona: il Dottor Turco è avvisato, il Genio lo aspetta. Mr. Sbuffo, interpellato sulla questione, non ha rilasciato dichiarazioni. Ha sbuffato.",
   "Ci chiamano cattivi? Ringraziamo per la promozione. E per festeggiare, la redazione annuncia la prima Fiera del Gatto, il [Giorno X], nel cuore della Nube Acida: c'è chi a Zou cerca la cura, noi andiamo a farci male. Al centro della fiera, un manichino dello Stregatto a grandezza naturale, donato ai Moschettieri del Ducato, su cui chiunque potrà finalmente sfogare la propria rabbia a colpi di pugni. Ingresso libero, guantoni a noleggio. Il manichino avrà baffi veri. Almeno uno. Ci stiamo lavorando.",
   "E per chi trova i manichini troppo tranquilli, a seguire una rissa vera, tra le nebbie, con fuochi d'artificio e pubblico pagante. Chi ha qualcosa da ridire, venga pure a dircelo di persona: lo aspettiamo lì.",
   "Capitan Mutanda è sano, salvo e, ci assicurano, perfettamente vestito. Alla redazione resta una sola domanda per i nostri lettori: se i difensori della libertà sono questi, chi difende Zou da loro?",
  ],
  "firma": "Donna Malcronaca",
  "riquadro": ("Fiera del Gatto", "[Giorno X] · Nube Acida · Ingresso libero, guantoni a noleggio · A seguire: rissa vera!", "img/n1_volantino.jpg"),
  "galleria": [("img/locandina_gatto_ballata.jpg", "Dall'archivio: «Il Gatto e la Ballata», edizione straordinaria")],
 },
]

def head(titolo, base):
    return f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titolo)}</title>
<link rel="stylesheet" href="{base}style.css"><link rel="icon" href="{base}img/piuma.svg">
</head><body>
<header class="testata"><a href="{base}index.html"><h1>Gior<span class="male">Male</span><img class="piuma" src="{base}img/piuma.svg" alt=""></h1></a>
<div class="sottotestata"><span>Zou · Nuovo Mondo</span><span>Cronaca nera, rosa e di tutti i colori</span><span>Diretto da Donna Malcronaca</span></div></header>
<nav><a href="{base}index.html">Ultimo numero</a><a href="{base}archivio.html">Archivio</a></nav>
<main class="wrap">"""

FOOT = """</main><footer>Il GiorMale non risponde di esplosioni, rapimenti e baffi mancanti. Qui nessuno è invisibile.</footer></body></html>"""

def articolo(N, base):
    return f'<figure class="pagina-intera"><a href="{base}{N["copertina"]}"><img src="{base}{N["copertina"]}" alt="GiorMale numero {N["n"]}: {html.escape(N["titolo"])}"></a></figure>'

os.makedirs("numeri",exist_ok=True)
ult=NUMERI[0]
open("index.html","w",encoding="utf-8").write(head("GiorMale — "+ult["titolo"],"")+articolo(ult,"")+FOOT)
for N in NUMERI:
    open(f"numeri/{N['slug']}.html","w",encoding="utf-8").write(head(f"GiorMale n.{N['n']} — "+N["titolo"],"../")+articolo(N,"../")+FOOT)
cards="".join(f'<a class="numero" href="numeri/{N["slug"]}.html"><img src="{N["copertina"]}" alt=""><h4>N. {N["n"]} — {html.escape(N["titolo"])}</h4><span>{html.escape(N["sommario"])}</span></a>' for N in NUMERI)
open("archivio.html","w",encoding="utf-8").write(head("GiorMale — Archivio","")+'<h2 class="titolo">Archivio</h2><p class="sommario">Tutti i numeri del GiorMale, dal più recente</p><div class="archivio">'+cards+'</div>'+FOOT)
open(".nojekyll","w").close()
print("ok")
