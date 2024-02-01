from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model): # models.Model is a parent class
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self) -> str:
        return "Question: " + self.question_text
#one to many, each question can have multiple choices, but each choice can only have one question. 
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #using the whole table as PK
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return "Choice: "+self.choice_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# okay this is how it works, django models.Model automatically provides tables names with an ID field





