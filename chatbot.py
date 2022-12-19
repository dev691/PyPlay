import tkinter as tk

class ChatbotWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Chatbot")
        self.geometry("400x600")

        frame = tk.Frame(self)
        frame.pack(side="top", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        self.text_area = tk.Text(frame, yscrollcommand=scrollbar.set, state="disabled")
        self.text_area.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.text_area.yview)

        self.entry = tk.Entry(self, font=("Arial", 16))
        self.entry.pack(side="bottom", fill="x", pady=10)
        self.entry.focus_set()

        self.bind("<Return>", self.send_message)

    def send_message(self, event=None):

        message = self.entry.get()

        self.entry.delete(0, "end")
        self.text_area.config(state="normal")

        self.text_area.insert("end", "You: " + message + "\n", "user")
        self.text_area.insert("end", "Chatbot: " + self.generate_response(message) + "\n", "bot")

        self.text_area.config(state="disabled")
        self.text_area.yview(tk.END)

    def generate_response(self, message):
        responses = [
            "Hello Nishant!",
            "I am fine and you?",
            "don't be, its fine!",
            "Yaa! really happy to see you",
            " Sure! share the question with me",
            "glad.",
            "I'm sorry I didn't understand",
        ]

          # Check for certain keywords and return a corresponding response
        if "hello" in message.lower():
            return responses[0]
        elif "how are you" in message.lower():
            return responses[1]
        elif "i'm sorry" in message.lower():
            return responses[2]
        elif "clarify" in message.lower():
            return responses[3]
        elif "glad" in message.lower():
            return responses[4]
        else:
            return responses[5] # Return the default response    


if __name__ == "__main__":
    app = ChatbotWindow()
    app.mainloop()



