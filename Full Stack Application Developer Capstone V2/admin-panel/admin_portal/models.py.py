# admin-panel/admin_portal/models.py
from django.db import models

class PatientAssessment(models.Model):
    symptoms_text = models.TextField()
    predicted_condition = models.CharField(max_length=100)
    confidence_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    reviewed_by_doctor = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'patient_assessments'
    
    def __str__(self):
        return f"Assessment {self.id} - {self.predicted_condition}"