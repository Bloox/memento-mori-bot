import requests as r
import random,io
import discord
from bs4 import BeautifulSoup as bs
version=2.0
name="first commit!"

def get_urban(word,rand=False):
    url="https://www.urbandictionary.com/define.php?term="+word.lower()
    website = r.get(url)
    if website.ok:
        webpage = bs(website.text,features="html.parser")
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


radek_PRELOAD={

}
def get_radek(num=None):
        #being 
        if num==None:
            if "R.PAGES_C" not in radek_PRELOAD:
                main=r.get('http://radzieccyuczeni.pl/category/radzieccy-uczeni/')
                eff=bs(main.text,features="html.parser")
                n=int(eff.select_one(".pages").text.split("z ")[1][:-2])
                radek_PRELOAD['R.PAGES_C']=n
                pages=n
            else:
                pages=radek_PRELOAD['R.PAGES_C']
            num=random.randint(1,pages)
        if 'R.articles' not in radek_PRELOAD:
            radek_PRELOAD['R.articles']={}
        if num not in radek_PRELOAD['R.articles']:
            data = r.get(f"http://radzieccyuczeni.pl/category/radzieccy-uczeni/page/{num}")
            list=bs(data.text,features="html.parser")
            radek_PRELOAD['R.articles'][num]=[i['href'] for i in list.select(".post > .postmetadata > div > a")]
        
        #making embed
        
        art=random.choice(radek_PRELOAD['R.articles'][num])
        docs=r.get(art)
        docs=bs(docs.text,features="html.parser")
        
        embed=discord.Embed(
                url=art,
                title=docs.select_one(".post>h2").text,
                color=discord.Colour.from_rgb(0xb9,0x2e,0x2e),
            )
        
        embed.add_field(name="Story",value=docs.select_one(".post > .entry").text,inline=False)
        return embed


def Sachara():
    web=r.get("http://piszsuchary.pl/losuj")
    
    page=bs(web.text,features="html.parser")
    img=page.select_one(".cytat>.kot_na_suchara > a > img")['src']
    
    use=img.split("_by_")[1].split('.')
    
    
    autor=use[0]
    format=use[1]
    this=nextcord.File(io.BytesIO(r.get(img).content),f"suchar.{format}")

    return [this,autor]

def make_cat_request(self,order='r'):
    base_url = "https://api.thecatapi.com/v1/images/search"
    respons=r.get(base_url).json()

    return respons[0]['url']

#?disnay
def card_analize(card):
    data={"subchild":"https://dsny.pl"+card['href']}
    
    full=r.get(data['subchild'])
    full=bs(full.text,features="html.parser")

    data['rating']=card.select_one("button > div.MuiCardHeader-root.css-1yg7hz4 > div.MuiCardHeader-avatar.css-1p83tvv > div").text
    data['cat'] = card.select_one("button > div.MuiCardHeader-root.css-1yg7hz4 > div.MuiCardHeader-content.css-11qjisw > span.MuiTypography-root.MuiTypography-body2.MuiCardHeader-title.css-no131b").text
    data['metadata']=card.select_one("div.MuiCardHeader-root.css-1yg7hz4 > div.MuiCardHeader-content.css-11qjisw > span.MuiTypography-root.MuiTypography-body2.MuiCardHeader-subheader.css-1m15n0u").text.split(',')
    data['formatt']=data['metadata'][0]
    meta=data['metadata'][1][1:]
    if "season" in meta:
        data['type']="Series"
        data['seasons']=meta.split(' ')[0]
        data['episodes']=full.select_one("#__next > div > div.MuiBox-root.css-l2vy7a > div > div.MuiBox-root.css-1hmjhwl > aside > div.MuiBox-root.css-4mo7ls > div:nth-child(2) > div > div > div:nth-child(8)").text
    else:
        czas=meta.split(' ')
        #print(czas)
        h=int(czas[0][:-1])
        m=int(czas[1][:-3])
        s=int(czas[2][:-1])
        total=(h*60)+(m)+(s/60)
        if total<30:
            data['type']="short"
        else:
            data['type']="movie"    
        data['span']={"total":total,"h":h,"min":m,"s":s}
    data['img']=card.select_one("button > div.MuiBox-root.css-79elbk > div.MuiBox-root.css-i94kc1 > img")['src']
    data['title']=card.select_one("button > div.MuiCardContent-root.css-1qw96cp > h2 > strong").text
    data['desc']=card.select_one("button > div.MuiCardContent-root.css-1qw96cp > p").text
    data['watch-url']=full.select_one("#__next > div > div.MuiBox-root.css-l2vy7a > div > div.MuiBox-root.css-1hmjhwl > aside > div.MuiBox-root.css-4mo7ls > a")['href']
    data['genres']=[i.text for i in full.select("#__next > div > div.MuiBox-root.css-l2vy7a > div > div.MuiBox-root.css-1hmjhwl > main > div.MuiBox-root.css-6zeo2z > div:nth-child(1) > div:nth-child(2) > div > a")]
    data['fran']=[i.text for i in full.select("#__next > div > div.MuiBox-root.css-l2vy7a > div > div.MuiBox-root.css-1hmjhwl > main > div.MuiBox-root.css-6zeo2z > div:nth-child(2) > div:nth-child(2) > div > a")]
    return data

def disney_sercher(term):
    webpage=r.get(f"https://dsny.pl/library/en/pl?search={term}")
    site=bs(webpage.text,features="html.parser")
    card=site.select_one("#__next > div > div.MuiContainer-root.MuiContainer-maxWidthLg.MuiContainer-fixed.css-1r3upk9 > div.MuiBox-root.css-1tw4wyn > div.MuiBox-root.css-3rf0uh > a")
    data=card_analize(card)
    embed=discord.Embed(
            url=data['subchild'],
            title=data['title'],
            color=discord.Colour.from_rgb(0x1b,0x1d,0x3a),#1B1D3
    )
    if data['rating']!='n/a':
        rat=int(float(data['rating']))
        embed.add_field(name="Rating:",value=f"{'★'*rat}{'☆'*(10-rat)}",inline=True)
    else:
        embed.add_field(name="Rating:",value=f"n/a",inline=True)
    embed.add_field(name="Cat:",value=data['cat'],inline=True)
    embed.add_field(name="​",value="​",inline=False)
    if data['type'].startswith("S"):
        embed.add_field(name="Content:",value=f"{data['seasons']}season ({data['episodes']} episodes)",inline=True)
    else:
        embed.add_field(name="Lenghth:",value=f"{int(data['span']['total'])}m",inline=True)
    embed.add_field(name="Type:",value=data['type'],inline=True)
    embed.add_field(name="Description:",value=data['desc'],inline=False)
    embed.add_field(name="Genres:",value=", ".join(data['genres']),inline=True)
    embed.add_field(name="Franshise:",value=", ".join(data['fran']),inline=True)
    embed.set_image(url=data['img'])
    embed.set_author(name="WATCH ON Disney+",url=data['watch-url'],icon_url="https://pageflows.imgix.net/media/logos/disneyPlusLogo.jpg?auto=compress&ixlib=python-1.1.2&s=62e82d60ee2ef660457b71f39fd0af20")
    return embed