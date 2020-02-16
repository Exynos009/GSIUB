"""spamwatch for uniborg users. Credits : @By_Azade"""

from asyncio import sleep
from os import remove
import asyncio
from telethon import events
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (MessageTooLongError,
                                          UserIdInvalidError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsBots, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat)

from sample_config import Config
from uniborg.util import admin_cmd
import spamwatch

ENABLE_LOG = True
LOGGING_CHATID = Config.PRIVATE_CHANNEL_BOT_API_ID
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

@borg.on(events.ChatAction())
async def spam_watch_(event):
    chat_id = event.chat_id
    client = spamwatch.Client('get api')
    ban = client.get_ban(chat_id)
    if event.user_joined or event.user_added:
        try:
            if ban:
                await event.client(
                EditBannedRequest(
                    event.chat_id,
                    user.id,
                    BANNED_RIGHTS
                )
            )
            else:
                return
        except BadRequestError:
            return
        if ENABLE_LOG:
            await event.client.send_message(
                LOGGING_CHATID,
                "#SPAM_WATCH_BAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {event.chat.title}(`{event.chat_id}`)"
            )