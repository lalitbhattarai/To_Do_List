def task():
    tasks= [] #empty list
    print("........WELCOME MY LORD....")

    total_task=int(input("ENter the number of tasks you want to add ="))
    for i in range (1 ,total_task+1):
        task_name=input(f"Enter tasks {i} = ")
        tasks.append(task_name)
    print(f"Today's Tasks are \n{tasks}")


    while True:#this is a main part where you choose  wahat u want to do
        operation=int( input("Enter 1-ADD \n 2-Update \n 3-Delete \n 4-view \n 5-Exit/stop"))
        if operation==1:
            add=input("enter tasks you want to add: ")
            tasks.append(add)
            print(f"Tasks {add}  have been added... ")
        
        elif operation ==2:
            update_val=input("Enter the tasks name you want to update:")
            if update_val in tasks:
                up =input("enter new task:")
                ind=tasks.index(update_val)
                tasks[ind] ==up
                print(f"Updated tasks {up}")
                
        elif operation==3:
            del_value=input("which task you want to delete")
            if del_value in task:
               ind=tasks.index(del_value)
               del tasks[ind]
               print(f"Tasks {del_value }  has been deleted")
       
        elif operation==4:
            print(f"Total Tasks ={tasks}")
        
        elif operation==5:
            print("Closing the program....")
            break

        else:
            print("invalid input")

