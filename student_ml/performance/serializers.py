from rest_framework import serializers
from .models import StudentPerformance


class StudentPerformanceSerializer(serializers.ModelSerializer):
    # The model stores `performance_index`, but the prediction API only
    # expects input features. Mark `performance_index` as read-only so
    # requests don't need to include it.
    performance_index = serializers.FloatField(read_only=True)

    class Meta:
        model = StudentPerformance
        fields = ['hours_studied', 'previous_scores', 'extracurricular', 'sleep_hours', 'sample_papers', 'performance_index']

    def validate(self, data):
        hours_studied = data.get('hours_studied', 0)
        sleep_hours = data.get('sleep_hours', 0)

        total_hours = hours_studied + sleep_hours
        if total_hours > 24:
            raise serializers.ValidationError(
                f'Total hours studied and sleep ({total_hours}) cannot exceed 24 hours in a day.'
            )

        return data
