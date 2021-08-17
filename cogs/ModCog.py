import discord
import re
from discord.enums import ActivityType, Status
from discord.ext import commands

class Mods(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Purge cog is now live!')

    @commands.group(invoke_without_command=True)
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx,amount:int=10):
        if amount >98:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(f"Deleted {len(deleted)-1} message(s)")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def links(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False
            chunks = " ".join(m.content.lower().split("\n"))
            chunks = chunks.split(" ")
            for chunk in chunks:
                if (True if re.search(r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))", chunk) else False): # stupid url regular expression ._.
                    counter += 1
                    return True
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which had links")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which started with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which ended with the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which contained the given keyword")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which were sent by the mentioned user")

    @purge.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send("Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"Deleted {len(deleted)}/{amount} message(s) which contained invites")

    @commands.command(aliases=["presence"], hidden=True)
    @commands.is_owner()
    async def activity(
            self, ctx, activity_type: str.lower, status_type: str.lower, *, message: str
    ):
        if activity_type == "clear":
            await self.set_presence()
            embed = discord.Embed(
                title="Activity Removed", color=ctx.message.author.color
            )
            return await ctx.send(embed=embed)

        try:
            activity_type = ActivityType[activity_type]
        except KeyError:
            return await ctx.send(
                f"{ctx.message.author.mention}, mention a proper activity object."
            )

        try:
            status_type = Status[status_type]
        except KeyError:
            return await ctx.send(
                f"{ctx.message.author.mention}, mention a proper status object."
            )

        activity, _ = await self.set_presence(
            activity_type=activity_type, activity_message=message, status=status_type
        )
        msg = f"Activity set to: {activity.type.name.capitalize()} "
        if activity.type == ActivityType.listening:
            msg += f"to {activity.name}."
        elif activity.type == ActivityType.competing:
            msg += f"in {activity.name}."
        else:
            msg += f"{activity.name}."

        embed = discord.Embed(
            title="Activity Changed", description=msg, color=ctx.message.author.color
        )
        return await ctx.send(embed=embed)

    # helper function for activity command

    async def set_presence(
            self, *, status=None, activity_type=None, activity_message=None
    ):
        if status == "idle":
            status = discord.Status.idle
        elif status == "online":
            status = discord.Status.online
        elif status == "offline":
            status = discord.Status.invisible
        elif status == "dnd":
            status = discord.Status.do_not_disturb

        if activity_type is None:
            activity_type = discord.Game
        url = None
        if activity_type is not None and not activity_message:
            activity_message = "Erin-bot"

        if activity_type == ActivityType.listening:
            if activity_message.lower().startswith("to "):
                activity_message = activity_message[3:].strip()
        elif activity_type == ActivityType.competing:
            if activity_message.lower().startswith("in "):
                activity_message = activity_message[3:].strip()
        elif activity_type == ActivityType.streaming:
            url = "https://www.twitch.tv/pokimane"  # cuz i'm a simp
            pass

        if activity_type is not None:
            activity = discord.Activity(
                type=activity_type, name=activity_message, url=url
            )
        else:
            activity = None
        await self.bot.change_presence(activity=activity, status=status)
        return activity, status

def setup(bot):
    bot.add_cog(Mods(bot))
