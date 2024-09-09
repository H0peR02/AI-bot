import discord
from model import money
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("Я убрал токен")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file.nsme = attachment.filename 
            file.url = attachment.url
            await attachment.save(f'images/{file_name}')
            await ctx.send(f'Сохранили сылку в images/{file_name}')
            await ctx.send(name)
        else:
            await ctx.send('Вы забыли загрузить картинку  :(')

    name = money(f'изоображение сохранено в images/{file_name}')
    await ctx.send(name)
    if name == 'доллар':
        await ctx.channel.send('это - доллар')
    if name == 'теньге':
        await ctx.channel.send('это - теньге')
    if name == 'рубль':
        await ctx.channel.send('это - рубль')
    if name == 'фунт':
        await ctx.channel.send('это - фунт')


@bot.run('Я убрал токен')
