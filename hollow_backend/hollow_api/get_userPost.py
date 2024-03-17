from django.http import JsonResponse
from hollow_api.models import Post, CustomUser  # Import CustomUser model
from django.views.decorators.http import require_GET
import json
from django.views.decorators.http import require_POST

@require_POST
def get_user_post(request):
  try:
    # 获取所有帖子
    data = json.loads(request.body)
    user_id = data.get('userID')
    # 使用 filter 获取指定用户的所有帖子
    posts = Post.objects.filter(poster__user_id=user_id)

    # 使用 Django 的序列化器将帖子转换为 JSON 格式
    serialized_posts = []

    for post in posts:
      # 获取关联用户的用户名
      poster_username = post.poster.username if post.poster else None
      img = post.poster.img if post.poster else None  # Check if the poster exists
      # 将帖子数据转为字典
      post_dict = {
        'pk': post.pk,
        'img': img,
        'poster': poster_username,
        'title': post.title,
        'content': post.content,
        'publish_date': post.publish_date,
        'classification': post.classification,
        'views_count': post.views_count,
        'likes': post.likes,
      }

      serialized_posts.append(post_dict)

    serialized_posts.reverse()  # Move this outside of the loop
    # 返回 JSON 响应
    return JsonResponse({'success': True, 'posts': serialized_posts})
  except Exception as e:
    # 记录错误日志
    print(f'Error getting posts: {str(e)}')
    return JsonResponse({'success': False, 'message': 'Error getting posts'})
