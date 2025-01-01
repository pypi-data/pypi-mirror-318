'''
2019 Bjoern Annighoefer
'''

from .logger import Logger,RegisterLogger, DEFAULT_LOGGER_LEVELS, LOG_LEVELS_NAME_LUT

import os
import logging

class FileLogger(Logger):
    """A logger that logs to a file.
    Each log level has its own file.
    The log files are created in the logDir with the prefix and the log level as name.
    """
    def __init__(self,activeLevels:int=DEFAULT_LOGGER_LEVELS.L2_WARNING,logDir:str='./log',prefix:str=''):
        super().__init__(activeLevels)
        self.logDir = logDir
        self.prefix = prefix #the text added infront of the log file name
        self.pyLoggers = {}
        #make sure the dir exists
        if(not os.path.isdir(self.logDir)):
            os.makedirs(self.logDir)
        #create native python loggers for each level
        for k,v in LOG_LEVELS_NAME_LUT.items():
            if(k & activeLevels):
                #init error python logger
                logger = logging.getLogger(v)
                logFile = os.path.join(self.logDir,"%s%s.log"%(self.prefix,v))
                fh = logging.FileHandler(logFile,'w')
                fh.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s - %(message)s')
                fh.setFormatter(formatter)
                logger.addHandler(fh)
                logger.setLevel(logging.INFO)
                self.pyLoggers[v] = logger
                
    #@Override         
    def _Log(self,levelName:str,msg:str):
        self.pyLoggers[levelName].info(msg)

RegisterLogger("FIL",FileLogger,[ "logDir","prefix"])

