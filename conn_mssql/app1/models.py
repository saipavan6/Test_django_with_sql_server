from django.db import models

# Create your models here.


class Otregister(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    casenumber = models.CharField(db_column='CaseNumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    casename = models.CharField(db_column='CaseName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    casestatus = models.IntegerField(db_column='CaseStatus', blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HospitalId')  # Field name made lowercase.
    surgerydate = models.DateTimeField(db_column='SurgeryDate', blank=True, null=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='PatientName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    surgeonid = models.IntegerField(db_column='SurgeonId', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientdiagnostics = models.CharField(db_column='PatientDiagnostics', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bookfavphysician = models.IntegerField(db_column='BookFavPhysician', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    hospitalotroomid = models.IntegerField(db_column='HospitalOTRoomId', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTRegister'

