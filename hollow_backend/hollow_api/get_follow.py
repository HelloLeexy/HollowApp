# Assuming this is in your views.py

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Follow, CustomUser
import json
@require_POST
def get_follow(request):
    try:
        # Extract user ID from the JSON payload
        data = json.loads(request.body)  # Assuming data is sent as form data
        user_id = data.get('userID')

        # Get the user for the provided ID
        user = CustomUser.objects.get(user_id=user_id)

        # Get the users the provided user is following
        following_users = Follow.objects.filter(follower=user).select_related('followed')

        # Get the users who are following the provided user
        followers = Follow.objects.filter(followed=user).select_related('follower')

        # Extract user details from the Follow objects
        following_data = [
            {
                'user_id': follow.followed.user_id,
                'username': follow.followed.username,
                'aboutMe': follow.followed.aboutMe,
                'dbo':follow.followed.dob,
                'studyOfYear':follow.followed.yearOfStudy,
                'img': follow.followed.img,
            }
            for follow in following_users
        ]
        followers_data = [
            {
                'id': follow.followed.user_id,
                'username': follow.followed.username,
                'aboutMe': follow.followed.aboutMe,
                'img': follow.followed.img,
            }
            for follow in followers
        ]

        return JsonResponse({'success': True, 'following': following_data})
    except CustomUser.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'User not found'}, status=404)
    except Exception as e:
        print(f'Error fetching follow data: {str(e)}')
        return JsonResponse({'success': False, 'message': 'Error fetching follow data'})
