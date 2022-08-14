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
import discord,os
import praw
import time,random
import requests as r
from bs4 import BeautifulSoup as bs
import key as token
import bib
version="42.0.004.2"

def f():
    return 0
reddit = praw.Reddit(client_id=token.reddit['id'], client_secret=token.reddit['secret'],user_agent="<console:DISCORDBOT:1.0>")

class Gungnir(discord.Client):
    DATA = {
        "USERS":{"404230163740491777":{"name":"Eragon",}},
    }
    async def on_ready(self):
        self.reddit_timeout=0
        print(f"We are setup! USER: {self.user}")

    async def on_message(self,msg):
        #*COMMENDS
        if msg.content.startswith("$"):
            try:
            
                #URBAN DICTIONARY COMAND
                if msg.content.startswith("$dict"):
                    content=msg.content.split(" ")
                    word=content[1]
                    embed =self.get_urban(word,False)
                    await msg.channel.send(embed=embed)
                elif msg.content.startswith("$dictR"):
                    content=msg.content.split(" ")
                    word=content[1]
                    embed =self.get_urban(word,True)
                    await msg.channel.send(embed=embed)
                elif msg.content.startswith("$rcat"):
                    await msg.channel.send(self.make_cat_request())
                elif msg.content.startswith("$quin_"):
                    await msg.channel.send(file=discord.File("app.py"))
                elif msg.content.startswith("$round"):
                    data=msg.content.split(" ")
                    if len(data)==2:
                        try:
                            float(data[1])
                            if data[1]=="42":
                                await msg.channel.send("1.618033988749894")
                            else:
                                await msg.channel.send("42")
                        except:
                            data = [i for i in data[1]]
                            last = data[-1]
                            data.pop(-1)
                            data = [last] + data
                            await msg.channel.send("".join(data))
                    
                elif msg.content.startswith("$ping"):
                    await msg.channel.send("pong!")
                elif msg.content.startswith("$sin"):
                    data= msg.content.split(" ")
                    if len(data)==1:
                        c = random.choice(bib.sins_e)
                        if type(c)==type(f):
                            c=c(msg)
                        if "%s" in c:
                            c= c%msg.author.name
                        await  msg.channel.send(c)
                    elif len(data)==2:
                        if data[1]=="42":
                            await msg.channel.send("-0.9165215479156338")
                        else:
                            await msg.channel.send("~")
                elif msg.content.startswith("$title"):
                    ID=-random.randint(1,2)
                    data = bib.random_title(msg)
                    await msg.author.edit(nick=data)
                    await msg.channel.send(f"Welcom our new companian:{msg.author.mention}")
                elif msg.content.startswith("$prist"):
                    ID=-random.randint(1,2)
                    prist_name=bib.random_title(msg,starter=0,indexB=ID)
                    await msg.author.edit(nick=prist_name)
                    await msg.channel.send(f"Welcom aboard Your highnest {msg.author.mention}")
                elif msg.content.startswith("$rename"):
                    data=msg.content.split(" ")
                    if len(data)==2:
                        name=data[-1]
                        await msg.author.edit(nick=name)
                        await msg.channel.send(f"Your new identity is: {msg.author.mention}")
                    else:
                        await msg.channel.send("418 - 🫖")
                elif msg.content.startswith("$mul"):
                    data = msg.content.split(" ")
                    if len(data)!=3:
                        await msg.channel.send("you need to specify 2 arguments")
                    else:
                        await msg.channel.send("do you meen: 6*7 = 42?")
                elif msg.content.startswith("$version"):
                    await msg.channel.send("version:"+version)
                    await msg.channel.send("essteregglib:"+bib.version)
            except Exception as e:
                await msg.channel.send(f"{e}")
        #! SPECIAL EMBEDS!
        elif msg.content.startswith("https://www.reddit.com/r/"):
            cooldown=time.time() - self.reddit_timeout
            if cooldown > 10:
                post=reddit.submission(url=msg.content)
                embed=self.embed_reddit_post(post,msg)
                self.reddit_timeout=time.time()
                await msg.channel.send(embed=embed)
                await msg.delete()
            else:
                await msg.channel.send(f"reddit has cool down: {cooldown}s")
        
        elif (msg.content.startswith("https://www.instagram.com/p/")) & (msg.author.bot == False):
          await msg.channel.send(msg.content+"/media/?size=l")
        

        #! reditor channel
        elif msg.channel.name.startswith("reditor"):
            if msg.content.startswith("$"):
                cooldown=time.time() - self.reddit_timeout
                if cooldown > 10:
                    subreddit=reddit.subreddit(msg.content[1:])
                    post=subreddit.random()
                    embed=self.embed_reddit_post(post,msg)
                    self.reddit_timeout=time.time()
                    await msg.channel.send(embed=embed)
                else:
                    await msg.channel.send(f"reddit has cool down: {cooldown}s")
            if msg.content.startswith("!CLEAR"):
                for i in await msg.channel.history().flatten():
                    await i.delete()
                
                await msg.channel.send("Mors ad hunc rivum venit")
    
    def get_urban(self,word,rand=False):
        url="https://www.urbandictionary.com/define.php?term="+word.lower()
        website = r.get(url)
        if website.ok:
            webpage = bs(website.text,'html')
            definitions = webpage.select(".p-5")
            if rand == False:
                definiton = definitions[0]
            else:
                definiton = random.choice(definitions)
            
            text_me = definiton.select_one(".meaning").text
            text_ex = definiton.select_one(".example")
            text_co = definiton.select_one(".contributor").select_one("a")
            text_exc=""
            for i in text_ex.contents:
                if isinstance(i,str):
                    text_exc+=i
                elif i.name=="br":
                    text_exc+='\n'
                else:
                    text_exc+=i.text
            embed=discord.Embed(
                url=url,
                title=word,
                color=discord.Colour.from_rgb(0x1b,0x29,0x36),
            )
            embed.set_author(name=text_co.text,url="https://www.urbandictionary.com/"+(text_co.attrs)['href'])
            embed.add_field(name="Definition",value=text_me,inline=False)
            embed.add_field(name="Example",value=text_exc,inline=False)
            return embed
            


    def embed_reddit_post(self,post,msg):
        #FF5212
        embed=discord.Embed(
            title=post.title,
            url=("https://www.reddit.com" + post.permalink),
            color=discord.Colour.from_rgb(0xff,0x52,0x12),
        )
        embed.set_author(name=msg.author.name,icon_url=msg.author.avatar_url)
        embed=embed.set_thumbnail(url=post.subreddit.icon_img)

        if hasattr(post,"post_hint"):
            hint = post.post_hint
            if hint == "image":embed=embed.set_image(url=post.url)
            if hint == "hosted:video":embed.add_field(name="Video",value=post.url,inline=False)
            if hint == "rich:video":embed.add_field(name="Video",value=post.url,inline=False)
        return embed

    def make_cat_request(self,order='r'):
        base_url = "https://api.thecatapi.com/v1/images/search"
        respons=r.get(base_url).json()

        return respons[0]['url']

client = Gungnir()

client.run(token.token)