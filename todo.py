class Todolist:
    def __init__(self):
        self.tasks = []
        self.loadtask()
        
    def loadtask(self):
        try:
            file = open("text.txt", "r")
            for line in file:
                self.tasks.append(line.strip())
            file.close()
        except FileNotFoundError:
            file = open("test.txt", "w")
            file.close()

    def savetask(self):
        file = open("text.txt", "w")
        for task in self.tasks:
            file.write(task + "\n")
        file.close()

    def addTask(self):
        add = input("Enter Task: ")
        self.tasks.append(add)
        self.savetask()
        print("Task added successfully")
    
    def viewTask(self):
        if len(self.tasks) == 0:
            return print("No task to view")
        for i in range(len(self.tasks)):
            print(f"{i} {self.tasks[i]}")
        
        
    def deleteTask(self):
        self.viewTask()
        if len(self.tasks) == 0:
                return print("No task to delete!")
        
        delete = int(input("Enter Task number to delete: "))
        new_list = []
        for i in range(len(self.tasks)):
            
            
            if i!=delete:
                new_list.append(self.tasks[i])
        self.tasks = new_list
        self.savetask()


op = Todolist()

while True:

    print('''
            1. Enter Task
            2. View Task
            3. Delete Task
            4. Exit''')

    en = input("Enter your choice: ")
    if en=="1":
        op.addTask()
    elif en=="2":
        op.viewTask()
    elif en=="3":
        op.deleteTask()

    elif en=="4":
        break