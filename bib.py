from operator import index
import random

version="42. 3.5/0" #for every new version increase number befor /

def random_title(msg,starter=1,ender=1,indexA=None,indexB=None):
    gods = [
        "Artemis","Athena","Hephaestus","Hades",'Tanatos',"Morpheus",'Tartarus',
        "Flying Spaghetti Monster","Cthulhu","True","Lie","Azothot","Spthot","Nyks","Chaos",
        "Dreamer","Eldrich ones","the Uninvited","Eros","Law","Justice","One who watch us",
        "One from beyond words",'One above our world',"Who think","Odin","Thor","Loki","Monokuma",
        "From upsidedown","Karl with the Hat","Tinkerer of existenc","Apollo","the Sun","Higher being",
        "of Greates evil","Death, last horsmen of the apocalypse","War, second horsmen of the apocalypse",
        "Conquest first horsmen of the apocalypse","Famine third horsmen of the apocalypse",
        "Youtube algoritmes"
    ]
    starters = [
        "Bloody ","Deadly ","Precise ","Unknow ","Forgoten ",'Dead ',
        "Chosen ","Psychopatchic ","English ",'Slavic ',"Romanic ",
        "Accuret ","Powered ",'Immortal ',"Actual "
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
        "Great Dreamer",f"Higher Prist of {random.choice(gods)}",f"Prist of {random.choice(gods)}"
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
    if indexA==None:
        indexA=random.randrange(0,len(starters))
    if indexB==None:
        indexB=random.randrange(0,len(enders))
    return msg.author.name +" "+ starters[indexA]*starter + enders[indexB]*ender + ' ' + random.choice(num)*int((random.randrange(0,6)<1))
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
    "Wszyscy się kłucą co powino się dać pierwsze, mleko czy platki, a wszyscy powinniśmy wiedzieć że pierwsza powinna być miska",
    "Every day, I wake up,then i start to brake up\nLonely is man without love",
    "Co było pierwsze: jajko czy kura? pierwsze był 42 pierogi.",
    "Let me introduce you to my cult",
    "This server starter pack: Beaing nerd, Dark Humor, beaing brain connected...",
    "If i was blind i will be happy that i'm not deef",
    "if i was deef, than there is no happynes in word :(",
    "Don't regret any decision, because you can't change the past",
    "10⁹ is ...",
    "Własnym oczom już nie wieże, na przystanku siedzi pies, ma na sobie gps",
    "𝅘𝅥𝆕Kids die for free𝅘𝅥𝆕",
    "studnia∈💼",
    "Widzimy się w piątek o 5 chyba że zapomne lub nie będzie mi się chciało",
    "Avater(i nie chodzi o niebieskie ludzie)",
    "Clause-04",
    "5 stops killing people",
    "karl that kills people",
    "Blood of ⚡",
    "My font recomendation:Fire Code, Noto Emoji(black&white)",
    "Biedronkowy merch!",
    "Eden",
    "Cats movie was somthing",
    "Monty Python and the Holy Grail",
    "Żywot Braiana",
    "Latający Cyrk",
    "Ku czci Neil Gaiman",
    "Big fat, and very boring, god, with small pp, yes you guessed right i meam: Zeus",
    "https://www.youtube.com/channel/UClPPmQw2t1e7KlM5wxTXluw",
    "Jake Lockley","Steaven Grant",
    "MLP *was* the best!",
    "Khonshu",
    "Brazzos",
    "https://tenor.com/view/your-mother-great-argument-however-megamind-your-mom-yo-mama-gif-22994712",
    "Flee",
    'Audio > Graphic',
    "2d > 3d",
    "4d > 3d & 4d > 2d",
    "Yanderdev",
    "This is a school announcement; it is now 10pm, at such it is officialy nighttime!",
    "Good mornig everone, get ready to greet another beautiful day",
    "Za wszelkie orty serdecznie pszepraszam",
    "Przed u życie skonsultujsię z Orgologiem lub Lamacałtą",
    "Power of Fishing pool!",
    "Let's game it out",
    f"This is version:{version} of text lib",
    "Tajemnicza Irma Vep - Teatr wybrzerze",
    "Awantura w Chioggi - Teatr wybrzerze",
    "Inteligenci - Teatr wybrzerze",
    "Kim jest pan Schmitt? - Teatr wybrzerze",
    "Sztuka - Teatr wybrzerze",
    "Zieloone pesto > Czerwone pesto",
    "Zielone zielone robie sobie zielone",
    "We love trees",
    "We love forest",
    "I have feling that somone here is scared to death by bugs",
    "Covid-19 rejoing the server",
    "Ej, co jest doktorku?",
    "Chyba widziałem kotecka, Tak tak dobrze mi się zdawało widziałem kotecka",
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
    "I like my code like i like my life without bugs.",
    "onomatopeje",
    "Apokalpisa się zblirza (prznajmniej mam taką nadzieje)",
    "Co wydzi na cmętarzu optymista? Same plusy\n A co wydzi na cmentarzu pesymista? Też same plusy",
    "↑↑↓↓←→←→AB,START",
    "My father hate bugs",
    "Mógłbym jeśc naleśniki całe życie",
    "I am operator of my pocke calculator",
    "You will be Okey",
    "Materials can't go to Heven, they just endup in recycle bin",
    "Never say never exept where you say that exact line",
    "Beep Beep I'm a Sheep",
    "He is gay or european is hard to guarantee!",
    "To be continued!",
    "Brimstone!",
    "C,C++,C# or CARBON?",
    "JS,typescript,node.js",
    "Python,Ruby,Go",
    "Java,Kotlin",
    "```py\nmsg=lambda: random.choice(sins_e)```",
    "```py\nc='c=%r;print(c%%c)';print(c%c)```",
    'exec(s:=\'print("exec(s:=%r)"%s)\')'
    'Litarature Club!',
    "Anolog horror!",
    "THIS IS YELLING FOR MOJANG",
    "dlaczego √2 zabiłó 3? bo jest nie obliczalne!",
    "DON`T always USE CAPSLOCK",
    "Sok z kaktusa, bardzo pyszny i odżwyczy!",
    "Smartgasm: Zaraz pokaże jak zmienić kostke `Co` w super radioaktywnty `⁶⁰Co`, opowiem też jak zrobić z niego bombe kobaltową...",
    "" 

]
class DummName:
    name="none"
class Dummy:
    author=DummName

#bottom anchorn
sins_e+=[random_title]*25



sins_e+=[f"lącznie napisałem: {len(sins_e)+1} tekstów do tego"]
print(sins_e[-1])
print(random_title(Dummy(),indexB=-1))