
import threading


class PressEnter2Exit(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.start()

    def run(self):
        input('Press enter to exit:')
