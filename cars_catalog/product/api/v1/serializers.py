from rest_framework import serializers
from product.models import Car, Comment


class ListCarSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = '__all__'


class ListCommentSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        car = Car.objects.create(
            make=validated_data['make'],
            model=validated_data['model'],
            year=validated_data['year'],
            description=validated_data['description'],
            owner=user
        )
        return car

    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.model = validated_data.get('model', instance.model)
        instance.year = validated_data.get('year', instance.year)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['content', 'car']

    def create(self, validated_data):
        user = self.context['request'].user
        car = self.context['car']
        comment = Comment.objects.create(
            content=validated_data['content'],
            author=user,
            car=car
        )
        return comment
