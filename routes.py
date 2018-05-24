def template(name):
    path = '/home/dz/src/js/'+name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def route_index(request):

    header = 'HTTP/1.1 210 OK\r\nContent-type: text/html\r\n'
    body = template('index.html')
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

def route_login(request):
    
    header = 'HTTP/1.1 210 OK\r\nContent-type: text/html\r\n'
    if request.method=='POST':
        form = {"username":"123",
                "password":"123",
                }
        u = User(form)
    body = template('index.html')
    body = body.replace('{{result}}',resutl)
    r = head + '\r\n' +body
    return r.encode(encoding='utf-8')

def route_register(request):
    pass    

route_dict = {
        '/login': route_login,
        '/register': route_register,
        }

