import random
class TypingTestPassages():
    def __init__(self):
        self.passages = [
            "The quick brown fox jumps over the lazy dog.",
            "Pack my box with five dozen liquor jugs.",
            "How vexingly quick daft zebras jump!"
        ]
        self.current_index_on = 0

    def get_passage(self):
        self.current_index = random.randint(0, 2)
        self.current_index_on = self.current_index
        return self.passages[self.current_index]

    def get_current_passage(self):
        return self.passages[self.current_index_on]