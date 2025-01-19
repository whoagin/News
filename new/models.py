from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.urls import reverse
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = Post.objects.filter(author=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        posts_comments_rating = Comment.objects.filter(post__author=self).aggregate(pcr=Coalesce(Sum('rating'), 0))[
            'pcr']
        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Post(models.Model):
    news = 'NE'
    article = 'AR'
    post_type = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    article_or_news = models.CharField(max_length=10, choices=post_type, default=article)
    category = models.ManyToManyField(Category, through=PostCategory)
    publication_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    @property
    def preview(self):
        return f'{self.text[:123]}...'

    def as_tuple(self):
        return (
            self.author.user.username, self.rating, self.preview, self.publication_date
        )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
