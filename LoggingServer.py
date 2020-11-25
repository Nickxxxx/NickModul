import logging
from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)

class LoggingServer(Resource):
    
    @classmethod
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
            LoggingServer.FiltereraddFilter(self, arguments)

        elif method == 'Filterer.removeFilter':
            LoggingServer.FiltererremoveFilter(self, arguments)

        elif method == 'Filterer.filter':
            LoggingServer.Filtererfilter(self, arguments)

        ##############################################################

        elif method == 'handler.get_name':
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

        ######################################################

        elif method == 'logger.warning':
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

        ######################################################

        elif method == 'StreamHandler.flush':
            LoggingServer.StreamHandlerflush(self)

        elif method == 'StreamHandler.emit':
            LoggingServer.StreamHandleremit(self, arguments)

        elif method == 'StreamHandler.setStream':
            LoggingServer.StreamHandlersetStream(self, arguments)

        ######################################################

        elif method == 'FileHandler.close':
            LoggingServer.FileHandlerclose(self)

        elif method == 'FileHandler.emit':
            LoggingServer.FileHandleremit(self, arguments)

        elif method == 'Filter.filter':
            LoggingServer.Filterfilter(self, arguments)
        
        #####################################################

        elif method == 'LogRecord.getMessage':
            pass
            
        #####################################################

        elif method == 'LoggerAdapter.process':
            LoggingServer.LoggerAdapterprocess(self, arguments)
        
        #####################################################

        elif method == 'Formatter.formatTime':
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

    def getLogger(self, arguments):
        name = arguments
        self.h1_getLogger = logging.getLogger(name)
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

##############################################################

    def loggerwarning(self,arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warning(message, *args, **kwargs)

    def loggerdebug(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.debug(message, *args, **kwargs)

    def loggerinfo(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.info(message, *args, **kwargs)

    def loggererror(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.error(message, *args, **kwargs)

    def loggercritical(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.critical(message, *args, **kwargs)

    def loggerlog(self, arguments):
        level = arguments[0]
        message = arguments[1]
        args = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(level, message, *args, **kwargs)

    def loggersetLevel(self, arguments):
        level = arguments
        self.h1_getLogger.setLevel(level)

    def loggerwarn(self, arguments):
        msg = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warn(msg, *args, **kwargs)

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
        message = arguments[0]
        args = arguments[1]
        exc_info = arguments[2]
        kwargs = arguments[3]
        self.h1_getLogger.log(message, *args, exc_info, **kwargs)

    def loggercallHandlers(self, arguments):
        record = arguments
        self.h1_getLogger.callHandlers(record)

    def loggeraddHandler(self, arguments):
        hdlr = arguments
        if hdlr == 'FileHandler':
            hdlr = self.h4_FileHandler
            self.h1_getLogger.addHandler(hdlr)
        elif hdlr == 'StreamHandler':
            hdlr = self.h5_StreamHandler
            self.h1_getLogger.addHandler(hdlr)
        else:
            pass

    def loggerremoveHandler(self, arguments):
        hdlr = arguments
        self.h1_getLogger.removeHandler(hdlr)

    def loggerfindCaller(self, arguments):
        stack_info = arguments[0]
        stacklevel = arguments[1]
        self.h1_getLogger.findCaller(stack_info, stacklevel)

    def loggerhandle(self, arguments):
        record = arguments
        self.h1_getLogger.handle(record)

    def loggermakeRecord(self, arguments):
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

    def loggerhasHandlers(self):
        self.h1_getLogger.hasHandlers()

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
        #arguments are h1_getlogger or h2_handler or h4_FileHandler or h5_StreeamHandler
        fmt = arguments
        self.h2_handler.setFormatter(fmt)

    def Handlerflush(self):
        self.h2_handler.flush()

    def Handlerclose(self):
        self.h2_handler.close()

    def HandlerhandleError(self, arguments):
        record = arguments
        self.h2_handler.handleError(record)

##############################################################

    def StreamHandlerflush(self):
        self.h5_StreamHandler.flush()

    def StreamHandleremit(self, arguments):
        record = arguments
        self.h5_StreamHandler.emit(record)

    def StreamHandlersetStream(self, arguments):
        stream = arguments
        self.h5_StreamHandler.setStream(stream)

##############################################################

    def FileHandlerclose(self):
        self.h4_FileHandler.close()

    def FileHandleremit(self, arguments):
        record = arguments
        self.h4_FileHandler.emit(record)

##############################################################

    def Filterfilter(self, arguments):
        record = arguments
        self.h7_Filter.filter(record)

##############################################################

    def LogRecordgetMessage(self):
        pass

##############################################################

    def LoggerAdapterprocess(self, arguments):
        msg = arguments[0]
        kwargs = arguments[1]
        self.h9_LoggerAdapter.process(msg, **kwargs)

##############################################################

    def FormatterformatTime(self, arguments):
        record = arguments[0]
        datefmt = arguments[1]
        self.h6_Formatter.formatTime(record, datefmt)

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

api.add_resource(LoggingServer, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
