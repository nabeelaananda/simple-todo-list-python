todo_list = []

while True:
  print("Options:")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) View Task")
  print("4) Quit")
  choice = input("Choose 1/2/3/4: ")
  if choice == "1":
    print("Adding task")
    new_task = input()
    todo_list.append(new_task)
    print("Task succesfully added!")
  elif choice == "2":
    if todo_list:
      try:
        task_num_to_remove = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num_to_remove <= len(todo_list):
          removed_task = todo_list.pop(task_num_to_remove - 1)
          print(f"Task '{removed_task}' removed!")
        else:
          print("Invalid task number.")
      except ValueError:
        print("Please enter a valid number.")
    else:
      print("No tasks to remove.")
  elif choice == "3":
    if not todo_list:
      print("Your ToDo list is empty.")
    else:
      print("\n--- Your ToDo List ---")
      index = 1
      for task in todo_list:
        print(f"{index}. {task}")
        index += 1
      print("----------------------")
  elif choice == "4":
    print("Quitting")
    break
  else:
    print("Invalid number! Try again.")
