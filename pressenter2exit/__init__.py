
import time
import threading

__version__ = '0.0.7'


class PressEnter2Exit(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.start_time = time.time()
        self.end_time = None
        self.start()

    def run(self):
        input('Press enter to exit:')
        self.end_time = time.time()

    def get_runtime(self):
        """
        returns run time in seconds
        :return: run time in seconds
        """
        if self.end_time is None:
            self.end_time = time.time()
        return self.end_time - self.start_time
