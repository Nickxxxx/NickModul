import logging
from flask_restful import Api, Resource
from flask import Flask, request

app = Flask(__name__)
api = Api(app)


class LoggingServer(Resource):

    @classmethod
    def post(self):
        self.method = request.json['method']
        self.arguments = request.json['arguments']
        Test.decision(self)

        
class Test:
    def decision(self):
        method = self.method
        arguments = self.arguments


        if method == 'getLogger':
            Test.getLogger(self, arguments)

        elif method == 'logger.warning':
            Test.loggerwarning(self, arguments)

        elif method == 'logger.error':
            Test.loggererror(self, arguments)

    
    def getLogger(self, arguments):
        name = arguments
        self.h1_getLogger = logging.getLogger(name)
        return self.h1_getLogger

    def loggerwarning(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.warning(message, *args, **kwargs)

    def loggererror(self, arguments):
        message = arguments[0]
        args = arguments[1]
        kwargs = arguments[2]
        self.h1_getLogger.error(message, *args, **kwargs)


api.add_resource(LoggingServer, '/')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
