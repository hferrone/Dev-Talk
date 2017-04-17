import web
from Models import RegisterModel, LoginModel


# Routes

routes = (
    '/', 'Home',
    '/register', 'Register',
    '/post-registration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin'
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


class Login:
    def GET(self):
        return render.Login()


class CheckLogin:
    def POST(self):
        data = web.input()

        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)

        if isCorrect:
            return isCorrect

        return "error"


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


if __name__ == "__main__":
    app.run()


