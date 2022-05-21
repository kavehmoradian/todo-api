from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TaskList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data)

class TaskDetail(APIView):
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
        except:
            return Response(status=404)
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)

    def put(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
        except:
            return Response(status=404)
        todo_serializer = TodoSerializer(todo, data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=200)
        return Response(todo_serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
        except:
            return Response(status=404)
        todo.delete()
        return Response(status=200)

class AddTask(APIView):
    def post(self, request):
        todo_serializer = TodoSerializer(data=request.data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=201)
        return Response(todo_serializer.errors, status=400)
