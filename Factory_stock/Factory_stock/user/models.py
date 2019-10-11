from django.db import models
from django.contrib.auth.models import User


number = models.CharField(max_length=10, default='7777777777')
number.contribute_to_class(User, 'number')

address = models.TextField(default='Bopal')
address.contribute_to_class(User, 'address')