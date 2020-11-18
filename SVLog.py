import requests
from requests.api import request
import pickle

BASE = 'http://127.0.0.1:5000'

class SVLog:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    def getLogger(self, name):
        method = 'getLogger'
        requests.post(BASE, json={'method': method, 'arguments': name}, verify=True)
        return logger()

    def addLevelName(self, level, levelname):
        method = 'addLevelName'
        args = [level, levelname]
        requests.post(BASE, json={'method': method,'arguments': args}, verify=True)

    def basicConfig(self, **kwargs):
        method = 'basicConfig'
        requests.post(BASE, json={'method': method,'arguments': kwargs}, verify=True)

    def disable(self, level):
        method = 'disable'
        request.post(BASE, json={'method': method,'arguments': level}, verify=True)

    def debug(self, message, *args, **kwargs):
        method = 'debug'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})

    def info(self, message, *args, **kwargs):
        method = 'info'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})

    def warning(self, message, *args, **kwargs):
        method = 'warning'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})

    def error(self, message, *args, **kwargs):
        method = 'error'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})
        
    def critical(self, message, *args, **kwargs):
        method = 'critical'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})
        
    def log(self, level, message, *args, **kwargs):
        method = 'log'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [level, message, args, kwargs]})

    def exception(self, message, *args, exc_info=True, **kwargs):
        method = 'exception'
        requests.post(BASE, json={'method': method, 'arguments': [message, args, exc_info, kwargs]}, verify=True)

    def DEBUG(self):
        method = 'DEBUG'
        print("Hello")
        requests.post(BASE, json={'method': method}, verify=True)
        int = 10
        return int

    def shutdown(self):
        method = 'shutdown'
        requests.post(BASE, json={'method': method}, verify=True)

    def captureWarnings(self, capture:bool):
        method = 'captureWarnings'
        requests.post(BASE, json={'method': method, 'arguments':capture}, verify=True)

    def lastResort(self):
        method = 'lastResort'
        requests.post(BASE, json={'method': method}, verify=True)

    def setLogRecordFactory(self, factory):
        #factory:(*args:Any, **kwargs:Any)
        method = 'setLogRecordFactory'
        requests.post(BASE, json={'method': method,'arguments': factory}, verify=True)

    def setLoggerClass(self):
        method = 'setLoggerClass'
        requests.post(BASE, json={'method': method}, verify=True)
    
    def makeLogRecord(self, dict):
        method = 'makeLogRecord'
        requests.post(BASE, json={'method': method, 'arguments':dict}, verify=True)
    
    def getLogRecordFactory(self, *args, **kwargs):
        method = 'getLogRecordFactory'
        arguments = [args, kwargs]
        requests.post(BASE, json={'method': method,'arguments': arguments}, verify=True)

    def getLoggerClass(self):
        method = 'getLoggerClass'
        requests.post(BASE, json={'method': method}, verify=True)

    def LoggerAdapter(self, logger, dict):
        method = 'LoggerAdapter'
        requests.post(BASE, json={'method': method, 'arguments':[logger, dict]}, verify=True)

    def LogRecord(self, name: str, level: int, pathname, lineno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
        method = 'LogRecord'
        requests.post(BASE, json={'method': method, 'arguments': [name, level, pathname, lineno, msg, args, exc_info, func, sinfo, kwargs]}, verify=True)
    
    def warn(self, message, *args):
        method = 'warn'
        requests.post(BASE, json={'method': method, 'arguments': [message, args]}, verify=True)

    def BASIC_FORMAT():
        method = 'BASIC_FORMAT'
        request.post(BASE, json={'method': method}, verify=True)

    def FileHandler(fname, *args, **kwargs):
        method = 'BASIC_FORMAT'
        request.post(BASE, json={'method': method, 'arguments': [fname, args, kwargs]}, verify=True)

    def Formatter(self):
        pass

    def test(self):
        pass

    class Logger:

        def propagate():
            pass

        def setLevel():
            pass

        def isEnabledFor():
            pass

        def getEffectiveLevel():
            pass

        def getChild():
            pass

        def debug(message, *args, **kwargs):
            method = 'debug'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [message, args, kwargs]})

        def info(message, *args, **kwargs):
            method = 'info'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [message, args, kwargs]})

        def warning(message, *args, **kwargs):
            method = 'warning'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [message, args, kwargs]})

        def error(message, *args, **kwargs):
            method = 'error'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [message, args, kwargs]})

        def critical(message, *args, **kwargs):
            method = 'critical'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [message, args, kwargs]})

        def log(level, message, *args, **kwargs):
            method = 'log'
            requests.post(BASE, verify=True, json={
                        'method': method, 'arguments': [level, message, args, kwargs]})

        def exception(message, *args, exc_info=True, **kwargs):
            method = 'exception'
            requests.post(BASE, json={'method': method, 'arguments': [
                        message, args, exc_info, kwargs]}, verify=True)

        def addFilter(self):
            pass

        def removeFilter(self):
            pass

        def filter(self):
            pass

        def addHandler(self):
            pass

        def removeHandler(self):
            pass

        def findCaller(self):
            pass

        def handle():
            pass

        def makeRecord():
            pass

        def hasHandlers():
            pass

    class Handler:
        pass

class logger(object):
    def warning(self, message, *args, **kwargs):
        method = 'logger.warning'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [message, args, kwargs]})

NickModul = SVLog()

