import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process {} says: {}".format(os.getpid(), what))
