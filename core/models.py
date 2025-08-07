from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class CustomUserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, email, username, password=None, **extra_fields):
        """Create and saves a User with the given email, username and password."""
        if not email:
            raise ValueError('Email is required.')
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and saves a superuser with the given email,username and password."""
        if not email:
            raise ValueError('Email is required')
        
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields
        )
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model representing a system user."""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """Return string representation of the user."""
        return self.email
