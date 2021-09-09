from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import UUIDField
from django.utils.translation import gettext_lazy as _
import uuid
from . manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    image = models.ImageField(verbose_name=_("Image"), upload_to= 'profile_pictures', default= 'default.jpg')
    first_name = models.CharField(verbose_name= _("First Name"), max_length=30)
    last_name = models.CharField(verbose_name= _("Last Name"), max_length=30)
    email = models.EmailField(verbose_name= _("Email"), unique= True)
    age = models.IntegerField(verbose_name= _("Age"))
    uuid_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, unique=True)
    unique_id = models.CharField(verbose_name= _("Unique Id"), max_length=8, blank= True, null= True, unique= True)

    def __init__(self, **kwargs):
        if self.unique_id is None:
            kwargs['max_length'] = 8
            self.unique_id = self.uuid_id
            return super(CustomUser, self).__init__(**kwargs)
              

    def __str__(self):
        return self.first_name

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []



