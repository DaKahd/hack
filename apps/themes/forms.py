from django import forms

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', required=False)


class ProductSortForm(forms.Form):

    SORT_CHOICES = (
    ('lowest', 'Lowest to Highest Price'),
    ('highest', 'Highest to Lowest Price'),
    ('sale', 'By Sale Price'),
)

    sort_option = forms.ChoiceField(label='Sort By', choices=SORT_CHOICES, required=False)