from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmailVerify(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE) # here we are creating a model with the relation of OnetoOneField(User) so that effective email verification can be perform.
    auth_token = models.CharField(max_length=250) # auth_token model field uses to store the token value
    token_verified = models.BooleanField(default=False) # token_verified field uses to check either token is verifed or not if yes then boolean value will be true else boolean value will be false
    token_generated_date = models.DateTimeField(auto_now_add=True) # this will added the date automatically whenever the token is generated
 
    def __str__(self) -> str:
        return self.user.username
    