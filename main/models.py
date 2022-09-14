from django.db import models


class Contact(models.Model):
    fio=models.CharField(max_length=250)
    email=models.EmailField(default='example@gmail.com')
    phone=models.CharField(max_length=50)
    topic=models.CharField(max_length=100)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic