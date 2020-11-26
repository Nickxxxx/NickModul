import logging
from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

<<<<<<< HEAD
class Logging(Resource):
=======
class LoggingServer(Resource):
    
    @classmethod
>>>>>>> Branch2_only_one_class
    def post(self):

        method = request.json['method']
        arguments = request.json['arguments']
<<<<<<< HEAD
        print(method)
=======
>>>>>>> Branch2_only_one_class

        if method == 'getLogger':
            LoggingServer.getLogger(self, arguments)

        elif method == 'Handler':
            LoggingServer.Handler(self, arguments)

        elif method == 'Logger':
            LoggingServer.Logger(self, arguments)

        elif method == 'FileHandler':
            LoggingServer.FileHandler(self, arguments)

        elif method == 'StreamHandler':
            LoggingServer.StreamHandler(self, arguments)

        elif method == 'Formatter':
            LoggingServer.Formatter(self, arguments)

        elif method == 'Filter':
            LoggingServer.Filter(self, arguments)

        elif method == 'Filterer':
            LoggingServer.Filterer(self)

        elif method == 'Template':
            LoggingServer.Template(self, arguments)

        elif method == 'warning':
            LoggingServer.warning(self, arguments)

        elif method == 'debug':
            LoggingServer.debug(self, arguments)

        elif method == 'error':
            LoggingServer.error(self, arguments)

        elif method == 'critical':
            LoggingServer.critical(self, arguments)

        elif method == 'info':
            LoggingServer.info(self, arguments)

        elif method == 'log':
            LoggingServer.log(self, arguments)

        elif method == 'getLevelName':
            LoggingServer.getLevelName(self, arguments)

        elif method == 'addLevelName':
            LoggingServer.addLevelName(self, arguments)

        elif method == 'exception':
            LoggingServer.exception(self, arguments)

        elif method == 'disable':
            LoggingServer.disable(self, arguments)

        elif method == 'shutdown':
            LoggingServer.shutdown(self)

        elif method == 'captureWarnings':
            LoggingServer.captureWarnings(self, arguments)

        elif method == 'lastResort':
            LoggingServer.lastResort(self)

        elif method == 'setLogRecordFactory':
            LoggingServer.setLogRecordFactory(self, arguments)

        elif method == 'setLoggerClass':
            LoggingServer.setLoggerClass(self)

        elif method == 'basicConfig':
            LoggingServer.basicConfig(self, arguments)

        elif method == 'makeLogRecord':
            LoggingServer.makeLogRecord(self, arguments)

        elif method == 'getLogRecordFactory':
            LoggingServer.getLogRecordFactory(self, arguments)

        elif method == 'getLoggerClass':
            LoggingServer.getLoggerClass(self)

        elif method == 'LoggerAdapter':
            LoggingServer.LoggerAdapter(self, arguments)

        elif method == 'warn':
            LoggingServer.warn(self, arguments)

        elif method == 'DEBUG':
            LoggingServer.DEBUG(self)

        elif method == 'BASIC_FORMAT':
            LoggingServer.BASIC_FORMAT(self)

        elif method == 'LogRecord':
            LoggingServer.LogRecord(self, arguments)

        ###############################################################

        elif method == 'Filterer.addFilter':
<<<<<<< HEAD
            Filterer.addFilter(self, arguments)

        elif method == 'Filterer.removeFilter':
            Filterer.removeFilter(self, arguments)

        elif method == 'Filterer.filter':
            Filterer.filter(self, arguments)
=======
            LoggingServer.FiltereraddFilter(self, arguments)

        elif method == 'Filterer.removeFilter':
            LoggingServer.FiltererremoveFilter(self, arguments)

        elif method == 'Filterer.filter':
            LoggingServer.Filtererfilter(self, arguments)
>>>>>>> Branch2_only_one_class

        ##############################################################

        elif method == 'handler.get_name':
<<<<<<< HEAD
            Handler.get_name(self)

        elif method == 'Handler.set_name':
            Handler.set_name(self, arguments)

        elif method == 'Handler.createLock':
            Handler.createLock(self)

        elif method == 'Handler.acquire':
            Handler.acquire(self)

        elif method == 'Handler.release':
            Handler.release(self)

        elif method == 'Handler.setLevel':
            Handler.setLevel(self, arguments)

        elif method == 'Handler.format':
            Handler.format(self, arguments)

        elif method == 'Handler.emit':
            Handler.emit(self, arguments)

        elif method == 'Handler.handle':
            Handler.handle(self, arguments)

        elif method == 'Handler.setFormatter':
            Handler.setFormatter(self, arguments)

        elif method == 'Handler.flush':
            Handler.flush(self)

        elif method == 'Handler.close':
            Handler.close(self)

        elif method == 'Handler.handleError':
            Handler.handleError(self, arguments)
