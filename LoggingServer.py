import logging
from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

print(dir(logging))

#h1_getLogger = None
h2_handler = None
h4_FileHandler = None
h5_StreamHandler = None
h6_Formatter = None
h7_Filter = None
h8_Filterer = None
h9_LoggerAdapter = None

class Logging(Resource):
    def post(self):
        #LoggingServer.data(self)

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

        elif method == 'handler.get_name':
            Handler.get_name(self)

        elif method == 'Handler.set_name':#
            Handler.set_name(self, arguments)

        elif method == 'Handler.createLock':
            h2_handler.createLock()

        elif method == 'Handler.acquire':
            h2_handler.acquire()

        elif method == 'Handler.release':
            h2_handler.release()

        elif method == 'Handler.setLevel':
            level = request.json['arguments']
            h2_handler.setLevel(level)

        elif method == 'Handler.format':
            record = request.json['arguments']
            h2_handler.format(record)

        elif method == 'Handler.emit':
            record = request.json['arguments']
            h2_handler.emit(record)

        elif method == 'Handler.handle':
            record = request.json['arguments']
            h2_handler.handle(record)

        elif method == 'Handler.setFormatter':
            fmt = request.json['arguments']
            h2_handler.setFormatter(fmt)

        elif method == 'Handler.flush':
            h2_handler.flush()

        elif method == 'Handler.close':
            h2_handler.close()

        elif method == 'Handler.handleError':
            record = request.json['arguments']
            h2_handler.handleError(record)

        elif method == 'logger.warning':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1_getLogger.warning(message, *args, **kwargs)

        elif method == 'logger.debug':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1_getLogger.debug(message, *args, **kwargs)

        elif method == 'logger.info':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1_getLogger.info(message, *args, **kwargs)

        elif method == 'logger.error':
            logger.error(self, arguments)

        elif method == 'logger.critical':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1_getLogger.critical(message, *args, **kwargs)

        elif method == 'logger.log':
            arguments = request.json['arguments']
            level = arguments[0]
            message = arguments[1]
            args = arguments[2]
            kwargs = arguments[3]
            h1_getLogger.log(level, message, *args, **kwargs)

        elif method == 'logger.setLevel':
            #def setLevel(self, level):
            level = request.json['arguments']
            h1_getLogger.setLevel(level)

        elif method == 'logger.warn':
            arguments = request.json['arguments']
            msg = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1_getLogger.warn(msg, *args, **kwargs)

        elif method == 'logger.propagate':
            h1_getLogger.propagate()

        elif method == 'logger.isEnabledFor':
            level = request.json['arguments']
            h1_getLogger.level(level)

        elif method == 'logger.getEffectiveLevel':
            h1_getLogger.getEffectiveLevel()

        elif method == 'logger.getChild':
            suffix = request.json['arguments']
            h1_getLogger.getChild(suffix)

        elif method == 'logger.exception':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            exc_info = arguments[2]
            kwargs = arguments[3]
            h1_getLogger.log(message, *args, exc_info, **kwargs)

        elif method == 'logger.callHandlers':
            record = request.json['arguments']
            h1_getLogger.callHandlers(record)

        elif method == 'logger.addHandler':
            hdlr = request.json['arguments']
            if hdlr == 'FileHandler':
                hdlr = h4_FileHandler
                h1_getLogger.addHandler(hdlr)
            elif hdlr == 'StreamHandler':
                hdlr = h5_StreamHandler
                h1_getLogger.addHandler(hdlr)

        elif method == 'logger.removeHandler':
            hdlr = request.json['arguments']
            h1_getLogger.removeHandler(hdlr)

        elif method == 'logger.findCaller':
            arguments = request.json['arguments']
            stack_info = arguments[0]
            stacklevel = arguments[1]
            h1_getLogger.findCaller(stack_info, stacklevel)

        elif method == 'logger.handle':
            record = request.json['arguments']
            h1_getLogger.handle(record)

        elif method == 'logger.makeRecord':
            arguments = request.json['arguments']
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
            h1_getLogger.makeRecord(
                name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

        elif method == 'logger.hasHandlers':
            h1_getLogger.hasHandlers()

        elif method == 'StreamHandler.flush':
            h5_StreamHandler.flush()

        elif method == 'StreamHandler.emit':
            record = request.json['arguments']
            h5_StreamHandler.emit(record)

        elif method == 'StreamHandler.setStream':
            stream = request.json['arguments']
            h5_StreamHandler.setStream(stream)

        elif method == 'FileHandler.close':
            h4_FileHandler.close()

        elif method == 'FileHandler.emit':
            record = request.json['arguments']
            h4_FileHandler.emit(record)

        elif method == 'Filter.filter':
            record = request.json['arguments']
            h7_Filter.filter(record)

        elif method == 'LogRecord.getMessage':
            pass

        elif method == 'LoggerAdapter.process':
            arguments = request.json['arguments']
            msg = arguments[0]
            kwargs = arguments[1]
            h9_LoggerAdapter.process(msg, **kwargs)

        elif method == 'Formatter.formatTime':
            arguments = request.json['arguments']
            record = arguments[0]
            datefmt = arguments[1]
            h6_Formatter.formatTime(record, datefmt)

        elif method == 'Formatter.formatException':
            exc_info = request.json['arguments']
            h6_Formatter.formatException(exc_info)

        elif method == 'Formatter.usesTime':
            h6_Formatter.usesTime()

        elif method == 'Formatter.formatMessage':
            record = request.json['arguments']
            h6_Formatter.formatMessage(record)

        elif method == 'Formatter.formatStack':
            stack_info = request.json['arguments']
            h6_Formatter.formatStack(stack_info)

        elif method == 'Formatter.format':
            record = request.json['arguments']
            h6_Formatter.format(record)


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
        self.LoggingServer = LoggingServer

    def warning(self, message, *args, **kwargs):
            pass

    def debug(self, message, *args, **kwargs):
            pass

    def info(self, message, *args, **kwargs):
            pass

    def error(self, arguments):
        print("Test")
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.LoggingServer.h1_getLogger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
            pass

    def log(self, level, message, *args, **kwargs):
            pass

    def setLevel(self, level):
            pass

    def warn(self, msg, *args, **kwargs):
            pass

    def propagate(self):
            pass

    def isEnabledFor(self, level):
            pass

    def getEffectiveLevel(self):
            pass

    def getChild(self, suffix):
            pass

    def exception(message, *args, exc_info=True, **kwargs):
            pass

    def callHandlers(self, record):
            pass

    def addHandler(self, hdlr):
            if isinstance(hdlr, FileHandler):
                pass

            elif isinstance(hdlr, StreamHandler):
                pass

            else:
                pass

    def removeHandler(self, hdlr):
            pass

    def findCaller(self, stack_info=False, stacklevel=1):
            pass

    def handle(self, record):
            pass

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
            pass

    def hasHandlers(self):
            pass


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
        h2_handler.get_name()

    def set_name(self, arguments):
        name = arguments
        h2_handler.set_name(name)

    def createLock(self):
        pass

    def acquire(self):
        pass

    def release(self):
        pass

    def setLevel(self, level):
        pass

    def format(self, record):
        pass

    def emit(self, record):
        pass

    def handle(self, record):
        pass

    def setFormatter(self, fmt):
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def handleError(self, record):
        pass



class StreamHandler(Handler):
    def flush(self):
        pass

    def emit(self, record):
        pass

    def setStream(self, stream):
        pass


class FileHandler(StreamHandler):
    def close(self):
        pass

    def emit(self, record):
        pass


class Filter(object):
    def filter(self, record):
        pass

class LogRecord(object):
    def getMessage(self):
        pass


class LoggerAdapter(object):
    def process(self, msg, **kwargs):
        pass


class Formatter(object):
    def formatTime(self, record, datefmt=None):
        pass

    def formatException(self, exc_info):
        pass

    def usesTime(self):
        pass

    def formatMessage(self, record):
        pass

    def formatStack(self, stack_info):
        pass

    def format(self, record):
        pass


api.add_resource(Logging, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
