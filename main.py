import discord
from discord import activity
from discord import embeds
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
import datetime
import asyncio
from discord import Permissions, embeds
from colorama import Fore, Style
import random
from requests import get

bot = commands.Bot(command_prefix='c!', help_command=None) # Prefix

# Status presence and bot on

@bot.event
async def on_ready():
    print("Bot is ready")
    while True:  # BUCLE
        await bot.change_presence(activity=discord.Game(name="🆘 c!help"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(
            name="⚙ Creator by Paw#0743"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(
            name="🛠 Buggy created to help users"))
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game(name="😴 sleeping..."))
        await asyncio.sleep(15)

# Help command

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Comandos de Buggy",
        description="",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.blue())
    embed.add_field(name="► Menu de ayuda", value="Tenemos 2 categorias y mas de 100 comandos creados.\n\n Lista de comandos: !help <categoria>\n Comandos en detalle: !help <comando>ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ")
    embed.add_field(name="► Categorias",
                    value='''

    `c!mod` = Comandos de moderador                
    `c!fun` = Comandos para reirse
    `c!romance` = Comandos de romance

    ''',
                    inline="False")
    embed.add_field(name="► Enlaces",value="[Pagina Web](http://google.com) | [Privacidad](http://youtube.com) | [Comandos]( http://wikipedia.com)",  inline="False")

    await ctx.send(embed=embed)

# Help Mod

