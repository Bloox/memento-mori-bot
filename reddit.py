import praw,time
import discord
import key as token
reddit = praw.Reddit(client_id=token.reddit['id'], client_secret=token.reddit['secret'],user_agent="<console:DISCORDBOT:1.0>")

def get_post(url):
    return reddit.submission(url=url)
def embed_reddit_post(post,msg):
    #FF5212

    
    embed=discord.Embed(
        title=post.title,
        url=("https://www.reddit.com" + post.permalink),
        color=discord.Colour.from_rgb(0xff,0x52,0x12),
    )
    embed.set_author(name=msg.author.name,icon_url=msg.author.display_avatar)
    embed=embed.set_thumbnail(url=post.subreddit.icon_img)

    if hasattr(post,"post_hint"):
        hint = post.post_hint
        if hint == "image":embed=embed.set_image(url=post.url)
        if hint == "hosted:video":embed.add_field(name="Video",value=post.url,inline=False)
        if hint == "rich:video":embed.add_field(name="Video",value=post.url,inline=False)

    return embed