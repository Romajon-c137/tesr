from apps.main.models import Lab, Result
from rest_framework import serializers


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"

    #update ot r create 
    # def create(self, validated_data):
    #     try:
    #         lab = Lab.objects.get(oder_number=validated_data['oder_number'])
    #         lab.full_name = validated_data['full_name']
    #         lab.born_date = validated_data['born_date']
    #         lab.order_date = validated_data['order_date']
    #         lab.client_code = validated_data['client_code']
    #         lab.status = validated_data['status']
    #         lab.gender = validated_data['gender']
    #         lab.pin = validated_data['pin']
    #         lab.comment = validated_data['comment']
    #         lab.list = validated_data['list']
    #         lab.save()
    #         return lab
    #     except Lab.DoesNotExist:
    #         return Lab.objects.create(**validated_data)