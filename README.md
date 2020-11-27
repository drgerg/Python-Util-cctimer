# Python-Util-cctimer.py
Casspop Codelette: A short, useful, educational utility.  Countdown Timer Fun.

This is what I'm calling a codelette.  It's a little bit of code that does something, but has some value beyond that for learners like me.  (I don't know about you, but I'm always learning.  Always.)

"cctimer.py" stands for Codelette Countdown Timer.py, and is a command line utility that will do one of two things immediately:
 - it will tell you it needs more info if you don't provide any command line arguments
 - it will give you one of two visual countdowns based on the value you provide on the command line

There is nothing awe-inspiring about this codelette, but there is a lot that can be learned from it.
For example, in this tiny file, you'll find working examples of:
- logging: sends data to a file called cctimer.log. I like to use the command <code>tail -fn40 cctimer.log</code> in a terminal and watch it happen.
- command line arguments parsing. Type <code>./cctimer.py --help</code> for more info.
- provides a way to stop a threaded loop when called as an imported function.
- demonstrates how you can modify the output seen on the command line by use of ANSI escape codes. More on ANSI escape [here](https://stackoverflow.com/questions/17771287/python-octal-escape-character-033-from-a-dictionary-value-translates-in-a-prin).
- a fair example of a <code>try: except: Exception</code> section (way down at the bottom)

Maybe you'll find this useful in some way.  If so, wonderful.  If not, also wonderful.  

And as always, "It may not be pretty, but it works!"

Enjoy it like this:<br>
<code>greg@felicity:~/scripts$ ./cctimer.py -n -s 5</code>