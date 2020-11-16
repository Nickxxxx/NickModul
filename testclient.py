import requests
from requests.api import request
import pickle

BASE = 'http://127.0.0.1:5000'
#test = requests.post(BASE, verify=True)

class NickModul:

    def getLogger(self, name):
        method = 'getLogger'
        requests.post(BASE, json={'method': method, 'arguments': name}, verify=True)
        #return_value = requests.get(BASE, json={'method': method, 'arguments': name}, verify=True)
        model = pickle.load(requests.get(BASE, json={'method': method, 'arguments': name}, verify=True))
        return model

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

    def debug(self, message):
        method = 'debug'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': message})

    def info(self, message):
        method = 'info'
        requests.post(BASE, verify=True, json={'method':method, 'arguments':message})

    def warning(self, message):
        method = 'warning'
        requests.post(BASE, verify=True, json={'method':method, 'arguments':message})

    def error(self, message):
        method = 'error'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': message})
        
    def critical(self, message):
        method = 'critical'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': message})
        
    def log(self, level, message):
        method = 'log'
        requests.post(BASE, verify=True, json={'method': method, 'arguments': [level, message]})

    def exception(self):
        pass

    def DEBUG(self):
        method = 'DEBUG'
        print("Hello")
        requests.post(BASE, json={'method': method}, verify=True)
        #int = requests.get(BASE, json={'method': method}, verify=True)
        model = pickle.loads(requests.get(
            BASE, json={'method': method}, verify=True, encoding="utf-8"), )
        print(model)
        return model

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

    def test(self):
        pass





####################################################

NickModul = NickModul()

def main(x, y):

    if y != 0:
        solution = x/y
        print(solution)
    else:
        NickModul.debug("This is a warning")
        NickModul.warning("This is a warning")
        NickModul.error("This is a warning")
        NickModul.info("This is a warning")
        print("hello")
        NickModul.DEBUG
        NickModul.captureWarnings(True)

main(10, 0)
