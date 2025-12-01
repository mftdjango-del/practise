from django import forms

from contact_app.models import ContactModel


# class ContactForm(forms.Form):
#     image = forms.ImageField(widget=forms.FileInput(attrs = {}))
#     name = forms.CharField(label="", max_length=70, min_length=1, required="required", widget=forms.TextInput(attrs={
#         "class": "form-control",
#         'placeholder': "نام"
#     }))
#     email = forms.EmailField(label="", max_length=50, min_length=6, required="required", widget=forms.EmailInput(attrs={
#         'class': "form-control",
#         'placeholder': "ایمیـل",
#     }))
#     subject = forms.CharField(max_length=200, min_length=3, required='required', widget=forms.TextInput(attrs={
#         'class': "form-control",
#         'placeholder': "موضـوع"
#     }))
#     message = forms.CharField(max_length=500, min_length=6, required="required", widget=forms.Textarea(attrs={
#         'id': "message",
#         'class': "form-control",
#         'rows': "8",
#         'placeholder': "پیغـام شمـا"
#     }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["image", "full_name", "email", "subject", "message"]
        widgets = {
            "image": forms.FileInput(attrs={
                "class": "form-control",
                'placeholder': "تصویر"
            }) ,
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                'placeholder': "نام"
            }),
            "email": forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': "ایمیـل",
            }),
            "subject": forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "موضـوع"
            }),
            "message": forms.Textarea(attrs={
                'id': "message",
                'class': "form-control",
                'rows': "8",
                'placeholder': "پیغـام شمـا"
            })
        }
    def clean_full_name(self):
        full_name:str = self.cleaned_data.get("full_name")
        full_name = full_name.replace(" ", "-").strip()
        if not 3 < len(full_name) < 40:
            raise forms.ValidationError("نام کاربری نامعتبر است")
        return full_name
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email = email.replace(" ", "")
        if not 3 < len(email) < 40:
            raise forms.ValidationError("ایمیل نامعتبر است")
        return email
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        old_message = ContactModel.objects.filter(email=email, status="PENDING").first()
        if old_message is not None:
            raise forms.ValidationError(message="شما یک پیام در صف بررسی دارید بعد از پاسخ ادمین امکان ارسال مجدد پیام هست")
        return cleaned_data