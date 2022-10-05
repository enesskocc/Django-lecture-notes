from rest_framework import serializers
from .models import Student, Path



##! 1. Yöntem
# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance


##! 2. Yöntem

class StudentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField() ## asagiya get yazmak istemiyorsak, burada parantez icine method="full_name" diye belirtebiliriz

    def get_full_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'

    path = serializers.StringRelatedField() ## id yerine isim getiriyor. Modelse gidiyor ordaki str'den aliyor!
    id = serializers.IntegerField(write_only=True) ## ekranda görmek istemedigimiz seyleri bu sekilde engelleyebiliriz!

    class Meta:
        model = Student
        fields = ["id", "full_name", "first_name", "last_name", "number", "path"]
        # fields = '__all__'
        # exclude = ['number']


class PathSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True)
    students = StudentSerializer(many=True)
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    

    class Meta:
        model = Path
        fields = ["id", "path_name", "students"]
        # fields = '__all__'
        # exclude = ['number']
    

  


