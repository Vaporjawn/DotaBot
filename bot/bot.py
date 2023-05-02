import discord
from bot import responses

intent = discord.Intents.default()
intent.message_content = True


async def send_message(message, user_message, is_private):

    try:
        response = responses.handle_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)
