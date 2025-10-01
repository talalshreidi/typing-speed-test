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


        self.logic.update_live_stats(user_input, target_text)

        self.ui.update_status_text()

        for i in range(min(len(user_input), len(target_text))):
            start_pos = f"1.{i}"
            end_pos = f"1.{i+1}"
            
            if user_input[i] == target_text[i]:
                self.ui.text_area.tag_add("correct", start_pos, end_pos)
            else:
                self.ui.text_area.tag_add("incorrect", start_pos, end_pos)

        # Configure tag styles
        self.ui.text_area.tag_configure("correct", foreground="green")
        self.ui.text_area.tag_configure("incorrect", foreground="red", background="lightcoral")


    def countdown(self):
        if self.logic.time_left > 0:
            self.ui.set_test_state("running")
            self.logic.time_left -= 1
            self.ui.update_status_text()
            self.timer_id = self.ui.after(1000, func=self.countdown)
        else:
            self.ui.set_test_state("stopped")
            self.logic.end_test()