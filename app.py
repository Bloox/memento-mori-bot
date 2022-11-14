# WARNIG, to run a bot you need file called `key.py` and with in:
"""
privat_key=discord-app-privat-key:str
token=dicord-bot-secret:str
reddit={
    "name":reddit-app-name:str
    "redirect_url":"https://localhost",
    "secret":reddit-app-secret:str
    "id":reddit-app-id:str
}
catapi = {
    "apiKey":cat-api-string:str #curentyl not using, not neccesery
}

"""
import os,asyncio,io,rightway,babel,sys,discord,reddit,scrap,train
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
import praw
import time,random
import requests as r

from bs4 import BeautifulSoup as bs
import key as token
import bib
version="42.0.010.0"
version_name="Migration time!"


def f():...

#PRIEST_ID=random.randint(1,2)


#main(needed)
class Gugnir(commands.Bot):
    @tasks.loop(seconds=10)
    async def change_myself(self,arg=[1]):
        #print(arg[0])
        if arg[0]==3:
            try: 
                eff=random.choice(bib.names)
                print(eff)
                [await server.me.edit(nick=eff) for server in self.guilds]
                self.defult=bib.Dummy(eff)
                arg[0]=-1
            except:
                arg[0]=2
        try:
            decsr = self.bib_help(msg=self.defult,no_links=True,gen=self.gez)
            #discord.utils.get(self.get_all_members, id=self.id)
            #print(decsr)
            await self.change_presence(activity=discord.Game(name=decsr))
            #await self.user.edit()
        except Exception as e:
            print(e)
        arg[0]+=1
        

            #input(decsr)
    async def on_ready(self):
        self.gez = bib.Libra()
        self.dummu="Memento Mori Bot"
        self.defult=bib.Dummy(self.dummu)
        self.reddit_timeout=time.time()
        print("ready")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
        self.change_myself.start()
    
    async def on_message(self, msg: discord.Message, /) -> None:

        if msg.content.startswith("https://www.reddit.com/r/"):
            cooldown=time.time() - self.reddit_timeout
            if cooldown > 10:
                post=reddit.get_post(msg.content)
                embed=reddit.embed_reddit_post(post,msg)
                self.reddit_timeout=time.time()
                await msg.channel.send(embed=embed)
                await msg.delete()
            else:
                await msg.channel.send(f"reddit has cool down: {cooldown}s")
        
        elif (msg.content.startswith("https://www.instagram.com/p/")) & (msg.author.bot == False):
          await msg.channel.send(msg.content+"/media/?size=l")
        return await super().on_message(msg)
    
    def bib_help(self,msg,no_links=False,gen=None):
        
        if hasattr(msg,"user")&(not hasattr(msg,"author")):
            name=msg.user.display_name
        else:
            name=msg.author.display_name
        if gen==None:
            gen=self.gez
        c = gen.gen()
        if type(c)==type(f):
            c=c(msg)
        if "%s" in c:
            c= c%name
        while c.startswith("https://") & no_links:
            c = gen.gen()
            if type(c)==type(f):
                c=c(msg)
            if "%s" in c:
                c= c%name
        return (c)
bot= Gugnir("$",intents=discord.Intents.all())

#custom commends
@bot.tree.command(name="ping",description="how table has turned!")
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message("Pong! 🏓")

@bot.tree.command(name="dict",description="Look up words in Urban dictionary!")
@app_commands.describe(word = "word to search!")
async def urban(ctx: discord.Interaction,word:str):
    await ctx.response.send_message(embed=scrap.get_urban(word))

@bot.tree.command(name="quin",description="output a file from source")
@app_commands.describe(file_name="Optional file to specify")
@app_commands.choices(file_name=[
    app_commands.Choice(name="app.py",value="app.py"),
    app_commands.Choice(name="babel.py",value="babel.py"),
    app_commands.Choice(name="bib.py",value="bib.py"),
    app_commands.Choice(name="reddit.py",value="reddit.py"),
    app_commands.Choice(name="rightway.py",value="rightway.py"),
    app_commands.Choice(name="scrap.py",value="scrap.py"),
    app_commands.Choice(name="train.py",value="train.py")
])
async def quin_(ctx: discord.Interaction, file_name:str ="app.py"):
    await ctx.response.send_message(file=discord.File(file_name))

@bot.tree.command(name="round",description="Zawrotówka!")
@app_commands.describe(value="float number!(or not)")
async def roundabout(ctx: discord.Interaction, value:str):
    try:
        value=float(value)
        if value==42.0:
            await ctx.response.send_message("1.618033988749894")
        else:
            await ctx.response.send_message("42")
    except:
        data = [i for i in value]
        last = data[-1]
        data.pop(-1)
        data = [last] + data
        await ctx.response.send_message("".join(data))
@bot.tree.command(name="sin",description="it's fine, because the sin of pi is always zero.")
@app_commands.describe(value="floating point number")
async def sinus(ctx: discord.Interaction,value:float = 4.24224067):
    if value!=4.24224067:
        try:
            value=float(value)
            if value==42:
                await ctx.response.send_message("-0.9165215479156338")
            if value==3.14:
                await ctx.response.send_message("you are no longer sinful!")
        except:
            await ctx.response.send_message("~")
    else:
        await ctx.response.send_message(bot.bib_help(ctx))
