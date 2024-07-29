#!/usr/bin/python3
"""
Given an employee ID, returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    userId = sys.argv[1]
    try:
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId)).json()
        name = user.get('name')

        todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                             .format(userId)).json()
        totalTasks = len(todos)
        completedTasks = [task for task in todos if task.get('completed')]

        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(completedTasks, totalTasks)))

        for task in completedTasks:
            print('\t {}'.format(task.get('title')))

    except requests.exceptions.RequestException as e:
        print("HTTP Request failed: {}".format(e))
    except ValueError:
        print("Invalid user ID")
