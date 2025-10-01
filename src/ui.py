import tkinter as tk
from config import FONT_MAIN, BG_COLOR, TEXT_COLOR
from passages import TypingTestPassages
from controller import TypeTestingController
from logic import TypeTestingLogic

class TypingTestUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test - Talal Shreidi")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")

        # Connecting the Logic

        self.passages = TypingTestPassages()
        self.logic = TypeTestingLogic()
        self.controller = TypeTestingController(self, self.logic, self.passages)


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
        self.passage_text = tk.Label(self.top_frame, text="Press start to get a passage.", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.passage_text.pack(pady=5)

        # Typing Area

        self.text_area = tk.Text(self.middle_frame, height=10, font=FONT_MAIN, wrap=tk.WORD)
        self.text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Status Bar
        self.status_label = tk.Label(self.bottom_frame, text=f"Timer: {self.logic.time_left} | WPM: {self.logic.words_per_min} | Accuracy: {self.logic.accuracy}%", font=FONT_MAIN, bg=BG_COLOR, fg=TEXT_COLOR)
        self.status_label.pack(pady=10)

        # Control Buttons
        self.nested_control_frame = tk.Frame(self.control_frame, bg=BG_COLOR)
        self.nested_control_frame.pack()

        self.start_button = tk.Button(self.nested_control_frame, text="Start Test", font=FONT_MAIN, command=self.controller.start_test)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")
        self.reset_button = tk.Button(self.nested_control_frame, text="Reset", font=FONT_MAIN, command=self.controller.reset_test)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")
        self.change_passage_button = tk.Button(self.nested_control_frame, text="Change Passage", font=FONT_MAIN, command=self.change_passage)
        self.change_passage_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="center")

    def change_passage(self):
        self.passages.get_passage()
        self.passage_text.config(text=self.passages.get_passage())
    
    def reset_passage_text(self):
        self.passage_text.config(text="Press start to get a passage.")

    def clear_typing_box(self):
        self.text_area.delete('1.0', tk.END)

    def update_status_text(self):
        self.status_label.config(text=f"Timer: {self.logic.time_left} | WPM: {self.logic.words_per_min} | Accuracy: {self.logic.accuracy}%")

    
            