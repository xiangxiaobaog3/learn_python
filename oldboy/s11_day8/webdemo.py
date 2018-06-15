# -*- coding:utf-8 -*-
from wsgiref.simple_server import  make_server

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    filename = url.split('/')[1]
    function_name = url.split('/')[2]

    module = __import__(filename)
    # 去home模块中检查，是否含有指定的函数
    is_exist = hasattr(module, function_name)
    # 如果存在指定的函数
    if is_exist:
        func = getattr(module, function_name)
        # 执行函数并获取返回值
        ret = func()
        # 将函数返回响应给请求者
        return ret
    else:
        return '404 not found'


if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print "Serving HTTP on port 8001..."
    httpd.serve_forever()