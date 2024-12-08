import discord
from discord.ext import commands

description='''este es un programa donde vamos a vincular a discord con visual studio code para lanzar imagenes'''

intents=discord.Intents.default()
intents.members=True
intents.message_content=True

bot=commands.Bot(command_prefix="Darwin ",description=description,intents=intents)


@bot.event
async def on_ready():
    print(f'logueado como {bot.user} (ID: {bot.user.id}) ')

@bot.event
async def on_member_join(member):
    # Obtiene el canal de bienvenida (asegúrate de reemplazarlo por el ID real del canal)
    canal_bienvenida = bot.get_channel(general)


# Crea un mensaje de bienvenida personalizado
    mensaje = f"¡Hola! Bienvenido "

    # Envía el mensaje de bienvenida al canal
    await ctx.send(mensaje)

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return

@bot.command(name='hola')
async def _hola(ctx):
        
        await ctx.send('BIENVENIDO AL CANAL SOBRE EL CUIDADO DEL MEDIO AMBIENTE.\nHola te saluda Darwin, para hablar conmigo porfavor escribe mi nombre primero.\nDime eres niño, joven o adulto?')

@bot.command(name='niño')
async def _edad(ctx):
        

    
    if message.content.lower()=="/mono":
        with open('mono.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(content="aqui esta la imagen de tu mono",file=picture)
   
        
@bot.command(name='joven')
async def _edad(ctx):
        await ctx.send('Eres un joven que puedes aportar con proyectos para mejorar el medio Ambiente')

@bot.command(name='adulto')
async def _edad(ctx):
        await ctx.send('Como adulto dime que aportes has realizado en el cuidado del medio Ambiente')
        
bot.run("Token")

















bot.run("MTI1MjgwNTEyNDE0MTg3OTQ2MA.G9GbkP.PmMSzxv32DLfIkoHs2lbJHsIHYrTgVxqkZf8Jg")