=======
            LoggingServer.Handlerget_name(self)

        elif method == 'Handler.set_name':
            LoggingServer.Handlerset_name(self, arguments)

        elif method == 'Handler.createLock':
            LoggingServer.HandlercreateLock(self)

        elif method == 'Handler.acquire':
            LoggingServer.Handleracquire(self)

        elif method == 'Handler.release':
            LoggingServer.Handlerrelease(self)

        elif method == 'Handler.setLevel':
            LoggingServer.HandlersetLevel(self, arguments)

        elif method == 'Handler.format':
            LoggingServer.Handlerformat(self, arguments)

        elif method == 'Handler.emit':
            LoggingServer.Handleremit(self, arguments)

        elif method == 'Handler.handle':
            LoggingServer.Handlerhandle(self, arguments)

        elif method == 'Handler.setFormatter':
            LoggingServer.HandlersetFormatter(self, arguments)

        elif method == 'Handler.flush':
            LoggingServer.Handlerflush(self)

        elif method == 'Handler.close':
            LoggingServer.Handlerclose(self)

        elif method == 'Handler.handleError':
            LoggingServer.HandlerhandleError(self, arguments)

        elif method == 'Handler.addFilter':
            LoggingServer.HandleraddFilter(self, arguments)

        elif method == 'Handler.removeFilter':
            LoggingServer.HandlerremoveFilter(self, arguments)

        elif method == 'Handler.filter':
            LoggingServer.Handlerfilter(self, arguments)
>>>>>>> Branch2_only_one_class

        ######################################################

        elif method == 'logger.warning':
<<<<<<< HEAD
            logger.warning(self, arguments)

        elif method == 'logger.debug':
            logger.debug(self, arguments)

        elif method == 'logger.info':
            logger.info(self, arguments)

        elif method == 'logger.error':
            logger.error(self, arguments)

        elif method == 'logger.critical':
            logger.critical(self, arguments)

        elif method == 'logger.log':
            logger.log(self, arguments)

        elif method == 'logger.setLevel':
            logger.setLevel(self, arguments)

        elif method == 'logger.warn':
            logger.warn(self, arguments)

        elif method == 'logger.propagate':
            logger.propagate(self)

        elif method == 'logger.isEnabledFor':
            logger.level(self, arguments)

        elif method == 'logger.getEffectiveLevel':
            logger.getEffectiveLevel(self)

        elif method == 'logger.getChild':
            logger.getChild(self, arguments)

        elif method == 'logger.exception':
            logger.exception(self, arguments)

        elif method == 'logger.callHandlers':
            logger.callHandlers(self, arguments)

        elif method == 'logger.addHandler':
            logger.addHandler(self, arguments)

        elif method == 'logger.removeHandler':
            logger.removeHandler(self, arguments)

        elif method == 'logger.findCaller':
            logger.findCaller(self, arguments)

        elif method == 'logger.handle':
            logger.handle(self, arguments)

        elif method == 'logger.makeRecord':
            logger.makeRecord(self, arguments)

        elif method == 'logger.hasHandlers':
            logger.hasHandlers(self)

        ######################################################

        elif method == 'StreamHandler.flush':
            StreamHandler.flush(self)

        elif method == 'StreamHandler.emit':
            StreamHandler.emit(self, arguments)

        elif method == 'StreamHandler.setStream':
            StreamHandler.setStream(self, arguments)
