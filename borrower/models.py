from django.db import models
from django.contrib.auth.models import User


class Borrower(models.Model):
    SECTORS = (
        ('re', 'Retail'),
        ('pf', 'Professional Services'),
        ('fd', 'Food & Drink'),
        ('en', 'Entertainment'),
    )
    # links a Borrower to User.
    user = models.OneToOneField(User)

    # The additional attributes
    phone = models.IntegerField(null=True)
    company_name = models.CharField(max_length=20)
    company_address = models.CharField(max_length=100)
    company_number = models.IntegerField(null=True)
    company_sector = models.CharField(max_length=20, choices=SECTORS)
    loan_amount = models.IntegerField(null=True)
    loan_period = models.IntegerField(null=True)
    loan_reason = models.TextField()


User.profile = property(lambda u: Borrower.objects.get_or_create(user=u)[0])
