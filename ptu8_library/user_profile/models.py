from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='profile',
        unique=True,
    )
    # user = models.ForeignKey(
    #     get_user_model(), 
    #     verbose_name=_("user"), 
    #     on_delete=models.CASCADE,
    #     related_name='profile',
    #     unique=True,
    # )
    photo = models.ImageField(
        _("photo"), 
        upload_to='user_profile/photos/',
        default='user_profile/photos/default.png',
        blank=True,
    )

    def __str__(self) -> str:
        return str(self.user)
