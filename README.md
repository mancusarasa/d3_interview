# Task tracker

This project implements the backend of a task tracker platform. It exposes the following features:

* Present visually a list of tasks in 3 different states: Planned, In Progress, Completed.
* Each task contains, name, description, estimate and state.
* The user needs to be able to add/remove and change the state of the tasks.
* Somewhere in the application you need to present an up to date status, adding up all hours for each state.

It doesn't offer any sort of authentication capabilities.

# How to start the API

The API is fully virtualized, using docker-compose. To build and run it, follow these steps:

```shell
$ docker-compose build && docker-compose up
```

Alternatively, you can create a virtualenv, install the dependencies in it, and run the API locally, like so:

```shell
$ mkdir venv/
$ virtualenv --python=python3 venv/
$ . ./venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```

However, note that the API functionality depends on Django models, which in turn depend on the database (PostgreSQL, in this case), so running the API in you host will probably be somewhat tricky.

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
    "Planned": [
        {
            "id": 1,
            "name": "Task 1",
            "description": "a new task",
            "estimate": 20,
            "state": "Planned"
        }
    ],
    "In Progress": [],
    "Completed": []
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

In order to run unit tests, use the provided `docker-compose-test.yml` file, like so:

```shell
docker-compose -f docker-compose-test.yml build && docker-compose -f docker-compose-test.yml up --abort-on-container-exit --exit-code-from task_tracker
```

You'll get a bunch of output from PostgreSQL (since the tests need interaction with the database), and then at the end the result of your tests:

```shell
task_tracker_1  | test_create_task_in_non_default_state_creates_the_task_in_correct_state (task_tracker.tests.test_task_collection.TaskCollectionTests) ... ok
task_tracker_1  | test_create_task_with_correct_fields_creates_the_task (task_tracker.tests.test_task_collection.TaskCollectionTests) ... ok
task_tracker_1  | test_create_task_without_mandatory_fields_returns_error (task_tracker.tests.test_task_collection.TaskCollectionTests) ... ok
task_tracker_1  | test_deleting_created_task_removes_it_from_the_collection (task_tracker.tests.test_task_detail.TaskDetailTests) ... ok
task_tracker_1  | test_retrieving_created_task_returns_it_correctly (task_tracker.tests.test_task_detail.TaskDetailTests) ... ok
task_tracker_1  | test_updating_task_status_changes_task (task_tracker.tests.test_task_detail.TaskDetailTests) ... ok
task_tracker_1  | test_state_without_tasks_returns_zero (task_tracker.tests.test_tasks_status.TaskStatusTest) ... ok
task_tracker_1  | test_tasks_in_different_states_are_summarized_correctly (task_tracker.tests.test_tasks_status.TaskStatusTest) ... ok
task_tracker_1  | 
task_tracker_1  | ----------------------------------------------------------------------
task_tracker_1  | Ran 8 tests in 0.258s
task_tracker_1  | 
task_tracker_1  | OK
task_tracker_1  | Destroying test database for alias 'default' ('test_tasks_tracker')...

```

Alternatively, create a virtualenv and then run the Django test command:


```shell
$ virtualenv --python=python3 venv/
$ . ./venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py test
```

But note that unit tests are coupled with Django models, which in turn are coupled to the database (PostgreSQL, in this case), so running these tests locally will probably be somewhat tricky.
