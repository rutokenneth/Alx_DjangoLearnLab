from django.db import models
from django.contrib.auth.models import User #django inbuilt user mode
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        permissions = (
            ('can_add_book','Can add a new book'),
            ('can_change_book','Can change an existing book'),
            ('can_delete_book','can delete a book'),
        )

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# new UserProfile Model
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin','Admin'),
        ('Librarian','Librarian'),
        ('Member','Member'),        
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MEMBER')
    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"

# signal to automatically create a new userProfile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user.instance)

# signal to automatically save UserProfile when a User instance is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
