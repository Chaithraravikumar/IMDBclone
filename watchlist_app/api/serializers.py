from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only = True)
    # len_title = serializers.SerializerMethodField()
    platform = serializers.CharField(source ='platform.name')
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['active']
        
    def get_len_title(self, object):
        return len(object.title)

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only = True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'

def name_validator(self, value):
        if len(value)< 2:
            raise serializers.ValidationError("Name is too short")
        return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(validators=[name_validator])
    description = serializers.CharField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    
    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance
    
    def validate_name(self, value):
        if len(value)< 2:
            raise serializers.ValidationError("Name is too short")
        return value
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name should not be same as that of description")
        return data