from django.db import models

# Create your models here.


class Label(models.Model):
    label_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=255)
    datum_zalozeni = models.IntegerField()

    class Meta:
        db_table = "Labely"
        verbose_name = "Label"
        verbose_name_plural = "Labely"

    def __str__(self):
        return self.nazev


class Interpret(models.Model):
    interpret_id = models.AutoField(primary_key=True)

    jmeno = models.CharField(max_length=100)

    prijmeni = models.CharField(max_length=100)

    foto = models.ImageField(
        upload_to='interpreti/',
        blank=True,
        null=True
    )

    label = models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="interpreti"
    )

    class Meta:
        db_table = "Interpreti"
        verbose_name = "Interpret"
        verbose_name_plural = "Interpreti"

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"


class Diskografie(models.Model):
    TYP_CHOICES = [
        ("Album", "Album"),
        ("Single", "Single"),
        ("Duet", "Duet"),
    ]

    diskografie_id = models.AutoField(primary_key=True)

    nazev = models.CharField(max_length=255)

    interpret = models.ForeignKey(
        Interpret,
        on_delete=models.CASCADE,
        related_name="diskografie"
    )

    datum_vydani = models.IntegerField()

    poslechy = models.CharField(max_length=100)

    typ = models.CharField(
        max_length=20,
        choices=TYP_CHOICES
    )

    class Meta:
        db_table = "Diskografie"
        verbose_name = "Diskografie"
        verbose_name_plural = "Diskografie"

    def __str__(self):
        return self.nazev


class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)

    nazev_turne = models.CharField(max_length=255)

    prvni_koncert = models.CharField(max_length=255)

    kapacita = models.IntegerField()

    class Meta:
        db_table = "Tour"
        verbose_name = "Turné"
        verbose_name_plural = "Turné"

    def __str__(self):
        return self.nazev_turne


class Program(models.Model):
    ROLE_CHOICES = [
        ("Hlavní interpret", "Hlavní interpret"),
        ("Předkapela", "Předkapela"),
    ]

    program_id = models.AutoField(primary_key=True)

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="program"
    )

    interpret = models.ForeignKey(
        Interpret,
        on_delete=models.CASCADE,
        related_name="vystoupeni"
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES
    )

    class Meta:
        db_table = "Program"
        verbose_name = "Program"
        verbose_name_plural = "Program"

    def __str__(self):
        return f"{self.interpret} - {self.role}"