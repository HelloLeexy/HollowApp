from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Favorite, CustomUser
from django.views.decorators.http import require_POST
import json

@require_POST
def get_user_favorite_posts(request):
    try:
        # Retrieve the user based on the user_id provided in the request

        data = json.loads(request.body)
        user_id = data.get('userID')
        user = get_object_or_404(CustomUser, user_id=user_id)

        # Retrieve the user's favorite posts
        favorite_posts = Favorite.objects.filter(user=user).values_list('post_id', flat=True)

        # Retrieve the details of the favorite posts
        favorite_post_details = Post.objects.filter(id__in=favorite_posts).values('id')

        # Convert the queryset to a list for JsonResponse
        favorite_post_list = list(favorite_post_details)
        # Return the favorite posts data as JSON
        return JsonResponse({'favorite_posts': favorite_post_list})

    except CustomUser.DoesNotExist:
        # Return a 404 response if the user is not found
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        # Handle other exceptions and return an error response
        return JsonResponse({'error': str(e)}, status=500)
