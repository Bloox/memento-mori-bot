import random

version="42. 7.001/0" #for every new version increase number befor /
note="𝅘𝅥𝆕"
update_name="⮔ NO MORE" 
splash=["terra.txt",'minecraft.txt']
PRELOAD={"SH":{}}
def baba_generator(msg):
    
    nouns = ['ROCK',"BABA","KEKE","WALL",'ME','ROBOT','BIRD','BOG','BELT','BUNNY','TEXT','LEVEL','ALL','LOVE',"UFO"]
    adverbs= ["YOU","PUSH","PULL","MOVE","STOP","SHIFT","DEFEAT","HOT","MELT","OPEN","SHUT","SINK","WEAK","TELE","SWAP","WIN","WORD"]
    rule=f"{random.choice(nouns)}"
    condytionA = ["ON %s","NEAR %s","FACING %s","WITHOUT %s"]
    prefix=["IDLE ","LONELY ","OFTEN ","SELDOM "]
    beA=["HAS %s","EAT  %s", "FEAR %s","FOLOW %s","MAKE %s","MIMIC %s"]

    if random.randint(0,3)==0:
        rule=rule+' '+random.choice(condytionA)%random.choice(nouns)
    elif random.randint(0,3)==0:
        rule=rule+f" FEELING {random.choice(adverbs)}"
    if random.randint(0,3)==0:
        rule=random.choice(prefix)+rule
    tt=random.randint(0,2)
    if tt==0:
        rule+=f' {random.choice(beA)%random.choice(nouns)}'
    elif tt==1:
        rule+=f' IS {random.choice(adverbs)}'
    else:
        rule+=f' IS {random.choice(nouns)}'
    return rule
def minecraft_splash(msg):
    chosen=random.choice(splash)
    if chosen not in PRELOAD['SH']:
        with open(f"gameslpash/{chosen}",encoding="utf-8") as f:
            text=f.read()
            PRELOAD['SH'][chosen]=text.splitlines()
    #print(chosen)
    return f"{chosen} says:{random.choice(PRELOAD['SH'][chosen])}"


def random_title(msg,starter=1,ender=1,indexA=None,indexB=None):
    gods = [
        "Artemis","Athena","Hephaestus","Hades",'Tanatos',"Morpheus",'Tartarus',
        "Flying Spaghetti Monster","Cthulhu","True","Lie","Azothot","Spthot","Nyks","Chaos",
        "Agape",
        "Dreamer","Eldrich ones","the Uninvited","Eros","Law","Justice","One who watch us",
        "One from beyond words",'One above our world',"Who think","Odin","Thor","Loki","Monokuma",
        "From upsidedown","Karl with the Hat","Tinkerer of existenc","Apollo","the Sun","Higher being",
        "of Greates evil","Death, last horsmen of the apocalypse","War, second horsmen of the apocalypse",
        "Conquest first horsmen of the apocalypse","Famine third horsmen of the apocalypse",
        "Youtube algoritmes","TVN","TVP","Muse","Erabus", "Nyx","Oneiroi","Moros","Momus","Philotes",'Gares',
        "Hypnos","Eris","Apate","Oizys"
    ]
    starters = [
        "Bloody ","Deadly ","Precise ","Unknow ","Forgoten ",'Dead ',
        "Chosen ","Psychopatchic ","English ",'Slavic ',"Romanic ",
        "Accuret ","Powered ",'Immortal ',"Actual ","Nonperfect ","Perfect ",
        "Better ","Worse ","Psychopathic ","Romantic ","Emo ","Memorable ",
        "Bitter ","Confused ","Bipolar ","Confused ", "Defused "
        "Capitalistic ", "Comunistic ","Socialistic ","Democratic ", "Monarchist ",
        "Individualistic "
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
        "The Dreamer","The Executer","Savior of worlds",'Destroyer of words',
        "without a name","with name",
        "Great Dreamer",f"Higher Prist of {random.choice(gods)}",f"Prist of {random.choice(gods)}"
    ]
    num = [
        "XCII",
        "IX",
        "XIII",
        "IVXXXX",
        "XVI",
        "XVIII",
        "XII",
        "ICXIVI",
    ]
    if indexA==None:
        indexA=random.randrange(0,len(starters))
    if indexB==None:
        indexB=random.randrange(0,len(enders))
    return msg.author.name +" "+ starters[indexA]*starter + enders[indexB]*ender + ' ' + random.choice(num)*int((random.randrange(0,6)<1))
