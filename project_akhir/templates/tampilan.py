from tkinter import *
# import textwrap
# import os
# import random
# import datetime
# import wikipedia
# import time
# import json
# from googlesearch import search
# from wikipedia.exceptions import WikipediaException
# from bs4 import BeautifulSoup
# from youtubesearchpython import VideosSearch
# import requests
# import math

# # ---- bagian GUI-nya window ----
# window = tk.Tk()
# window.title("Carebot")
# window.geometry("400x650") # --> ubah ukuran layar
# window.configure(bg="gray94")

# # --- bagian teks ---
# teks = Text(window)
# teks.grid(row=0,column=0,columnspan=2)

# # --- bagian entry ---
# entry = tkinter.Text(window, height = 10, width=100)
# entry.pack()

# # --- bagian tampilan entry ---
# tampilan_entry = tkinter.font.Font(family="Times New Roman",
#                                   size = 18,
#                                   slant="italic")
# entry.configure(font = tampilan_entry)
# # --- bagian footer

# # --- bagian ending ---
# window.mainloop() # --> supaya bisa running

window = Tk()
window.config(bg="light grey")
window.title('CareBot')
logo = PhotoImage(file="templates/logo2.png")
window.iconphoto(True,logo)
lebar=1200
tinggi=720
x=1000
y=1000
window.resizable(0,0)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight() 
newx = int((screenwidth/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2))
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

# Main window
canvas = Canvas(window, width=1200, height=720, bg="gray94")
canvas.grid(row=0, column=0, columnspan=8)
canvas.place(x=10, y=10, width=1180, height=700)
label = Label(canvas)
bg = PhotoImage(file="templates/bg1.png")
w1 = Label(canvas, image=bg).pack(side="right")

# # memuat file json
# with open("intents.json", "r", encoding='utf-8') as f:
#     COMMAND = json.load(f)


# messages = []
# class Me:
#     def __init__(self, master, message=""):
#         self.master = master
#         self.frame = Frame(master, bg="#B2EEC0")
#         self.i = self.master.create_window(270, 390, window=self.frame, anchor="ne")
#         Label(self.frame, text=textwrap.fill(message, 20), font=("Sogue", 10), bg="#B2EEC0").grid(row=1, column=0, sticky="w", padx=1, pady=3)
#         window.update_idletasks()
#         ask.delete(0, END)

#         # Apply commands
#         if 'translate' in message:
#             translator(message)
#         elif 'wikipedia' in message:
#             Search(message)
#         elif 'timer' in message:
#             Timer(message)
#         elif 'google' in message:
#             Google(message)
#         elif 'note' in message:
#             Note(message)
#         elif 'mentalillness' in message:
#             try:
#                 cases, deaths, recovered = get_data(message)
#                 put_answer(f"Cases {cases}")
#                 put_answer(f"Deaths {deaths}")
#                 put_answer(f"Recovered {recovered}")
#             except Exception:
#                 put_answer("I can't find your country")

#         elif 'video' in message:
#             find_video(message)
#             put_answer('Have a nice day!')
#         elif 'what is' in message:
#             x = Math_Operations(message)
#             put_answer(str(x))
#         elif 'weather' in message:
#             try:
#                 temp, w = weather(message)
#                 put_answer(f"The temperature is {temp}°C")
#                 put_answer(w)
#             except Exception:
#                 put_answer("I can't find your place")
#         else:
#             keys = COMMAND.keys()

#             for key in keys:
#                 if message in key and len(message) > 1 or key == "error":
#                     commands = COMMAND.get(key)
#                     for command in commands[0]:
#                         os.startfile(command)

#                     answer = random.choice(commands[1])
#                     put_answer(answer)

#                     if "rock" in message or "scissors" in message or "paper" in message:
#                         result = Rock(message, answer)
#                         put_answer(result)
#                     elif 'tell me a joke' in message or "joke" in message:
#                         canvas.move(ALL, 0, -120)
#                     elif 'clear' in message:
#                         canvas.move(ALL, -1000, 0)
#                     elif 'time' in message:
#                         Time = datetime.datetime.now().strftime("%H:%M:%S")
#                         put_answer(Time)
#                     elif 'stop' in message or 'bay' in message or 'bey' in message or 'see you soon' in message:
#                         window.quit()
#                     break


# answers = []


# class Assistant:
#     def __init__(self, master, answer=""):
#         self.master = master
#         self.frame = Frame(master, bg="#C2E3CA")
#         self.i = self.master.create_window(10, 390 + 40, window=self.frame, anchor="nw")
#         Label(self.frame, text=textwrap.fill(answer, 25), font=("Sogue", 10),bg="#C2E3CA").grid(row=1, column=0, sticky="w", padx=1, pady=3)
#         window.update_idletasks()

# # Functions


# def send_message():
#     if messages or answers:
#         canvas.move(ALL, 0, -50)
#     message = ask.get()
#     me = Me(canvas, message.lower())
#     messages.append(me)
#     put_answer('Ada yang bisa dibantu?')


# def put_answer(answer):
#     assistant = Assistant(canvas, answer=answer)
#     answers.append(assistant)
#     if answers or messages:
#         canvas.move(ALL, 0, -35)


# def key(event=None):
#     send_message()


