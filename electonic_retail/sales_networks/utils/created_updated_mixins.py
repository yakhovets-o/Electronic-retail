from  django.db import models



class CreatedUpdatedMixins(models.Model):
    """Mixins add created and updated timestamp fields in model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
