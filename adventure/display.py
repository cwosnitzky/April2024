import os
import sys
from time import sleep
import random


class Display:

    def __init__(self, slow_text=True):
        self.slow_text = slow_text

    def text(self, text):
        if not self.slow_text:
            print(f'{text}\n')
            return

        for char in text:
            if char != '\n':
                sleep_time = random.uniform(0.05, 0.15)
            else:
                sleep_time = .5
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(sleep_time)
        print()

    @staticmethod
    def title(title: str):
        sys.stdout.write(title)

    @staticmethod
    def clear():
        os.system('cls')
