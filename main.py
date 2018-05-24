import socket
from routes import route_index
from routes import route_dict

class Request(object):
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.body = ''

request = Request()

def response_for_path(path):
    r = {
            '/': route_index,
            }
    r.update(route_dict)
    response = r.get(path,error)
    return response(request)

def error(code=404):
    error_dict = {
            404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 Not Found</h1>'
    }
    return error_dict.get(code,b'')

def run(host='',port=3000):
    with socket.socket() as s:
        s.bind((host,port))
        while True:
            s.listen()
            connection, addr = s.accept()
            r = connection.recv(1024).decode('utf-8')
            print(r)
            if (len(r.split())<2):
                continue
            request.method = r.split()[0]
            request.body = r.split('\r\n\r\n')[1]
            request.path = r.split()[1]
            response = response_for_path(request.path)
            connection.sendall(response)
            connection.close()
            addr = ''
run('',3000)



