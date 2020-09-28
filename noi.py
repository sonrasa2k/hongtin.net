import playsound
from gtts import gTTS

bot_nghi = "anh nam"
bot_noi = gTTS(text=bot_nghi,lang='vi',slow = False)
bot_noi.save("bot_noi.mp3")
playsound.playsound('bot_noi.mp3', True)