import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = open("token.txt", "r").read()  # this token is saved in the directory in a text file

client = discord.Client()  # starts the discord client.


@client.event 
async def on_ready():  # method that runs only once
    print(f'We have logged in as {client.user}')  # prints which bot is logged in.


@client.event
async def on_message(message):  # event that happens per any message.

    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")


client.run(token)  # recall my token was saved!