import web
from Models import RegisterModel, LoginModel, Posts


web.config.debug = False

# Routes


routes = (
    '/', 'Home',
    '/register', 'Register',
    '/post-registration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin',
    '/logout', 'Logout',
    '/post-activity', 'PostActivity'
)


# Initialize webb app and session


app = web.application(routes, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})


# Classes/Routes


class Home:
    def GET(self):
        login_data = type('obj', (object,), {'username': 'hferrone', 'password': 'Test123'})
        login_model = LoginModel.LoginModel()
        is_valid = login_model.check_user(login_data)

        if is_valid:
            session_data["user"] = is_valid

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)


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


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data["user"]["username"]

        post_model = Posts.Posts()
        post_model.insert_post(data)

        return "success"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None

        session.kill()
        return "logout successful"


if __name__ == "__main__":
    app.run()


