from django.db import models
from django_mysql.models import ListCharField

# Create your models here.


class Database(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    superCategory = models.CharField(max_length=50)  # topwear, bottomwear
    subCategories = ListCharField(
        base_field=models.CharField(max_length=20),
        size=20,
        max_length=(20 * 21),  # 20 * 21 character nominals, plus commas
    )
    color = models.CharField(max_length=15)
    brandName = models.CharField(max_length=25)
    availableSize = ListCharField(
        base_field=models.CharField(max_length=10),
        size=20,
        max_length=(20 * 11),  # 20 * 11 character nominals, plus commas
    )
    age = models.CharField(max_length=5)
    season = models.CharField(max_length=10)
    image = models.FileField(upload_to='productImages', default=None)
    imageName = models.CharField(max_length=50)

    def __str__(self): 
        return self.brandName + '\'s ' + self.color + ' ' + self.name + ' for ' + self.gender + ' of sizes ' + '-'.join([str(elem) for elem in self.availableSize]) + ' ( ' + self.superCategory + ' ) '