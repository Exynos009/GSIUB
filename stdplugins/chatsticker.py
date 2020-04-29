#New Qoute module by @PhycoNinja13b 😉
#Uses another bot named @es3n1n_bot
# .quote for making quote

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="quote ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.reply("```Reply to text message```")
       return
    chat = "@es3n1n_bot"
    sender = reply_message.sender 

    if reply_message.sender.bot:
       await event.reply("```Reply to actual users message.```")
       return

    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=810547723))
              message = await event.client.forward_messages(chat, reply_message)
              await message.reply("/quote")

              await asyncio.sleep(4)
              response = await response

          except YouBlockedUserError: 
              await event.reply("```Please unblock me u Nigga```")
              return

          if response.text.startswith("Hi!"):
             await event.reply("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message, reply_to=event.message.reply_to_msg_id)
