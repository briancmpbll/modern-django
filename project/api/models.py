from django.db import models

class TimestampedModel(models.Model):
    # Timestamp for when this object was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp for when the object was last updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        '''
        By default, any TimestampedModel should be ordered in reverse chronological
        order. This can be overridden on a per model basis as necessary.
        '''
        ordering = ['-created_at', '-updated_at']
