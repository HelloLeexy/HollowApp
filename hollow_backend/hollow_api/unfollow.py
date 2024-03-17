from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import CustomUser, Follow
import json
@require_POST
def unfollow_user(request):
    try:
        data = json.loads(request.body)  # Assuming data is sent as form data
        user_id = data.get('userID')
        target_user_id = data.get('posterID')

        # Get the corresponding user objects
        user = CustomUser.objects.get(user_id=user_id)
        target_user = CustomUser.objects.get(user_id=target_user_id)

        # Check if the follow relationship exists
        existing_follow = Follow.objects.filter(follower=user, followed=target_user).exists()

        if existing_follow:
            # Remove the follow relationship
            follow = Follow.objects.get(follower=user, followed=target_user)
            follow.delete()

            return JsonResponse({'success': True, 'message': f'You have unfollowed {target_user.username}.'})
        else:
            return JsonResponse({'success': False, 'message': 'You are not following this user.'})

    except Exception as e:
        # Log the error
        print(f'Error unfollowing user: {str(e)}')
        return JsonResponse({'success': False, 'message': 'Error unfollowing user'})
