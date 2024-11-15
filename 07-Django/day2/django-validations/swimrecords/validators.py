from django.core.exceptions import ValidationError
import re

class SwimRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimRecord
        fields = ['first_name','last_name','team_name','relay','stroke','distance','record_date','record_broken_date']