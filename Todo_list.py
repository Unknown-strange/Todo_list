def creat_list():
    print("Creat your list")
    user_input= input("Enter your list:  ")
    
    item_splits= user_input.split(",")
    todo_list = [item for item in item_splits]
    
    print(todo_list)
    list_editor(todo_list)
    

def list_editor(todo_list):
    while True:
        edit = input("what do you want to do with the list: ").lower()
        
        if edit == "add":
            print(todo_list)
            A_input = input("Add an item to the list: ")
            todo_list.append(A_input)
            print(todo_list)
            
        elif edit == "delete":
            print(todo_list)
            D_input = input("Delet an item: ")
            if D_input in todo_list:
                todo_list.remove(D_input)
                print(todo_list)
            else:
                print("Item not in list")
                
        else:
            print(todo_list)
        
        continue_list = input("Do you want to continue with the list yes/no : ").lower()
        if continue_list != "yes":
            break
    
    print(" ")
    
    next_effect = input("Do you want to prioritize you list?  ").lower()
    if next_effect == "yes":
        task_prioritisation(todo_list)
    elif next_effect == "no":
        for list in todo_list:
            print(list) 
        
        
def task_prioritisation(todo_list):
      task = {
          "1" : "very low urgent",
          "2" : " low urgency",
          "3" : "urgent",
          "4" : "very urgency",
          "5" : "extreamly urgent"
    }
      new_list = []
      print("")
      print("From a range of 1 to 5 how urgent are the items")
      for item in todo_list:
          task_input = input(f'how urgent is the task "{item}": ')
          if task_input in task:
            urgency = task[task_input]
            new_list.append(f"{item} - {urgency}")
            
          else:
              print("Invalid urgency number. Range between 1 to 5")
      for item in new_list:
        print(item)
      
          
    
if __name__ == "__main__":
   creat_list()
        
