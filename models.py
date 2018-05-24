import json

def dump(data, path):
    s = json.dumps(data,indent=2, ensure_ascii=False)
    with open(path, 'w+',encoding='utf-8') as f:
        f.write(s)

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        return json.loads(s)


class Model(object):
    @classmethod
    def db_path(cls):
        class_name = cls.__name__
        path = '{}.txt'.format(class_name)
        return path

    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [[cls(m) for m in models
        return ms

    def save(self):
        models = self.all()
        models.append(self)
        l= [m.__dict__ for m in models]
        path = db_path(self)
        dump(l,path)

class User(Model):
    def __init__(self):
        self.username = form.get('username','')
        self.password = form.get('password','')
    
    def validate_login(self):
        path = self.db_path()
        models = load(path)
        for i in models:
        if i['username'] == self.username and i['password'] == self.password:
            return True
        return False

    def validate_register(self):
        return True;
