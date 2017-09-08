from django.db import models
from .validators import validate_file_extension


# you can add Generators by admin panel
# typed template info field is more important than template given by uploading file
# template has to be in format 'I like {}, you like {}...'
# par has to be in format 'orange, banana ...' - separate values by coma
class StringGenerator(models.Model):
    generator_id = models.AutoField(primary_key=True)
    template = models.TextField(blank=True)
    template_file = models.FileField(upload_to="files", validators=[validate_file_extension], blank=True)
    par = models.TextField()

    def __str__(self):
        return str(self.generator_id)
