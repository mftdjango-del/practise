from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import EmailValidator, URLValidator
from django.core.validators import RegexValidator
# Create your models here.

class ContactModel(models.Model):
    STATUS_CHOICE = [
        ("PENDING", "pending message"),
        ("READ", "read message"),
        ("RESPONDED", "responded message")
    ]
    image = models.ImageField(upload_to="contact", null=True, blank=True)
    full_name = models.CharField(max_length=50, validators=[MaxLengthValidator(50, message="max length invalid must 50 character")])
    email = models.EmailField(max_length=50, help_text="ایمیل کاربر")
    subject = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="PENDING")
    response = models.TextField(null=True, blank=True)
    # meta data
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}-{self.subject}"

    class Meta:
        ordering = ["-create_at"]
