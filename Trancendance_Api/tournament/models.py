from django.db import models

# Create your models here.

class Tournament_4(models.Model):
    user1 = models.ForeignKey('users.User', related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey('users.User', related_name='user2', on_delete=models.CASCADE)
    user3 = models.ForeignKey('users.User', related_name='user3', on_delete=models.CASCADE)
    user4 = models.ForeignKey('users.User', related_name='user4', on_delete=models.CASCADE)
    winner1 = models.ForeignKey('users.User', related_name='winner1', on_delete=models.CASCADE)
    winner2 = models.ForeignKey('users.User', related_name='winner2', on_delete=models.CASCADE)
    
class Tournament_8(models.Model):
	user1 = models.ForeignKey('users.User', related_name='user11', on_delete=models.CASCADE)
	user2 = models.ForeignKey('users.User', related_name='user22', on_delete=models.CASCADE)
	user3 = models.ForeignKey('users.User', related_name='user33', on_delete=models.CASCADE)
	user4 = models.ForeignKey('users.User', related_name='user44', on_delete=models.CASCADE)
	user5 = models.ForeignKey('users.User', related_name='user55', on_delete=models.CASCADE)
	user6 = models.ForeignKey('users.User', related_name='user66', on_delete=models.CASCADE)
	user7 = models.ForeignKey('users.User', related_name='user77', on_delete=models.CASCADE)
	user8 = models.ForeignKey('users.User', related_name='user88', on_delete=models.CASCADE)
	winner1 = models.ForeignKey('users.User', related_name='winner11', on_delete=models.CASCADE)
	winner2 = models.ForeignKey('users.User', related_name='winner22', on_delete=models.CASCADE)
	winner3 = models.ForeignKey('users.User', related_name='winner33', on_delete=models.CASCADE)
	winner4 = models.ForeignKey('users.User', related_name='winner44', on_delete=models.CASCADE)
	semifinal1 = models.ForeignKey('users.User', related_name='semifinal1', on_delete=models.CASCADE)
	semifinal2 = models.ForeignKey('users.User', related_name='semifinal2', on_delete=models.CASCADE)