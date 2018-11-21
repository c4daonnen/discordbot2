 
import discord
client = discord.Client()

TOKEN = "NTAyNzE0ODA1NzY2MDYyMDgx.Dqr9xA.-8UE7ayGNM1aqA3PIg2H2tP0m0M"

from collections import defaultdict
user_reaction_dic = defaultdict(dict)

@client.event
async def on_reaction_add(reaction, user):
    
    message = reaction.message
    
    if message.id not in user_reaction_dic[user.id]:
        user_reaction_dic[user.id][message.id] = reaction.emoji
    else:
        await client.remove_reaction(message, user_reaction_dic[user.id][message.id], user)
        user_reaction_dic[user.id][message.id] = reaction.emoji

@client.event
async def on_reaction_remove(reaction, user):
    
    message = reaction.message
    
    if user_reaction_dic[user.id][message.id] == reaction.emoji:
        del user_reaction_dic[user.id][message.id]

client.run(TOKEN)