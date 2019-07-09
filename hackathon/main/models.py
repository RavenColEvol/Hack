from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class CompanyInfo(models.Model):
    company_logo = models.ImageField(blank=True)
    company_name = models.CharField(max_length=150)
    company_problem_statement = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.company_name).capitalize()

class StudentForm(models.Model):

    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please Enter a Valid Number.")

    TSIZE_CHOICES = (
        ('S','S-36'),
        ('M','M-38'),
        ('L','L-40'),
        ('XL','XL-42'),
        ('XXL','XXL-44'),
    )

    YEAR_CHOICES = (
        ('I','First Year'),
        ('II','Second Year'),
        ('III','Third Year'),
        ('IV','Fourth Year'),
    )

    problem_statement_1 = models.CharField(max_length=300)
    abstract_1 = models.TextField(default="")

    problem_statement_2 = models.CharField(max_length=300)
    abstract_2 = models.TextField(default="")

    problem_statement_3 = models.CharField(max_length=300)
    abstract_3 = models.TextField(default="")

    problem_statement_4 = models.CharField(max_length=300)
    abstract_4 = models.TextField(default="")


    # Team Leader
    team_name = models.CharField(max_length=150)
    team_leader_name = models.CharField(max_length=150)
    team_leader_college_name = models.CharField(max_length=150)
    team_leader_year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    team_leader_email = models.EmailField(max_length=150)
    team_leader_tel_number = models.CharField(validators=[phone_regex],max_length=15)
    team_leader_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,default='S')

    # Teammate 1
    teammate1_name = models.CharField(max_length=150,null=True,blank=True)
    teammate1_college_name = models.CharField(max_length=150,null=True,blank=True)
    teammate1_year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    teammate1_email = models.EmailField(max_length=150,null=True,blank=True)
    teammate1_tel_number = models.CharField(validators=[phone_regex],max_length=15,null=True,blank=True)
    teammate1_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,null=True,blank=True,default='S')

    # Teammate 2
    teammate2_name = models.CharField(max_length=150,null=True,blank=True)
    teammate2_college_name = models.CharField(max_length=150,null=True,blank=True)
    teammate2_year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    teammate2_email = models.EmailField(max_length=150,null=True,blank=True)
    teammate2_tel_number = models.CharField(validators=[phone_regex],max_length=15,null=True,blank=True)
    teammate2_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,null=True,blank=True,default='S')
    # Teammate 3
    teammate3_name = models.CharField(max_length=150,null=True,blank=True)
    teammate3_college_name = models.CharField(max_length=150,null=True,blank=True)
    teammate3_year = models.CharField(max_length=10,choices=YEAR_CHOICES,null=True,blank=True)
    teammate3_email = models.EmailField(max_length=150,null=True,blank=True)
    teammate3_tel_number = models.CharField(validators=[phone_regex],max_length=15,null=True,blank=True)
    teammate3_tsize = models.CharField(('T-SHIRT'),max_length=5,choices=TSIZE_CHOICES,null=True,blank=True,default='S')

    class Meta:
        verbose_name = 'Student_Form'
    
    def __str__(self):
        return self.team_name + " - " + self.team_leader_college_name
