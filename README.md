# Task tracker

This project implements the backend of a task tracker platform. It exposes the following features:

* Present visually a list of tasks in 3 different states: Planned, In Progress, Completed.
* Each task contains, name, description, estimate and state.
* The user needs to be able to add/remove and change the state of the tasks.
* Somewhere in the application you need to present an up to date status, adding up all hours for each state.

It doesn't offer any sort of authentication capabilities.

# How to start the API

```shell
$ mkdir venv/
$ virtualenv --python=python3 venv/
$ . ./venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py runserver
```

# How to use the API

The API exposes endpoints to perform several operations regarding the management of tasks:

- Creating a new task:

```shell
$ curl -H "Content-Type: application/json" -X POST localhost:8000/tasks/ -d '{"name":"Task 1","description":"a new task", "state": "Planned", "estimate": 20}'
{
    "id": 1,
    "name": "Task 1",
    "description": "a new task",
    "estimate": 20,
    "state": "Planned"
}
```

- Retrieving the full list of tasks:

```shell
$ curl -X GET localhost:8000/tasks/
{
    "id": 1,
    "name": "Task 1",
    "description": "a new task",
    "estimate": 20,
    "state": "Planned"
}
```

- Retrieving the full status of our tasks, which contains the consolidate time for each task state:

```shell
$ curl -X GET localhost:8000/tasks/status
{
    "Planned": 20,
    "In Progress": 0,
    "Completed": 0
}
```

- Retrieving a particular task, which returns the full representation of a task:

```shell
$ curl -X GET localhost:8000/tasks/1
{
    "id": 1,
    "name": "Task 1",
    "description": "a new task",
    "estimate": 20,
    "state": "Planned"
}
```

- Changing the state of a task:

```shell
$ curl -H "Content-Type: application/json" -X PATCH localhost:8000/tasks/1 -d '{"state": "In Progress"}'
{
    "id": 1,
    "name": "Task 1",
    "description": "a new task",
    "estimate": 20,
    "state": "In Progress"
}
```

- Deleting a task:

```shell
$ curl -X DELETE localhost:8000/tasks/1
{
    "id": 1,
    "name": "Task 1",
    "description": "a new task",
    "estimate": 20,
    "state": "In Progress"
}
```

# Testing

To run the unit tests suite, create a virtualenv and then run the Django test command:

```shell
$ virtualenv --python=python3 venv/
$ . ./venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py test
```
