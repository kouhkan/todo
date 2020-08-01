from .models import Todo
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


# def index(request):
# 	todo_list = []
#
# 	for todo in Todo.objects.all():
# 		todo_list.append({
# 			'title': todo.title,
# 			'description': todo.description,
# 			'do_date': todo.do_date,
# 			'status': todo.status,
# 		})
#
# 	return JsonResponse(todo_list)