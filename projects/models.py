import uuid
from django.db import models
from data.data import MyInfo
from django.utils.text import slugify
from django.contrib.auth.models import User


class Projects(models.Model):

    LANGUAGE_CHOICES = [
        (ln.lower(), ln) for ln in MyInfo.PROGRAMMING_LANGUAGES['backend']
        ]

    STATUS_CHOICES = [
        ('Completed', 'completed'),
        ('In Progress', 'in progress'),
    ]

    title = models.CharField(max_length=100)
    # Slug (URL uchun: masalan-loyiha-nomi)
    slug = models.SlugField(unique=True, null=True, blank=True)

    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='python')
    description = models.TextField(null=True, blank=True)

    # Media
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    document = models.FileField(upload_to='project_files/', null=True, blank=True)

    # Linklar
    github_url = models.URLField(max_length=200, null=True, blank=True)
    live_url = models.URLField(max_length=200, null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def save(self, *args, **kwargs):
        if not self.slug:
            # Sarlavhadan slug yasaymiz
            base_slug = slugify(self.title)
            # Agar bunday slug bo'lsa, oxiriga tasodifiy harf qo'shamiz
            if Projects.objects.filter(slug=base_slug).exists():
                self.slug = f"{base_slug}-{uuid.uuid4().hex[:4]}"
            else:
                self.slug = base_slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(Projects, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Eng yangi izohlar tepada turadi

    def __str__(self):
        return f"Comment by {self.author.username} on {self.project.title}"