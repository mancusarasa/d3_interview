from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TaskStatusTest(APITestCase):
    def test_tasks_in_different_states_are_summarized_correctly(self):
        planned_tasks = [
            self._create_task({
                "name": "planned task",
                "description": "desc",
                "state": "Planned",
                "estimate": 10
            })
            for _ in range(3)
        ]
        in_progress_tasks = [
            self._create_task({
                "name": "in progress task",
                "description": "desc",
                "state": "In Progress",
                "estimate": 20
            })
            for _ in range(5)
        ]
        completed_tasks = [
            self._create_task({
                "name": "completed task",
                "description": "desc",
                "state": "Completed",
                "estimate": 30
            })
            for _ in range(4)
        ]
        tasks_status = self._retrieve_tasks_status()
        self.assertEqual(
            tasks_status,
            {
                "Planned": sum([t['estimate'] for t in planned_tasks]),
                "In Progress": sum([t['estimate'] for t in in_progress_tasks]),
                "Completed": sum([t['estimate'] for t in completed_tasks]),
            }
        )

    def test_state_without_tasks_returns_zero(self):
        planned_tasks = [
            self._create_task({
                "name": "planned task",
                "description": "desc",
                "state": "Planned",
                "estimate": 10
            })
            for _ in range(3)
        ]
        in_progress_tasks = [
            self._create_task({
                "name": "in progress task",
                "description": "desc",
                "state": "In Progress",
                "estimate": 20
            })
            for _ in range(5)
        ]
        tasks_status = self._retrieve_tasks_status()
        self.assertEqual(
            tasks_status,
            {
                "Planned": sum([t['estimate'] for t in planned_tasks]),
                "In Progress": sum([t['estimate'] for t in in_progress_tasks]),
                "Completed": 0,
            }
        )

    def _create_task(self, task_data):
        response = self.client.post(reverse("tasks-list"), task_data)
        return response.data

    def _retrieve_tasks_status(self):
        url = reverse("tasks-status")
        response = self.client.get(url)
        return response.data
