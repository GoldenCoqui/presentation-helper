import tkinter as tk
from llm_script import llm_advice 
from tkinter.ttk import *
from tkinter import *
from speech_to_text import speech_text

# Function to handle button click event

def on_submit(user_data, transcript_label, helper_label):

    speech_text()
    llm_advice(user_data)

    with open(user_data, 'r') as file:
        user_input = file.read()
    
    transcript_label.config(text=f"Transcript:\n\n{user_input}")  # Update user input label
    # print(f"User Desired Cards in {output}")


    with open("../data/processed/helper_advice.txt", 'r') as file:
        helper_advice = file.read()
    
    helper_label.config(text=f"Advice:\n\n{helper_advice}")  # Update user input label    


def gui_maker(user_data):

    # Create the main application window
    app = tk.Tk()
    app.title("Presentation Helper")

    # Sets the window size to 800 pixels wide and 600 pixels high
    app.geometry("800x600")  

    # Set the application icon using wm_iconbitmap
    favicon = PhotoImage(file = "../data/img/cursor.png")
    app.iconphoto(False, favicon)


    # Create frames for layout
    output_frame = tk.Frame(app)
    output_frame.pack(fill=tk.X)  # Stretch output frame horizontally


    # Create a button widget
    button = tk.Button(
        output_frame, text="Start Helper", width=80, height=10, font=100, background="lightblue", command=lambda: on_submit(user_data, transcript_label, helper_label)
        )
    button.pack()


    # Labels for displaying user input, cardkingdom output, and future finder output
    transcript_label = tk.Label(output_frame, text="")
    transcript_label.pack(side=tk.LEFT)

    helper_label = tk.Label(output_frame, text="")
    helper_label.pack(side=tk.LEFT)



    # Run the application
    app.mainloop()
