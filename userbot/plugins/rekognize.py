#credits: @Mr_Hops
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="rekognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```reply to media file```")
       return
    chat = "@Rekognition_Bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply to actual users message.```")
       return
    await event.edit("```Processing this shit!```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @Rekognition_Bot and try again```")
              return
          if response.text.startswith("See next message."):
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461083923))
              response = await response
              await event.client.send_message(event.chat_id, response.message)
          else:
              await event.client.send_message(event.chat_id, response.message)
              
