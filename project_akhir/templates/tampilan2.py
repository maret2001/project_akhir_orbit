import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
import json
import random
# untuk GUI tkinter
from tkinter import *
import tkinter as tk
# ================================================================================================================================================================================================================================
# AWAL GUI APLIKASI
aplikasi = tk.Tk()
aplikasi.resizable(False,False) # agar aplikasi tidak bisa di maximize/minimize
aplikasi.title("CareBot")
aplikasi.geometry("1200x720+160+40") # --> # ("lebar aplikasinya + posisi x + posisi y") ukuran aplikasi setelah running
logo = PhotoImage(file="templates/logo2.png")
aplikasi.iconphoto(True,logo)
# =========================================================================================
# frame body
frame_body = tk.Frame(aplikasi, bg="gray94")
frame_body.place(height=720, width=1200)
# =========================================================================================
# FUNGSI-FUNGSI & JSON
# --- fungsi navigasi/pindah frame ---
def navigasi_frame(frame):
  frame.tkraise()
  
# def send():
#     msg = EntryBox.get("1.0",'end-1c').strip()
#     EntryBox.delete("0.0",END)

#     if msg != '':
#         ChatLog.config(state=NORMAL)
#         ChatLog.insert(END, "You: " + msg + '\n\n')
#         ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

#         res = chatbot_response(msg)
#         ChatLog.insert(END, "Bot: " + res + '\n\n')

#         ChatLog.config(state=DISABLED)
#         ChatLog.yview(END)
  

# # --- variable untuk model chatbot ---
# model = load_model('model\chat_model.h5')
# intents = json.loads(open('dataset\intents.json').read())
# words = pickle.load(open('model\words.pkl','rb'))
# classes = pickle.load(open('model\classes.pkl','rb'))

# def clean_up_sentence(sentence):
#     sentence_words = nltk.word_tokenize(sentence)
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     return sentence_words
  
# # ---  ---
# def bow(sentence, words, show_details=True):
#     # tokenize the pattern
#     sentence_words = clean_up_sentence(sentence)
#     # bag of words - matrix of N words, vocabulary matrix
#     bag = [0]*len(words)
#     for s in sentence_words:
#         for i,w in enumerate(words):
#             if w == s:
#                 # assign 1 if current word is in the vocabulary position
#                 bag[i] = 1
#                 if show_details:
#                     print ("found in bag: %s" % w)
#     return(np.array(bag))

# def predict_class(sentence, model):
#     # filter out predictions below a threshold
#     p = bow(sentence, words,show_details=False)
#     res = model.predict(np.array([p]))[0]
#     ERROR_THRESHOLD = 0.25
#     results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
#     # sort by strength of probability
#     results.sort(key=lambda x: x[1], reverse=True)
#     return_list = []
#     for r in results:
#         return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
#     return return_list

# def getResponse(ints, intents_json):
#     tag = ints[0]['intent']
#     list_of_intents = intents_json['intents']
#     for i in list_of_intents:
#         if(i['tag']== tag):
#             result = random.choice(i['responses'])
#             break
#     return result

# def chatbot_response(msg):
#     ints = predict_class(msg, model)
#     res = getResponse(ints, intents)
#     return res

# =========================================================================================
# BAGIAN VARIABLE IMAGE/FOTO
bg1 = PhotoImage(file="templates/bg1.png")
bg2 = PhotoImage(file="templates/bg1.png")
bg3 = PhotoImage(file="templates/bg1.png")
foto1 = PhotoImage(file="static/image/mic-32x32.png")
foto2 = PhotoImage(file="static/image/keyboard-32x32.png")
foto3 = PhotoImage(file="static/image/send(1).png")
foto4 = PhotoImage(file="static/image/audio_wave-32x32.png")
foto5 = PhotoImage(file="static/image/silang-48x48.png")
# =========================================================================================
# BAGIAN FRAME 3, HALAMAN KETIKAN

# Frame layar ketikan
frame3 = tk.Frame(frame_body)
frame3.place(height=650, width=1200)

# frame3 layar ketikan
frame3_ketikan = tk.Frame(frame_body, bg = "#c9f1d0")
frame3_ketikan.place(y = 650, height=70, width=1200)

# sub-frame3 layar ketikan
subFrame3 = tk.Frame(frame3_ketikan, bg = "#c9f1d0")
subFrame3.pack(expand=True)
subFrame3.place(height=50, width=1180, y=10, x=10)

# canvas layar ketikan
canvas_frame3 = Canvas(frame3, width=1200, height=720, bg="gray94")
canvas_frame3.grid(row=0, column=0, columnspan=8)
canvas_frame3.place(x=10, y=10, width=1180, height=700)
label = Label(canvas_frame3)
w3 = Label(frame3, image=bg3).pack(side="right")

