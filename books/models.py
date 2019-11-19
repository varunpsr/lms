from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.urls import reverse
from library.models import Library
from accounts.models import Member, Librarian
from datetime import date, timedelta


# Create your models here.

class Author(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})

class Publication(models.Model):
    name = models.CharField(_("Name"), max_length=200)

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Publication_detail", kwargs={"pk": self.pk})

class Language(models.Model):
    name = models.CharField(_("name"), max_length=100)

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Language_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    name = models.CharField(_("name"), max_length=250)
    author = models.ForeignKey(Author, verbose_name=_("Author"), on_delete=models.CASCADE, null=False, blank=False)
    publication = models.ForeignKey(Publication, verbose_name=_("Publication"), on_delete=models.CASCADE, null=False, blank=False)
    price = models.FloatField(_("price"), null=False, blank=False)
    summary = models.TextField(_("summary"), null=True, blank=True)
    language = models.ForeignKey(Language, verbose_name=_("Language"), on_delete=models.CASCADE)
    isbn = models.CharField(_("isbn"), max_length=13, null=False, blank=False)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})


class LibraryBooks(models.Model):
    AVAILABLE = 'AL'
    ON_LOAN = 'OL'
    BOOKED = 'BK'
    BOOK_STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('ON_LOAN', 'On Loan'),
        ('BOOKED', 'Booked'),
    ]
    library = models.ForeignKey(Library, verbose_name=_("Library"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=2, choices=BOOK_STATUS_CHOICES, default=AVAILABLE)

    class Meta:
        verbose_name = _("Library Books")
        verbose_name_plural = _("Library Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("LibraryBooks_detail", kwargs={"pk": self.pk})

class IssuedBook(models.Model):
    member = models.ForeignKey(Member, verbose_name=_("Member"), on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, verbose_name=_("Book"), on_delete=models.DO_NOTHING)
    date_of_issue = models.DateField(_("Date of Issue"), auto_now_add=True)
    date_of_return = models.DateField(_("Date of Return"), default=date.today()+timedelta(days=7))
    actual_date_of_return = models.DateField(_("Actual Date of Return"), auto_now=False, auto_now_add=False, null=True, blank=True)
    librarian = models.ForeignKey(Librarian, verbose_name=_("Librarian"), on_delete=models.CASCADE)
    library = models.ForeignKey(Library, verbose_name=_("Library"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Issued Book")
        verbose_name_plural = _("Issued Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("IssuedBook_detail", kwargs={"pk": self.pk})
