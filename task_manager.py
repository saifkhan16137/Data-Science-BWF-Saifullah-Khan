class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'status': 'pending'
        }
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                self._display_task(task)

    def update_task(self, task_id, title=None, description=None, status=None):
        task = self._find_task_by_id(task_id)
        if task:
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            print(f"Task ID {task_id} updated successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def delete_task(self, task_id):
        task = self._find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"Task ID {task_id} deleted successfully.")
        else:
            print(f"Task ID {task_id} not found.")

    def _find_task_by_id(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

    def _display_task(self, task):
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print("-" * 20)
