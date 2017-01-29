import appier

class HelloApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "app_name",
            *args, **kwargs
        )

HelloApp().serve()
