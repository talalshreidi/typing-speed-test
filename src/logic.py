import tkinter as tk

class TypeTestingLogic():
    def __init__(self):
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False



    def reset_stats(self):
        # Reset the Stats
        self.words_per_min = 0
        self.accuracy = 100
        self.time_left = 60
        self.is_active = False
    
    def start_test(self):
        self.is_active = True


    def end_test(self):
        self.is_active = False