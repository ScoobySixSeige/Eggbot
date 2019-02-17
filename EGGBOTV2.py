import discord
from discord.ext import commands



TOKEN = 'NTE4OTc0NjE5ODYxMTIzMDcy.Dy6rLg.px9EnI3d8iSPWgo6qor9Wap2HgY'
version = 'v3.0'

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
	print('Bot is ready.')
	await client.change_presence(game=discord.Game(name='for .help ' + str( version),type = 3))

@client.event
async def on_memeber_join(memeber):
	print('Recognised that a menber called ' + memeber.name + 'joined')
	await client.send_message(memeber, 'sup, Im your overlord egg bot, use .help for cmds!')
	print('sent message to ' + memeber.name)

@client.event
async def on_message(message):
	author = message.author
	content = message.content
	print('{}: {}'.format(author, content))
	await client.process_commands(message)


@client.event
async def on_message(message):
	channel = message.channel
	if message.content.startswith('.ping'):
		await client.send_message(channel, 'Pong!')

	if message.content.startswith('.say'):
		msg = message.content.split()
		output = ''
		for word in msg[1:]:
			output += word
			output += ' '
		await client.send_message(channel, output)
	if message.content.startswith('.help'):
		await client.send_message(channel, 'Click here for the full list of commands!: https://eggbotdiscord.weebly.com  ')
	if message.content.startswith('.egg'):
		await client.send_message(channel, 'https://cdn.discordapp.com/attachments/538524656366387212/538525470476599298/EGG.JPG')
	if message.content.startswith('.supreme'):
		await client.send_message(channel, 'https://cdn.discordapp.com/attachments/538524656366387212/538588868656496640/576px-Supreme_Logo.svg.png')
	if message.content.startswith('.add'):
		await client.send_message(channel, 'Add me here! https://discordapp.com/oauth2/authorize?&client_id=518974619861123072&scope=bot&permissions=8' )
	if message.content.startswith('.bot'):
		await client.send_message(channel,'There are many bots but im the best')
	if message.content.startswith('.version'):
		await client.send_message(channel, 'my current version is ' + (version))
	if message.content.startswith('.sam'):
		await client.send_message(channel, '*Screams N word*')
	if message.content.startswith('.aidan'):
		await client.send_message(channel, 'https://cdn.discordapp.com/attachments/538524656366387212/538589826543255553/Aidan.JPG')
	if message.content.startswith('.test'):
		await client.send_message(channel, ':thumbsup:')
	if message.content.startswith('.troll'):
		await client.send_message(channel, 'https://cdn.discordapp.com/attachments/538524656366387212/539246087572291584/SmartSelect_20190127-174817_Instagram.jpg')
	if message.content.startswith('.shaggy'):
		await client.send_message(channel,'https://cdn.discordapp.com/attachments/538127171923869713/539952993580220438/ShaggyRogers.jpg')
	
		

client.run(TOKEN)