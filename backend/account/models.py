from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    licence = models.BooleanField(default=True)
    exp_date = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name

class CompanyRole(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, blank=True, null=True)
    role_name = models.CharField(max_length=15)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.role_name



class StaffPermission(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.BooleanField(default=False)
    hr = models.BooleanField(default=False)
    qc = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    supervisor = models.BooleanField(default=False)
    warehouse = models.BooleanField(default=False)
    cutting = models.BooleanField(default=False)
    packing = models.BooleanField(default=False)

    def __str__(self):
        return self.usr.username

class LineName(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, blank=True, null=True)
    line_name = models.CharField(max_length=25)
    target = models.PositiveIntegerField(default=0)
    redcolor = models.PositiveIntegerField(default=0)
    successcolor = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line_name
    

# class LineSchedule(models.Model):
#     line = models.ForeignKey(LineName, on_delete=models.CASCADE)
#     style_name = models.ForeignKey(Style, on_delete=models.CASCADE)
#     item = models.CharField(max_length=255, blank=True, null=True)
#     target_qty = models.IntegerField(default=0)
#     total_qty = models.IntegerField(default=0)
#     start_date = models.DateField(blank=True, null=True)
#     due_date = models.DateField(blank=True, null=True)
#     color = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     complete = models.BooleanField(default=False)
#     complete_date = models.DateField(blank=True, null=True)

#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class ScheduleNote(models.Model):
#     schedule = models.ForeignKey(LineSchedule, on_delete=models.CASCADE)
#     date = models.DateField()
#     note = models.TextField()
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)