from django.db import models


# you can add Generators by admin panel
# template has to be in format 'I like {a}, you like {b}, ...'
# par has to be in format 'a="chocolate", b="sweets",...'
class StringGenerator(models.Model):
    generator_id = models.AutoField(primary_key=True)
    template = models.CharField(max_length=224)
    par = models.CharField(max_length=224)

    def __str__(self):
        return str(self.generator_id)
