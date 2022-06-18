from django import forms
from .models import Contact, Invoice
from django.core.mail import send_mail
# from config.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','phone','email','subject','message']
    
    def get_info(self):
        
        cleaned_data = super().clean()

        name = cleaned_data.get('name').strip()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        subject = cleaned_data.get('subject')
        msg = f'Bonjour {name},'
        msg +=  "Octopus-consultung vous remercie de l'intérêt que vous portez à ses services, nous vous contacterons prochainement avec un e-mail détaillé concernant votre demande."
        
        msg +='Merci de votre temps,'
        
        msg +='Bien à vous, '
        return subject, msg, phone

    def send_email(self):

        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email= EMAIL_HOST_USER,
            recipient_list=EMAIL_RECIPIENT,
        )

def must_be_empty(value):
    if value:
        raise forms.ValidationError('ce champs doit etre vide')

# class ContactForm(forms.Form):
#     name = forms.CharField(required = True, max_length=150) 
#     email = forms.CharField(max_length=254)
#     phone = forms.CharField(max_length=25)
#     subject = forms.CharField(max_length=300) 
#     honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])
#     message = forms.CharField()    

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('client', 'client_rc', 'client_nif', 'client_art', 'client_adresse', 'invoice_number', 'invioce_date', 'note', 'discount',)
        required = ('client',)
       
