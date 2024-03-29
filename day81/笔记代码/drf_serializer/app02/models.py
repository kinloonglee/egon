from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.IntegerField()
    pub_date=models.DateField()
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE,null=True)
    authors=models.ManyToManyField("Author")
    def __str__(self):
        return self.title
    def test(self):
        return 'lqz is big'

class Publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()
    # def __str__(self):
    #     return self.name+'ccccc'

class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    def __str__(self):
        return self.name