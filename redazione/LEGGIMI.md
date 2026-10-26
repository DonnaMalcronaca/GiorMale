# Redazione GiorMale (sorgenti, non pubblicate nel sito)
- prima_pagina_nN.html: impaginato fisso 1122px di ogni numero (font Rye / IM Fell English / Great Vibes).
- Render: python3 shotfull.py "$PWD/prima_pagina_nN.html" out.png  (screenshot di .pagina, scala 2)
- Poi: convertire in JPEG largo 2000px -> ../img/nN_prima_pagina.jpg, aggiungere il numero in ../build.py (lista NUMERI), python3 build.py, commit e push.
- numeroN_testo.md: testo definitivo dell'articolo.
