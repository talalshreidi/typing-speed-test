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
        self.ui.change_passage()
        self.logic.start_test()
        self.countdown()

    def reset_test(self):
        self.logic.reset_stats()
        self.ui.clear_typing_box()
        self.stop_timer()
        self.ui.reset_passage_text()

    def stop_timer(self):
        if self.timer_id:
            self.ui.after_cancel(self.timer_id)
            self.timer_id = None
            self.ui.set_test_state("stopped")
            self.ui.update_status_text()


    def check_user_words(self, event):
        if not self.logic.is_active:
            return
        
        user_input = self.ui.text_area.get('1.0', tk.END).strip()
        target_text = self.passages.get_current_passage()

        for i in range(min(len(user_input), len(target_text))):
            if user_input[i] == target_text[i]:
                tag_name = f"char_{i}"
                color = "green"
                self.ui.text_area.tag_configure(tag_name, foreground=color)
                self.ui.text_area.tag_add(tag_name, f"1.0+{i}c")
            else:
                color = "red"
                self.ui.text_area.tag_configure(tag_name, foreground=color)
                self.ui.text_area.tag_add(tag_name, f"1.0+{i}c")


    def countdown(self):
        if self.logic.time_left > 0:
            self.ui.set_test_state("running")
            self.logic.time_left -= 1
            self.ui.update_status_text()
            self.timer_id = self.ui.after(1000, func=self.countdown)
        else:
            self.ui.set_test_state("stopped")
            self.logic.end_test()