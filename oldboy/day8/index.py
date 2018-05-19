
class AlexError(Exception):

    def __init__(self, msg=None):
        self.message = msg

    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'alex error'

try:
    raise AlexError('dfasdf')
except Exception, e:
    print e