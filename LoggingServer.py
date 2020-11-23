import logging
from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

print(dir(logging))

h1_getLogger = None
h2_handler = None
h4_FileHandler = None
h5_StreamHandler = None
h6_Formatter = None
h7_Filter = None
h8_Filterer = None
h9_LoggerAdapter = None

class Logging(Resource):
    def post(self):
        
        method = request.json['method']
        arguments = request.json['arguments']

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
            Filterer.addFilter(self, arguments)

        elif method == 'Filterer.removeFilter':
            Filterer.removeFilter(self, arguments)

        elif method == 'Filterer.filter':
            Filterer.filter(self, arguments)

        ##############################################################

        elif method == 'handler.get_name':
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

        ######################################################

        elif method == 'logger.warning':
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

        ######################################################

        elif method == 'FileHandler.close':
            FileHandler.close(self)

        elif method == 'FileHandler.emit':
            FileHandler.emit(self, arguments)

        elif method == 'Filter.filter':
            Filter.filter(self, arguments)
        
        #####################################################

        elif method == 'LogRecord.getMessage':
            pass
            
        #####################################################

        elif method == 'LoggerAdapter.process':
            LoggerAdapter.process(self, arguments)
        
        #####################################################

        elif method == 'Formatter.formatTime':
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

    def getLogger(self, arguments):
        name = arguments
        self.h1_getLogger = logging.getLogger(name)
        return self.h1_getLogger

    def Handler(self, arguments):
        level = arguments
        h2_handler = None
        h2_handler = logging.Handler(level)
        return h2_handler

    def Logger(self, arguments):
        name = arguments[0]
        level = arguments[1]
        h1_getLogger = None
        h1_getLogger = logging.Logger(name, level)
        return h1_getLogger

    def FileHandler(self, arguments):
        filename = arguments[0]
        mode = arguments[1]
        encoding = arguments[2]
        delay = arguments[3]
        h4_FileHandler = None
        h4_FileHandler = logging.FileHandler(filename, mode, encoding, delay)
        return h4_FileHandler

    def StreamHandler(self, arguments):
        stream = arguments
        h5_StreamHandler = None
        h5_StreamHandler = logging.StreamHandler(stream)
        return h5_StreamHandler

    def Formatter(self, arguments):
        fmt = arguments[0]
        datefmt = arguments[1]
        style = arguments[2]
        validate = arguments[3]
        h6_Formatter = logging.Formatter(fmt, datefmt, style, validate)
        return h6_Formatter

    def Filter(self, arguments):
        name = arguments
        h7_Filter = logging.Filter(name)
        return h7_Filter

    def Filterer(self):
        h8_Filterer = logging.Filterer()
        return h8_Filterer

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



class logger(LoggingServer):

    def __init__(self, LoggingServer):
        self.LoggingServer = LoggingServer()

    def warning(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warning(message, *args, **kwargs)

    def debug(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.debug(message, *args, **kwargs)

    def info(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.info(message, *args, **kwargs)

    def error(self, arguments):
        print("Test")
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.LoggingServer.h1_getLogger.error(message, *args, **kwargs)

    def critical(self, arguments):
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

    def setLevel(self, arguments):
        level = arguments
        self.h1_getLogger.setLevel(level)

    def warn(self, arguments):
        msg = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warn(msg, *args, **kwargs)

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
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(message, *args, exc_info, **kwargs)

    def callHandlers(self, arguments):
        record = arguments
        self.h1_getLogger.callHandlers(record)

    def addHandler(self, arguments):
        hdlr = arguments
        if hdlr == 'FileHandler':
            hdlr = h4_FileHandler
            self.h1_getLogger.addHandler(hdlr)
        elif hdlr == 'StreamHandler':
            hdlr = h5_StreamHandler
            self.h1_getLogger.addHandler(hdlr)
        else:
            pass

    def removeHandler(self, arguments):
        hdlr = arguments
        self.h1_getLogger.removeHandler(hdlr)

    def findCaller(self, arguments):
        stack_info = arguments[0]
        stacklevel = arguments[1]
        self.h1_getLogger.findCaller(stack_info, stacklevel)

    def handle(self, arguments):
        record = arguments
        self.h1_getLogger.handle(record)

    def makeRecord(self, arguments):
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

    def hasHandlers(self):
        self.h1_getLogger.hasHandlers()


class Filterer(object):
    def addFilter(self, arguments):
        filter = arguments
        h8_Filterer.addFilter(filter)

    def removeFilter(self, arguments):
        filter = arguments
        h8_Filterer.removeFilter(filter)

    def filter(self, arguments):
        record = arguments
        h8_Filterer.filter(record)


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
        msg = arguments[0]
        kwargs = arguments[1]
        self.h9_LoggerAdapter.process(msg, **kwargs)


class Formatter(object):
    def formatTime(self, arguments):
        record = arguments[0]
        datefmt = arguments[1]
        self.h6_Formatter.formatTime(record, datefmt)

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
        h6_Formatter.format(record)


api.add_resource(Logging, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
