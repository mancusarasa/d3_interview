from django.shortcuts import render
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics, status

from task_tracker.models import Task, TaskState
from task_tracker.serializers import TaskSerializer


class TaskListView(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        response = {state: [] for state in TaskState.values}
        for task in serializer.data:
            response[task['state']].append(task)
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetailView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskStatusView(APIView):
    def get(self, request):
        query_set = Task.objects.values('state').annotate(total_time=Sum('estimate'))
        response = {state: 0 for state in TaskState.values}
        for item in query_set:
            response[item['state']] = item['total_time']
        return Response(response, status=status.HTTP_200_OK)
