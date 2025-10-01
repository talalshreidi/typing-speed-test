import tkinter as tk
from config import FONT_MAIN, BG_COLOR, TEXT_COLOR

class TypingTestUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test - Talal Shreidi")
        self.geometry("800x600")
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

        self.control_frame = tk.Frame(self, bg=BG_COLOR)
        self.control_frame.pack(fill=tk.X)


        # Passage Display
        self.passage_label = tk.Label(self.top_frame, text="Type the following passage:", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.passage_label.pack(pady=10)
        self.passage_text = tk.Label(self.top_frame, text="The quick brown fox jumps over the lazy dog.", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.passage_text.pack(pady=5)

        # Typing Area

        self.text_area = tk.Text(self.middle_frame, height=10, font=FONT_MAIN, wrap=tk.WORD)
        self.text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Status Bar
        self.status_label = tk.Label(self.bottom_frame, text="Timer: 60s | WPM: 0 | Accuracy: 100%", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.status_label.pack(pady=10)

        # Control Buttons
        
        self.nested_control_frame = tk.Frame(self.control_frame, bg=BG_COLOR)
        self.nested_control_frame.pack()

        self.start_button = tk.Button(self.nested_control_frame, text="Start Test", font=FONT_MAIN, command=self.start_test)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")
        self.reset_button = tk.Button(self.nested_control_frame, text="Reset", font=FONT_MAIN, command=self.reset_test)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")
        self.change_passage_button = tk.Button(self.nested_control_frame, text="Change Passage", font=FONT_MAIN, command=self.change_passage)
        self.change_passage_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")



    def start_test(self):
        pass
    def reset_test(self):
        pass
    def change_passage(self):
        pass