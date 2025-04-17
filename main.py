"""ToDo Liste"""
todo_inhalt = []

print("ToDo Liste gestartet\nBefehle:\nnew - erstellen\nexit - schließen\nshow - todos zeigen\ndelete - löschen eines tasks")

running = True
while (running):
    print("________________")
    input_1 = input()
    if (input_1 == "new"):
        task_name = str(input("Bitte namen eingeben\n"))
        if task_name:
            todo_inhalt.append(task_name)
        else:
            print("ungültiger wert")

    elif (input_1 == "exit"):
        running = False
    
    elif (input_1 == "show"):
        print(f"anzahl an aufgaben: {len(todo_inhalt)}")
        for task in todo_inhalt:
            print(task)
    
    elif (input_1 == "delete"):
        to_delete_task = input("Welche aufgabe soll gelöscht werden?")
        todo_inhalt.remove(to_delete_task)

print("Programm wird geschlossen")
