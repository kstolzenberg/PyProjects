import web
# needs a database module MySQLdb?
# there are issues with the database module that cause the whole to fail! :<

# (deprecated)db = web.database(dbn='mysql', db='todo', user='justin')
# this is totally broken!

db = web.database(dbn='sqlite', db='testdb')

def get_todos():
    return db.select('todo', order='id')

def new_todo():
    db.insert('todo', title=text)

def del_todo():
    db.deleted('todo', where='id=$id', vars=locals())