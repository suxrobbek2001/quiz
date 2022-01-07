from django.db import models

class Quiz(models.Model):
    nom = models.CharField(max_length=50)
    batafsil = models.CharField(max_length=200, blank=True)
    savol_son = models.PositiveSmallIntegerField()
    davomiyligi = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nom}    {self.batafsil}"

class Savol(models.Model):
    matn = models.CharField(max_length=500)
    quiz = models.ForeignKey(Quiz, models.SET_NULL, null=True)

    def __str__(self):
        return self.matn

class Javob(models.Model):
    matn = models.CharField(max_length=500)
    togri = models.BooleanField(default=False)
    savol = models.ForeignKey(Savol, models.SET_NULL, null=True)

    def __str__(self):
        return self.matn
