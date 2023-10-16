from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone 
from django.core import exceptions as django_exceptions


class CustomizeUser(BaseUserManager):

    def create_user(self, email, **kwargs):
        try:
           
            
            if not email:
                raise ValueError("Provide Email")
            email = self.normalize_email(email)
            now = timezone.now()

            user = self.model(
                email = email,
                last_login=now,
                date_joined=now,
                **kwargs
                )
            

            if kwargs.get('password') is not None: 
                
                user.set_password(kwargs['password'])
            user.is_active = True
            user.save()

            return user

        except django_exceptions.ValidationError as e:
            
            print(e)
            
    
    def create_superuser(self, email, **kwargs):

        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError("User Must be Staff")
        if kwargs.get('is_superuser') is not True:
            raise ValueError("User Must be Super User")
        if kwargs.get('is_active') is not True:
            raise ValueError("User Must be active")
        
        return self.create_user(email, **kwargs)