sins_e = [
    "your only sin is iq %s",
    "your sin is amount of social interactions %s",
    "yes you have many of them",
    "no sin has been found :(",
    "404666 - no sin has been found",
    "I am teapot 🫖",
    "Your name: %s",
    "Returnig random number in range -∞ to ∞ : 42",
    "Returnig random number in range -∞ to ∞ : 424224067",
    "You are a wizard Harry",
    "Kill the HEAD!",
    "Co to było Harry? Dzikie zwirze? A może stado dzikich zwierząt?",
    "Bedę go zjadł",
    "--Tutaj wpisz nawiązanie--",
    "Aua!, bcdefghijklmnoprsuwxyz",
    "Aua!, ciwenia...",
    "Never gonna give you up, never gonna let you down",
    "Frank: Howard \nHoward: Yes frank",
    "O it's you, it was a loooong time, how have you been? I was very busy; being dead",
    "Chrissy, wake up! I don't like this!",
    "In memory of Edi",
    "Minecraft 2d",
    "Terraria 3d",
    "Hey Vsauce, Michel here",
    "Kukabura chichotliwa, https://pl.wikipedia.org/wiki/Kukabura_chichotliwa",
    "Welcome to the Internet",
    "λ",
    "🦀",
    "Carcinisation",
    "Pamiętaj żeby zasugerować własne estereggi",
    "Polglish",
    "Enpolski",
    "Memento mori",
    "''Koty, tak koty są fajne''-Śmierć",
    "I know you're here, DRACULA, you big fucking nerd, where's my goddamn money?",
    "I'm okey, I'm not alcoholic",
    "Go bananas, go banana men",
    "Stolas:I'll pay you\nBlitz∅:with what?\nStolas:Money\nBlitz∅:Done",
    "engenirs:3.14≈4",
    "π*👁️",
    "v={n | n is set and n∉n}, v∈v?",
    "The Dead don't die",
    "Only murders in the building",
    "♃♀♁♂♄♅♆♇⚷⚶⚵⚴⚳🜨☿☾☉ gotta know them all!",
    "42 is esteregg on it's own",
    "minCEraft",
    "genshin impact :(",
    "https://tenor.com/view/helluva-boss-helluva-boss-blitzo-its-complicated-gif-21389955",
    "all of us are nerds and geeks",
    "William James Moriarty, Louis James Moriarty, Albert Moriarty",
    "Jamie died a virgin, but at least he wasn't buried as one.",
    "Jews that makes your head explode",
    "Juice that makes your head explode",
    "We live in darkness",
    'scp-963',
    'things that dr. Bright can\'t do ...',
    "Ozyr scp  ...... nadal nie żyje :(",
    'Ozyr nadal czekamy',
    "Piofil",
    "Jabłko składa się z: papieru, nadjabłcza i krainy grzybów",
    "Poradnik uśmiechu",
    'I hope this text will never appear',
    "3 2 1 ..."
    "You can't spell america without Erica!",
    "who do you work for? Sir I told you already, Scoops Ahoy",
    "Dustybun",
    "11 vs 1",
    'Mindflayer or 1 or Vecna',
    'Vecna wants to play some d&d',
    "1.618",
    '3.1415',
    "418 - 🫖",
    "spider works as a web developer",
    "if you see this message don't contact with owner of the bot!",
    "Captcha scary!",
    "The worst pies in London",
    "I am a pickle rick",
    "Hades is the best!",
    "Love you Odin!",
    "Atena? bardziej jak Antena!",
    "Akcja Bałtycka 2022: kapibara obchodziara",
    "Jeloń",
    "Helena aka Demoemo",
    "ᚣᛟᚢ ᛞᛟᚾ`ᛏ ᚢᚾᛞᛖᚱᛊᛏᛖᚾᛞ ᛏᚺᛁᛊ ᛗᛖᛊᛊᚨᚷᛖ",
    "I don't see what is in this for Erica",
    "Nerdziaki moje wy słodziaki (mówią o StrangerThings)",
    "Steve 💗",
    "THIS MESSAGE IS SEND BY AI!",
    "Bo prochem jesteś i w kraba się obrócisz!",
    "Crab cycle:\n1.Become crab\n2.Repeat step 1"
    "Arszeniku tam bez liku!",
    "what is that:\nHas color of milk\nSmells like milk\nTastes like milk\nFeels like milk?\n answer is: milk with arsenic",
    "Rozstaliśmy się przez różnice w guście artystycznym, on wolał akty, ja martwą naturę",
    "skąd mogłam wiedzieć że ma uczulenie na arszenik",
    "i się przewrócił na nóż, 7 razy",
    "Może mnie pan wyrzucić przez okno? Nie. Ale dlaczego? Nie można wyrzucać śmieci przez okno",
    "Pamiętajcie dzieci, pal dzieci, dbaj o śmieci!",
    "this message has id:99",
    "Ja jestem Staszek Igraszek wasz chodowca Lam!",
    "To jest po prostu bardzo dobre - stillgart",
    "Pachnie to wręcz nieziemsko - stillgart",
    "Jest to takie bardzo esencjonalne -stillgart",
    "Jeżeli Bóg ceni inteligencję już jest pan zbawiony",
    """S:Dla pana specjalnie 1000zł
    K:Ja nie mam tyle przy sobie
    S: No dobrze dobrze 500!
    K: Ale to sie tak źle kojarzy
    S: Dobrze to niech będzie 200zł
    K: Wie pan ja tak dobrze nie zarabiam
    S: 100zł
    K: Czasy są cięzkie...
    S: 0 zł
    K: Prosze Pana ja z Polski jestem
    S: A to ja jeszcze dopłace!""",
    "Szedł Mozart i... Bach!",
    "Toss a Coin to Your Witcher",
    "Złota daj wiedźmie mojej, sakiewką potrząśnij ...",
    "No more Room in hell",
    "Go Burnham",
    "Tomsky",
    "Maybe I am too dark",
    "Death, love & robots",
    "Hail is synonimus to Hay!",
    "Axiom Verge",
    "Axiom Verge 2"
    "Wolf among us soundtrack",
    "Ratman & Chell",
    "Na początku były 42 pierogi",
    "Chyba nie chcesz wracać do więzienia, do tych kapitalistycznych świń?!",
    "this message is empty",
    "nothing to see here: ||👌muka|| ",
    "Tulio i Miguel",
    "0x2a",
    "Chrissnojoke",
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
    "Joahim is a correct speeling",
    "ϡ - Sampi",
    "424224067 is prime",
    "Kraby w Grach",
    "Crap skład i Gry z kosza",
    "Hedowa linia kosmemytków do włosów kręconych",
    "To znowu oni!",
    "Ku chwale Miedzińskiego",
    "+1 Mietczyński",
    "Erwin Schrödinger and his Cat",
    "End is never the End is never the ...",
    "The end is night",
    "Co robi papierek na szczycie góry? Celeści",
    "UNUSUAL MEMES COMPILATION V42",
    "In memory of: Gravity Falls",
    "Marc Spector",
    "Marko 27",
    "Pancake shot",
    "Pasta, Chees & Tomatoes",
    "Puzzle games!",
    "Platformer games!",
    "Remember kiddo, do not play in genshino",
    "Remember kiddo, don't watch tiktiko",
    "Remember kiddo, don't play fortnito",
    "Pamiętaj głupia cholero nigdy nie dziel przez 0!",
    "n/0 = ∅",
    "Tamashi",
    "Baba is Love",
    "Textorcis more like Notfunrcis",
    "Happy meat farm",
    "Pizza is a sandwich",
    "my favourite meal: sand wich",
    "7 billion Robots",
    "Toiletturret (pozdro dla kumatych)",
    "Can I cook chicken by slapping it?",
    "Bad Dream: Narcosis",
    "Botanimacula",
    "Browara halla?",
    'Bracia - Opowieść dwojga synowie',
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
    "Dziwniejsze rzeczy",
    "Dobry zły znak", 
    "Terry Prechet!",
    "Mak Kwacz",
    "Panie Doceńcie doceń mnie pan!",
    "Styrta się pali!",
    "h4rd +0 d3c0d3!",
    "The Świadek",
    "Fez",
    "Jaka to soundtracka?",
    "Gwiezdny deweloper dolina",
    "Kabaret 5 fala",
    "Grupa filmowa KLPS",
    "Earth is a torus you fools",
    "Spodniepowieści",
    "#LegendyGdańskie",
    "r/programmerhummor",
    "So you are programmer? then center div both horizontal and vertical",
    "Well in that case",
    "Are you human?",
    "Staszek pije *Kompocik*",
    "*itali* **bold** ||spoiler||",
    "Mark Rober",
    "H₂O",
    "Powinniśmy zakazać diwodorkutlenu w szkołach",
    "Czy wiesz że 100% ludzi któży spożyli diwodorektlenu umarło?",
    "Picie dzieci, nie pal śmieci... Coś mi się chyba pomieszało",
    "Mamo, Tato wole wode!",
    "Wiecie co najbardziej lubie w picu kawy? picie kawy",
    "Wiecie co najbardziej lubie w picu wody? picie wody",
    "Wszyscy się kłócą co powino się dać pierwsze, mleko czy płatki, a wszyscy powinniśmy wiedzieć, że pierwsza powinna być miska",
    "Every day I wake up, then I start to brake up\nLonely is man without love",
    "Co było pierwsze: jajko czy kura? pierwsze były 42 pierogi.",
    "Let me introduce you to my cult",
    "This server starter pack: Being nerd, Dark Humor, being brain connected...",
    "If I was blind I would be happy that I'm not deaf",
    "if I was deaf, then there is no happines in a world :(",
    "Don't regret any decision, because you can't change the past",
    "10⁹ is ...",
    "Własnym oczom już nie wierze, na przystanku siedzi pies, ma na sobie gps",
    "𝅘𝅥𝆕Kids die for free𝅘𝅥𝆕",
    "studnia∈💼",
    "Widzimy się w piątek o 5 chyba, że zapomne albo mi sie nie będzie chciało",
    "Avatar(i nie chodzi o niebieskie ludzie)",
    "Klaus-04",
    "5 stop killing people",
    "karl that kills people",
    "Blood of ⚡",
    "My font recomendation: Fire Code, Noto Emoji(black&white)",
    "Biedronkowy merch!",
    "Eden",
    "Cats movie was somthing",
    "Monty Python and the Holy Grail",
    "Żywot Braiana",
    "Latający Cyrk",
    "Ku czci Neil Gaiman",
    "Big fat, and very boring, god, with small pp, yes you guessed right I meant: Zeus",
    "https://www.youtube.com/channel/UClPPmQw2t1e7KlM5wxTXluw",
    "Jake Lockley","Steaven Grant",
    "MLP *was* the best!",
    "Khonshu",
    "Brazzos",
    "https://tenor.com/view/your-mother-great-argument-however-megamind-your-mom-yo-mama-gif-22994712",
    "Splash",
    'Audio > Graphic',
    "2d > 3d",
    "4d > 3d & 4d > 2d",
    "Yanderedev",
    "This is a school announcement; it is now 10pm, at such it is officialy nighttime!",
    "Good mornig everyone, get ready to greet another beautiful day",
    "Za wszelkie orty serdecznie pszepraszam",
    "Przed użycie skonsultuj się z Ortologiem lub Lamacełtą",
    "Power of Fishing pool!",
    "Let's game it out",
    f"This is version:{version} of text lib",
    "Tajemnicza Irma Vep - Teatr Wybrzeże",
    "Awantura w Chioggi - Teatr Wybrzeże",
    "Inteligenci - Teatr Wybrzeże",
    "Kim jest pan Schmitt? - Teatr Wybrzeże",
    "Sztuka - Teatr Wybrzeże",
    "Zieloone pesto > Czerwone pesto",
    "Zielone zielone robie sobie zielone",
    "We love trees",
    "We love forest",
    "I have feeling that someone here is scared to death by bugs",
    "Covid-19 rejoing the server",
    "Ej, co jest doktorku?",
    "Chyba widziałem kotecka, Tak tak dobrze mi się zdawało naprawde widziałem kotecka",
    "I hate game with qrcodes",
    "Zasady talosa",
    "Zasady robotyki, who cares",
    "Quantum computing will not replace humans",
    "Math or M3th? (discord is just a joke)",
    "Google vs DuckDuckGo",
    "Chrome Ultron",
    "Mój stary to fanatyk wędkarstwa",
    "Mój stary to fanatyk leczo",
    "UwU",
    '🦉',
    "I like my code how like I like my life, without bugs.",
    "Onomatopeje",
    "Apokalipsa się zbliża (prznajmniej mam taką nadzieje)",
    "Co widzi na cmentarzu optymista? Same plusy\n A co wydzi na cmentarzu pesymista? Też same plusy",
    "↑↑↓↓←→←→AB,START",
    "My father hates bugs",
    "Mógłbym jeść naleśniki całe życie",
    "I am operator of my pocket calculator",
    "You will be Okey",
    "Materials can't go to Heven, they just endup in recycle bin",
    "Never say never exept the time that you say to never say never",
    "Beep Beep I'm a Sheep",
    "He is gay or european is hard to guarantee!",
    "To be continued!",
    "Brimstone!",
    "C,C++,C# or CARBON?",
    "JS,typescript,node.js",
    "Brainfuck,Malbolge,Whitespace",
    "Java,Kotlin",
    "```py\nmsg=lambda: random.choice(sins_e)```",
    "```py\nc='c=%r;print(c%%c)';print(c%c)```",
    'exec(s:=\'print("exec(s:=%r)"%s)\')'
    'Litarature Club!',
    "Mornel Kornel - Morneliusz Korneliusz",
    "Anolog horror!",
    "THIS IS YELLING FOR MOJANG",
    "dlaczego √2 zabiłó 3? bo jest nie obliczalne!",
    "DON`T always USE CAPSLOCK",
    "Sok z kaktusa, bardzo pyszny i odżwyczy!",
    "Smartgasm: Zaraz pokaże jak zmienić kostke `Co` w super radioaktywnty `⁶⁰Co`, opowiem też jak zrobić z niego bombe kobaltową...",
    "Ayato gozaimasu",
    "No goverment plis",
    "You know, some guys just can't hold their arsenic",
    "Mroczny złodziej",
    "Memento Mori vs Vita Aeterna",
    "Pani Basia",
    "Acid Dragon",
    "Nożyczki siódemki",
    'MRS. HUDSON: "Oh, I\'m sure something will turn up. A nice murder. That\'ll cheer you up',
    "I'm not a psychopath, I'm a high-functioning sociopath. Do your research.",
    "456 unfortunutly",
    "MIB",
    "There is nothing behind red doors Jane",
    "𝅘𝅥𝆕0118 999 881 999 119 725.. 3𝅘𝅥𝆕",
    "Green eggs" ,
    "To nie jest tak że dobrze, lub nie dobrze...",
    "Gdybym miał powiedziec co najbadziej cenie w życiu, to powiedział bym ze ludzi",
    "Jeżeli ja jestem mną bo ty jesteś sobą, a ty jesteś sobą ....",
    "Ale na siku, nie żeby zabijać",
    "Ale ten pan dalej nie oddycha",
    "Polska się nam skończyła [nerwowy śmiech]",
    "Głupia tak tżywać kumpla w lodziarce, nawet martwego.",
    "Ty ,ty, ty, ty! Nie bądz taki ornitolog.",
    "BNA, Brand new Air - Krakow",
    "The end of the Flirting world",
    "Horsin` Around",
    "Tok Tok",
    "Every time somone take picture of you, he trap part of your soul in it",
    "This is nicest thing that you said to my dad",
    "✋Hay Goodbay✋",
    "Punishment it anthonym of Crime",
    "So you are gamer? Then mine the Bedrock",
    "So you know javascript? Then name every fatal error",
    "John sin",
    "Phoenix SC",
    "If you feel usless remember than English quin death Protocole exist",
    "If you feel usless remember that this bot exist",
    "Chat report system belong in trash!",
    "#7834",
    '@evryone',
    "@evertwo",
    "Minectafg PocGet Edition",
    "<3",
    "<3",
    "<3",
    "Lilo & Kicz",
    "I am root, Marvel original",
    "Lighmonth",
    "Bulian",
    "Aloic in Whateverland",
    "Lunar ipposites",
    "Quenwomens",
    "Livepool 2, where is Wald",
    "Raya and the last of us",
    "Untangled",
    "Beauty and the Person",
    "Too big Mermaid",
    "Coffe Beauty",
    "Cinicalrella",
    "MIW",
    "Princess and The animal right fighters",
    "The Duck King 1.5 Hakuna Matata",
    "Nowa szaty Cesarzowej",
    "Ralph Demolka na Reddicie",
    "Herkules more like Dumbandusless",
    "Herkules more like HERAkles",
    "Tarzan po ziemi",
    "tidzimi:Chińskie Bajki",
    f"Updata:{update_name}",
    "HypeTrain D+",
    "HBO max",
    "Netflix",
    "Amazon Prime Video",
    "Player-",
    "Enjoy RoxMb - XD",
    "Rotten Groom",
    "Night Befor Easter",
    "Reymond Red Redington",
    "In memory of Zachtronics",
    "^-^",
    "Pół Życie",
    "Bird-human",
    "Phonix-human",
    "I am potato rick!",
    "Chees,pasta and eggs; my recomendation",
    "Non-nativerock",
    "150-hour Spaghetti bolognese",
    'że też mnie to nie tidzimi',
    "Alan Blacker",
    "AugustTheGoos",
    "Begula",
    "BenDoker",
    "Ciumkal Smoczki R.I.P",
    'Corle was wytłumaczy co to za biała substancja',
    "Dani goes for milk",
    "Dr Bond",
    "Emce▲" ,
    "Forggotten",
    "Airship.io",
    "Gaming on Teafeine",
    "Harry404UK",
    "iammotherbod",
    "Fiery Puzzle",
    "ilmelon",
    "JK legoworks",
    "Juseppi",
    "Jo🔑po🔑",
    "Jon Duo",
    "Macieje",
    "Kartofelek",
    "Kartofelek.YB | Grajd...",
    f"{note}You suck at cookin, yes you totaly do{note}",
    "Nile:red,green,blue basicly whole rainbow",
    "Słysze animacje",
    "Vivzierock",
    "Wagarsy",
    "tvteatr",
    "Tomsky",
    "His eyes are so empty, when he is playing",
    "Vimlag",
    "TierFauna",
    "ThePenicl",
    "This place is happy",
    "The theater Theorists",
    "The Spiffing Burger",
    "Stillingar",
    "Simon's dog",
    "Reid Cempaing"
]


