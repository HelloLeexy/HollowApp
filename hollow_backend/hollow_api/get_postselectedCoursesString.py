from django.http import JsonResponse
from hollow_api.models import CustomUser
from django.views.decorators.http import require_GET
from django.core.serializers import serialize
from django.views.decorators.http import require_POST
import json

@require_POST
def get_selected_courses(request):

  try:
    data = json.loads(request.body)
    user_id = data.get('userID')
    user = CustomUser.objects.get(user_id=user_id)
    selected_courses = user.selectedCoursesString
    return JsonResponse({'selectedCourses': selected_courses})
  except CustomUser.DoesNotExist:
    return JsonResponse({'selectedCourses': []})
