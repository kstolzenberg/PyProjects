CREATE TABLE todo (id integer primary key, title text, created date, done boolean default 'f');
CREATE TRIGGER insert_todo_created after insert on todo
begin
update todo set created = datetime('now')
where rowid = new.rowid;
end;
