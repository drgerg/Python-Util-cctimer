#!/usr/bin/env python3
#
# cctimer.py
# Codelette Countdown Timer Fun.
#
# Casspop Codelette: A short, useful, educational utility.
#
#     Copyright (c) 2006,2020 - Gregory Allen Sanders.

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
""" This little timer codelette is useful for general purpose countdown timing uses.  It has limitations (what doesn't?).
    It relies on time.sleep(), which means the 1-second sleep time is tacked on after whatever amount of time your system
    requires to run the other lines of code.  What that means is that the actual amount of time between ticks is a tee-tiny
    little bit more than 1 second.  So you wouldn't want to rely on this utility for uses where split-second accuracy is critical.
"""
## The import line gets run all the time.
import time, os, logging
#
## BETWEEN HERE AND 'BELOW HERE' are the 'def'ined functions that can be run
##  when you import cctimer as a module in another program. In this .py file, there is only one.
#
def timer(duration, dotNum, threadStop): ## this function can be used in a threaded function as part of a  
    logger = logging.getLogger(__name__) ## while loop to stop the loop and exit the thread.
    starttime = time.time()
    dur = duration
    logging.info("Variable 'duration' == " + str(duration) + "; Variable 'dur' == " + str(dur))
    logging.debug("Main() started with a parameter of : " + str(dur) + ", threadStop = " + str(threadStop))
    while time.time() - starttime < dur and threadStop == False:
        print('The boolean for threadstop is: \033[1;32m' + str(threadStop) + '\033[0;0m\n')
        for i in range(dur):
            if dotNum == "N":
                print("\033[F\033[1;34m" + str(dur-i) + "     ")
            else:
                print("\033[F\033[K\033[1;31m" + "." * (i+1))
            time.sleep(1)
    else:
        timerReturn = "done"
        threadStop = True
        print('\033[0;0mThe boolean for threadstop is: \033[1;31m' + str(threadStop) + "\033[0;0m")
        logger.info("The timer returned: " + timerReturn + ". ThreadStop is " + str(threadStop))
        return timerReturn, threadStop
#
##  BELOW HERE is the code that supports running this as a command line application.
#
if __name__=="__main__":    ## It all starts with this line.
    try:
        import argparse
        global threadStop
        threadStop = False
## Command line arguments parsing
#
        cctimerHome = os.getcwd()
        parsertmr = argparse.ArgumentParser()
        parsertmr.add_argument("-d", "--debug", help="Turn on debugging output to stderr", action="store_true")
        parsertmr.add_argument("-n", "--nums", help="Print countdown numbers rather than the progress dots.", action="store_true")
        parsertmr.add_argument("-s", "--seconds", type=int, metavar='N', default=0, help="How long (in seconds) this timer should run before exiting and returning 'done'.")
        parsertmr.add_argument("-dd", "--ddebug", help="Turn on Deep Debugging output to log file.", action="store_true")
        argstmr = parsertmr.parse_args()
        if argstmr.debug:
            logging.basicConfig(filename= cctimerHome + '/cctimer.log', format='[%(name)s]:%(levelname)s: %(message)s. - %(asctime)s', datefmt='%D %H:%M:%S', level=logging.DEBUG)
            logging.info("ohdtimer.py started with debugging output enabled")
        else:
            logging.basicConfig(filename= cctimerHome + '/cctimer.log', format='%(asctime)s - %(message)s.', datefmt='%a, %d %b %Y %H:%M:%S', level=logging.INFO)
        if argstmr.seconds:
            duration = argstmr.seconds
            print("\ncctimer.py started with a duration value of " + str(duration) + ' seconds.')
            logging.debug("End of config section.  duration == " + str(duration))
## End Command line arguments parsing
        if argstmr.nums:
            dotNum = "N"
        elif argstmr.seconds:
            dotNum = None
        else:
            print("\nNo length of time given to count down. Try ./cctimer.py --help \n")
            dotNum = None
            duration = 0
        timer(duration, dotNum, threadStop)
    except:
        pass
                

