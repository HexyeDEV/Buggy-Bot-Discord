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

        # Load cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')



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
