from rest_framework import serializers

from task_tracker.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'estimate', 'state']
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "required": "Task name is required",
                },
            },
            "description": {
                "error_messages": {
                    "required": "Description is required",
                },
            },
            "estimate": {
                "error_messages": {
                    "required": "Estimate is required",
                },
            },
        }
