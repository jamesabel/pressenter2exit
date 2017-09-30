# pressenter2exit (Press Enter To Exit) #

pressenter2exit ("Press Enter To Exit") facilitates long-running CLI programs to 
exit in clean and controlled way.

# The Problem #

Long running CLI (command line interface) programs can be useful, but there is often 
a need to exit them in a clean manner (as opposed to, for example, pressing ctrl-c).

## Examples ##

- Programs that 'crunch' on a large number of input data sets, but you want to be able 
to cleanly interrupt the processing after it's done with the current data set.
- Programs that run in an 'infinite loop' waiting for input data or files to appear.  You'd 
like to be able to exit the 'infinite loop' in a controlled way.

The benefit to exiting in a controlled way is that you don't end up with a data set 
partially processed and/or in an unknown state.  By using pressenter2exit, processing 
that has been done so far can be useful, and not merely thrown away which can happen if 
a program is forcefully and immediately aborted.

## Example Code ##

```python

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

```