# def wishMe():
#     hour = datetime.datetime.now().hour
#     if hour >= 0 and hour < 12:
#         put_answer("Hallo Selamat Pagi!")
#         put_answer("Ada yang bisa dibantu??")
#     elif hour >= 12 and hour < 15:
#         put_answer("Hallo Selamat Siang!")
#         put_answer("Ada yang bisa dibantu?")
#     elif hour >= 15 and hour < 18:
#         put_answer("Hallo Selamat Sore!")
#         put_answer("Ada yang bisa dibantu?")
#     else:
#         put_answer("Hallo Selamat Malam!")
#         put_answer("Ada yang bisa dibantu?")


# def Timer(message):
#     t = message.replace("timer", "")
#     try:
#         time.sleep(int(t))
#         put_answer('Time is over')
#     except Exception:
#         put_answer("Write your time")


# def Rock(message, answer):
#     if message == 'rock' or message == 'paper' or message == 'scissors':
#         if answer == 'Rock' and message == 'paper':
#             result = 'You won'
#         elif answer == 'Paper' and message == 'rock':
#             result = 'I won'
#         elif answer == 'Scissors' and message == 'rock':
#             result = 'You won'
#         elif answer == 'Rock' and message == 'scissors':
#             result = 'I won'
#         elif answer == 'Paper' and message == 'scissors':
#             result = 'You won'
#         elif answer == 'Scissors' and message == 'paper':
#             result = 'I won'
#         else:
#             result = 'Draw'
#         return result


# def Search(message):
#     put_answer('Searching Wikipedia...')
#     statement = message.replace("wikipedia", "")
#     try:
#         results = wikipedia.summary(statement, sentences=3)
#         put_answer(results)
#         canvas.move(ALL, 0, -len(results)*0.68)
#     except WikipediaException:
#         put_answer('I can not find it')


# def Google(message):
#     query = message.replace("google", "")
#     j = search(query)
#     put_answer(j[0])
#     window.clipboard_clear()
#     window.clipboard_append(j[0])
#     window.update()
#     canvas.move(ALL, 0, -20)


# def Note(message):
#     message = message.replace('note ', '')
#     window.clipboard_clear()
#     window.clipboard_append(message)
#     window.update()
#     os.startfile(COMMAND[0]['note'][0])
#     put_answer('Paste a note!')


# def get_data(message):
#     coutry = message.replace("coronavirus ", "")
#     if coutry == "czech republic":
#         coutry = "czech-republic"
#     url = f"https://www.worldometers.info/coronavirus/country/{coutry}/"

#     # Make a request
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     # Extract and store in top_items according to instructions on the left
#     products = soup.select('div.content-inner')
#     for elem in products:
#         total_cases = elem.select('div.maincounter-number')[0].text
#         total_deaths = elem.select('div.maincounter-number')[1].text
#         total_recovered = elem.select('div.maincounter-number')[2].text
#     return total_cases, total_deaths, total_recovered


# def find_video(message):
#     video = message.replace("video ", "")
#     videosSearch = VideosSearch(video, limit=1)
#     info = videosSearch.result()
#     url = f"https://www.youtube.com/watch?v={info['result'][0]['id']}"
#     os.startfile(url)


# def Math_Operations(operation):
#     ex = operation.replace("what is ", "")
#     try:
#         if "sin" in ex:
#             ex = ex.replace("sin ", "")
#             result = math.sin(float(ex))

#         elif "cos" in ex:
#             ex = ex.replace("cos ", "")
#             result = math.cos(float(ex))

#         elif "factorial" in ex:
#             ex = ex.replace("factorial ", "")
#             result = math.factorial(int(ex))

#         elif "binary" in ex:
#             ex = ex.replace("binary ", "")
#             ex = bin(int(ex))
#             result = ex.replace("0b", "")

#         else:
#             result = str(eval(ex))

#         return result

#     except Exception:
#         result = "I don't understand"

#     return result


# def translator(sentence):
#     sentence = sentence.replace("translate to ", "")
#     if 'czech' in sentence:
#         sentence = sentence.replace("czech", "csech")
#     try:
#         sentence = sentence.split(" ", 1)
#         url = f'https://translate.google.cz/?hl=cs&sl=auto&tl={sentence[0][:2]}&text={sentence[1]}&op=translate'
#         os.startfile(url)
#         put_answer("I get advice from google")
#     except Exception:
#         put_answer("Try again")


# def weather(city):
#     city = city.replace('weather ', '')
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=8ef61edcf1c576d65d836254e11ea420"
#     r = requests.get(url)
#     r = r.json()
#     temp = r['main']['temp'] - 273.15
#     weather = r['weather'][0]['description'].capitalize()

#     temp = round(temp, 1)
#     return temp, weather



# Entry
ask = Entry(window, bd=3, width=26, font=("Times New Roman", 18, "italic"))
ask.place(x=10, y=675, width=1140, height=35)
ask.focus()
ask.insert(0, "")

# Button
button = Button(window, justify=LEFT)
photo = PhotoImage(file="templates/image/send(1).png")
button.config(image=photo, width="32", height="30", relief=FLAT)
button.pack(side=LEFT)
button.place(x=1150, y=673)

window.bind('<Return>')
window.resizable(width=False, height=False)
# wishMe()
window.lift()
window.call('wm', 'attributes', '.', '-topmost', True)

window.mainloop()