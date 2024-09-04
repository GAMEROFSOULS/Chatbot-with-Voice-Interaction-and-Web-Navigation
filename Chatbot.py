import tkinter as tk
import pyttsx3
import speech_recognition as sr
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for speech-to-text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, my speech service is down."

# Chatbot response logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm a simple Python chatbot."

    # Opening websites
    elif "open google" in user_input:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    elif "open linkedin" in user_input:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn"
    elif "open github" in user_input:
        webbrowser.open("https://www.github.com")
        return "Opening GitHub"
    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    else:
        return "I'm sorry, I don't understand that."

# Function to handle sending messages
def send_message():
    user_message = entry_box.get("1.0", "end-1c").strip()
    if user_message:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_message + "\n\n")
        response = chatbot_response(user_message)
        chat_log.insert(tk.END, "Bot: " + response + "\n\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)
        entry_box.delete("1.0", tk.END)
        speak(response)

# Function to handle voice input
def voice_input():
    user_message = listen()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_message + "\n\n")
    response = chatbot_response(user_message)
    chat_log.insert(tk.END, "Bot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    speak(response)

# GUI Setup
root = tk.Tk()
root.title("Chatbot with Voice Interaction and Web Navigation")
root.geometry("400x600")

# Chat Log
chat_log = tk.Text(root, bd=1, bg="white", height="8", width="50", font="Arial",)
chat_log.config(state=tk.DISABLED)
chat_log.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=chat_log.yview, cursor="heart")
chat_log['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Entry Box
entry_box = tk.Text(root, bd=0, bg="white", width="29", height="5", font="Arial")
entry_box.pack(pady=10)

# Send Button
send_button = tk.Button(root, text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=send_message)
send_button.pack()

# Voice Button
voice_button = tk.Button(root, text="Speak", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff', command=voice_input)
voice_button.pack()

root.mainloop()
