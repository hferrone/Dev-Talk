import web


# Routes
routes = (
    '/', 'home'
)

app = web.application(routes, globals())

# Classes/Routes

class home:
    def GET(self):
        return "home"

if __name__ == "__main__":
    app.run()