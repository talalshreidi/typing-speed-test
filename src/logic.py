import tkinter as tk
import time
class TypeTestingLogic():
    def __init__(self):
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False
        self.start_time = None



    def reset_stats(self):
        # Reset the Stats
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False
        self.start_time = None
    
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



    def calculate_accuracy(self, target_text, user_input):
        """
        Calculates the typing accuracy based on target text and user input.

        Args:
            target_text (str): The text the user was supposed to type.
            user_input (str): The actual text entered by the user.

        Returns:
            float: The typing accuracy as a percentage.
        """
        if not user_input or not target_text:
            return 100.0

        correct_chars = 0
        total_chars = min(len(user_input), len(target_text))

        for i in range(total_chars):
            if target_text[i] == user_input[i]:
                correct_chars += 1

        if len(target_text) == 0:
            return 0.0
        else:
            return round((correct_chars / len(user_input)) * 100, 1)
        

    def update_live_stats(self, user_input, target_text):
        if self.is_active:
           self.words_per_min =  self.calculate_wpm(user_input)
           self.accuracy = self.calculate_accuracy(target_text, user_input)



    def end_test(self):
        self.is_active = False