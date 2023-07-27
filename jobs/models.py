from django.db import models
from datetime import datetime

class Working(models.Model):
    name=models.CharField(max_length=100)
    jdate=models.DateField()
    start=models.TimeField()
    end=models.TimeField()
    holyday=models.TextField(max_length=3)
    lunch=models.TextField(max_length=3)
    def __str__(self):
        return self.name
    
    def workhour(self):
        s1 = str(self.start)
        s2 = str(self.end)
        start_dt = datetime.strptime(s1, '%H:%M:%S')
        end_dt = datetime.strptime(s2, '%H:%M:%S')
        diff = (end_dt - start_dt)
        days = diff.days
        days_to_hours = days * 24
        diff_btw_two_times = (diff.seconds) / 3600
        overall_hours = days_to_hours + diff_btw_two_times
        if self.lunch=='Yes':
            overall_hours=overall_hours-1
        return overall_hours
    def __str__(self):
        self.overtime=0
        s1 = str(self.start)
        s2 = str(self.end)
        start_dt = datetime.strptime(s1, '%H:%M:%S')
        end_dt = datetime.strptime(s2, '%H:%M:%S')
        diff = (end_dt - start_dt)
        days = diff.days
        days_to_hours = days * 24
        diff_btw_two_times = (diff.seconds) / 3600
        overall_hours = days_to_hours + diff_btw_two_times
        if self.lunch=='Yes' and self.holyday=='No' and overall_hours>7:
            overall_hours=overall_hours-1
            self.overtime=overall_hours-7
        if self.lunch=='No' and self.holyday=='Yes':
            self.overtime=overall_hours
        if self.lunch=='No' and self.holyday=='No':
            self.overtime=overall_hours
        if self.lunch=='Yes' and self.holyday=='Yes':
            overall_hours=overall_hours-1
            self.overtime=overall_hours
        return str(self.overtime)
    