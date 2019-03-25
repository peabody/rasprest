from subprocess import run
import os

from flask import Flask, request

app = Flask(__name__)
passwd = open(os.path.expanduser('~/.passwd.txt')).readlines()[0].strip()

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
    run(['sudo', 'shutdown', '-r'])
    return 'Rebooting...'

@app.route('/shutdown')
@auth
def shutdown():
    run(['sudo', 'shutdown'])
    return 'Shutting down...'

if __name__ == '__main__':
    app.run()
