# This example requires the 'message_content' intent.

import discord
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "code_block", description = "Rewrite the message in code block") 
async def first_command(interaction, value:str):
    await interaction.response.send_message("```" + value + "```")

@tree.context_menu(name = "code_block")
async def test(interaction, value: discord.Message):
    await value.delete()
    await interaction.response.send_message("```" + value.content + "```")

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/code '):
        await message.delete()
        new = message.content.split("/code ")
        await message.channel.send("```" + new[1] + "```")

client.run('Secret Key')