=======
            LoggingServer.loggerwarning(self, arguments)

        elif method == 'logger.debug':
            LoggingServer.loggerdebug(self, arguments)

        elif method == 'logger.info':
            LoggingServer.loggerinfo(self, arguments)

        elif method == 'logger.error':
            LoggingServer.loggererror(self, arguments)

        elif method == 'logger.critical':
            LoggingServer.loggercritical(self, arguments)

        elif method == 'logger.log':
            LoggingServer.loggerlog(self, arguments)

        elif method == 'logger.setLevel':
            LoggingServer.loggersetLevel(self, arguments)

        elif method == 'logger.warn':
            LoggingServer.loggerwarn(self, arguments)

        elif method == 'logger.propagate':
            LoggingServer.loggerpropagate(self)

        elif method == 'logger.isEnabledFor':
            LoggingServer.loggerlevel(self, arguments)

        elif method == 'logger.getEffectiveLevel':
            LoggingServer.loggergetEffectiveLevel(self)

        elif method == 'logger.getChild':
            LoggingServer.loggergetChild(self, arguments)

        elif method == 'logger.exception':
            LoggingServer.loggerexception(self, arguments)

        elif method == 'logger.callHandlers':
            LoggingServer.loggercallHandlers(self, arguments)

        elif method == 'logger.addHandler':
            LoggingServer.loggeraddHandler(self, arguments)

        elif method == 'logger.removeHandler':
            LoggingServer.loggerremoveHandler(self, arguments)

        elif method == 'logger.findCaller':
            LoggingServer.loggerfindCaller(self, arguments)

        elif method == 'logger.handle':
            LoggingServer.loggerhandle(self, arguments)

        elif method == 'logger.makeRecord':
            LoggingServer.loggermakeRecord(self, arguments)

        elif method == 'logger.hasHandlers':
            LoggingServer.loggerhasHandlers(self)

        elif method == 'logger.addFilter':
            LoggingServer.loggeraddFilter(self, arguments)

        elif method == 'logger.removeFilter':
            LoggingServer.loggerremoveFilter(self, arguments)

        elif method == 'logger.filter':
            LoggingServer.loggerfilter(self, arguments)

        ######################################################


        elif method == 'StreamHandler.flush':
            LoggingServer.StreamHandlerflush(self)

        elif method == 'StreamHandler.emit':
            LoggingServer.StreamHandleremit(self, arguments)

        elif method == 'StreamHandler.setStream':
            LoggingServer.StreamHandlersetStream(self, arguments)

        elif method == 'StreamHandler.get_name':
            LoggingServer.StreamHandlerget_name(self)

        elif method == 'StreamHandler.set_name':
            LoggingServer.StreamHandlerset_name(self, arguments)

        elif method == 'StreamHandler.createLock':
            LoggingServer.StreamHandlercreateLock(self)

        elif method == 'StreamHandler.acquire':
            LoggingServer.StreamHandleracquire(self)

        elif method == 'StreamHandler.release':
            LoggingServer.StreamHandlerrelease(self)

        elif method == 'StreamHandler.setLevel':
            LoggingServer.StreamHandlerset_name(self, arguments)

        elif method == 'StreamHandler.format':
            LoggingServer.StreamHandlerformat(self, arguments)

        elif method == 'StreamHandler.handle':
            LoggingServer.StreamHandlerhandle(self, arguments)

        elif method == 'StreamHandler.setFormatter':
            LoggingServer.StreamHandlersetFormatter(self, arguments)

        elif method == 'StreamHandler.close':
            LoggingServer.StreamHandlerclose(self)

        elif method == 'StreamHandler.handleError':
            LoggingServer.StreamHandlerhandleError(self, arguments)

        elif method == 'StreamHandler.addFilter':
            LoggingServer.StreamHandleraddFilter(self, arguments)

        elif method == 'StreamHandler.removeFilter':
            LoggingServer.StreamHandlerremoveFilter(self, arguments)

        elif method == 'StreamHandler.filter':
            LoggingServer.StreamHandlerfilter(self, arguments)
>>>>>>> Branch2_only_one_class

        ######################################################

        elif method == 'FileHandler.close':
<<<<<<< HEAD
            FileHandler.close(self)

        elif method == 'FileHandler.emit':
            FileHandler.emit(self, arguments)

        elif method == 'Filter.filter':
            Filter.filter(self, arguments)
        
