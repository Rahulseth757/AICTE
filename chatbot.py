#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
import random
import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define pairs of input and output patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you!",]
    ],
    [
        r"what is your name?",
        ["I'm ChatBot, how can I assist you today?",]
    ],
    [
        r"Hi?",
        ["Hello Sir... Welocme to the everchanging chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, so I don't have feelings, but thanks for asking!",]
    ],
    [
        r"(.*) (good|well)",
        ["That's great to hear!",]
    ],
    [
        r"(.*) (bad|not good|unwell)",
        ["I'm sorry to hear that. How can I help you feel better?",]
    ],
    [
        r"(.*) (help|assist|support)",
        ["I can help you with various tasks. Just let me know what you need assistance with.",]
    ],
    [
        r"tell me a joke",
        ["Why did the computer keep freezing? Because it left its Windows open!",]
    ],
    [
        r"who created you?",
        ["I was created by a team of developers using Python programming and cibc bca 1st sem student.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.", "Goodbye!"]
    ],
    [
        r"what is education",
        ["the teaching or training of people.",]
    ],
    [
        r"what is python programming",
        ["Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."]
    ],
    [
        r"what is coding",
        ["Coding tells a machine which actions to perform and how to complete tasks."]
    ],
    [
        r"tell me a fun fact",
        ["Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",]
    ],
    [
        r"what's the weather like today?",
        ["I'm sorry, I don't have access to real-time data. You can check the weather on a weather website or app for accurate information.",]
    ],
    [
        r"(.*) (love|like) you",
        ["Thank you! I'm just a computer program, but I appreciate the sentiment.",]
    ],
    [
        r"(.*) (hate|dislike) you",
        ["I'm sorry to hear that. Is there anything specific I can do to improve your experience with me?",]
    ],
    [
        r"where do you live?",
        ["I exist in the digital world, so I don't have a physical location. I'm here to assist you online.",]
    ],
    [
        r"what can you do?",
        ["I can answer questions, tell jokes, provide information, and more. Feel free to ask me anything!",]
    ],
    [
        r"who is the President of the United States?",
        ["The President of the United States is joe biden.",]
    ],
    [
        r"what is the capital of France?",
        ["The capital of France is Paris.",]
    ],
    [
        r"what is the largest planet in our solar system?",
        ["The largest planet in our solar system is Jupiter.",]
    ],
    [
        r"who wrote the play 'Romeo and Juliet'?",
        ["'Romeo and Juliet' was written by William Shakespeare.",]
    ],
    [
        r"what is the boiling point of water?",
        ["The boiling point of water at standard atmospheric pressure is 100 degrees Celsius (212 degrees Fahrenheit).",]
    ],
    [
        r"what is the currency of Japan?",
        ["The currency of Japan is the Japanese Yen (JPY).",]
    ],
    [
        r"who discovered electricity?",
        ["Electricity was not discovered by a single person; it's a natural phenomenon. However, many scientists contributed to our understanding of electricity, including Benjamin Franklin and Michael Faraday.",]
    ],
    [
        r"What is the capital of India?",
        ["The capital of India is New Delhi.",]
    ],
    [
        r"What is the largest state in India?",
        ["The largest state in India is Rajasthan.",]
    ],
    [
        r"What is the national bird of India?",
        ["The national bird of India is the Indian Peafowl, also known as the Peacock.",]
    ],
    [
        r"What is the national flower of India?",
        ["The national flower of India is the Lotus.",]
    ],
    [
        r"What is the currency of India?",
        ["The currency of India is the Indian Rupee (INR).",]
    ],
    [
        r"Who is the Father of the Nation in India?",
        ["The Father of the Nation in India is Mahatma Gandhi.",]
    ],
    [
        r"What is the highest mountain in India?",
        ["The highest mountain in India is Kangchenjunga, which is also the third-highest peak in the world.",]
    ],
    [
        r"Tell me an interesting fact about India",
        ["India is the world's largest democracy and has a rich cultural heritage with over 2,000 distinct ethnic groups and more than 1,600 languages spoken.",]
    ],
    [
        r".*",
        ["I didn't understand that. Can you please rephrase your question?",]
    ]
]

# Create a chatbot
chat = Chat(pairs, reflections)

def send_message():
    message = entry.get()
    if message.startswith("calculate"):
        calculate()
    else:
        response = chat.respond(message)
        chatbox.configure(state='normal')  # Enable the chatbox for editing
        chatbox.insert(tk.END, "\nUser: " + message)
        chatbox.insert(tk.END, "\nChatBot: " + response, "bold")
        chatbox.configure(state='disabled')  # Disable the chatbox for editing
    entry.delete(0, tk.END)

# Exit command
    if message.lower() in [ "exit", "close"]:
            close_application()
    entry.delete(0, tk.END)

def close_application():
    window.destroy()
    
# Create the main window
window = tk.Tk()
window.title("Chatbot Interface")

# Create the chatbox
chatbox = tk.Text(window, height=20, width=50)
chatbox.pack()
chatbox.configure(state='disabled')  # Set the chatbox as read-only

# Create the entry field for the user's input
entry = tk.Entry(window, width=50)
entry.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Link the send button with Enter
def send_message_from_enter(event):
    send_message()

entry.bind("<Return>", send_message_from_enter)

# Create a calculator
def calculate():
    expression = entry.get().split("calculate ", 1)[1]
    try:
        result = str(eval(expression))
        chatbox.configure(state='normal')  # Enable the chatbox for editingp
        chatbox.insert(tk.END, "\nUser: calculate " + expression)
        chatbox.insert(tk.END, "\nChatBot: " + result)
        chatbox.configure(state='disabled')  # Disable the chatbox for editing
    except Exception as e:
        chatbox.configure(state='normal')  # Enable the chatbox for editing
        chatbox.insert(tk.END, "\nUser: calculate " + expression)
        chatbox.insert(tk.END, "\nChatBot: Invalid expression")
        chatbox.configure(state='disabled')  # Disable the chatbox for editing

    entry.delete(0, tk.END)
    
     # Add tokenization in chatbot

import nltk
from nltk.tokenize import word_tokenize

# Tokenize user input
user_input = "Hello, how are you?"
tokens = word_tokenize(user_input)
print(tokens)  # Output: ['Hello', ',', 'how', 'are', 'you', '?']

     # Add POS tagging
import nltk
from nltk.tokenize import word_tokenize

# POS tagging
tokens = word_tokenize("I love cats")
tagged = nltk.pos_tag(tokens)
print(tagged)  # Output: [('I', 'PRP'), ('love', 'VBP'), ('cats', 'NNS')]

     # Add NER(Named Entity Recognition)
import nltk
from nltk.tokenize import word_tokenize

# NER
tokens = word_tokenize("I live in New York")
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)
print(entities)  # Output: (S (GPE I/PRP) live/VBP in/IN (GPE New/NNP York/NNP))

# Start the chatbot interface
window.mainloop()


# In[ ]:




