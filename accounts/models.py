from django.db import models
from library.models import Library
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Librarian(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    library = models.OneToOneField(Library, verbose_name=_("Library"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Librarian")
        verbose_name_plural = _("Librarians")

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Library_detail", kwargs={"pk": self.pk})

class Member(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    city = models.CharField(_("City"), max_length=150)

    class Meta:
        verbose_name = _("Member")
        verbose_name_plural = _("Members")

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("Library_detail", kwargs={"pk": self.pk})
