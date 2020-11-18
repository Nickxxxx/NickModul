import logging
from logging import LoggerAdapter
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask import Flask, render_template, request, flash, url_for
import sys
import pickle
import requests

app = Flask(__name__)
api = Api(app)

print(dir(logging))


class Logging(Resource):
    def get(self):
        '''
        #data = request.json['method']
        y = LoggingServer.data(self)
        return pickle.dumps(y)
        '''
        pass

    def post(self):
        LoggingServer.data(self)


class LoggingServer:
    def data(self):
        method = request.json['method']

        global h1
        if method == 'warning':
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

        
        elif method == 'getLogger':
            name = request.json['arguments']
            h1 = logging.getLogger(name)

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
            logging.LoggerAdapter(logger, dict)
        
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

        elif method == 'logger.warning':
            arguments = request.json['arguments']
            message = arguments[0]
            args = arguments[1]
            kwargs = arguments[2]
            h1.warning(message, *args, **kwargs)

        else:
            pass

class Logger:
    def warning(self):
        pass

api.add_resource(Logging, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
