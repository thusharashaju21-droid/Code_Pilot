from rest_framework import serializers
from exams.models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id", "created_by"]

