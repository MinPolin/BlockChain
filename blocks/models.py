from django.db import models



class Block(models.Model):
    height = models.PositiveIntegerField(primary_key = True, blank=False,unique=True)
    hash = models.CharField(max_length=64,blank=False,unique=True)
    date = models.DateTimeField(blank=False)
    miner = models.CharField(max_length=64,blank=False)
    transaction_count=models.PositiveIntegerField(blank=False)


    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.height)
    class Meta:
        ordering=['-height']