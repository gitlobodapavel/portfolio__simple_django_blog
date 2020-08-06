from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(blank=True, null=True)


class Comment(models.Model):
    content = models.TextField(max_length=3000)
    author_name = models.CharField(max_length=30)
    author_surname = models.CharField(max_length=30)
    author_email = models.EmailField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    response = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.author_email)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.post.title


