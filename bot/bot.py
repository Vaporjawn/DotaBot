import discord
from bot import responses
import io

intent = discord.Intents.default()
intent.message_content = True


async def send_message(message, user_message, is_private):

    try:
        response = responses.handle_responses(user_message)
        with io.StringIO(response) as file:

            msg = file.read(1999).strip()
            while len(msg) > 0:

                await message.author.send(msg) if is_private else await message.channel.send(msg)
                msg = file.read(1999).strip()

    except Exception as e:
        print(e)
