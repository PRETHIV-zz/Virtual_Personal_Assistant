from gtts import gTTS
import os
print("Enter the Text u want to convert into voice")
text_of_me=input()
language = 'en'
voice = gTTS(text=text_of_me, lang=language, slow=False)
file=input("Enter the file name to save the voice (Eg: hello.mp3)")
os.chdir('../../voice')
voice.save(file) 
print("Voice created successfully")
