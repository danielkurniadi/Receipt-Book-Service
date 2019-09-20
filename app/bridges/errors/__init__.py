class Error:
    message = ''
    error_code = 1
    http_status = 400

    def __init__(self, message, http_status):
        self.message = message
        self.http_status = http_status

    def to_json(self):
        return {
            'result': isinstance(self, ServerOk),
            'error_message': self.message,
            'error_code': self.error_code,
        }


class ServerOk(Error):
    error_code = 0
    http_status = 200

    def __init__(self, http_status=200):
        self.http_status = http_status


class DatabaseError(Error):
    error_code = 2


class OperationNotSupported(Error):
    error_code = 3


class InvalidRequest(Error):
    error_code = 99
