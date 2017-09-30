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
