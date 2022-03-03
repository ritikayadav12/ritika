from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

class owner(models.Model):
      owner_name=models.CharField(max_length=20)
      owner_age=models.SmallIntegerField()
      owner_contact=models.IntegerField()
      owner_address=models.CharField(max_length=120,null=False,blank=True)



class employee(models.Model):
      employee_name=models.CharField(max_length=20)
      employee_id=models.IntegerField(null=True)
      employee_salary=models.IntegerField(null=True,blank=True)

class total_employees(models.Model):
      total_workers=models.IntegerField()

def __str__(self):
    return self.total_workers

      
  

#class chappan(models.Model):
 #    shop_number=models.SmallIntegerField(max_length=12)
  #    dishname=models.CharField(max_length=120)
   #   cuisines=models.CharField(max_length=120)
    #  price=models.IntegerField()
    #  def __str__(self):
     #     return self.shop_name
#class chinese_food(models.Model):
 #     name=models.CharField(max_length=120)
  #    food_price=models.IntegerField()

        # def __str__(self):
         #  return self.name

