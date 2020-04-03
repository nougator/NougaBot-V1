import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')

TOKEN = 'Place your token here'


@client.event
async def on_ready():
    print('Ready')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))


@client.command(aliases=['8ball'])
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
    if str(message.channel.id) == 'channelId':
        async def YesNoDetect(msg):
            output = msg.content.replace(',', '').replace('.', '').replace('!', '').replace('?', '').lower().split()

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
    channel = discord.utils.get(member.guild.channels, name='👋bienvenue')
    welcome_embed = discord.Embed(title=f'Bienvenue, {member}', description='Va lire <#channelId>',
                                  color=discord.Colour.from_rgb(115, 0, 255),
                                  url='message link')
    await channel.send(embed=welcome_embed)
    await member.send(f'Bienvenue {member.mention} regarde dans <#channeId> pour éviter de te faire sanctionner débilement :wink:')
    print(f'{member} has joined.')

client.run(TOKEN)
