#using web py
import web

urls = (
    '/hello', 'Index'
    )

app = web.application(urls, globals())

# connect template to python = render.index() && tell it where to find the templates
# add a base template for all pages to render off!
render = web.template.render('templates/', base = "layout")

class Index(object):
    def GET(self):
        #points to hello_form.html
        return render.hello_form()

        # html form sends data as a POST method
    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s %s" % (form.greet, form.name)
        #points to index.html
        return render.index(greeting = greeting)

# this is doing two things now! taking in fields and returning on index /url!
# the magic is the html - form action = /hello, method post = send to /hello url
    
if __name__ == "__main__":
    app.run()

