from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.IntegerField()
    door_number = models.IntegerField()


class Telephone(models.Model):
    number = models.IntegerField()
    types = (("1", "Home Number"), ("2", "Work Number"))
    type = models.CharField(choices=types, default=1, max_length=32)


class Email(models.Model):
    email = models.CharField(max_length=32)
    types = (("1", "Home Email"), ("2", "Work Email"))
    type = models.CharField(choices=types, default=1, max_length=32)


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    telephone = models.ForeignKey(Telephone, on_delete=models.CASCADE, null=True)
    e_mail = models.ForeignKey(Email, on_delete=models.CASCADE, null=True)
    description = models.TextField()
