from django.db import models

# Create your models here.


class Question(models.Model): # models.Model is a parent class
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
#one to many, each question can have multiple choices, but each choice can only have one question. 
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #using the whole table as PK
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# okay this is how it works, django models.Model automatically provides tables names with an ID field