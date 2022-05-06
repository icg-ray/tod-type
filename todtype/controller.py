from models import Model
from views import View
import time


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.starttime = time.time()

    def main(self):
        self.view.after(50, self.check_completion)
        self.view.main()

    def new_prompt(self):
        prompts = self.model.generate_prompt()
        self.view.update_prompt(prompts)

    def check_completion(self):
        answer = self.view.get_answer()
        if len(answer.split(' ')) == self.model.prompt_length + 1:
            endtime = time.time()
            seconds = endtime - self.starttime
            wpm = self.model.calculate_wpm(answer, seconds)
            self.view.complete_test(wpm)
        else:
            self.view.after(50, self.check_completion)
