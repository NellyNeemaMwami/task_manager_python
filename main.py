tasks =[]
def add_task():
    name = input('Enter task name: ')
    description = input('Enter task description: ')
    priority = input('Enter task priority: ')
    due_date = input('Enter task due date: ')
    notes = input('Enter task notes: ')

    task = {
        'id': f'task_{len(tasks) + 1}',
        # calculate the task id based on the number of tasks in the list
        'name': name,
        'description': description,
        'status': 'pending',
        'priority': priority,
        'due_date': due_date,
        'notes': notes
    }
    tasks.append(task)
    # append the task(dictionary) to the tasks list
