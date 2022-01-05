from discord.ext import commands
import discord, datetime

class moderation(commands.Cog):
	def __init__(self, bot):
      self.bot = bot # defining bot as global var in class

    # Clear command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=0):
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
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

    # Ban command
    @commands.command(name="ban", help="command to ban user")
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

    # Kick command
    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(ctx, user: discord.Member, *, reason="No hay razones"):
        await user.kick(reason=reason)
        kick = discord.Embed(
            title=f":boom: Se ha expulsado a {user.name}!",
            description=f"Por la razon de : {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)


def setup(bot): # a extension must have a setup function
	bot.add_cog(moderation(bot)) # adding a cog