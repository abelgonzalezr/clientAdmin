from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)


    def __str__(self):
        return f"Address of {self.client}: {self.address}, {self.city}"
