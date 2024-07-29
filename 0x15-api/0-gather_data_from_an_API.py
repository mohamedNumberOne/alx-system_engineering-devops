#!/usr/bin/python3
"""
Given an employee ID, returns information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        user = requests.get(user_url).json()
        todos = requests.get(todos_url).json()

        employee_name = user.get('name')
        total_tasks = len(todos)
        completed_tasks = [task for task in todos if task.get('completed')]

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, len(completed_tasks), total_tasks))

        for task in completed_tasks:
            print("\t {}".format(task.get('title')))

    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        sys.exit(1)
