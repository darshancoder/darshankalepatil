from django import forms

class CustomerRegistration(forms.Form):
      name = forms.CharField()
      email = forms.EmailField()
      subject = forms.CharField()


      def clean_name(self):
            valname = self.cleaned_data['name']
            if len(valname)<4:
                  raise forms.validationError("Enter Name greater than ")