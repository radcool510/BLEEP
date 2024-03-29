import random
import discord
import os
from discord.ext import tasks
from discord.ext.commands import Greedy, Context
from discord import app_commands
from discord.ext import commands
import asyncio
import time
from datetime import datetime
import re
from discord.ui import Button, View
import json
import urllib.parse
from bs4 import BeautifulSoup



bot = commands.Bot("!", intents=discord.Intents.all())

censored_words = ["nigga", "kms", "suicide", "retard","nigger"]




@bot.event
async def on_ready():
    print(f"logged as {bot.user}")
    change_status.start()


@tasks.loop(seconds=5)
async def change_status():
  await bot.change_presence(activity=discord.Game(random.choice(["BLEEP", "BOOP"])))



@bot.event
async def on_message(message):
    content = message.content.lower()

    if message.content == "uh oh":
        await message.channel.send("https://cdn.discordapp.com/attachments/1122408339570180147/1137485909453971506/mc.jpg", reference=message)

    if message.content == "XD":
        await message.channel.send("CD", reference=message)

    if message.content == "mario":
        await message.channel.send("https://media.discordapp.net/attachments/1122408339570180147/1140644983037239336/world-1-1.gif", reference=message)

    if message.content == "<@1116012552728617041>":
        await message.channel.send("HELLO THERE YOU PING AN OWNER SO I WILL DO IT <@1116012552728617041> THIS PERSON IS TELLING YOU SOMETHING", reference=message)

    if message.content == "mad":
        await message.channel.send("hhttps://discord.com/channels/@me/1122408339570180147/1158486608182513744", reference=message)
    else:
        await bot.process_commands(message)
    if message.content == "lol":
        await message.channel.send("you got a whole squad laughing", reference=message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(word in message.content.lower() for word in censored_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, your message containing a censored word has been deleted.")

@bot.command()
async def ascii(ctx):
    art = """
      /\\_/\\  
     ( o.o ) 
     > ^ <
    """
    await ctx.send(f"Here's some ASCII art for you:\n```\n{art}\n```")


@bot.command()
async def game(ctx):
    await ctx.send("Welcome to the guessing game! I'm thinking of a number between 1 and 100. Start guessing!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    while True:
        def check(message):
            return message.author == ctx.author and message.content.isdigit()

        try:
            user_guess = await bot.wait_for('message', check=check, timeout=30)
            guess = int(user_guess.content)

            if guess < secret_number:
                await ctx.send("Too low! Guess higher.")
            elif guess > secret_number:
                await ctx.send("Too high! Guess lower.")
            else:
                await ctx.send(f"Congratulations! You guessed the correct number: {secret_number}")
                break  # Exit the loop when the user guesses correctly

        except asyncio.TimeoutError:
            await ctx.send("Time's up! The secret number was: {secret_number}")
            break



@bot.command()
async def hello(ctx):
  await ctx.send(ctx.author.mention + " hello!")

@bot.command(aliases=['8ball'])
async def ball(ctx,*, question):
  responses = [
  discord.Embed(title='It is certain.'),
  discord.Embed(title='It is decidedly so.'),
  discord.Embed(title='Without a doubt of your .'),
  discord.Embed(title='Yes - definitely.'),
  discord.Embed(title='You may rely on it to yourself not me.'),
  discord.Embed(title='Maybe idk'),
  discord.Embed(title='Outlook good.'),
  discord.Embed(title='Yes.'),
  discord.Embed(title='Signs point to yes.'),
  discord.Embed(title='say that again please.'),
  discord.Embed(title='could you say that again, it sound so soft.'),
  discord.Embed(title='Better not tell you now.'),
  discord.Embed(title='Cannot predict now because im toooooooo lazy.'),
  discord.Embed(title='Concentrate and ask again and listen closely.'),
  discord.Embed(title="Don't count on it because im not into this."),
  discord.Embed(title='no.'),
  discord.Embed(title='My sources say no.'),
  discord.Embed(title='im sorry but it not very good.'),
  discord.Embed(title='Very doubtful.')
    ]
  responses = random.choice(responses)
  await ctx.send(content=f'Question: {question}\nAnswer:', embed=responses)


@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called


@bot.command()
async def react(ctx):
    def check(reaction, user):  # Our check for the reaction
        return user == ctx.message.author  # We check that only the authors reaction counts

    await ctx.send("React to this for a test")  # Message to react to

    reaction = await bot.wait_for("reaction_add", check=check)  # Wait for a reaction
    await ctx.send(f"You reacted with: {reaction[0]}")  # With [0] we only display the emoji


@bot.command()
async def flipcoin(ctx):
  heads_tails = ['Heads', 'Tails']

  choice = random.choice(heads_tails)

  await ctx.send(choice)



@bot.command()
async def hey(ctx):
    msg = await ctx.send("Hello")
    reaction1 = '👋'
    reaction2 = ':stretchreaction:1134595302641381496'
    await msg.add_reaction(reaction1)
    await msg.add_reaction(reaction2)

@bot.command()
async def activity(ctx, user: discord.Member):
    try:
        for activity in user.activities:
            if activity.type == discord.ActivityType.playing:
                await ctx.send(f"{user.name} is playing {activity.name}")
                return
        await ctx.send(f"{user.name} is not playing anything.")
    except discord.NotFound:
        await ctx.send("User not found.")


@bot.command()
async def love(ctx, name1, name2):
    love_percentage = calculate_love_percentage(name1, name2)
    response = f"The love percentage between {name1} and {name2} is {love_percentage}%! ❤️"
    await ctx.send(response)

def calculate_love_percentage(name1, name2):
    combined_names = name1.lower() + name2.lower()
    love_percentage = hash(combined_names) % 101
    return love_percentage

@bot.command()
async def who(ctx):
    embedVar = discord.Embed(
        title="bleep", description="hey i'm bleep, i kinda need help", color=0x336EFF
    )
    embedVar.add_field(name="WIP", value="still in development", inline=False)
    embedVar.add_field(name="PLANS", value="alot of plans on me and my devs needs a raise which he dosen't need one", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    
    if data and 'url' in data[0]:
        cat_url = data[0]['url']
        await ctx.send(cat_url)
    else:
      await ctx.send("Sorry,I couldn't fetch a cat image atthemoment.") 

@bot.command()
async def dog(ctx):
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    data = response.json()

    if data and 'url' in data[0]:
        dog_url = data[0]['url']
        await ctx.send(dog_url)
    else:
        await ctx.send("Sorry, I couldn't fetch a dog image at the moment.")

@bot.command()
async def echo(ctx, *, message_to_send):
    if ctx.author.id in allowed_user_ids: 
        await ctx.message.delete()

        # Send the echoed message
        await ctx.send(message_to_send)
    else:
        await ctx.send("You don't have permission to use this command.")

@bot.command()
async def update(ctx):
    try:
        await ctx.send("Bot successfully updated!")
        sys.exit(0)
    except Exception as e:
        await ctx.send(f"Failed to update the bot: {str(e)}")

@bot.command()
async def findimage(ctx, *, query):
    image_results = perform_image_search(query)

    if image_results:
        await ctx.send("Here are the image my friend:")
        for result in image_results:
            await ctx.send(result)
    else:
        await ctx.send("No image search results found.")

def perform_web_search(query):
    try:
        search_results = list(re.search(query, num=5, stop=5, pause=2))
        return search_results
    except Exception as e:
        print(f"Error performing web search: {e}")
        return []

def perform_image_search(query):
    try:
        # Construct a search URL for image results
        search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&tbm=isch"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")

        image_results = []
        for img in soup.find_all("img"):
            img_url = img.get("src")
            if img_url and img_url.startswith("http"):
                image_results.append(img_url)

        return image_results[:1]  # Limit to the first 5 results
    except Exception as e:
        print(f"Error performing image search: {e}")
        return []

bot.run(os.environ['TOKEN'])
