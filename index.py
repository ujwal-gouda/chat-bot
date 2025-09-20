import customtkinter as ctk
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from Gemini
def get_bot_response(prompt):
    if not prompt.strip():
        return ""
    response = model.generate_content(prompt)
    return response.text

# --- CustomTkinter setup ---
ctk.set_appearance_mode("dark")  # dark/light mode
ctk.set_default_color_theme("blue")  # accent color

app = ctk.CTk()
app.title("ChatBot")
app.geometry("400x650")

# Chat frame
chat_frame = ctk.CTkScrollableFrame(app, width=380, height=520, corner_radius=10)
chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

# List to hold chat messages
messages = []

# Function to update chat
def append_message(text, sender="bot"):
    # Frame for each message (so we can round & pad properly)
    msg_frame = ctk.CTkFrame(chat_frame, corner_radius=12, fg_color="#1f2937" if sender=="bot" else "#6366f1")
    msg_frame.pack(pady=4, padx=5, anchor="w" if sender=="bot" else "e")
    
    # Label inside frame
    msg_label = ctk.CTkLabel(msg_frame, text=text, wraplength=300, justify="left", text_color="white")
    msg_label.pack(padx=10, pady=6)  # padding inside bubble
    
    messages.append(msg_frame)
    chat_frame.update_idletasks()
    # chat_frame.yview_moveto(1.0)


# Function for send button
def send_message():
    user_text = input_box.get().strip()
    if user_text == "":
        return
    append_message(user_text, sender="user")
    input_box.delete(0, "end")
    
    # Get bot response
    bot_reply = get_bot_response(user_text)
    append_message(bot_reply, sender="bot")

# Input frame
input_frame = ctk.CTkFrame(app, height=50, corner_radius=10)
input_frame.pack(fill="x", padx=10, pady=10)

input_box = ctk.CTkEntry(input_frame, placeholder_text="Type a message...")
input_box.pack(side="left", fill="x", expand=True, padx=(5,5), pady=5)
input_box.bind("<Return>", lambda e: send_message())

send_btn = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_btn.pack(side="right", padx=(0,5), pady=5)

app.mainloop()
