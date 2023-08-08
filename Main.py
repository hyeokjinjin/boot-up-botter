from typing import Optional
import discord
import time
from discord.ext import commands
from discord.ext.commands import MemberConverter
from apikey import *
import asyncio


intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("Bot has been booted up")
    print("----------------------")
    


@client.command()
async def shutdown(ctx):
    await ctx.send("Shutting Down")
    await client.close()


@client.command()
async def hello(ctx):
    await ctx.send("Hello. I'm booted up!")


@client.command()
async def everyone(ctx):
    for guild in client.guilds:
        for user in guild.members:
            if user != None:                
                await ctx.send(f'<@{user.id}>')


@client.command()
async def mention(ctx, *, user: discord.User=None):
    if user != None:        
        for i in range(10):
            await ctx.send(f'<@{user.id}>')
            time.sleep(1)
            await ctx.send("Boot up")
            time.sleep(1.25)
    else:
        await ctx.send('User not found. Try again.')


@client.command()
async def bootup(ctx, *, user: discord.User=None):
    if user != None:
        victim = client.get_user(user.id)
        for i in range(10):
            await victim.send("Boot up")
            await ctx.send(f'<@{user.id}>')
            time.sleep(1)
            await ctx.send("Boot up")
            time.sleep(1.25)
    else:
        await ctx.send('User not found. Try again.')
        

@client.command()
async def bootupPlan(ctx, *args):
    #try:
    print(f"Booting up {args[0]} in {args[1]} {args[2]}")
    if args[2] == "hours":
        seconds = (int(args[1]) * 3600)
    elif args[2] == "minutes":
        seconds = (int(args[1]) * 60)
    elif args[2] == "seconds":
        seconds = (int(args[1]))
        
    await ctx.send(f"Booting up {args[0]} in {args[1]} {args[2]}.")
    
    await asyncio.sleep(seconds) 
        
    converter = MemberConverter()
    user = await converter.convert(ctx, args[0])
        
    if user != None:
        for i in range(10):
            await ctx.send(f'<@{user.id}>')
            time.sleep(1)
            await ctx.send("Boot up")
            time.sleep(1.25)
    else:
        await ctx.send('User not found. Try again.')

    #except:
        #await ctx.send('No time specified. Try again with format "$bootupPlan {user} {time} {unit of seconds}."')

client.run(BOTTOKEN)