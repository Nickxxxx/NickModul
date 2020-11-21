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
        LoggingServer.data(self)

class LoggingServer:

    def data(self):
        method = request.json['method']

        #global h1_getLogger
        if method == 'getLogger':
            name = request.json['arguments']
            h1_getLogger = logging.getLogger(name)
            return self.h1_getLogger
            '''
            print("test1")
            print(h1_getLogger)
            print("-----")
            print("test2")
            print(type(h1_getLogger))
            print("-----")
            h1_getLogger = logging.getLogger(name)
            print("test3")
            print(h1_getLogger)
            print("-----")
            print("test4")
            print(type(h1_getLogger))
            print("-----")
            '''

        elif method == 'Handler':
            level = request.json['arguments']
            h2_handler = None
            h2_handler = logging.Handler(level)
            return h2_handler
        
        elif method == 'Logger':
            arguments = request.json['arguments']
            name = arguments[0]
            level = arguments[1]
            h1_getLogger = None
            h1_getLogger = logging.Logger(name, level)
            return h1_getLogger
            

        elif method == 'FileHandler':
            arguments = request.json['arguments']
            filename = arguments[0]
            mode = arguments[1]
            encoding = arguments[2]
            delay = arguments[3]
            h4_FileHandler = None
            h4_FileHandler = logging.FileHandler(filename, mode, encoding, delay)
            return h4_FileHandler

        elif method == 'StreamHandler':
            stream = request.json['arguments']
            h5_StreamHandler = None
            h5_StreamHandler = logging.StreamHandler(stream)
            return h5_StreamHandler

        elif method == 'Formatter':
            arguments = request.json['arguments']
            fmt = arguments[0]
            datefmt = arguments[1]
            style = arguments[2]
            validate = arguments[3]
            h6_Formatter = logging.Formatter(fmt, datefmt, style, validate)
            return h6_Formatter

        elif method == 'Filter':
            name = request.json['arguments']
            h7_Filter = logging.Filter(name)
            return h7_Filter
        
        elif method == 'Filterer':
            h8_Filterer = logging.Filterer()
            return h8_Filterer

        elif method == 'Template':
            template = request.json['arguments']
            logging.Template(template)

        elif method == 'warning':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            logging.warning(message, *args, **kwargs)

        elif method == 'debug':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            logging.debug(message, *args, **kwargs)
        
        elif method == 'error':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            logging.error(message, *args, **kwargs)
        
        elif method == 'critical':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            logging.critical(message, *args, **kwargs)
        
        elif method == 'info':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            logging.info(message, *args, **kwargs)
        
        elif method == 'log':
            arguments = request.json['arguments']
            level = arguments[0]
            message = arguments[1]
            args = arguments[2]
            kwargs = arguments[3]
            logging.log(level, message, *args, **kwargs)

        elif method == 'getLevelName':
            level = request.json['arguments']
            logging.getLevelName(level)

        elif method == 'addLevelName':
            level = request.json['arguments'][0]
            levelname = request.json['arguments'][1]
            logging.addLevelName(level, levelname)

        elif method == 'exception':
            arguments = request.json['arguments']
            message = arguments[0]
            args  = arguments[1]
            exc_info = arguments[2]
            kwargs = arguments[3]
            logging.exception(message, *args, exc_info, **kwargs)

        elif method == 'disable':
            level = request.json['arguments']
            logging.disable(level)
        
        elif method == 'shutdown':
            logging.shutdown()

        elif method == 'captureWarnings':
            capture = request.json['arguments']
            logging.captureWarnings(capture=capture)

        elif method == 'lastResort':
            logging.lastResort
        
        elif method == 'setLogRecordFactory':
            factory = request.json['arguments']
            logging.setLogRecordFactory(factory)
        
        elif method == 'setLoggerClass':
            logging.setLoggerClass
        
        elif method == 'basicConfig':
            kwargs = request.json['arguments']
            print(kwargs)
            logging.basicConfig(**kwargs)
        
        elif method == 'makeLogRecord':
            dict = request.json['arguments']
            logging.makeLogRecord(dict)
        
        elif method == 'getLogRecordFactory':
            args = request.json['arguments'][0]
            kwargs = request.json['arguments'][1]
            logging.getLogRecordFactory(*args, **kwargs)

        elif method == 'getLoggerClass':
            logging.getLoggerClass()

        elif method == 'LoggerAdapter':
            logger = request.json['arguments'][0]
            dict = request.json['arguments'][1]
            h9_LoggerAdapter = logging.LoggerAdapter(logger, dict)
        
        elif method == 'warn':
            message = request.json['arguments'][0]
            args = request.json['arguments'][0]
            logging.warn(msg=message, *args)

        elif method == 'DEBUG':
            print("hello")
            print(logging.DEBUG)
            logging.DEBUG
        
        elif method == 'BASIC_FORMAT':
            print("hello")
            logging.BASIC_FORMAT

        elif method == 'LogRecord':
            arguments = request.json['arguments']
            logging.LogRecord(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], arguments[6], arguments[7], arguments[8], **(arguments[9]))

        elif method == 'Filterer.addFilter':
            filter = request.json['arguments']
            h8_Filterer.addFilter(filter)

        elif method == 'Filterer.removeFilter':
            filter = request.json['arguments']
            h8_Filterer.removeFilter(filter)

        elif method == 'Filterer.filter':
            record = request.json['arguments']
            h8_Filterer.filter(record)

        elif method == 'handler.get_name':
            h2_handler.get_name()

        elif method == 'Handler.set_name':
            name = request.json['arguments']
            h2_handler.set_name(name)

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
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            self.h1_getLogger.error(message, *args, **kwargs)

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
            h1_getLogger.makeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

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
            arguments = request.josn['arguments']
            msg = arguments[0]
            kwargs = arguments[1]
            h9_LoggerAdapter.process(msg, **kwargs)

        elif method == 'Formatter.formatTime':
            arguments = request.josn['arguments']
            record = arguments[0]
            datefmt = arguments[1]
            h6_Formatter.formatTime(record, datefmt)

        elif method == 'Formatter.formatException':
            exc_info = request.josn['arguments']
            h6_Formatter.formatException(exc_info)

        elif method == 'Formatter.usesTime':
            h6_Formatter.usesTime()

        elif method == 'Formatter.formatMessage':
            record = request.josn['arguments']
            h6_Formatter.formatMessage(record)

        elif method == 'Formatter.formatStack':
            stack_info = request.josn['arguments']
            h6_Formatter.formatStack(stack_info)

        elif method == 'Formatter.format':
            record = request.josn['arguments']
            h6_Formatter.format(record)

        return h1_getLogger

api.add_resource(Logging, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
