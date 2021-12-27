from discord.ext import commands
import discord, datetime

class help(commands.Cog):
	def __init__(self, bot):
      self.bot = bot # defining bot as global var in class
      
    # Help command
	@commands.command()
    async def help(self, ctx):
		embed = discord.Embed(
            title="Comandos de Buggy",
            description="",
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.blue())
        embed.add_filed(name="► Menu de ayuda", value="Tenemos 2 categorias y mas de 100 comandos creados.\n\n Lista de comandos: !help <categoria>\n Comandos en detalle: !help <comando>ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ")
        embed.add_field(name="► Categorias",
                    value='''

    `c!mod` = Comandos de moderador                
    `c!fun` = Comandos para reirse
    `c!romance` = Comandos de romance

    ''',
                    inline="False")
        embed.add_field(name="► Enlaces",value="[Pagina Web](http://google.com) | [Privacidad](http://youtube.com) | [Comandos]( http://wikipedia.com)",  inline="False")
        await ctx.send(embed=embed)

    # Help mod
	@commands.command()
    async def mod(self, message):
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

    # Help fu
    @commands.command()
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

    @commands.command()
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

def setup(bot): # a extension must have a setup function
	bot.add_cog(help(bot)) # adding a cog