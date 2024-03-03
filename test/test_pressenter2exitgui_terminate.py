from time import sleep

from pressenter2exit import PressEnter2ExitGUI, __application_name__


def test_pressenter2exitgui():
    exit_control = PressEnter2ExitGUI(title=__application_name__)
    sleep(4)
    exit_control.terminate()
    exit_control.join()
    assert not exit_control.is_alive()
