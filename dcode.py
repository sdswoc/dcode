import discord
from discord.ext import commands 

ashish = discord.Intents.default()

ashish.members = True

client=commands.Bot(command_prefix='r!', case_insensitive=True , intents = ashish)
list1=['✅','❎']
@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_reaction_add(reaction, user):
    if not user.bot:
        if reaction.emoji=='✅':
            baby=client.get_channel(confesschannel code)
            await baby.send(reaction.message.content)
            await reaction.message.delete()
        if reaction.emoji=='❎':
            await reaction.message.delete()

@client.command()
@commands.dm_only()
async def confess(ctx,*,message):
    await ctx.send('Your confesssion will be posted anonymously after verification by the admins. The admins won\'t be able to know your identity.')
    jojo = client.get_channel(approval code)
    message1 = await jojo.send(f'{message}')
    for emoji in list1:
        await message1.add_reaction(emoji)


client.run('bot key')
