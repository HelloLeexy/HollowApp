from django.http import JsonResponse
from hollow_api.models import Post
from django.views.decorators.http import require_GET
from django.core.serializers import serialize

@require_GET
def get_posts(request):
    try:
        # 获取所有帖子
        posts = Post.objects.all()

        # 使用 Django 的序列化器将帖子转换为 JSON 格式
        serialized_posts = []

        for post in posts:
            # 获取关联用户的用户名
            poster_username = post.poster.username if post.poster else None
            poster_id = post.poster.user_id
            img = post.poster.img
            # 将帖子数据转为字典
            post_dict = {
                'id':post.id,
                'pk': post.pk,
                'img': img,
                'poster_id':poster_id,
                'poster': poster_username,
                'title': post.title,
                'content': post.content,
                'publish_date': post.publish_date,
                'classification': post.classification,
                'views_count': post.views_count,
                'likes': post.likes,
            }

            serialized_posts.append(post_dict)
            serialized_posts.reverse()
        # 返回 JSON 响应
        return JsonResponse({'success': True, 'posts': serialized_posts})
    except Exception as e:
        # 记录错误日志
        print(f'Error getting posts: {str(e)}')
        return JsonResponse({'success': False, 'message': 'Error getting posts'})
