import os

import discord
from dotenv import load_dotenv
import asyncio
import datetime

from keep_alive import keep_alive
from get_prompt import get_prompt


def round_time(dt=None, round_to=3600):
  """Round a datetime object to any time-lapse in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
  if dt is None:
    dt = datetime.datetime.now()
  seconds = (dt.replace(tzinfo=None) - dt.min).seconds
  rounding = seconds // round_to * round_to
  return dt.replace(microsecond=0) - datetime.timedelta(seconds=seconds) + datetime.timedelta(seconds=rounding)


load_dotenv()

TOKEN = os.environ['TOKEN']
channel_id = os.environ['CHANNEL_ID']
user_id = os.environ['USER_ID']

client = discord.Client(intents=discord.Intents.all())


async def send_daily_message():
  locked = False
  while not client.is_closed():
    # Get a time object for the current hour and minute
    current_time = datetime.datetime.utcnow()

    # Round the current time to the nearest minute
    rounded_time = round_time(current_time)

    # Get a date object for today's date
    today = datetime.date.today()

    # Replace this with your desired time
    msg_time = datetime.time(hour=12, minute=00)

    # Combine the date and time objects into a single datetime object
    message_time = datetime.datetime.combine(today, msg_time)

    # Replace this with your desired rest time
    rst_time = datetime.time(hour=7, minute=00)

    # Combine the date and time objects into a single datetime object
    reset_time = datetime.datetime.combine(today, rst_time)

    print(current_time)
    print(rounded_time)
    print(message_time)
    print(reset_time)
    print(rounded_time == message_time)
    print(rounded_time == reset_time)

    if rounded_time == message_time and not locked:
      locked = True
      prompt = get_prompt().rstrip()

      if prompt == "end":
        # Fetch the user by their user id
        user = await client.fetch_user(user_id)
        # Send the message to the user
        await user.send(
          "Prompts are empty, prolly should update that bro. Also send it manually today or not up to you lel."
        )
      else:
        # Replace "channel_id" with the ID of the channel you want to send the message to
        channel = await client.fetch_channel(channel_id)
        await channel.send(
          f"@everyone Today's drawing challenge is to draw Spook or one of the other voidlings as {prompt}. Good luck"
        )

    if rounded_time == reset_time and locked:
      locked = False
    await asyncio.sleep(3600)  # Check the current time every hour


async def main():
  keep_alive()
  try:
    await client.login(TOKEN)
  except: 
    os.system("kill 1")
  print("Discord client started")
  await send_daily_message()


asyncio.run(main())