# layar ketikan
lk = Text(canvas_frame3, width=1200, height=720, bg="gray94")
lk.config(state=DISABLED)
lk.place(x=10, y=10, width=1180, height=700)

# scrollbar
scrollbar = Scrollbar(canvas_frame3, command=lk.yview, cursor="heart")
lk['yscrollcommand'] = scrollbar.set
scrollbar.place(x=376,y=6, height=700)

# layar entry & send button
# Entry
ketik = Entry(subFrame3, bd=3, width=26, font=("helvetica", 12))
ketik.configure(relief=FLAT)
ketik.grid(column=0, row=0)
ketik.place(x=60, y=7, width=1050, height=35)
ketik.focus()
ketik.insert(0,"")

# send button
send = Button(subFrame3, image=foto3, bg = "#c9f1d0")
send.grid(column=2, row=0)
send.place(x=1120,y=7, height=35, width=35)
send.configure(relief=FLAT)

# =========================================================================================
# # BAGIAN FRAME 2, HALAMAN SUARA

# # Frame layar suara
# frame2 = tk.Frame(frame_body)
# frame2.place(height=650, width=1200)

# # frame2 layar suara
# frame2_suara = tk.Frame(frame_body, bg = "#c9f1d0")
# frame2_suara.place(y = 610, height=110, width=1200)

# # sub-frame2 layar suara
# subFrame2 = tk.Frame(frame2_suara, bg = "#c9f1d0")
# subFrame2.pack(expand=True)
# subFrame2.place(height=90, width=1180, y=10, x=10)

# # layar suara
# canvas_frame2 = Canvas(frame2, width=1200, height=720, bg="gray94")
# canvas_frame2.grid(row=0, column=0, columnspan=8)
# canvas_frame2.place(x=10, y=10, width=1180, height=700)
# label = Label(canvas_frame2)
# w2 = Label(frame2, image=bg2).pack(side="right")

# # layar suara, mendengar, cancel
# # gambar
# label_suara = Label(subFrame2,image=foto4, bg="#c9f1d0")
# label_suara.grid(column=0, row=0)
# label_suara.place(x=600, y=7, width=35, height=35)

# # tulisan mendengar...
# label_dengar = Label(subFrame2,text="mendengar ....", font="inter 14 italic", bg="#c9f1d0")
# label_dengar.grid(column=1, row=0)
# label_dengar.place(x=530, y=45, width=175, height=35)

# # cancel
# cancel = Button(subFrame2, image=foto5,bg="#c9f1d0")
# cancel.place(x=1100, y=20, width=50, height=50)
# cancel.configure(relief=FLAT)

# =========================================================================================
# # BAGIAN FRAME 1, HALAMAN AWAL

# # frame layar chatbot
# frame1 = tk.Frame(frame_body)
# frame1.place(height=650, width=1200)

# # frame1 layar 2 tombol
# frame1_2tombol = tk.Frame(frame_body, bg = "#c9f1d0")
# frame1_2tombol.pack(expand=True)
# frame1_2tombol.place(y = 650, height=70, width=1200)

# # sub-frame1 layar 2 tombol
# subFrame1 = tk.Frame(frame1_2tombol, bg = "#c9f1d0")
# subFrame1.pack(expand=True)
# subFrame1.place(height=50, width=1180, y=10, x=10)

# # layar chatbot
# canvas_frame1 = Canvas(frame1, width=1200, height=720, bg="gray94")
# canvas_frame1.grid(row=0, column=0, columnspan=8)
# canvas_frame1.place(x=10, y=10, width=1180, height=700)
# label = Label(canvas_frame1)
# w1 = Label(frame1, image=bg1).pack(side="right")
# # ---------------------------------------------------
# # layar 2 widget (suara & ketikan)
# suara = Button(subFrame1, image=foto2, command=lambda: navigasi_frame(frame3), bg = "#c9f1d0")
# suara.grid(column=0, row=0, padx=70.53)
# suara.place(x = 650, height=50, width=50)
# suara.configure(relief=FLAT)

# ketikan = Button(subFrame1, image=foto1, command=lambda: navigasi_frame(frame2), bg = "#c9f1d0")
# ketikan.grid(column=1, row=0)
# ketikan.place(x=500, height=50, width=50)
# ketikan.configure(relief=FLAT)
# =========================================================================================

aplikasi.mainloop() # --> supaya bisa running


# AKHIR GUI APLIKASI
# ================================================================================================================================================================================================================================