
import time
import threading

__version__ = '0.0.8'


class PressEnter2Exit(threading.Thread):
    """
    Press Enter to Exit class.
    """
    def __init__(self):
        super().__init__(daemon=True)
        self.start_time = time.time()
        self.exit_time = None
        self.start()

    def run(self):
        input('Press enter to exit:')
        self.exit_time = time.time()

    def get_start_time(self):
        """
        get time of instantiation (in seconds since epoch)
        :return: time of instantiation (in seconds since epoch)
        """
        return self.start_time

    def get_enter_duration(self):
        """
        time from instantiation to when enter was pressed
        :return: time from instantiation to when enter was pressed or None if enter not yet pressed (in seconds)
        """
        if self.exit_time is None:
            return None
        return self.exit_time - self.start_time

    def get_duration(self):
        """
        time since instantiation
        :return: time since instantiation (in seconds)
        """
        return time.time() - self.start_time

    def get_reaction_time(self):
        """
        get how long it too the program that uses this class to react to the pressing of enter
        :return: the time from when enter was pressed to now (in seconds)
        """
        if self.exit_time is None:
            # enter was never hit, so our reaction time is zero
            return 0.0
        return time.time() - self.exit_time
