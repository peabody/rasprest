import os
from threading import Thread
import time
from subprocess import run

from flask import Flask, request

app = Flask(__name__)
passwd = open(os.path.expanduser('~/.passwd.txt')).readlines()[0].strip()

class Command:
    '''
    Given a command argument list, run command after milliseconds delay.
    '''
    def __init__(self, command_list, milliseconds=10000):
        self.command_list = command_list
        self.milliseconds = milliseconds

    def __call__(self):
        time.sleep(self.milliseconds)
        run(self.command_list)


def check_password(password):
    return passwd == password

def auth(f):
    def wrapped_auth():
        password = request.args.get('password')        
        if check_password(password):
            return f()
        else:
            return 'Unauthorized', 401
    wrapped_auth.__name__ = f.__name__
    return wrapped_auth

@app.route('/reboot')
@auth
def reboot():
    Thread(target=Command(['sudo', 'reboot'])).start()
    return 'Rebooting...'

@app.route('/shutdown')
@auth
def shutdown():
    Thread(target=Command(['sudo', 'poweroff'])).start()
    return 'Shutting down...'

if __name__ == '__main__':
    app.run()
