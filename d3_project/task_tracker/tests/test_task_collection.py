from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskCollectionTests(APITestCase):
    def test_create_task_with_correct_fields_creates_the_task(self):
        new_task = self._assert_task_is_created_correctly({
            "name": "task 1",
            "estimate": 3,
            "description": "some description"
        })
        collection = self.client.get(reverse("tasks-list")).data
        self.assertEqual(collection, {
            "Planned": [new_task],
            "In Progress": [],
            "Completed": []
        })

    def test_create_task_without_mandatory_fields_returns_error(self):
        # this task is missing the "name" field
        task_data = {
            "estimate": 3,
            "description": "some description"
        }
        response = self.client.post(reverse("tasks-list"), task_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        collection = self.client.get(reverse("tasks-list")).data
        self.assertEqual(collection, {
            "Planned": [],
            "In Progress": [],
            "Completed": []
        })

    def test_create_task_in_non_default_state_creates_the_task_in_correct_state(self):
        planned_task = self._assert_task_is_created_correctly({
            "name": "Planned task",
            "estimate": 10,
            "description": "a planned task",
            "state": "Planned"
        })
        in_progress_task = self._assert_task_is_created_correctly({
            "name": "In Progress task",
            "estimate": 10,
            "description": "a task in progress",
            "state": "In Progress"
        })
        completed_task = self._assert_task_is_created_correctly({
            "name": "Completed task",
            "estimate": 20,
            "description": "a completed task",
            "state": "Completed" 
        })
        collection = self.client.get(reverse("tasks-list")).data
        self.assertEqual(collection, {
            "Planned": [planned_task],
            "In Progress": [in_progress_task],
            "Completed": [completed_task]
        })

    def _assert_task_is_created_correctly(self, task_data):
        response = self.client.post(reverse("tasks-list"), task_data)
        task = response.data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for field, value in task_data.items():
            self.assertEqual(task[field], value)
        return task
