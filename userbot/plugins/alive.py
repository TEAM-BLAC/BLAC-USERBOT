
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/f3a82860656f0263bc8aa.jpg"
file2 = "https://telegra.ph/file/a12fa182ccac24b2bb9a5.jpg"
file3 = "https://telegra.ph/file/581e32d5dae4c05d82fa1.jpg"
file4 = "https://telegra.ph/file/b39d4a5cb3f4ae080924b.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "__                       **😎🔥 𝐒𝐀𝐕𝐀𝐆𝐄 2.0 😎🔥**  __\n\n"
pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍         ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ 𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏      ➣ [𝐒𝐀𝐕𝐀𝐆𝐄](https://t.me/joinchat/RPrJW2IU-Uo4MGRl)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐍𝐋 ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/0KCyT0MHyAhmMmRl)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/qCIk-af6VW1kNDll)\n"
pm_caption += "➾ 𝐂𝐑𝐄𝐀𝐓𝐎𝐑     ➣ [⚡𝐒𝐀𝐌𝐄𝐄𝐑⚡](@SAMEER_795)\n" 
                  
pm_caption += " \n"
pm_caption += "[✨𝑫𝑬𝑷𝑳𝑶𝒀 𝒀𝑶𝑼𝑹 𝑺𝑨𝑽𝑨𝑮𝑬 2.0✨](https://github.com/sameerpanthi/SAVAGE-2.0-BOT)"


# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
