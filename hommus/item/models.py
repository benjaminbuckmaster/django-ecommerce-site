from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories' # make django show categories instead of categorys
        ordering = ('name',) # show in alphabetical descending order

    def __str__(self) -> str:
        return self.name