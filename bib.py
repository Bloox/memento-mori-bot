import random
def random_title(msg):
    starters = [
        "Bloody ","Deadly ","Precise ","Unknow ","Forgoten ",'Dead ',
        "Chosen ","Psychopatchic ","English ",'Slavic ',"Romanic ",
        "Accuret","Powered ",'Immortal'
    ]
    number=str(random.randrange(0,99))
    if len(number)<2:
        number='0'+number
    enders =  [
        "son of Vallhala","gang lider", "Cryptoman","Pretender",
        "king of evil", "Horsmen of Apocalypsa","Messenger of death",
        "Programmer of Reality","Spolier in your car","Men in your walls",
        "fanatic of Mythology", "Harvester of moon","Plag doctor","Kingsmen",
        "personfication of Cats","Marchant indead","Dead in Person","aka Death",
        "Cousin of Hades","Grandparent of Gaia","the Great",'egyptian Goddes',
        "Godlike",f'number {number}','Doctor of Chaos',f"scp-4242240{number}",
    ]
    num = [
        "XXXXII",
        "IX",
        "XIII",
        "IVXXXX",
        "XVI",
        "XVIII",
        "XII",
        "ICXIVI",
    ]
    return msg.author.name +" "+ random.choice(starters) + random.choice(enders) + ' ' + random.choice(num)
