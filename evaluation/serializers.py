from rest_framework import serializers
from evaluation.models import Submission,Answer

class SubmissionSerializer(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField(read_only = True)

    student = serializers.StringRelatedField(read_only = True)

    answers = serializers.SerializerMethodField(read_only = True)

    class Meta:

        model = Submission

        fields = "__all__"

        read_only_fields = [fields]

    def get_answers(self,obj):

        answer_objects = Answer.objects.filter(submission=obj) 

        serializer_instance = AnswerSerializer(answer_objects,many=True)

        return serializer_instance.data

        
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer  

        fields = "__all__"

        read_only_fields = ["id","submission","marks_awarded","feedback","evaluated_at"] 