=======
            LoggingServer.FileHandlerclose(self)

        elif method == 'FileHandler.emit':
            LoggingServer.FileHandleremit(self, arguments)

        elif method == 'FileHandler.flush':
            LoggingServer.FileHandlerflush(self)

        elif method == 'FileHandler.setStream':
            LoggingServer.FileHandlersetStream(self, arguments)

        elif method == 'FileHandler.get_name':
            LoggingServer.FileHandlerget_name(self)

        elif method == 'FileHandler.set_name':
            LoggingServer.FileHandlerset_name(self, arguments)

        elif method == 'FileHandler.createLock':
            LoggingServer.FileHandlercreateLock(self)

        elif method == 'FileHandler.acquire':
            LoggingServer.FileHandleracquire(self)

        elif method == 'FileHandler.release':
            LoggingServer.FileHandlerrelease(self)

        elif method == 'FileHandler.setLevel':
            LoggingServer.FileHandlersetLevel(self, arguments)

        elif method == 'FileHandler.format':
            LoggingServer.FileHandlerformat(self, arguments)

        elif method == 'FileHandler.handle':
            LoggingServer.FileHandlerhandle(self, arguments)

        elif method == 'FileHandler.setFormatter':
            LoggingServer.FileHandlersetFormatter(self, arguments)

        elif method == 'FileHandler.handleError':
            LoggingServer.FileHandlerhandleError(self, arguments)

        elif method == 'FileHandler.addFilter':
            LoggingServer.FileHandleraddFilter(self, arguments)

        elif method == 'FileHandler.removeFilter':
            LoggingServer.FileHandlerremoveFilter(self, arguments)

        elif method == 'FileHandler.filter':
            LoggingServer.FileHandlerfilter(self, arguments)

>>>>>>> Branch2_only_one_class
        #####################################################

        elif method == 'LogRecord.getMessage':
            pass
            
        #####################################################

        elif method == 'LoggerAdapter.process':
<<<<<<< HEAD
            LoggerAdapter.process(self, arguments)
=======
            LoggingServer.LoggerAdapterprocess(self, arguments)
>>>>>>> Branch2_only_one_class
        
        #####################################################

        elif method == 'Formatter.formatTime':
<<<<<<< HEAD
            Formatter.formatTime(self, arguments)

        elif method == 'Formatter.formatException':
            Formatter.formatException(self, arguments)

        elif method == 'Formatter.usesTime':
            Formatter.usesTime(self)

        elif method == 'Formatter.formatMessage':
            Formatter.formatMessage(self, arguments)

        elif method == 'Formatter.formatStack':
            Formatter.formatStack(self, arguments)

        elif method == 'Formatter.format':
            Formatter.format(self, arguments)


class LoggingServer:
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0

    def __init__(self):
        self.h1_getLogger = None
        self.h2_handler = None
        self.h4_FileHandler = None
        self.h5_StreamHandler = None
        self.h6_Formatter = None
        self.h7_Filter = None
        self.h8_Filterer = None
        self.h9_LoggerAdapter = None
=======
            LoggingServer.FormatterformatTime(self, arguments)

        elif method == 'Formatter.formatException':
            LoggingServer.FormatterformatException(self, arguments)

        elif method == 'Formatter.usesTime':
            LoggingServer.FormatterusesTime(self)

        elif method == 'Formatter.formatMessage':
            LoggingServer.FormatterformatMessage(self, arguments)

        elif method == 'Formatter.formatStack':
            LoggingServer.FormatterformatStack(self, arguments)

        elif method == 'Formatter.format':
            LoggingServer.Formatterformat(self, arguments)
>>>>>>> Branch2_only_one_class

    def getLogger(self, arguments):
        name = arguments
        self.h1_getLogger = logging.getLogger(name)
<<<<<<< HEAD
=======
        self.h1_getLogger.handlers.clear()
