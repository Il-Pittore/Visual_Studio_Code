import discord
import os
from random import choice
from discord.ext import commands, tasks

# Read the Data files and store them in a variable
TOKEN = 'NzUwMDQ0ODcwNDI4NzIxMzMy.X00zuA.CfLf-x4U65MiM10R40HafNU5hXk' 

OWNERID = 363660713060859914

# Define "bot"
bot = commands.Bot(command_prefix = "-", case_insensitive=True)

# Define "Status"
status = ['Sono al circo', 'Sto guardando le scimmie', 'Che bel clown']

# Let us Know when the bot is ready and has started
@bot.event
async def on_ready():
    change_status.start()
    print("Bot is ready")

# A simple and small ERROR handler
@bot.event 
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.red())
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

# Load command to manage our "Cogs" or extensions
@bot.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Unload command to manage our "Cogs" or extensions
@bot.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Reload command to manage our "Cogs" or extensions
@bot.command(name = "reload")
async def reload_(ctx, extension):
    # Check if the user running the command is actually the owner of the bot 
    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!") 
    else:
        await ctx.send(f"You are not cool enough to use this command")

# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('D:/VS_Code/Python/DiscordMusic/Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception
        
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity = discord.Game(choice(status)))
        
# Run our bot
bot.run(TOKEN)