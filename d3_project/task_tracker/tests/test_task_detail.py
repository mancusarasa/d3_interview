from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskDetailTests(APITestCase):
    def test_retrieving_created_task_returns_it_correctly(self):
        new_task = self._create_task({
            "name": "Planned task",
            "estimate": 10,
            "description": "a planned task",
            "state": "Planned"
        })
        retrieved_task = self._retrieve_task(new_task["id"])
        self.assertEqual(retrieved_task, new_task)

    def test_updating_task_status_changes_task(self):
        new_task = self._create_task({
            "name": "Planned task",
            "estimate": 10,
            "description": "a planned task",
            "state": "Planned"
        })
        self._edit_task(new_task["id"], {"state": "In Progress"})
        edited_task = self._retrieve_task(new_task["id"])
        self.assertEqual(edited_task["id"], new_task["id"])
        self.assertEqual(edited_task["name"], new_task["name"])
        self.assertEqual(edited_task["description"], new_task["description"])
        self.assertEqual(edited_task["state"], "In Progress")

    def test_deleting_created_task_removes_it_from_the_collection(self):
        new_task = self._create_task({
            "name": "Planned task",
            "estimate": 10,
            "description": "a planned task",
            "state": "Planned"
        })
        collection = self.client.get(reverse("tasks-list")).data
        self.assertEqual(collection, {
            "Planned": [new_task],
            "In Progress": [],
            "Completed": []
        })
        url = reverse("task-detail", args=[new_task["id"]])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        collection = self.client.get(reverse("tasks-list")).data
        self.assertEqual(collection, {
            "Planned": [],
            "In Progress": [],
            "Completed": []
        })

    def _create_task(self, task_data):
        response = self.client.post(reverse("tasks-list"), task_data)
        return response.data

    def _edit_task(self, task_id, new_data):
        url = reverse("task-detail", args=[task_id])
        response = self.client.patch(url, new_data)
        return response

    def _retrieve_task(self, task_id):
        url = reverse("task-detail", args=[task_id])
        response = self.client.get(url)
        return response.data