>>>>>>> Branch2_only_one_class
        return self.h1_getLogger

    def Handler(self, arguments):
        level = arguments
        self.h2_handler = logging.Handler(level)
        return self.h2_handler

    def Logger(self, arguments):
        name = arguments[0]
        level = arguments[1]
        self.h1_getLogger = logging.Logger(name, level)
        return self.h1_getLogger

    def FileHandler(self, arguments):
        filename = arguments[0]
        mode = arguments[1]
        encoding = arguments[2]
        delay = arguments[3]
        self.h4_FileHandler = logging.FileHandler(filename, mode, encoding, delay)
        return self.h4_FileHandler

    def StreamHandler(self, arguments):
        stream = arguments
        self.h5_StreamHandler = logging.StreamHandler(stream)
        return self.h5_StreamHandler

    def Formatter(self, arguments):
        fmt = arguments[0]
        datefmt = arguments[1]
        style = arguments[2]
        validate = arguments[3]
        self.h6_Formatter = logging.Formatter(fmt, datefmt, style, validate)
        return self.h6_Formatter

    def Filter(self, arguments):
        name = arguments
        self.h7_Filter = logging.Filter(name)
        return self.h7_Filter

    def Filterer(self):
        self.h8_Filterer = logging.Filterer()
        return self.h8_Filterer

    def Template(self, arguments):
        template = arguments
        logging.Template(template)

    def addLevelName(self, arguments):
        level = arguments[0]
        levelname = arguments[1]
        logging.addLevelName(level, levelname)

    def basicConfig(self, arguments):
        kwargs = arguments
        print(kwargs)
        logging.basicConfig(**kwargs)

    def disable(self, arguments):
        level = arguments
        logging.disable(level)

    def debug(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.debug(message, *args, **kwargs)

    def info(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.info(message, *args, **kwargs)

    def warning(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.warning(message, *args, **kwargs)

    def error(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.error(message, *args, **kwargs)

    def critical(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        logging.critical(message, *args, **kwargs)

    def log(self, arguments):
        level = arguments[0]
        message = arguments[1]
        args = arguments[2]
        kwargs = arguments[3]
        logging.log(level, message, *args, **kwargs)

    def exception(self, arguments):
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        logging.exception(message, *args, exc_info, **kwargs)

    #problem_kanidat
    def DEBUG(self):
        print("hello")
        print(logging.DEBUG)
        logging.DEBUG

    def shutdown(self):
        logging.shutdown()

    def getLevelName(self, arguments):
        level = arguments
        logging.getLevelName(level)

    def captureWarnings(self, arguments):
        capture = arguments
        logging.captureWarnings(capture=capture)

    def lastResort(self):
        logging.lastResort

    def setLogRecordFactory(self, arguments):
        factory = arguments
        logging.setLogRecordFactory(factory)

    def setLoggerClass(self):
        logging.setLoggerClass

    def makeLogRecord(self, arguments):
        dict = arguments
        logging.makeLogRecord(dict)

    def getLogRecordFactory(self, arguments):
        args = arguments[0]
        kwargs = arguments[1]
        logging.getLogRecordFactory(*args, **kwargs)

    def getLoggerClass(self):
        logging.getLoggerClass()

    def LoggerAdapter(self, arguments):
        logger = arguments[0]
        dict = arguments[1]
        h9_LoggerAdapter = None
        h9_LoggerAdapter = logging.LoggerAdapter(logger, dict)
        return h9_LoggerAdapter

    def LogRecord(self, arguments):
        logging.LogRecord(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4],arguments[5], arguments[6], arguments[7], arguments[8], **(arguments[9]))

    def warn(self, arguments):
        message = arguments[0]
        args = arguments[0]
        logging.warn(msg=message, *args)

    def BASIC_FORMAT(self):
        print("hello")
        logging.BASIC_FORMAT

    def raiseExceptions(self):
        pass

<<<<<<< HEAD

class logger(LoggingServer):

    def __init__(self):
        self.LoggingServer = self.LoggingServer()
        self.h1_getLogger = self.LoggingServer.h1_getLogger

    def warning(self, arguments):
=======
##############################################################

    def loggerwarning(self,arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warning(message, *args, **kwargs)

<<<<<<< HEAD
    def debug(self, arguments):
=======
    def loggerdebug(self, arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.debug(message, *args, **kwargs)

<<<<<<< HEAD
    def info(self, arguments):
=======
    def loggerinfo(self, arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.info(message, *args, **kwargs)

<<<<<<< HEAD
    def error(self, arguments):
        print("Test")
=======
    def loggererror(self, arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.error(message, *args, **kwargs)

<<<<<<< HEAD
    def critical(self, arguments):
=======
    def loggercritical(self, arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.critical(message, *args, **kwargs)

    def log(self, arguments):
        level = arguments[0]
        message = arguments[1]
        args = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(level, message, *args, **kwargs)

<<<<<<< HEAD
    def setLevel(self, arguments):
        level = arguments
        self.h1_getLogger.setLevel(level)

    def warn(self, arguments):
=======
    def loggersetLevel(self, arguments):
        level = arguments
        self.h1_getLogger.setLevel(level)

    def loggerwarn(self, arguments):
>>>>>>> Branch2_only_one_class
        msg = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warn(msg, *args, **kwargs)

<<<<<<< HEAD
    def propagate(self):
        self.h1_getLogger.propagate()

    def isEnabledFor(self, arguments):
        level = arguments
        self.h1_getLogger.level(level)

    def getEffectiveLevel(self):
        self.h1_getLogger.getEffectiveLevel()

    def getChild(self, arguments):
        suffix = arguments
        self.h1_getLogger.getChild(suffix)

    def exception(self, arguments):
=======
    def loggerpropagate(self):
        self.h1_getLogger.propagate()

    def loggerisEnabledFor(self, arguments):
        level = arguments
        self.h1_getLogger.level(level)

    def loggergetEffectiveLevel(self):
        self.h1_getLogger.getEffectiveLevel()

    def loggergetChild(self, arguments):
        suffix = arguments
        self.h1_getLogger.getChild(suffix)

    def loggerexception(self, arguments):
>>>>>>> Branch2_only_one_class
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(message, *args, exc_info, **kwargs)

<<<<<<< HEAD
    def callHandlers(self, arguments):
        record = arguments
        self.h1_getLogger.callHandlers(record)

    def addHandler(self, arguments):
=======
    def loggercallHandlers(self, arguments):
        record = arguments
        self.h1_getLogger.callHandlers(record)


    def loggeraddHandler(self, arguments):

>>>>>>> Branch2_only_one_class
        hdlr = arguments
        if hdlr == 'FileHandler':
            hdlr = self.h4_FileHandler
            self.h1_getLogger.addHandler(hdlr)
<<<<<<< HEAD
        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.addHandler(hdlr)
        else:
            pass

    def removeHandler(self, arguments):
        hdlr = arguments
        self.h1_getLogger.removeHandler(hdlr)

    def findCaller(self, arguments):
=======
            
            '''
            for h in list(self.h1_getLogger.handlers):
                if type(self.hdlr) == type(h):
                    print("hit")
                    self.h1_getLogger.removeHandler(hdlr)
                    print(self.h1_getLogger.handlers)
                else:
                    print("no hit")

            print(self.h1_getLogger.handlers)
            '''

        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.addHandler(hdlr)


        elif hdlr == 'Handler':
            hdlr = self.h2_handler
            self.h1_getLogger.addHandler(hdlr)

        elif hdlr == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.addHandler(hdlr)
            
        else:
            message = hdlr
            print(message)


        #else:
            #self.h1_getLogger.handlers.clear()

        #if self.h1_getLogger.hasHandlers():

        #print(self.h1_getLogger.handlers)
        #print(self.h1_getLogger.hasHandlers())


    def loggerremoveHandler(self, arguments):
        hdlr = arguments

        if hdlr == 'FileHandler':
            hdlr = self.h4_FileHandler
            self.h1_getLogger.removeHandler(hdlr)

        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.removeHandler(hdlr)
        
        elif hdlr == 'Handler':
            hdlr = self.h2_handler
            self.h1_getLogger.removeHandler(hdlr)

        elif hdlr == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.removeHandler(hdlr)
        
        else:
            message = hdlr
            print(message)


    def loggerfindCaller(self, arguments):
>>>>>>> Branch2_only_one_class
        stack_info = arguments[0]
        stacklevel = arguments[1]
        self.h1_getLogger.findCaller(stack_info, stacklevel)

<<<<<<< HEAD
    def handle(self, arguments):
        record = arguments
        self.h1_getLogger.handle(record)

    def makeRecord(self, arguments):
=======
    def loggerhandle(self, arguments):
        record = arguments
        self.h1_getLogger.handle(record)

    def loggermakeRecord(self, arguments):
>>>>>>> Branch2_only_one_class
        name = arguments[0]
        level = arguments[1]
        fn = arguments[2]
        lno = arguments[3]
        msg = arguments[4]
        args = arguments[5]
        exc_info = arguments[6]
        func = arguments[7]
        extra = arguments[8]
        sinfo = arguments[9]
        self.h1_getLogger.makeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

<<<<<<< HEAD
    def hasHandlers(self):
        self.h1_getLogger.hasHandlers()


class Filterer(object):
    def addFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.addFilter(filter)

    def removeFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.removeFilter(filter)

    def filter(self, arguments):
        record = arguments
        self.h8_Filterer.filter(record)


class Handler(Filterer):
    def get_name(self):
        self.h2_handler.get_name()

    def set_name(self, arguments):
        name = arguments
        self.h2_handler.set_name(name)

    def createLock(self):
        self.h2_handler.createLock()

    def acquire(self):
        self.h2_handler.acquire()

    def release(self):
        self.h2_handler.release()

    def setLevel(self, arguments):
        level = arguments
        self.h2_handler.setLevel(level)

    def format(self, arguments):
        record = arguments
        self.h2_handler.format(record)

    def emit(self, arguments):
        record = arguments
        self.h2_handler.emit(record)

    def handle(self, arguments):
        record = arguments
        self.h2_handler.handle(record)

    def setFormatter(self, arguments):
        #arguments are h1_getlogger or h2_handler or h4_FileHandler or h5_StreeamHandler
        fmt = arguments
        self.h2_handler.setFormatter(fmt)

    def flush(self):
        self.h2_handler.flush()

    def close(self):
        self.h2_handler.close()

    def handleError(self, arguments):
        record = arguments
        self.h2_handler.handleError(record)


class StreamHandler(Handler):
    def flush(self):
        self.h5_StreamHandler.flush()

    def emit(self, arguments):
        record = arguments
        self.h5_StreamHandler.emit(record)

    def setStream(self, arguments):
        stream = arguments
        self.h5_StreamHandler.setStream(stream)


class FileHandler(StreamHandler):
    def close(self):
        self.h4_FileHandler.close()

    def emit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)


class Filter(object):
    def filter(self, arguments):
        record = arguments
        self.h7_Filter.filter(record)

class LogRecord(object):
    def getMessage(self):
        pass


class LoggerAdapter(object):
    def process(self, arguments):
=======
    def loggerhasHandlers(self):
        self.h1_getLogger.hasHandlers()

    def loggeraddFilter(self, arguments):
        filter = arguments
        self.h1_getLogger.addfilter(filter)

    def loggerremoveFilter(self, arguments):
        filter = arguments
        self.h1_getLogger.removeFilter(filter)

    def loggerfilter(self, arguments):
        record = arguments
        self.h1_getLogger.filter(record)

##############################################################

    def FiltereraddFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.addFilter(filter)

    def FiltererremoveFilter(self, arguments):
        filter = arguments
        self.h8_Filterer.removeFilter(filter)

    def Filtererfilter(self, arguments):
        record = arguments
        self.h8_Filterer.filter(record)

##############################################################

    def Handlerget_name(self):
        self.h2_handler.get_name()

    def Handlerset_name(self, arguments):
        name = arguments
        self.h2_handler.set_name(name)

    def HandlercreateLock(self):
        self.h2_handler.createLock()

    def Handleracquire(self):
        self.h2_handler.acquire()

    def Handlerrelease(self):
        self.h2_handler.release()

    def HandlersetLevel(self, arguments):
        level = arguments
        self.h2_handler.setLevel(level)

    def Handlerformat(self, arguments):
        record = arguments
        self.h2_handler.format(record)

    def Handleremit(self, arguments):
        record = arguments
        self.h2_handler.emit(record)

    def Handlerhandle(self, arguments):
        record = arguments
        self.h2_handler.handle(record)

    def HandlersetFormatter(self, arguments):
        fmt = arguments
        
        if fmt == 'Formatter':
            hdlr = self.h6_Formatter
            self.h1_getLogger.removeHandler(hdlr)

        else:
            message = fmt
            print(message)


    def Handlerflush(self):
        self.h2_handler.flush()

    def Handlerclose(self):
        self.h2_handler.close()

    def HandlerhandleError(self, arguments):
        record = arguments
        self.h2_handler.handleError(record)

    def HandleraddFilter(self, arguments):
        filter = arguments
        self.h2_handler.addfilter(filter)

    def HandlerremoveFilter(self, arguments):
        filter = arguments
        self.h2_handler.removeFilter(filter)

    def Handlerfilter(self, arguments):
        record = arguments
        self.h2_handler.filter(record)

##############################################################

    def StreamHandlerflush(self):
        self.h5_StreamHandler.flush()

    def StreamHandleremit(self, arguments):
        record = arguments
        self.h5_StreamHandler.emit(record)

    def StreamHandlersetStream(self, arguments):
        stream = arguments
        self.h5_StreamHandler.setStream(stream)

    def StreamHandlerget_name(self):
        self.h5_StreamHandler.get_name()

    def StreamHandlerset_name(self, arguments):
        name = arguments
        self.h5_StreamHandler.set_name(name)

    def StreamHandlercreateLock(self):
        self.h5_StreamHandler.createLock()

    def StreamHandleracquire(self):
        self.h5_StreamHandler.acquire()

    def StreamHandlerrelease(self):
        self.h5_StreamHandler.release()

    def StreamHandlersetLevel(self, arguments):
        level = arguments
        self.h5_StreamHandler.setLevel(level)

    def StreamHandlerformat(self, arguments):
        record = arguments
        self.h5_StreamHandler.format(record)

    def StreamHandlerhandle(self, arguments):
        record = arguments
        self.h5_StreamHandler.handle(record)

    def StreamHandlersetFormatter(self, arguments):
        fmt = arguments
        
        if fmt == 'Formatter':
            fmt = self.h6_Formatter
            self.h5_StreamHandler.setFormatter(fmt)

        else:
            message = fmt
            print(message)

    def StreamHandlerclose(self):
        self.h5_StreamHandler.close()

    def StreamHandlerhandleError(self, arguments):
        record = arguments
        self.h5_StreamHandler.handleError(record)
    
    def StreamHandleraddFilter(self, arguments):
        filter = arguments
        self.h5_StreamHandler.addfilter(filter)

    def StreamHandlerremoveFilter(self, arguments):
        filter = arguments
        self.h5_StreamHandler.removeFilter(filter)

    def StreamHandlerfilter(self, arguments):
        record = arguments
        self.h5_StreamHandler.filter(record)
    

##############################################################

    def FileHandlerclose(self):
        self.h4_FileHandler.close()

    def FileHandleremit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)

    def FileHandlerflush(self):
        self.h4_FileHandler.flush()

    def FileHandleremit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)

    def FileHandlersetStream(self, arguments):
        stream = arguments
        self.h4_FileHandler.setStream(stream)

    def FileHandlerget_name(self):
        self.h4_FileHandler.get_name()

    def FileHandlerset_name(self, arguments):
        name = arguments
        self.h4_FileHandler.set_name(name)

    def FileHandlercreateLock(self):
        self.h4_FileHandler.createLock()

    def FileHandleracquire(self):
        self.h4_FileHandler.acquire()

    def FileHandlerrelease(self):
        self.h4_FileHandler.release()

    def FileHandlersetLevel(self, arguments):
        level = arguments
        self.h4_FileHandler.setLevel(level)

    def FileHandlerformat(self, arguments):
        record = arguments
        self.h4_FileHandler.format(record)

    def FileHandlerhandle(self, arguments):
        record = arguments
        self.h4_FileHandler.handle(record)

    def FileHandlersetFormatter(self, arguments):
        fmt = arguments

        if fmt == 'Formatter':
            fmt = self.h6_Formatter
            self.h4_FileHandler.setFormatter(fmt)

        else:
            message = fmt
            print(message)

    def FileHandlerhandleError(self, arguments):
        record = arguments
        self.h4_FileHandler.handleError(record)

    def FileHandleraddFilter(self, arguments):
        filter = arguments
        self.h4_FileHandler.addFilter(filter)

    def FileHandlerremoveFilter(self, arguments):
        filter = arguments
        self.h4_FileHandler.removeFilter(filter)

    def FileHandlerfilter(self, arguments):
        record = arguments
        self.h4_FileHandler.filter(record)
    

##############################################################

    def Filterfilter(self, arguments):
        record = arguments
        self.h7_Filter.filter(record)

##############################################################

    def LogRecordgetMessage(self):
        pass

##############################################################

    def LoggerAdapterprocess(self, arguments):
>>>>>>> Branch2_only_one_class
        msg = arguments[0]
        kwargs = arguments[1]
        self.h9_LoggerAdapter.process(msg, **kwargs)

<<<<<<< HEAD

class Formatter(object):
    def formatTime(self, arguments):
=======
##############################################################

    def FormatterformatTime(self, arguments):
>>>>>>> Branch2_only_one_class
        record = arguments[0]
        datefmt = arguments[1]
        self.h6_Formatter.formatTime(record, datefmt)

<<<<<<< HEAD
    def formatException(self, arguments):
        exc_info = arguments
        self.h6_Formatter.formatException(exc_info)

    def usesTime(self):
        self.h6_Formatter.usesTime()

    def formatMessage(self, arguments):
        record = arguments
        self.h6_Formatter.formatMessage(record)

    def formatStack(self, arguments):
        stack_info = arguments
        self.h6_Formatter.formatStack(stack_info)

    def format(self, arguments):
        record = arguments
        self.h6_Formatter.format(record)

=======
    def FormatterformatException(self, arguments):
        exc_info = arguments
        self.h6_Formatter.formatException(exc_info)

    def FormatterusesTime(self):
        self.h6_Formatter.usesTime()

    def FormatterformatMessage(self, arguments):
        record = arguments
        self.h6_Formatter.formatMessage(record)

    def FormatterformatStack(self, arguments):
        stack_info = arguments
        self.h6_Formatter.formatStack(stack_info)

    def Formatterformat(self, arguments):
        record = arguments
        self.h6_Formatter.format(record)
>>>>>>> Branch2_only_one_class

api.add_resource(LoggingServer, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
