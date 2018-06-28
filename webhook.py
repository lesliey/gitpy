import os
import json
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    if (path == '/hook'):
        os.system('cd /usr/share/nginx/www/myblog && git pull origin master')
        os.system('cd /home/gitpy && git pull origin master')
        print('git pull finish')
        return [b'Hello, webhook has done!']
    if (path == '/hello'):
        print('hello..')
        return [b'Hello, just welcome']
    return [b'Hello, default!']
