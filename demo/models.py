from django.db import models

# Create your models here.
class Observation(models.Model):
    Phase=models.CharField(max_length=255)
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase = models.CharField(max_length=255)
    ObservationID = models.CharField(max_length=255)
    SackNo = models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    Date = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    AnalysisType1 = models.CharField(max_length=255)
    AnalysisType2 = models.CharField(max_length=255)
    Projection = models.CharField(max_length=255)
    UTMZone = models.CharField(max_length=255)
    EastingM = models.CharField(max_length=255)
    NorthingM = models.CharField(max_length=255)
    ElevationM = models.CharField(max_length=255)
    Geologist1 = models.CharField(max_length=255)
    Geologist2 = models.CharField(max_length=255)
    RockType = models.CharField(max_length=255)
    RockTypeCode = models.CharField(max_length=255)
    Description = models.TextField()

class Rock(models.Model):
    # Rock modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    ObservationID = models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    Alt1_Int_Code= models.CharField(max_length=255)
    Alteration2_Type=models.CharField(max_length=255)
    Alt2_Style_Code= models.CharField(max_length=255)
    Alteration2_Intensity=models.CharField(max_length=255)
    Alt2_Int_Code=models.CharField(max_length=255)
    Mineral1=models.CharField(max_length=255)
    Min1_Code=models.CharField(max_length=255)
    Mineral1_percent=models.CharField(max_length=255)
    Mineral1_Occurence=models.CharField(max_length=255)
    Structure_Type=models.CharField(max_length=255)
    Structure_Type_Code= models.CharField(max_length=255)
    Azimuth=models.CharField(max_length=255)
    Dip=models.CharField(max_length=255)
    Description=models.TextField()
    
class Stream(models.Model):
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    ObservationID = models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    Projection = models.CharField(max_length=255)
    UTMZone = models.CharField(max_length=255)
    EastingM = models.CharField(max_length=255)
    NorthingM = models.CharField(max_length=255)
    ElevationM = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    SampleSubType = models.CharField(max_length=255)
    StreamCondition= models.CharField(max_length=255)
    CreekWidth= models.CharField(max_length=255)
    StreamGrade= models.CharField(max_length=255)
    SedSizeGravelPercent= models.CharField(max_length=255)
    SedSizeGravelPercent= models.CharField(max_length=255)
    SedSizeSandPercent= models.CharField(max_length=255)
    SedSizeSiltPercent= models.CharField(max_length=255)
    OrganicContent= models.CharField(max_length=255)
    Color= models.CharField(max_length=255)
    ColorCode= models.CharField(max_length=255)
    FeMnOxides= models.CharField(max_length=255)
    Character= models.CharField(max_length=255)
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()
class Soil(models.Model):
    # Soil modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    ObservationID = models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    Projection = models.CharField(max_length=255)
    UTMZone = models.CharField(max_length=255)
    EastingM = models.CharField(max_length=255)
    NorthingM = models.CharField(max_length=255)
    ElevationM = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    SoilSampleType=models.CharField(max_length=255)
    Moisture=models.CharField(max_length=255)
    OrganicContent= models.CharField(max_length=255)
    SoilSize=models.CharField(max_length=255)
    SoilSlope=models.CharField(max_length=255)
    Horizon=models.CharField(max_length=255)
    Depth=models.CharField(max_length=255)
    RockPercent=models.CharField(max_length=255)
    Color=models.CharField(max_length=255)
    ColorCode=models.CharField(max_length=255)
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()
class OreMicroscopy(models.Model):
    # OreMicroscopy modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    AnalysisType= models.CharField(max_length=255) 
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()
class Petrograph(models.Model):
    # Petrograph modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    AnalysisType= models.CharField(max_length=255) 
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()
class XRD(models.Model):
    # XRD modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    AnalysisType= models.CharField(max_length=255) 
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()
class FluidInclusion(models.Model):
    # FluidInclusion modeli alanları buraya eklenebilir.
    ClientName = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    Village = models.CharField(max_length=255)
    ER_No = models.CharField(max_length=255)
    Licence_No = models.CharField(max_length=255)
    Phase=models.CharField(max_length=255)
    SampleNo = models.CharField(max_length=255)
    SampleType = models.CharField(max_length=255)
    AnalysisType= models.CharField(max_length=255) 
    RockType= models.CharField(max_length=255)
    RockTypeCode= models.CharField(max_length=255)
    Description=models.TextField()