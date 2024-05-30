import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from keras.models import load_model
import json
import random
import time
import string
from io import BytesIO
import tensorflow as tf
import IPython.display as ipd
import pandas as pd
from tensorflow.keras.models import Model
from keras.utils.vis_utils import plot_model
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, LSTM
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Flatten, Dense, GlobalMaxPool1D
# untuk GUI tkinter
from tkinter import *
import tkinter

# ================================================================================================================================================================================================================================
# --- variable untuk model chatbot ---
model = load_model('model/chat_model.h5')
intents = json.load(open('dataset/intents.json').read())
words = pickle.load(open('model/words.pkl','rb'))
classes = pickle.load(open('model/classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

def send():
    msg = ketik.get("1.0",'end-1c').strip()
    ketik.delete("0.0",END)

    if msg != '':
        chatlog.config(state=NORMAL)
        chatlog.insert(END, "You: " + msg + '\n\n')
        chatlog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        chatlog.insert(END, "Bot: " + res + '\n\n')

        chatlog.config(state=DISABLED)
        chatlog.yview(END)


# ================================================================================================================================================================================================================================


# ================================================================================================================================================================================================================================
# AWAL GUI APLIKASI
aplikasi = Tk()
aplikasi.resizable(False,False) # agar aplikasi tidak bisa di maximize/minimize
aplikasi.title("CareBot")
aplikasi.geometry("1200x720+160+40") # --> # ("lebar aplikasinya + posisi x + posisi y") ukuran aplikasi setelah running
logo = PhotoImage(file="templates/logo2.png")
aplikasi.iconphoto(True,logo)
# =========================================================================================
# BAGIAN VARIABLE IMAGE/FOTO
bg1 = PhotoImage(file="templates/bg1.png")
bg2 = PhotoImage(file="templates/bg1.png")
bg3 = PhotoImage(file="templates/bg1.png")
# foto1 = PhotoImage(file="static/image/mic-32x32.png")
# foto2 = PhotoImage(file="static/image/keyboard-32x32.png")
foto3 = PhotoImage(file="static/image/send(1).png")
# foto4 = PhotoImage(file="static/image/audio_wave-32x32.png")
# foto5 = PhotoImage(file="static/image/silang-48x48.png")

# =========================================================================================
# frame chat
frame_chat = Frame(aplikasi)
frame_chat.place(height=720, width=1200)

# =========================================================================================
# layar chat
chatlog = Text(frame_chat, width=1200, height=720)
chatlog.config(state=DISABLED,relief=FLAT)
chatlog.place(x=10, y=10, width=1180, height=700)
w1 = Label(chatlog, image=bg3).pack(side="right")

# frame3 layar ketikan
frame3_ketikan = Frame(frame_chat, bg = "#c9f1d0")
frame3_ketikan.place(y = 650, height=70, width=1200)

# sub-frame3 layar ketikan
subFrame3 = Frame(frame3_ketikan, bg = "#c9f1d0")
subFrame3.pack(expand=True)
subFrame3.place(height=50, width=1180, y=10, x=10)

# scrollbar
scrollbar = Scrollbar(chatlog, command=chatlog.yview, cursor="heart")
chatlog['yscrollcommand'] = scrollbar.set
scrollbar.place(x=1150,height=620,y=10)

# layar entry & send button
# Entry
ketik = Entry(subFrame3, bd=3, width=26, font=("helvetica", 12))
ketik.configure(relief=FLAT)
ketik.grid(column=0, row=0)
ketik.place(x=60, y=7, width=1050, height=35)
ketik.focus()
ketik.insert(0,"")

# send button
kirim = Button(subFrame3, image=foto3, bg = "#c9f1d0", command = send)
kirim.grid(column=2, row=0)
kirim.place(x=1120,y=7, height=35, width=35)
kirim.configure(relief=FLAT)

aplikasi.mainloop() # --> supaya bisa running
# AKHIR GUI APLIKASI
# ================================================================================================================================================================================================================================