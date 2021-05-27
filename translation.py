from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} , You are warmly welcome to Leo Youtube Downloader Bot🙂

හායි {} , ඔයාලව සාදරයෙන් අපේ Leo Youtube Downloader Bot වෙත පිලිගන්නව🙂


Made By : @naviya2🇱🇰
Support Group : @leosupportx🇱🇰
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ මෙමගින් ඔයාලට youtube ලින්ක් එකක් දැම්මම ඒකට අදාල වීඩියෝ එක ඩවුන්ලෝඩ් කරගන්න පුලුවන්.

<b><u>Set Thumbnail</u></b>
➠ මේකෙන් ඔයාලගෙ වීඩියෝ එකට custom thumbnail එකක් අඩ් කරන්න ඕන නම් ඒක ඇඩ් කරගන්න පුලුවන්.

<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb මේ command එක මගින් ඔයාල ඇඩ් කරගත්ත Thumbnail එක අයින් කරගන්න පුලුවන්.

<b><u>Show Thumbnail</u></b>
➠ Send /showthumb මේ command එක යැවීමෙන් ඔයාල ඇඩ් කරපු Thumbnail එක බලාගන්න පුලුවන්.

Made by @naviya2
"""
    ABOUT_TEXT = """
- **Bot :** `Leo YouTube Downloader`
- **Creator :** [Naviya](https://telegram.me/naviya2)
- **Channel :** [Naviya Official](https://telegram.me/new_ehi)
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/Naviya2/YouTube-Downloader)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/new_ehi'),
        InlineKeyboardButton('Support Group', url='https://telegram.me/leosupportx')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    BLOCK_LIST_TEXT = "මේ URL එක බ්ලොක්😪 ඒනිසා මේක ඩවුන්ලෝඩ් බැ😶 මේ යූසර්නේම් එකෙන් ගිහින් බලන්න පොඩ්ඩක්.\n\nUse @FnURLUploadBot"
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>ඩවුන්ලෝඩ් කිරීම ඇරඹුනා🙂...</code>"    
    UPLOAD_START = "<code>දැන් Telegram එකට අප්ලෝඩ් වෙන ගමන් පොඩ්ඩක් ඉවසපම් බොමක🙂...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "ඔන්න ඩවුන්ලෝඩ් උනා මේ කාලය ඇතුලත {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @new_ehi"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry බොම්ක ඔයා අපේ චැනල් එක තවම subscribe කරලා නැ ඒනිසා බොට් එක පාවිච්චි කරන්න දෙන්න බැ. ඒනිසා @new_ehi අපේ චැනල් එකට ගිහින් Join බටන් එක ඔබල වරෙම්🙂😶....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
