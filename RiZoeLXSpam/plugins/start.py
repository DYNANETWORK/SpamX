import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, ALIVE_PIC

RIZ_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/87f1fb4d1ab2e95cfcfe.jpg"


Riz_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MAMBA_X_SUPPORT")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/SUKHPAL443/SpamX")
        ]
        ]


@Riz.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz2.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz2.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz2.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)      
 
@Riz3.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz3.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz3.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz4.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz4.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz4.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)  

@Riz5.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz5.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz5.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)

@Riz6.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz6.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETW0RK)**"
       await Riz6.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)       

@Riz7.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz7.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id 
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz7.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)

@Riz8.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz8.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz8.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz9.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz9.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)
                
@Riz10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       RizBot = await Riz10.get_me()
       bot_id = RizBot.first_name
       bot_username = RizBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheRiZoeL = event.chat_id
       firstname = replied_user.user.first_name
       Rizmsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝑀𝐴𝑀𝐵𝐴 𝑋](https://t.me/MAMBA_NETWORK)**"
       await Riz10.send_file(TheRiZoeL,
                RIZ_IMG,
                caption=Rizmsg, 
                buttons=Riz_Button)                
