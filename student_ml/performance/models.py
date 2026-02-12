from django.db import models
from django.core.exceptions import ValidationError


class StudentPerformance(models.Model):
    hours_studied = models.IntegerField()
    previous_scores = models.IntegerField()
    extracurricular = models.BooleanField()
    sleep_hours = models.IntegerField()
    sample_papers = models.IntegerField()
    performance_index = models.FloatField()

    def clean(self):
        total_hours = self.hours_studied + self.sleep_hours
        if total_hours > 24:
            raise ValidationError(
                f'Total hours studied and sleep ({total_hours}) cannot exceed 24 hours in a day.'
            )

    def __str__(self):
        return f"Performance: {self.performance_index}"
