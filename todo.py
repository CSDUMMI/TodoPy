#! /usr/bin/python3
import json, sys, time, datetime

class Todo:
    """
    Usage:
    ======
    Commands:
    list:\t\tList all Todos
    add <name> <deadline>:\t\tAdd new Todo
    remove <name>:\t\tRemove a todo
    check:\t\tPrint todos that are overdue
    """
    def __init__(self):
        self.todos = json.load(open('todo.json'))

    def list(self):
        print("ALL TODOS:")
        for todo in self.todos.keys():
            print("\t{}\n\t{}".format(todo,datetime.datetime.fromtimestamp(self.todos[todo]['deadline']).strftime("%d, %B %Y %M:%S")))

    def add(self,name,deadline):
        self.todos[name] = {'deadline':deadline}

    def remove(self,name):
        del self.todos[name]

    def check(self):
        now = time.time()
        overdue = []
        for todo in self.todos.keys():
            if int(self.todos[todo]['deadline']) < now:
                overdue.append(todo)
        return overdue
    def save(self):
        json.dump(self.todos,open('todo.json','w+'))
def run():
    todos = Todo()
    if len(sys.argv) == 1:
        print(Todo.__doc__)
    else:
        cmd = sys.argv[1]
        if cmd == 'add':
            name = sys.argv[2]
            deadline = sys.argv[3].split(':')
            deadline = datetime.datetime(
                        int(deadline[0]),
                        int(deadline[1]),
                        int(deadline[2]),
                        int(deadline[3]),
                        int(deadline[4]))
            deadline = time.mktime(deadline.timetuple())
            todos.add(name,deadline)
        elif cmd == 'remove':
            todos.remove(sys.argv[2])
        elif cmd == 'list':
            todos.list()
        elif cmd == 'check':
            overdue = todos.check()
            for o in overdue:
                print("OVERDUE: {}".format(o))
    todos.save()

if __name__ == '__main__':
    run()
