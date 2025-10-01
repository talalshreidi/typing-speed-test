import tkinter as tk
from config import FONT_MAIN, BG_COLOR, TEXT_COLOR

class TypingTestUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test - Talal Shreidi")
        self.geometry("800x400")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self.setup_ui()


    def setup_ui(self):

        # We will organize the UI components in three frames, TOP , MIDDLE, BOTTOM

        self.top_frame = tk.Frame(self, bg=BG_COLOR)
        self.top_frame.pack(fill=tk.X)

        self.middle_frame = tk.Frame(self, bg=BG_COLOR)
        self.middle_frame.pack(fill=tk.BOTH, expand=True)

        self.bottom_frame = tk.Frame(self, bg=BG_COLOR)
        self.bottom_frame.pack(fill=tk.X)


        # Passage Display
        self.passage_label = tk.Label(self.top_frame, text="Type the following passage:", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.passage_label.pack(pady=10)
        self.passage_text = tk.Label(self.top_frame, text="The quick brown fox jumps over the lazy dog.", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.passage_text.pack(pady=5)
