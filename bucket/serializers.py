from rest_framework.serializers import  ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from bucket.models import Users, BucketList, ListItems

class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = "__all__"

class BucketListSerializer(ModelSerializer):

    class Meta:
        model = BucketList
        fields = "__all__"

class ListItemsSerializer(ModelSerializer):
    bucket_list = StringRelatedField(many=True)



    class Meta:
        model = ListItems
        fields = "__all__"