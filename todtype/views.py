import tkinter as tk
from tkinter import ttk
import constants as c


class View(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(c.TITLE)
        self._create_frame()

    def main(self):
        self.mainloop()

    def _create_frame(self):
        frame = ttk.Frame(self)
        frame.config()
        frame.pack(padx=c.FRAME_PAD, pady=c.FRAME_PAD)

        # title
        label_title = ttk.Label(frame, text=c.TITLE)
        label_title.config(font=c.TITLE_FONT)
        label_title.pack(padx=c.PAD, pady=c.PAD)

        # instructions
        self.label_instructions = ttk.Label(frame, text="press [space] when done")
        self.label_instructions.config(font=c.FONT)
        self.label_instructions.pack(padx=c.PAD, pady=c.PAD)

        # prompt
        self.label_prompt = ttk.Label(frame, text="example prompt")
        self.label_prompt.config(font=c.FONT, wraplength=c.WRAPLENGTH)
        self.label_prompt.pack(padx=c.PAD, pady=c.PAD)

        # answer
        self.answer = tk.Text(frame)
        self.answer.config(font=c.FONT, width=c.ANSWER_WIDTH, height=c.ANSWER_HEIGHT, wrap=tk.WORD)
        self.answer.pack(padx=c.PAD, pady=c.PAD)

    def update_prompt(self, prompt):
        self.label_prompt.config(text=prompt)

    def get_answer(self):
        return self.answer.get('1.0', 'end')

    def complete_test(self, wpm):
        self.answer.pack_forget()
        self.label_instructions.config(text="Test completed.")
        self.label_prompt.config(text=f'WPM: {wpm}')
