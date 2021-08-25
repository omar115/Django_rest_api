from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
# Create your models here.

# now we will create custom user model

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            raise ValueError("User Must have an email")
        
        # normalize will handle the upper and lowercase issues of email
        email = self.normalize_email(email)
        user = self.model(email=email)

        # set_password will make the password as hash
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    # is_staff gives you access similar to admin activities
    is_staff = models.BooleanField(default=False)   

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email