sins_e = [
    "you only sin is iq %s",
    "your sin is amout of social interactions %s",
    "yes you have many of them",
    "no sin  has been found :(",
    "404666 - no sin has been found"
    "I am teapot 🫖",
    "Your name: %s",
    "Returnig random number in range -∞ to ∞ : 42",
    "Returnig random number in range -∞ to ∞ : 424224067",
    "You are wizard Harry",
    "Kill the HEAD!",
    "Co to było Hary? Dzikie zwirze? A może stado dzikich zwierząt?",
    "Bedę go zjadł",
    "--Tutaj wpisz nawiązanie--",
    "Aua!, bcdefghijklmnoprsuwxyz",
    "Aua!, ciwenia..."
    "Never gonna give you up, never gonna let you down",
    "Frank:Howard \nHoward:Yes frank",
    "O its you, it was a loooong time, how have you been? i was very busy; being dead",
    "Chrissy, wake up! Chrissy i don't like this.",
    "In memory of Edi",
    "Minecraft 2d",
    "Terraria 3d",
    "Hey Vsauce, Michel here",
    "Kukabura chichotliwa, https://pl.wikipedia.org/wiki/Kukabura_chichotliwa",
    "Welcom to the internet",
    "λ",
    "🦀",
    "Carcenizacja",
    "Pamiętaj żeby zasugerować własne estereggi",
    "Polglish",
    "Enpolski",
    "Memento mori",
    "''Koty, tak koty są fajne''-Śmierć",
    "I know you're here, DRACULA, you big fucking nerd, where's my goddamn money?",
    "I`m okey, i`m not alcocholic",
    "Go banana, go banana men",
    "Stolas:I pay you\nBlitz∅:with what?\nStolas:Money\nBlitz∅:Done",
    "engenirs:3.14≈4",
    "π*👁️‍🗨️",
    "v={n | n is set and n∉n}, v∈v?",
    "Dead don't die",
    "Only murders in the building",
    "♃♀♁♂♄♅♆♇⚷⚶⚵⚴⚳🜨☿☾☉ gottem know them all!",
    "42 is essteregg one its own",
    "minCEraft",
    "genshin impact :(",
    "https://tenor.com/view/helluva-boss-helluva-boss-blitzo-its-complicated-gif-21389955",
    "we are nerds and geeks",
    "William James Moriarty, Louis James Moriarty, Louis James Moriarty",
    "Jamie died a virgin, but at least he wasn't buried as one.",
    "Jaws that make you head explode",
    "Juice that make you head explode",
    "We live in darkness",
    'scp-963',
    'thing that dr. Bright...',
    "Ozyr scp  ...... nadal nie żyje :(",
    'Ozyr nadal czekamy',
    "Piofil",
    "Jabłko składa się z: papieru, nadjabłcza i krainy grzybów",
    "Poradnik uśmiechów",
    'I hope this text will never appear',
    "3 2 1 ..."
    "You can't spell america without Erica!",
    "who do you work for? sir i tell you already, Scoops Ahoy",
    "Dustybun",
    "11 vs 1",
    'Mindflayer or 1 or Vecna',
    'Vecna want to play some d&d',

    "1.618",
    '3.1415',
    "418 - 🫖",
    "spider work as web developer",
    "if you see this message don't contact with owner of bot!",
    "Captcha scary!",
    "The wors meat pie in london",
    "I am a pickle rick",
    "Hades is the best!",
    "Love you Odin!",
    "Atena? bardziej jak Antena!",
    "Akcja bałtycka 2022 (zaproponuj tekst tutaj)",
    "Jeloń",
    "Helena aka Demoemo",
    "ᚣᛟᚢ ᛞᛟᚾ`ᛏ ᚢᚾᛞᛖᚱᛊᛏᛖᚾᛞ ᛏᚺᛁᛊ ᛗᛖᛊᛊᚨᚷᛖ",
    "I don't see what is in this for Erica",
    "Nerdziaki moje wy słodziaki (mówią o StrangerThigns)",
    "Steve 💗",
    "THIS MESSAGE IS SEND BY AI!",
    "Bo prochem jesteś i w kraba się obrucisz!",
    "Crab cycle:\n1.Become crab\n2.Repeat step 1"
    "Arszeniku tam bez liku!",
    "what is that:\nHas color of milk\nSmell like milk\nTaste like milk\nFeel like milk?\n answer is:milk with arsenic",
    "Rozstaliśmy się przez rużnicą w guście artystycznym, on wolał akty, ja martwą nature",
    "skąd mogłam wiedzieć że ma uczulenie na arszenik",
    "i się przewrócił na nóż, 7 razy",
    "Może mnie pan wyżucić przez okno? Nie. Ale dlaczego? Nie można wyżucać śmieci przez okno",
    "Pamiętajcie dzieci, nie pal dzieci, dbaj o śmieci!",
    "this message has id:99",
    "Ja jestem Staszek Igraszek wasz chodowca Lam!",
    "To jest poprostu bardzo dobre - stillgart",
    "Pachnie to wręcz nieziemsko - stillgart",
    "Jest to takie bardzo esencjonalne -stillgart",
    "Jeżeli bóg ceni inteligencje już jest pan zbawiony",
    """S:Dla pana spycjalnie 1000zł
    K:Ja nie mam tyle przy sobie
    S: No dobrze dobrze 500!
    K: Ale to sie tak źle kojarzy
    S: Dobrze to niech będzie 200zł
    K: Wie pan ja tak dobrze nie zarabiam
    S: 100zł
    K: Czasy są cięzkie...
    S: 0 zł
    K: Prosze pana ja z polski jestem
    S: A to ja jezcze dopłace!""",
    "Szedł mozart i... bach!",
    "Toss a Coin to Your...",
    "Złota daj wiedzmie mojej, sakiewką potrząśnij ...",
    "No more Room in hell",
    "Go Burnham",
    "Tomsky",
    "Mayby i am to dark",
    "Death, love & robots",
    "Hail is synonimus to Hay!",
    "Axium Verge",
    "Axium Verge 2"
    "Wolf amonus soundtrack",
    "Ratman  & Chell",
    "Ma początku były 42 pierogi",
    "Chyba nie chcesz wracać do więzienia, do tych kapitalistycznych świń?!",
    "this messege is empty",
    "nothing to see here: ||👌muka|| ",
    "Tulio i Miguel",
    "0x2a",
    "Crissnojoke",
    "https://cdn.discordapp.com/attachments/724898905124372490/1002665063192199178/hahaha.png",
    "Where is Francis?",
    "See, Albert? I told you it was a flying tank!\nAnd it's coming right at us!\n\nBut it can't be! This is first class!",
    "https://cdn.discordapp.com/attachments/979369267650756671/1007964096093749269/unknown.png",
    "https://cdn.discordapp.com/attachments/724898905124372490/997170723086929",
    "Porpostu obrazek z kozłem:\nhttps://media.discordapp.net/attachments/890668508512399451/995003461013872720/20220708_182805.jpg"
    """Mam wolne o:
00:02
00:04
00:08
00:16
00:32
00:64
01:28
02:56
05:12
10:24
20:48""",
    "Data not found",
    "Joahim its correct speeling",
    "ϡ - Sampi",
    "424224067 is prime",
    "Craby w Grach",
    "Crap skład i Gry z kosza",
    "Hedowa linia kosmemytków do włosów kręconych",
    "To znowu oni!",
    "Ku chwale Miedzińskiego",
    "+1 Mietczyński",
    "Erwin Schrödinger and his Cat",
    "End is never the End is never the ...",
    "The end is night",
    "Co robie papierek na szczycie góry? Celeści",
    "UNUSUAL MEMES COMPILAION V42",
    "In memory of: Gravity Falls",
    "Marc Specter",
    "Marko 27",
    "Pancake shot",
    "Pasta, Chees & Tomatos",
    "Puzzle games!",
    "Platformer games!",
    "Remember kido, do not play with genshino",
    "Remember kido, don't watch tiktiko",
    "Remember kido, don't play fortnito",
    "Pamiętaj cholero nigdy nie dziel przez 0!",
    "n/0 = ∅",
    "Tamashi",
    "Baba is Love",
    "Textorcis more like Notfunrcis",
    "Happy meat farm",
    "Pizza is a sandwich",
    "my favorit meal sand wich",
    "7 bilion Robots",
    "Toiletturret (pozdro dla kumatych)",
    "Can i cook chicken by slapping it?",
    "Bad Dream: Narcoza",
    "Botanimacula",
    "Browara halla?",
    'Bracia - Opowiesz dwojga synowie',
    "Dumpster Truck",
    "Teapothead, Don't deal with The Server",
    "Δ🏃 1 & 2",
    "Cardydungeon",
    "Lagtorio",
    "Geomatry Mash",
    "Helltaker (nie ma przeróbki bo w samo sobie to parodnia)",
    "Logic Morph",
    "Mitoza",
    "Portal wombat X",
    "Portal wombat 11",
    "Noita was Wita",
    "Patrykalny Parapudełkalny",
    "Four horsmen of modern apocalipsa:\n1.Tiktok\n2.Fortnie\n3.Free online tutorials\n4.123 go!",
    "No … I am your Father…",
    "Dziwniejsze żeczy",
    "Dobry zły znak", 
    "Terry prechet!",
    "Mak Kwacz",
    "Panie doceńcie doceń mnie pan!",
    "Styrta się pali!",
    "h4rdy +0 d3c0d3!",
    "The Świadek",
]

sins_e+=[random_title]*20