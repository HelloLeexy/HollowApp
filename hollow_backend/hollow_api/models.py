# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
  def create_user(self, username, password=None, **extra_fields):
    user = self.model(username=username, **extra_fields)
    user.set_password(password)

    user.save(using=self._db)
    return user

  def create_superuser(self, username, password=None, **extra_fields):
    extra_fields.setdefault('is_superuser', True)

    return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=30)
  age = models.CharField(max_length=30, default='')
  dob = models.CharField(max_length=30, default='')
  yearOfStudy = models.CharField(max_length=30, default='')
  programme = models.CharField(max_length=30, default='')
  aboutMe = models.CharField(max_length=50, default='')
  selectedCoursesString = models.CharField(max_length=300, default='')  # Updated max_length to 100 characters
  user_id = models.CharField(max_length=36, unique=True, default='')  # Add a field for user_id
  img = models.CharField(max_length=30, default='')
  objects = CustomUserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['user_id']  # Add 'user_id' to REQUIRED_FIELDS

  def __str__(self):
    return self.username

class Post(models.Model):
  # 定义外键关联到 CustomUser 模型
  poster = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  content = models.TextField()
  publish_date = models.DateTimeField(default=timezone.now)
  classification = models.CharField(max_length=100)
  views_count = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)

  def increment_views(self):
    self.views_count += 1
    self.save()

  def increment_likes(self):
    self.likes += 1
    self.save()

  def create(cls, poster_id, title, content, author, classification):
    post = cls(poster_id=poster_id, title=title, content=content, author=author, classification=classification)
    return post

#comment
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
      return f"Comment by {self.user.username} on {self.post.title}"

#history
class UserPostHistory(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"User: {self.user.username}, Post: {self.post.title}, Timestamp: {self.timestamp}"



class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"{self.user.username} favorites {self.post.title}"



class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(CustomUser, related_name='followers', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
