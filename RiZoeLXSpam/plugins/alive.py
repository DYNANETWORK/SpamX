from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/87f1fb4d1ab2e95cfcfe.jpg"
  

          
rizoel = "✧ 𝑀𝐴𝑀𝐵𝐴 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑆 𝐻𝐸𝑅𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MAMBA_X_SUPPORT")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/SUKHPAL443/SpamX")
        ]
        ]
        )
    
