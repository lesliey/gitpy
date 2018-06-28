import os
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    os.system('cd /usr/share/nginx/www/myblog && git pull origin master')
    print('git pull finish')
    return [b'Hello, webhook!']
