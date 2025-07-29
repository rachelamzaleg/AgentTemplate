from ollama import chat
import tkinter as tk
from tkinter import scrolledtext

message_list=[]
def send_message():
    user_text = user_input.get()
    message_list.append(f'You:{user_text}')
    response = chat(model='deepseek-coder:latest', messages=[
        {
            "role": "user",
            "content": user_text
        }
    ])
    message_list.append(f'Bot:{response["message"]["content"]  }')
    scroll_area.insert(tk.END,f'You: {user_text}\n')
    scroll_area.insert(tk.END, f"Bot: {response['message']['content']}\n")
    

root = tk.Tk()
user_input = tk.Entry(width=50)
user_input.pack(padx=10, pady=10)
send_button =tk.Button(text="Send",command=send_message)
send_button.pack(padx=10, pady=10)
scroll_area = scrolledtext.ScrolledText(width=50, height=20,wrap=tk.WORD)
scroll_area.pack(padx=10, pady=10)
mainloop = root.mainloop()



