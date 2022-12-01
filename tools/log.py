# v2022-01-28 16:00
"""
Logging Modulg
"""
from tools import config
import os
import logging,logging.handlers
import sys
import time

def setup_path():
    config.path=os.path.dirname(os.path.abspath(__file__))
    if not config.app: 
        config.app=f[len(f)-1]
    config.logfile=config.app+".log"
    #print ("config.app: {}".format(config.app))
#####################################################################
#
# Logging 
#
#####################################################################
def setup_logging():
    #t=time.strftime("%Y%m%d%H%M%S")
    t=config.id
    uid=id(t)

    #logging.basicConfig(filename="log/log.txt", filemode='w', format='%(asctime)s : %(name)-12s - %(levelname)-8s - %(message)s')
    #logging.basicConfig(format='%(asctime)s : %(name)-12s - %(levelname)-8s - %(message)s')
    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.handlers.RotatingFileHandler(config.path+"/../log/"+config.logfile,maxBytes=100000000,backupCount=3)

    # Create formatters and add it to handlers
    #c_format = logging.Formatter('%(name)-15s - %(levelname)-8s - %(message)s')
    c_format = logging.Formatter('%(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    #f_format = logging.Formatter('%(asctime)s - %(name)-15s - %(levelname)-8s - %(message)s')
    f_format = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    loggerazure = logging.getLogger('azure')
    loggerazure.setLevel(logging.ERROR)

    c_handler.setLevel(config.consolelevel)
    f_handler.setLevel(config.filelevel)
    logger=logging.getLogger('')
    logger.setLevel(config.loglevel)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    config.logger=logger


def setlevel(level="INFO"):
    print("Level got: {}".format(level))
    if level=="DEBUG":
        loglevel=logging.DEBUG
    elif level=="INFO":
        loglevel=logging.INFO
    elif level=="WARN":
        loglevel=logging.WARN
    else:
        loglevel=logging.ERROR
    
    config.logger.setLevel(loglevel)
    #logging.setLevel(loglevel)
    return loglevel
#####################################################################
#
# EXECUTION
#
#####################################################################
setup_path()
setup_logging()
#module_logger=config.logger.getChild("tools")
