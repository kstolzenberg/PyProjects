#using web py
import web

urls = (
    '/hello', 'Index'
    )

app = web.application(urls, globals())

# connect template to python = render.index() && tell it where to find the templates
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        # intro to forms! you can add ?name = to the url to manipulate this
        form = web.input(name="Nobody")
        greeting = "hello %s, %s " % (form.name, form.greet)

        # greeting = "hello worldie friend!"
        # render.'html file name' in templates folder! this is how you point at a specific file
        
        return render.index(greeting = greeting) # pass greeting as a variable to html

if __name__ == "__main__":
    app.run()


# why don't we have to call index.GET?

# note this runs here : http://127.0.0.1:8080/
# local host connection at port 8080
# this uses web.py! similar to flask

# run this from the project folder via python bin/app.py\
# stay at the top of the files structure so python can access all related files!!
