import tkinter as tk

class TypeTestingController():
    def __init__(self, ui, logic, passages):
        self.ui = ui
        self.logic = logic
        self.passages = passages
        self.timer_id = None

    def start_test(self):
        self.ui.clear_typing_box()
        self.logic.reset_stats()
        self.countdown()

    def reset_test(self):
        self.logic.reset_stats()
        self.ui.clear_typing_box()
        self.stop_timer()

    def stop_timer(self):
        if self.timer_id:
            self.ui.after_cancel(self.timer_id)
            self.timer_id = None
            self.ui.start_button.config(state=tk.NORMAL)
            self.ui.update_status_text()

    def countdown(self):
        if self.logic.time_left > 0:
            self.ui.start_button.config(state=tk.DISABLED)
            self.logic.time_left -= 1
            self.ui.update_status_text()
            self.timer_id = self.ui.after(1000, func=self.countdown)
        else:
            self.ui.start_button.config(state=tk.NORMAL)
            self.logic.end_test()