import appier

class HelloApp(appier.App):

    @appier.route("/", "GET")
    def hello(self):
        return "Hello World"

HelloApp().serve()
