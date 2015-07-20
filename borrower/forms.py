from django import forms

from borrower.models import Borrower


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['phone',
                  'company_name',
                  'company_address',
                  'company_number',
                  'company_sector',
                  'loan_amount',
                  'loan_period',
                  'loan_reason']