@bot.tree.command(name="mul",description="1/0")
@app_commands.describe(a="floating point number",b="descending point number")
async def mul(ctx: discord.Interaction,a:float,b:float):
    if ((a==6)&(b==7))|((a==7)&(b==6)):
        ctx.response.send_message("42!")
    else:
        ctx.response.send_message("do you meant: 6*7 = 42?")

@bot.tree.command(name="baba",description="BOT IS LOVE!")
async def baba_is_you(ctx: discord.Interaction):
    await ctx.response.send_message(bib.baba_generator(ctx))

@bot.tree.command(name="radek",description="\"Radzieccy Uczen\" for live")
async def radek(ctx: discord.Interaction):
    await ctx.response.send_message(scrap.get_radek())

@bot.tree.command(name="goto",description="Piechotą Kurde Prędzej")
@app_commands.describe(
    _from="Z jakiej stacji odjeżdzasz?(nazwa stacji wyrazy odziell \"-\")",
    _to=  "do jakiej stacji jedziesz? (nazwa stacji wyrazy odziell \"-\")",
    _time="o której wyjeżdzasz        (HH:MM)",)
async def pkp_icc(ctx: discord.Interaction, _from:str, _to: str,_time: str="4224"):
    if _time!="4224":
        await ctx.response.send_message(train.main([0,_from,_to,_time]))
    else:
        await ctx.response.send_message(train.main([0,_from,_to]))

@bot.tree.command(name="title",description="CUSTOM NAME GENERATOR 2014!")
async def title(ctx: discord.Interaction):
    data = bib.random_title(ctx)
    await ctx.response.send_message(f"Welcom our new companian:{data}")

@bot.tree.command(name="priest",description="CUSTOM NAME GENERATOR 2014!")
async def title(ctx: discord.Interaction):
    PRIEST_ID=random.randint(1,2)
    data = bib.random_title(ctx,starter=0,indexB=PRIEST_ID)
    await ctx.channel.send(f"Welcom aboard Your highnest {data}")

@bot.tree.command(name="version",description="checke version!")
async def version(ctx:discord.Interaction):
    text=f"""```txt
    version:     {version:15} - {version_name}
    esteregglib: {bib.version:15} - {bib.update_name}
    jednostki:   {rightway.version:15} - {rightway.name}
    scrap:       {scrap.version:15} - {scrap.name}
    babel:       {babel.version:15} - {babel.name}
    train:       {train.version:15} - {train.version}
    ```"""
    await ctx.response.send_message(text)

@bot.tree.command(name="suchar",description="co robi papierek na szczycie góry? Celeści!")
async def suchar(ctx: discord.Interaction):
    data=scrap.Sachara()
    await ctx.response.send_message(f"Suchar dostarczony przez:{data[1]}",file=data[0])
@bot.tree.command(name="babel")
@app_commands.describe(direction="To/From",codec="[Translator]",text="[text]")
@app_commands.choices(direction=[
    app_commands.Choice(name="To",value=0),
    app_commands.Choice(name="From",value=1),
    ],
    codec=[app_commands.Choice(name=i,value=i) for i in babel.langs])
async def Bubel(ctx: discord.Interaction,direction:int,codec:str,text:str):
    #print(ctx.message)
    if direction==0:
        #print(True)
        await ctx.response.send_message(content=babel.translate_to(text,codec))
    if direction==1:
        await ctx.response.send_message(content=babel.translate_from(text,codec))
@bot.tree.command(name="m",description="jednoski mrał!")
@app_commands.describe(system="Jakiego systemu jednostek użyć?",to_convert="[float]",jednostka="z jakiej jednoski?")
@app_commands.choices(system=[
    app_commands.Choice(name=i, value=i ) for i in rightway.systemy
])
async def mral(ctx: discord.Interaction,system:str,to_convert:float,jednostka:str):
    print(rightway.systemy[system])
    inter=rightway.systemy[system]
    if jednostka in rightway.jednostki['czas']:
        data=rightway.base_convert(to_convert,rightway.jednostki['czas'][jednostka]) 
        await ctx.response.send_message(inter.czas(data))
    if jednostka in rightway.jednostki['dlug']:
        data=rightway.base_convert(to_convert,rightway.jednostki['dlug'][jednostka]) 
        await ctx.response.send_message(inter.dlug(data))
    if jednostka in rightway.jednostki['waga']:
        data=rightway.base_convert(to_convert,rightway.jednostki['waga'][jednostka]) 
        await ctx.response.send_message(inter.waga(data))

@bot.tree.command(name="displus",description="Search thing on D+")
@app_commands.describe(title="Title to search for")
async def d_plus(ctx: discord.Interaction,title:str):
    await ctx.response.send_message(embed=scrap.disney_sercher(title))


"""
@bot.tree.command(name="test",description="yes/no")
@app_commands.describe(option="Yes/No")
@app_commands.choices(option=[
    app_commands.Choice(name="Yes",value=1),
    app_commands.Choice(name="No",value=0)
])
async def test(ctx: discord.Interaction,option:int):
    print(option)
"""

bot.run(token=token.token)

app_commands.choices(["yes","no"])