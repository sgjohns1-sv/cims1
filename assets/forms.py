from django import forms

class NewAssetForm(forms.Form):
    manufacturer = forms.CharField(label="Manufacturer", max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    sn = forms.CharField(label="Serial Number", max_length=50)
    cost = forms.CharField(label="Cost", max_length=7)
    purchaseDate = forms.DateField(label="Purchase Date")
    eolDate = forms.DateField(label="EOL Date")
    notes = forms.CharField(label="Notes", max_length=500)
