from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    isDiscoverable = models.BooleanField(default=True)
    profilePicture = models.ImageField(upload_to='Profile-Pictures')
    position = models.CharField(max_length=100)
    biography = models.CharField(max_length=500)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname


class UserExperience(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=300)
    fullTime = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName


class UserProject(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    releaseDate = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=300)
    basedOn = models.CharField(max_length=100)
    projectImage = models.ImageField(upload_to='Project-Photos')
    projectLink = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class UserCertificate(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issuedBy = models.CharField(max_length=100)
    issueDate = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " BY " + self.issuedBy


class UserLink(models.Model):
    belongsTo = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return str(self.belongsTo)+"'s" + " " + str(self.name)