sins_e_1 = [
    "it is Tie dye guy",
    "I`m intj, that mean i`m a psychopath",
    "I`m infj, Hitler was too",
    "I`m infp, that mean i care too much",
    "I don't belive this mbti test, but damm they are correct this time",
    "Plis not intj again",
    "And again; it is intj",
    "Why i am always next to infj",
    "Why i am depicted as alien 👽",
    "Intj - in other words: alien",
    "Intj - in other words: a murderer",
    "Infj - in other words: murder of I**p",
    "Intj - in other words: dark person",
    "Maybye it is Tie dye guy?",
    "I still think it is Tie dye guy!",
    "It is a message to a leder",
    "Its dark in here",
    "ID, indenticle delusion",
    '"Slizg" o`tool',
    "Just saying",
    "I have no words, but i have many worlds!",
    "Snape, Snape, Savery Snape",
    "Moriarty the Liberalty",
    "Graphfruit + heart medications = 💞",
    "Better run, Better run",
    "Game of Life",
    "Puzzle Scipt",
    "SCP-5000",
    "Glyph!",
    "Papa luige",
    "Pozwalam, ja Marek",
    "Motel Polska",
    "Smigają dziś rośnilnki co?",
    "proper british dishes part 35: pretzels on fucking fire",
    "https://cdn.discordapp.com/attachments/998700147955486740/1012019326452256841/unknown.png",
    baba_generator,baba_generator,baba_generator,baba_generator,baba_generator,baba_generator
]

