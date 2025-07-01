from django.db import models
from django.contrib.auth.models import User

# Extend user with profile info if you need later
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Facility(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # cafe, restaurant, pg, etc.
    address = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to="facility_images", blank=True, null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.facility.name}"

