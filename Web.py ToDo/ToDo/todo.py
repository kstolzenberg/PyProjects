""" Basic todo list example from webpy.org """
# web is webpy module, model is our other python file with dunctions
import web
import model

web.config.debug = False

# url mapping
urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)

# point towards templates
render = web.template.render('templates/', base='base')

class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            description="I need to:"),
        web.form.Button("Add todo"),
        )

    def GET(self):
        """ show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """add new entry"""
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')

class Delete:
    def POST(self, id):
        """delete based on ID"""
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()













