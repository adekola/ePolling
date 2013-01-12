from django.db import models

# Create your models here.

class Responder(models.Model):
    '''
    Class to rep the responder to a poll question
    '''
    
class Poller(models.Model):
    '''
    Class to represent the perosn who raises a question
    '''
    
class Question(models.Model):
    date_posted = models.DateField()
    time_posted = models.TimeField()
    question_body = models.CharField(max_length=140)
    poller_id = models.ForeignKey(Poller)
    

    
    class Admin():
        pass
    
    def __str__(self):
        return "Question (text= '%s' )"%self.question_body
    
class Response(models.Model):
    date_sent = models.DateField()
    time_sent = models.TimeField()
    responder_id = models.ForeignKey(Responder)
    question_id = models.ForeignKey(Question)
    response_body = models.CharField(max_length=140)
    
    class Admin():
        pass
    
    def __str__(self):
        return "Response (text= '%s' )"%self.response_body
    
    
    
