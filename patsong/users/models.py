from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    """ User model """

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    LEAVE_CHOICES = (
        ('정상 회원', '정상 회원'),
        ('탈퇴한 회원', '탈퇴한 회원'),
    )

    phone = CharField(max_length=140, blank=True, null=True)
    address = CharField(max_length=255, blank=True, null=True)
    postalcode = CharField(max_length=80, blank=True, null=True)
    social_number = CharField(max_length=80, blank=True, null=True)
    applicant_number = CharField(max_length=80, blank=True, null=True)
    cumulative_pay_amount = CharField(max_length=80, blank=True, null=True)
    cumulative_usage_count = CharField(max_length=80, blank=True, null=True)
    signature_image = CharField(max_length=80, blank=True, null=True)
    push_token = CharField(max_length=80, blank=True, null=True)
    note = CharField(max_length=2000, blank=True, null=True)
    is_leave = CharField(max_length=80, choices=LEAVE_CHOICES, blank=True, null=True)

    @property
    def count_cases(self):
        return self.cases.all().count()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})