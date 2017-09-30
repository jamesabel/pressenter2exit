
from time import time

from pressenter2exit import PressEnter2Exit

exit_control = PressEnter2Exit()
print()  # optional, but without it the first print would be on the same line as the input

start_time = time()
# loops until return is pressed or we reach the end of our run time
while exit_control.is_alive() and time() - start_time < 20.0:
    print("I've been waiting for %f seconds." % (time() - start_time))
    exit_control.join(4.0)  # use join() instead of time.sleep() to ensure an immediate exit
print('Done! Exiting after %f seconds.' % (time() - start_time))
