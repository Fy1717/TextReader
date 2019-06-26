from gtts import gTTS
import os
while(True):
    x = input("Okutmak İstediğiniz Yazıyı Giriniz :")
    soyle = gTTS(text=x , lang='tr')
    soyle.save("isim2.wav")
    os.system("isim2.wav")