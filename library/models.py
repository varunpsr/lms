from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from datetime import datetime, timedelta

# Create your models here.
class Library(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    city = models.CharField(_("City"), max_length=50)
    is_active = models.BooleanField(_("Is Active"), default=False)
    fine_per_day =  models.IntegerField(_("Fine Per Day"), null=False, blank=False)

    class Meta:
        verbose_name = _("Library")
        verbose_name_plural = _("Libraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Library_detail", kwargs={"pk": self.pk})
