from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        exclude = ('is_active', 'token', 'merchant',)
    def save(self, merchant, *args, **kwargs):
        commit = kwargs.pop('commit', True)
        kwargs['commit'] = False
        store = super().save(*args, **kwargs)
        store.merchant = merchant
        # store.save()
        if commit:
            print ('commit', commit)
            store.save()
        return store
    # def __init__(self, *args, **kwargs):
    #     super(StoreForm, self).__init__(*args, **kwargs)
        # print (self.fields['email'], self.request.user.email)
        # self.fields['email'].initial = self.request.user.email
