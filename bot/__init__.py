import discord
from bot.bot import intent, send_message


def run_discord_bot():
    TOKEN = ''
    client = discord.Client(intents=intent)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in channel ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        elif user_message[0] == '!':
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)