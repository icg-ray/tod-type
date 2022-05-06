from prompts import *
import random
from difflib import SequenceMatcher


class Model:
    def __init__(self):
        self.prompt = None
        self.prompt_length = 0

    def generate_prompt(self):
        self.prompt = ' '.join(random.choices(prompts, k=3))
        self.prompt_length = len(self.prompt.split(' '))
        return self.prompt

    def calculate_wpm(self, answer, time):
        accuracy = SequenceMatcher(None, answer, self.prompt).ratio()
        raw_wpm = round(len(self.prompt.split(' ')) / (time / 60))
        wpm = round(raw_wpm * accuracy)
        return wpm
