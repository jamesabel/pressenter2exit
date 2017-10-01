
from time import time, sleep

from pressenter2exit import PressEnter2Exit

exit_control = PressEnter2Exit()

# optional, but makes sure things are on separate lines
sleep(0.1)
print()
sleep(0.1)

start_time = time()

# loops until return is pressed or we reach the end of our run time
while exit_control.is_alive() and time() - start_time < 20.0:
    print("I've been waiting for %f seconds." % (time() - start_time))
    exit_control.join(4.0)  # use join() instead of time.sleep() to ensure an immediate exit

print('Done! Exiting after %f seconds.' % (time() - start_time))
print('Time from start to exit was %f seconds' % exit_control.get_duration())
print('Time from start to enter pressed was %s seconds' % str(exit_control.get_enter_duration()))  # can be None
print('Reaction time was %f seconds' % exit_control.get_reaction_time())
