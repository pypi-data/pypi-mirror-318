from core import FrameAPI

def global_middlewares(request):
    print('Global middleware')

frameapi = FrameAPI(middlewares=[global_middlewares])

def local_middlewares(request):
    print('Local middleware')



@frameapi.get('/')
def home(req, res):
    res.send('Welcome to FrameAPI')

@frameapi.get('/users/{id}', middlewares=[local_middlewares])
def get_users(req, res, id):
    res.send(f'Hello {id} user method:GET')

@frameapi.post('/users')
def post_users(req, res):
    res.send('Hello from /users method:POST')



@frameapi.route('/class', middlewares=[local_middlewares])
class User:
    def __init__(self) -> None:
        pass

    def get(req, res):
        res.render('default.html', {'name': 'Admin'})
    