# sorteer-hoed

Deze repository is onderdeel van de eerste challengeweek in 2021/2022.

Het doel van deze challengeweek is om een quiz te maken die voor de gebruiker laat zien welke opleidingsrichting het beste is geschikt voor de gebruiker. 
Deze applicatie is geschreven in Python.

Er wordt gebruik gemaakt van een SQL-database met een relatie tussen de vragen en antwoorden. Dit wordt gedaan doormiddel van een foreign key relatie.

De data uit de database ziet er als volgt uit:

```json
[
  {
     "id":4,
     "question":"Hoe bereid je je voor als je een toets hebt?",
     "Answers":[
        {
           "answer":"Ik leer vanuit het boek en dat is genoeg.",
           "FICT":1,
           "SE":1,
           "IAT":2,
           "BDAM":0,
           "niks":0
        },
        ...
     ]
  },
  ...
]
```


Dit project maakt gebruik van bepaalde Python bibliotheken (**Supabase**, **.env**, **PyGame**). Deze zijn als volgt te instaleren:

```
pip install supabase pygame python-dotenv
```

Vervolgens kun je het programma starten via:

```
python main.py
```
