from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):
    choices=(('student','student'),('manager','manager'))
    user_type = forms.ChoiceField(choices=choices)
 
    def save(self, request):
         user = super(CustomSignupForm, self).save(request)
         user.user_type = self.cleaned_data['user_type']
         user.save()
         return user

from allauth.socialaccount.forms import SignupForm 
class MyCustomSocialSignupForm(SignupForm):
    choices=(('student','student'),('manager','manager'))
    user_type = forms.ChoiceField(choices=choices)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save(request)

        # Add your own processing here.
        user.user_type = self.cleaned_data['user_type']
        user.save()
        # You must return the original result.
        return user