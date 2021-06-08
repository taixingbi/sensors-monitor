from django.db import models
from django.conf import settings

class Heartbeat(models.Model):
    # serialNumber = models.IntegerField()
    state = models.IntegerField()
    message = models.IntegerField()

    def __str__(self):
        return str(self.serialNumber)

    class Meta:
        db_table = 'Heartbeat'

class Sensor(models.Model):
    serialNumber = models.IntegerField()
    metadata = models.CharField(max_length=255)
    heartbeat = models.ForeignKey(Heartbeat, on_delete=models.CASCADE)

    # heartbeat = models.ManyToManyField(Heartbeat)

    def __str__(self):
        return str(self.serialNumber)

    class Meta:
        db_table = 'Sensors'



# class Membership(models.Model):
#     heartbeat = models.ForeignKey(Heartbeat, on_delete=models.CASCADE)
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
#     serialNumber = models.IntegerField()

    # person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField()
    # invite_reason = models.CharField(max_length=64)



# class Ml_test(models.Model):
#     email = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         db_table = 'ml_test'






# class Teleconference_transcribe(models.Model):
#     filename = models.CharField(max_length=100)
#     transcription = models.TextField(max_length=500)
#     transcription_baseline = models.TextField(max_length=500)

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         db_table = "teleconference_transcribe"



# class Example(models.Model):
#     account_id = models.IntegerField()
#     session_id = models.IntegerField()
#     slice_probabilities = models.TextField(max_length=100)
#     response_time = models.CharField(max_length=100)
#     threshold = models.FloatField()
#     PHQ8 = models.IntegerField()
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return str(self.account_id)

#     class Meta:
#        



