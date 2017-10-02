
import time
import threading

__version__ = '0.0.10'


class PressEnter2Exit(threading.Thread):
    """
    Press Enter to Exit class.  Facilitates exit of a Python CLI program in a controlled way.
    """
    def __init__(self, message='Enter pressed'):
        """

        :param message: message to be displayed after a enter hit (if None, no message is displayed).  Default is 'Enter pressed'
        """
        super().__init__(daemon=True)
        self.message = message
        self.start_time = time.time()
        self.exit_time = None
        self.start()

    def run(self):
        input('Press enter to exit:')
        if self.message:
            print(self.message)
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
        get how long it took the program that uses this class to react to the pressing of enter

        :return: the time from when enter was pressed to now (in seconds)
        """
        if self.exit_time is None:
            # enter was never hit, so our reaction time is zero
            return 0.0
        return time.time() - self.exit_time