sins_e+=sins_e_1
class DummName:
    def __init__(self,name="Memento Mori") -> None:
        self.name=name
    #name=
class Dummy:
    def __init__(self,name="Memento Mori") -> None:
        self.author=DummName(name)
    #author=

#bottom anchorn

sins_e+=[f"lącznie napisałem: {len(sins_e)+1} tekstów do tego"]
print(sins_e[-1])
update_name+=f"; lines:{len(sins_e)}"

sins_e+=[minecraft_splash]*int(len(sins_e)*0.09)
sins_e+=[random_title]*int(len(sins_e)*0.24) #making this more often

class Libra:
    "Sprawiedliwy generator"
    def __init__(self) -> None:
        self.deck = sins_e.copy()
        self.used=[]

    def gen(self):
        "Generate output"
        if len(self.deck)!=1:
            element=random.choice(self.deck)
            self.deck.remove(element)
            self.used.append(element)
        else:
            element=self.deck[0]
            self.deck=self.used
            self.used.clear()
        return element
        

names = [
    "Prist of Konshu",
    "Memenot Mori",
    "Destroyer of worlds",
    "Prist of Tanatos",
    "Halper of Stars",
    "5th Horsemen",
    "Prist of Cats",
    "mr Death",
    "mr Law",
    "Prist of Cthulhu",
    "Conquerer",
    "Prist of ♎︎",
    "Prist of ♋︎",
    "Divine Ruler",
    "101010(2)",
    "Crazy Doctor",
    'Dr Bright',
    'scp-963',
    "Allknowing",
    "Him, a Libra",
    "Disruptor",
    "Dreaming One",
    "Dead One",
    "Undead One",
    "HIM",
    "NOT",
    "Doppelganger",
    "Highest",
    "Lowest",
    "All IS NOT Baba",
    "KNOWING ONE",
    "Definition of knowledger",
    "KIEROWNIK DZIAŁA IT: DARET"

]
#print(random_title(Dummy(),indexB=-1))

#print(minecraft_splash(0))
print(f"Zarejestrowane nicki:{len(names)}")
print(baba_generator(Dummy()))