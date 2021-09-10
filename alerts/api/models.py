from django.db import models

# Create your models here.
class AutoTimestampedModel(models.Model):
    """AutoTimestampedModel

    This model can be inherited to give install_ts and update_ts
    fields to your django model by default.

    Extends:
        models.Model

    """
    install_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Wieght(AutoTimestampedModel):
    name = models.CharField(max_length=300)
    total_wieght = models.IntegerField()
    wieght = models.IntegerField()
    
    def __str__(self):
        return self.name
