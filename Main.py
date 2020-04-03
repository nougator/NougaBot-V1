import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix='.')

TOKEN = 'Place your token here'


@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))


@client.command()
async def _8ball(self, ctx, *, question):
        responses = ['Oui.',
                     'Non.',
                     'Je ne sais pas.',
                     'Heureusement pas',
                     'Heureusement oui.',
                     'Malheureusement oui.',
                     'Malheureusement non.',
                     'Je n\'espère pas.',
                     'Bien sûr!',
                     'Bien sûr que non!',
                     'T\'as vraiment envie de savoir?',
                     'La réponse va te choquer... Oui!',
                     'La réponse va te choquer... Non!',
                     'NON!!!',
                     'OUI!!!']
        await ctx.send(f'> {question}\n{random.choice(responses)}')

@client.command()
async def load(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong, `{round(client.latency * 1000)}ms`')


@client.command()
async def choice(ctx, *, args):
    if len(args) > 0:
        await ctx.send(f'Mon choix est: **{random.choice(args.split())}**')
    else:
        await ctx.send('Utilisation: `.choice chat chien lapin`')


@client.command()
async def say(ctx, *, args):
    await ctx.send(args)


@client.event
async def on_message(message):
    if str(message.channel.id) == '694614592030244895':
        async def YesNoDetect(msg):
            inputStr = msg.content.replace(',', '')
            inputStr1 = inputStr.replace('.', '')
            inputStr2 = inputStr1.replace('!', '')
            inputStr3 = inputStr2.replace('?', '')
            output = inputStr3.lower().split()

            async def sendLoseMsg():
                await msg.channel.send(f'Tu as perdu **{message.author.mention}**!')

            for checking in output:
                if checking == 'oui':
                    sendLoseMsg()
                elif checking == 'non':
                    sendLoseMsg()
                elif checking == 'nan':
                    sendLoseMsg()
                elif checking == 'ouais':
                    sendLoseMsg()
                elif checking == 'yes':
                    sendLoseMsg()
                elif checking == 'no':
                    sendLoseMsg()

        await YesNoDetect(message)

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    # welcome messages
    channel = discord.utils.get(member.guild.channels, name='👋𝖇𝖎𝖊𝖓𝖛𝖊𝖓𝖚𝖊')
    welcome_embed = discord.Embed(title=f'Bienvenue, {member}', description='Va lire <#693487377481596968>',
                                  color=discord.Colour.from_rgb(115, 0, 255),
                                  url='https://discordapp.com/channels/693474364795912265/693487377481596968/693494127740059718')
    await channel.send(embed=welcome_embed)
    await member.send(f'Bienvenue {member.mention} regarde dans <#693487377481596968> pour éviter de te faire sanctionner débilement :wink:')
    print(f'{member} has joined.')

client.run(TOKEN)
