#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Aa gaye Betichod string generate karne. 
lodu use ==>> my.telegram.com (vpn use karna) <<==
Apna Telegram Account login kar btc
Click on API Development Tools Blah Blah Maa ki chu
Create a new application, by entering the required details Maa ka bhosda""")
APP_ID = int(input("Madarchod Enter APP ID here: "))
API_HASH = input("Gandu ab API HASH daal: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
