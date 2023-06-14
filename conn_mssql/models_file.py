# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Otanaethesia(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    otnoteid = models.ForeignKey('Otnote', models.DO_NOTHING, db_column='OTNoteId')  # Field name made lowercase.
    anaesthesiaid = models.IntegerField(db_column='AnaesthesiaId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAnaethesia'


class Otdocument(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HospitalId', blank=True, null=True)  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='PhysicianId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    documentpath = models.CharField(db_column='DocumentPath', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    documenttype = models.CharField(db_column='DocumentType', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTDocument'


class Otnote(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='PhysicianId')  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HospitalId')  # Field name made lowercase.
    notedate = models.DateField(db_column='NoteDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    note1 = models.CharField(db_column='Note1', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    note2 = models.CharField(db_column='Note2', max_length=300, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hospitalnotes = models.CharField(db_column='HospitalNotes', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    option = models.IntegerField(db_column='Option', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTNote'


class Otpac(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='PhysicianId')  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HospitalId')  # Field name made lowercase.
    otnoteid = models.ForeignKey(Otnote, models.DO_NOTHING, db_column='OTNoteId')  # Field name made lowercase.
    pacq1 = models.IntegerField(db_column='PACQ1', blank=True, null=True)  # Field name made lowercase.
    pacq2 = models.IntegerField(db_column='PACQ2', blank=True, null=True)  # Field name made lowercase.
    pacq3 = models.IntegerField(db_column='PACQ3', blank=True, null=True)  # Field name made lowercase.
    pacq4 = models.IntegerField(db_column='PACQ4', blank=True, null=True)  # Field name made lowercase.
    pacq5 = models.IntegerField(db_column='PACQ5', blank=True, null=True)  # Field name made lowercase.
    pacq6 = models.IntegerField(db_column='PACQ6', blank=True, null=True)  # Field name made lowercase.
    pacq7 = models.IntegerField(db_column='PACQ7', blank=True, null=True)  # Field name made lowercase.
    pacq8 = models.IntegerField(db_column='PACQ8', blank=True, null=True)  # Field name made lowercase.
    pacq9 = models.IntegerField(db_column='PACQ9', blank=True, null=True)  # Field name made lowercase.
    pacq10 = models.IntegerField(db_column='PACQ10', blank=True, null=True)  # Field name made lowercase.
    pacq11 = models.IntegerField(db_column='PACQ11', blank=True, null=True)  # Field name made lowercase.
    pacq12 = models.IntegerField(db_column='PACQ12', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.
    tac = models.BooleanField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTPAC'


class Otphysician(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    physicianid = models.IntegerField(db_column='PhysicianId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTPhysician'


class Otpreexisitngcondition(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey('Otregister', models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    otnoteid = models.ForeignKey(Otnote, models.DO_NOTHING, db_column='OTNoteId')  # Field name made lowercase.
    preexistingconditionid = models.IntegerField(db_column='PreExistingConditionId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='UpdatedBy', blank=True, null=True)  # Field name made lowercase.
    updatedon = models.DateTimeField(db_column='UpdatedOn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTPreExisitngCondition'


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


class Otsurgery(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey(Otregister, models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    surgeryid = models.IntegerField(db_column='Surgeryid')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTSurgery'


class Otvitaldata(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.ForeignKey(Otregister, models.DO_NOTHING, db_column='CaseId')  # Field name made lowercase.
    temperature = models.CharField(db_column='Temperature', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='HeartRate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.CharField(db_column='BloodPressure', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    oxygensaturation = models.CharField(db_column='OxygenSaturation', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    respiratoryrate = models.CharField(db_column='RespiratoryRate', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTVitalData'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
