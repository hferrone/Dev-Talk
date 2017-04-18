import web
from Models import RegisterModel, LoginModel


web.config.debug = False

# Routes


routes = (
    '/', 'Home',
    '/register', 'Register',
    '/post-registration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin',
    '/logout', 'Logout'
)


# Initialize webb app and session


app = web.application(routes, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})


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
            session_data["user"] = isCorrect

            return isCorrect

        return "error"


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "logout successful"


if __name__ == "__main__":
    app.run()