@bot.command()
async def mod(message):
    embed = discord.Embed(
        title="Comandos de Buggy",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Moderador", value="Ayuda sobre los comandos de moderadorﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Comandos**",value='''
    kick
    ban
    mute
    ''',  inline="True")
    embed.add_field(name="**Comandos**",value='''
    clear
    nuke
    none
    ''', inline="True")
    embed.add_field(name="**Comandos**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)

# Help Fun

@bot.command()
async def fun(message):
    embed = discord.Embed(
        title="Comandos de Buggy",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Diversion", value="Ayuda sobre los comandos de diversionﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Comandos**",value='''
    banana
    ship
    lucky
    ''',  inline="True")
    embed.add_field(name="**Comandos**",value='''
    roll
    8ball
    none
    ''', inline="True")
    embed.add_field(name="**Comandos**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)

# Help Romance

@bot.command()
async def romance(message):
    embed = discord.Embed(
        title="Comandos de Buggy",
        description="",
        color=discord.Color.blue())
    embed.add_field(name="Romance", value="Ayuda sobre los comandos de Romanceﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ", inline="False")
    embed.add_field(name="**Comandos**",value='''
    hug
    kiss
    none
    ''',  inline="True")
    embed.add_field(name="**Comandos**",value='''
    none
    none
    none
    ''', inline="True")
    embed.add_field(name="**Comandos**",value='''
    none
    none
    none
    ''')
    await message.channel.send(embed=embed)

# clear command

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)

# nuke command

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, amount=12000):
    await ctx.channel.purge(limit=amount + 12000)
    embed = discord.Embed(
        title="Buggy Bot",
        description="Buggy, exploto una bomba nuclear por aciddente",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.purple())
    embed.add_field(name="Se han eliminado toda la conversacion del canal",
                    value="Clown dice que lo siente :c",
                    inline="False")
    embed.set_thumbnail(
        url=
        "https://t3.ftcdn.net/jpg/03/33/09/88/360_F_333098851_oaiN8o7glILcg7nsT1vhSPewI1wSjzyN.jpg"
    )
    embed.set_image(
        url=
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/41606d9e-1486-4bb8-a9b4-eba3eccb1b35/ddmmjz8-10a4c85f-41d7-4d16-b011-e329762165a7.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzQxNjA2ZDllLTE0ODYtNGJiOC1hOWI0LWViYTNlY2NiMWIzNVwvZGRtbWp6OC0xMGE0Yzg1Zi00MWQ3LTRkMTYtYjAxMS1lMzI5NzYyMTY1YTcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Gj7uC00OS8Ow8mAvS0SHWz0ecu9E_EQilFjEqK-FKrk"
    )
    await ctx.send(embed=embed)

# ban command

@bot.command(name="ban", help="command to ban user")
@commands.has_permissions(ban_members=True)
async def _ban(ctx, member: discord.Member, *, reason=None):
    """ command to ban user. Check !help ban """
    try:
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.channel.send(
            f'{member.name} Ha sido baneado de este servidor por la '
            f'Razon: {reason}')
    except Exception:
        await ctx.channel.send(
            f"No tienes el permiso suficiente para banear"
        )

# kick command

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason="No hay razones"):
    await user.kick(reason=reason)
    kick = discord.Embed(
        title=f":boom: Se ha expulsado a {user.name}!",
        description=f"Por la razon de : {reason}\nBy: {ctx.author.mention}")
    await ctx.message.delete()
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)


words = [
    'esta triste', 'esta feliz', 'esta enojado', 'esta solitario',
    'tiene ansiedad', 'tiene miedo', 'esta interesado', 'esta enamorado',
    'esta nostalgico'
]

# command feels

@bot.command()
async def feels(ctx):
    randomsx = random.choice(words)
    await ctx.send(">>> Clown dice que " + ctx.author.mention + f" {randomsx}")


memesszx = [
    "https://tenor.com/view/peppa-pig-minecraft-meme-peppa-pig-minecraft-meme-gif-14960039",
    "https://tenor.com/view/spongebob-nickelodeon-handsome-squidward-funny-meme-gif-14625359",
    "https://tenor.com/view/bye-memes-dead-wow-incredible-gif-12520076",
    "https://tenor.com/view/meme-gif-13939251",
    "https://tenor.com/view/dance-baby-fun-varinha-gif-4766783",
    "https://tenor.com/view/baseball-mlb-slide-butt-ass-gif-9642083"
]

# command memes

@bot.command()
async def meme(ctx):
    randomsxa = random.choice(memesszx)
    await ctx.send(f" {randomsxa}")

# command kiss

@bot.command(name="kiss")
async def kiss(ctx, *, member: discord.Member):
  kissz = [
  "https://tenor.com/view/anime-kiss-love-mwah-gif-16687888",
  "https://tenor.com/view/anime-kiss-love-sweet-gif-5095865",
  "https://tenor.com/view/kiss-anime-love-couple-intimate-gif-17193768",
  "https://tenor.com/view/kiss-me-%D0%BB%D1%8E%D0%B1%D0%BB%D1%8E-anime-kiss-intimate-gif-17382422",
  "https://tenor.com/view/anime-kiss-crying-cute-couple-gif-13970544",
  "https://tenor.com/view/koi-to-uso-kiss-animes-anime-boy-girl-gif-18025936",
  "https://tenor.com/view/anww-hug-kiss-anime-cartoon-gif-4874618",
  "https://tenor.com/view/anime-cute-kiss-couple-romantic-gif-12192868",
  "https://tenor.com/view/toloveru-unexpected-surprise-kiss-gif-5372258",
  "https://tenor.com/view/kuzu-no-honkai-kissing-anime-affection-hanabi-yasuraoka-gif-11831573",
  "https://tenor.com/view/anime-zero-kiss-couple-lover-gif-12925177",
  "https://tenor.com/view/anime-kiss-gif-4829336",
  "https://tenor.com/view/kiss-anime-love-couple-gif-14240425",
  "https://tenor.com/view/anime-kissing-kiss-love-gif-10358839",
  "https://tenor.com/view/mikagura-school-suite-kyoma-kuzuryuu-kiss-kissing-shocked-gif-5391560",
  "https://tenor.com/view/kiss-anime-cute-couple-gif-19445519",
  "https://tenor.com/view/shirayuki-akagami-no-shirayukihime-akagami-anime-anime-love-gif-20545366",
  "https://tenor.com/view/love-couple-sad-cry-kiss-gif-18710804",
  "https://tenor.com/view/anime-sword-art-online-sao-gif-13862432",
  "https://tenor.com/view/kiss-passionate-passion-love-kisses-gif-12887280",
  "https://tenor.com/view/domekano-domestic-girlfriend-kiss-anime-shocked-gif-16799654",
  "https://tenor.com/view/anime-kiss-kissing-gif-3531829"
 ]
  besos = random.choice(kissz)
  await ctx.send(ctx.author.mention + " Le ha tirado un beso a " + member.mention)
  await ctx.send(f" {besos}")

# command hug

@bot.command(name="hug")
async def hug(ctx, *, member: discord.Member):

  abrazos = [
      "https://tenor.com/view/hug-anime-love-sweet-tight-hug-gif-7324587",
      "https://tenor.com/view/anime-hug-cuddle-love-care-gif-17265727",
      "https://tenor.com/view/abrazo-hug-anime-gif-10307432",
      "https://tenor.com/view/anime-hug-sweet-in-love-love-gif-17770800",
      "https://tenor.com/view/anime-cheeks-hugs-gif-14106856",
      "https://tenor.com/view/hug-anime-hug-cry-happy-anime-happy-gif-19679116",
      "https://tenor.com/view/hug-anime-sweet-couple-gif-12668480",
      "https://tenor.com/view/chuunibyou-anime-couple-anime-couple-cute-gif-13576064",
      "https://tenor.com/view/puuung-puung-love-you-hug-comfort-gif-13883173",
      "https://tenor.com/view/anime-hug-gif-15249774",
      "https://tenor.com/view/hug-anime-gif-19674705",
      "https://tenor.com/view/anime-hug-kawaii-hugs-gif-9862193",
      "https://tenor.com/view/anime-cuddles-hug-in-love-gif-16329758",
      "https://tenor.com/view/hug-love-sweet-anime-couple-gif-16300141",
      "https://tenor.com/view/anime-couple-anime-winter-anime-cold-anime-snow-anime-snuggle-gif-15764601",
      "https://tenor.com/view/girls-hugging-yuri-hug-anime-girls-502198-gif-19599352",
      "https://tenor.com/view/hug-love-anime-gif-14566838",
      "https://tenor.com/view/anime-anime-head-rub-anime-head-pat-anime-couple-anime-snuggle-gif-16085314"
    ]
  abrazosx = random.choice(abrazos)
  await ctx.send(ctx.author.mention + " Le ha dado un abrazo a " + member.mention)
  await ctx.send(f" {abrazosx}")

# Discord bot run

bot.run(TOKEN)
