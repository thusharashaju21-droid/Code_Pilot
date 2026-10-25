from django.db import models
from accounts.models import User
from datetime import datetime,time,timedelta

# Create your models here.
class Assessment(models.Model):

    title=models.CharField(max_length=100)

    batch=models.CharField(max_length=50)


    LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("java", "Java"),
        ("javascript", "JavaScript"),
        ("c", "C"),
        ("c++", "C++"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("sql", "SQL"),
        ("django", "Django"),
        ("react", "React"),
    ]

    language=models.CharField(max_length=20,choices=LANGUAGE_CHOICES)

    exam_date=models.DateField()

    duration=models.PositiveIntegerField()

    start_time=models.TimeField()

    end_time=models.TimeField(null=True)

    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("upcoming", "Upcoming"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
        ("postponed", "Postponed"),
        ("rescheduled", "Rescheduled"),
        ("pending", "Pending"),
        ("draft", "Draft"),
]

    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="scheduled")

    def save(self,*args,**kwargs):

        end_date_time = datetime.combine(self.exam_date,self.start_time) + timedelta(hours=self.duration)

        self.end_time=end_date_time.time()

        return super().save(*args,**kwargs)

    


