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
async def bootup(ctx, *args):
    for user in args:
        try:
            converter = MemberConverter()
            user = await converter.convert(ctx, user)
            try:
                victim = client.get_user(user.id)
                for i in range(5):
                    await victim.send(f'<@{user.id}> Boot up!')
                    await ctx.send(f'<@{user.id}> Boot up!')
                    await asyncio.sleep(.75) 
            except:
                for i in range(5):
                    await ctx.send(f'<@{user.id}> Boot up!')
                    await asyncio.sleep(.75) 
        except:
            print(f"Who is {user}???")
            await ctx.send('User not found. Try again.')


@client.command()
async def bootupLater(ctx, *args):
    if (args[-1] == "hours" or args[-1] == "minutes" or args[-1] == "seconds"):
        print(f"Booting them up in {args[-2]} {args[-1]}")
        if args[-1] == "hours":
            seconds = (int(args[-2]) * 3600)
        elif args[-1] == "minutes":
            seconds = (int(args[-2]) * 60)
        elif args[-1] == "seconds":
            seconds = (int(args[-2]))
            
        await ctx.send(f"Booting them up in {args[-2]} {args[-1]}.")
        await asyncio.sleep(seconds) 
            
        for user in args[0: -2]:
            try:
                converter = MemberConverter()
                user = await converter.convert(ctx, user)
                try:
                    victim = client.get_user(user.id)
                    for i in range(5):
                        await victim.send(f'<@{user.id}> Boot up!')
                        await ctx.send(f'<@{user.id}> Boot up!')
                        await asyncio.sleep(.75) 
                except:
                    for i in range(5):
                        await ctx.send(f'<@{user.id}> Boot up!')
                        await asyncio.sleep(.75) 
            except:
                print(f"Who is {user}???")
                await ctx.send('User not found. Try again.')
    else:
        await ctx.send('Unknown input. Try again using "$bootupLater (username [multiple]) (time) (plural units).')



client.run(BOTTOKEN)