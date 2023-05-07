from django import forms
from navigation.models import MenuItem


class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].queryset = MenuItem.objects.filter(menu=self.instance.menu)
