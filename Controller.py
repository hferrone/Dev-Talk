import web
from Models import RegisterModel


# Routes

routes = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(routes, globals())


# Classes/Routes

class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


if __name__ == "__main__":
    app.run()


