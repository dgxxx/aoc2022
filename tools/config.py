import logging
import os
import time


id=time.strftime("%Y%m%d%H%M%S")
#### CONFIG ###
logfile="aoc.log"
loglevel=logging.DEBUG
filelevel=logging.DEBUG
consolelevel=logging.DEBUG
app="aoc"
##################################
configuration={}
configuration['LOGLEVEL']=os.getenv("LOGLEVEL","INFO")
if configuration['LOGLEVEL']=="DEBUG":
    loglevel=logging.DEBUG
elif configuration['LOGLEVEL']=="INFO":
    loglevel=logging.INFO
elif configuration['LOGLEVEL']=="WARN":
    loglevel=logging.WARN
else:
    loglevel=logging.ERROR


