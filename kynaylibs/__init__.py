import sys

import pyrogram
from pyrogram import *

BL_GCAST = [
    -1001982790377,  #cemarasupport
    -1001473548283,  #sharing
    -1001864253073,  #rito
    -1001812143750,  #kynan
    -1001287188817,  #kazu
    -1001294181499,  #anjani
    -1001692751821,  #geezram
    -1001608701614,  #uputt
    -1001797285258,  #ayiinchat
    -1001876092598,  #lumiere
]


DEVS = [
    1898065191,  # @rizzvbss
    1054295664,  # @kenapanan
    1889573907,  # @kanaayyy
    1755047203,  # @Bangjhorr
    2133148961,  # @mnaayyy
    2076745088,  # @gua
    5876222922,  # Tomay
    1936017380,  # otan
    2013365169,  # liona
    1966129176,  # doms
    5063062493, #kazu
    1939171309, #doni
    1810243126, #om
    1992087933, #zen
]


async def ajg(client):
    try:
        await client.join_chat("syavenstore")
        await client.join_chat("lumiereproject")
        await client.join_chat("gabutanlu")
        await client.join_chat("Lumieresupport")
    except pyrogram.errors.exceptions.bad_request_400.UserBannedInChannel:
        print(
            "Anda tidak bisa menggunakan bot ini, karna telah diban dari @Lumieresupport\nHubungi @urfavtoyy untuk dibuka blokir nya."
        )
        sys.exit()
