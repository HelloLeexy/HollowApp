# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import uuid
import random
from hollow_api.models import CustomUser


@csrf_exempt
@require_POST
def create_account(request):
  try:
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    age = data.get('age')
    dob = data.get('dob')
    yearOfStudy = data.get('yearOfStudy')
    programme = data.get('programme')
    aboutMe = data.get('aboutMe')
    selectedCoursesString = data.get('selectedCoursesString')
    # Generate a unique UserID using UUID
    user_id = str(uuid.uuid4())
    img = str(random.randint(1, 9))

    # Create a new user with the provided data and generated UserID
    user = CustomUser.objects.create_user(
      username=username,
      password=password,
      age=age,
      dob=dob,
      yearOfStudy=yearOfStudy,
      programme=programme,
      aboutMe=aboutMe,
      selectedCoursesString=selectedCoursesString,
      user_id=user_id,
      img = img,
      # Add other fields as needed
    )

    # Perform logic to create user account in the database
    user.save()

    # Return the generated UserID to the frontend
    return JsonResponse({'success': True, 'message': 'Account created successfully', 'userID': user_id})
  except Exception as e:
    return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
