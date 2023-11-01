# Thanks For: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/ramsupportt


from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph//file/ea39b52686ec35ed9950a.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hi, I'm Arab-Ubot.")
API_HASH = getenv("API_HASH", "947327cf5ff0053a66bf7951f9db5658")
API_ID = getenv("API_ID", "17896688")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001812143750, -1001571197486]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001571197486").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_TOKEN = getenv("BOT_TOKEN", "6484534684:AAFhc381-zhXgXLXG9eNf37ED4DDafZc1yc")
BOT_VER = "1.0.7"
BRANCH = getenv("BRANCH", "main")
CH_SFS = getenv("CH_SFS", "cehaarab")
IG_ALIVE = getenv("IG_ALIVE", "fadhilabdat")
CHANNEL = getenv("CHANNEL", "arabc0de")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
CMD_HNDLR = CMD_HANDLER
ID_OWNER = getenv("ID_OWNER", "1877012539")
DB_URL = getenv("DATABASE_URL", "postgres://utcfssmp:vmsLHIto_p-puPeN2Q25mA3vYxFxdYc5@suleiman.db.elephantsql.com/utcfssmp")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
GROUP = getenv("GROUP", "SiArab_Support")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/fadhilarab47/Ubot-Pyro")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAP-GEArKLaDZgtXoc_dBwe-Rc_vI8rbo2jNN6ruqHmcbEh28eonADkgEjp-XpSkGBE-Vuzve-5KFI0Jr-_wxys8yvr3GVbajRHHYY76rtf0QrVEsNfQn-_vr4-RkfYz7F9SnRvlTGIQXZNbu2X6cwFrPXNOPTAVafBueop1V4rfQDA6y2cpRKko24BfqFRx0-N_S3BRCQWQDRFNtX7jeFTpyPId-SbnCyQnxsyCQPg5y-9rm4HCJHxd5FB69oeJX_7CExApYy4hVknaEUqRG-d4nRRMeZ3pbYjY0orrFJqT3jQAjy8ECAMXC91-XPtgLAH2UOQNtMLABJKXIUNnDU1rYEDjgAAAABWOQ-EAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQAP-GEAL6rlB_fTE9dFr9UZibakTPm60IFQO-KP3xHY63RRJIHjrtcdyr8RyJN3CpgEpJoK4vJRVMxCfQEK_WFPyE16eGU5wY1AN61DAtFe9IWWMxIureadJpyMNHQDkBXbOnOfnrW4JqHj3Ryt8LSQ-aOtGUb92f1jvGdEeLdJvIWH-ijP8GQ9i9VXlsXSuBgaqA1PxkZXR8jPCINoBG6n8EchhqxLQQqj84pE8w6Bk388YKifBGZO2b-a-BTHrekN2s9GTGefAjEvjjg5BpYwBmNVoGcf3ibTUqDy6HGUnXD4d8D-6d_wpahj0rlsFrkrN3EXg7ez2PVFzSveNvf8aIDsxAAAAAB4kvM2AA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1877012539").split()))
