import logging
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask import Flask, render_template, request, flash, url_for
import sys
import pickle
import requests

app = Flask(__name__)
api = Api(app)

print(dir(logging))

#logging.request(the thing you send)

class Logging(Resource):
    def get(self):
        #data = request.json['method']
        y = Nicklogging.data(self)
        return pickle.dumps(y)

    def post(self):
        Nicklogging.data(self)


class Nicklogging:
    def data(self):
        method = request.json['method']
        print(method)

        if method == 'warning':
            message = request.json['arguments']
            return logging.warning(message)

        elif method == 'debug':
            message = request.json['arguments']
            return logging.debug(message)
        
        elif method == 'error':
            message = str(request.json['arguments'])
            return logging.error(message)
        
        elif method == 'critical':
            message = str(request.json['arguments'])
            return logging.critical(message)
        
        elif method == 'info':
            message = str(request.json['arguments'])
            return logging.info(message)
        
        elif method == 'log':
            arguments = request.json['arguments']
            level = arguments[0]
            message = arguments[1]
            return logging.log(level=level, msg=message)

        elif method == 'getLevelName':
            level = request.json['arguments']
            return logging.getLevelName(level)

        elif method == 'addLevelName':
            level = request.json['arguments'][0]
            levelname = request.json['arguments'][1]
            return logging.addLevelName(level, levelname)

        elif method == 'getLogger':
            name = request.json['arguments']
            return logging.getLogger(name)

        elif method == 'exception':
            message = request.json['arguments']
            return logging.exception(message)

        elif method == 'disable':
            level = request.json['arguments']
            return logging.disable(level)
        
        elif method == 'shutdown':
            return logging.shutdown()

        elif method == 'captureWarnings':
            capture = request.json['arguments']
            return logging.captureWarnings(capture=capture)

        elif method == 'lastResort':
            return logging.lastResort
        
        elif method == 'setLogRecordFactory':
            factory = request.json['arguments']
            return logging.setLogRecordFactory(factory)
        
        elif method == 'setLoggerClass':
            return logging.setLoggerClass
        
        elif method == 'basicConfig':
            kwargs = request.json['arguments']
            return logging.basicConfig(**kwargs)
        
        elif method == 'makeLogRecord':
            dict = request.json['arguments']
            return logging.makeLogRecord(dict)
        
        elif method == 'getLogRecordFactory':
            args = request.json['arguments'][0]
            kwargs = request.json['arguments'][1]
            return logging.getLogRecordFactory(*args, **kwargs)

        elif method == 'DEBUG':
            print("hello")
            print(logging.DEBUG)

            return logging.DEBUG

        else:
            pass

api.add_resource(Logging, '/')

#logging.data("Hello this is a test")

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
