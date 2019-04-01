from django.db import models

class Business(models.Model):
    '''
    Business model, holds information about the business 
    '''
    business_name = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='businesses', on_delete=models.CASCADE)

    class meta:
        ordering = ('created_on',)


class Reviews(models.Model):
    '''
    Review model holds reviews for registered businesses
    '''
    review = models.TextField()
    business = models.ForeignKey(Business, related_name='reviews', on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey('auth.User', related_name='reviews',on_delete=models.CASCADE)
    reviewed_on = models.DateTimeField(auto_now_add=True)

