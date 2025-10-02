import tkinter as tk
import time
class TypeTestingLogic():
    def __init__(self):
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False
        self.start_time = None

        # Track all typing activity
        self.total_chars_typed = 0
        self.correct_chars = 0
        self.incorrect_chars = 0
        self.backspaces = 0



    def reset_stats(self):
        # Reset the Stats
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False
        self.start_time = None

        
        self.total_chars_typed = 0    
        self.correct_chars = 0          
        self.incorrect_chars = 0       
        self.backspaces = 0             
    
    def start_test(self):
        self.is_active = True
        self.start_time = time.time()


    def calculate_wpm(self, user_input):
        """Calculate Words Per Minute based on current input """
        if not self.start_time or not user_input.strip():
            return 0
        
        elapsed_time = (time.time() - self.start_time) / 60
        if elapsed_time == 0:
            return 0
        

        characters_typed = len(user_input)
        words_typed = characters_typed / 5

        return int(words_typed / elapsed_time)

    def track_keystroke(self, event, current_text, target_text):
        """Track individual keystrokes for accurate statistics"""
        if not self.is_active:
            return
            
        key = event.keysym

        if key == 'BackSpace':
            self.backspaces += 1
            self.total_chars_typed += 1
        elif len(key) == 1:  
            self.total_chars_typed += 1
         
            cursor_pos = len(current_text) - 1  
            
            if cursor_pos >= 0 and cursor_pos < len(target_text) and current_text[cursor_pos] == target_text[cursor_pos]:
                self.correct_chars += 1
            else:
                self.incorrect_chars += 1


    def calculate_accuracy(self):
        """Calculate accuracy based on all keystrokes"""
        if self.total_chars_typed == 0:
            return 100.0
        
        # Don't count backspaces in accuracy calculation
        actual_typing_chars = self.total_chars_typed - self.backspaces
        if actual_typing_chars == 0:
            return 100.0
        
        accuracy = (self.correct_chars / actual_typing_chars) * 100
        return round(accuracy, 1)
        

    def update_live_stats(self, user_input, target_text):
        if self.is_active:
           self.words_per_min =  self.calculate_wpm(user_input)
           self.accuracy = self.calculate_accuracy()



    def end_test(self):
        self.is_active = False


    def get_detailed_stats(self):
        """Return detailed statistics for end-of-test summary"""
        return {
            'wpm': self.words_per_min,
            'accuracy': self.accuracy,
            'total_keystrokes': self.total_chars_typed,
            'correct_keystrokes': self.correct_chars,
            'incorrect_keystrokes': self.incorrect_chars,
            'backspaces': self.backspaces
        }