from rest_framework import serializers 
from tutorials.models import TutorialsTutorial as Tutorial 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')