# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from bucket.serializers import UsersSerializer, ListItemsSerializer, BucketListSerializer
from bucket.models import Users, ListItems, BucketList

# Create your views here.


class UsersListViewset(ListCreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetailViewset(RetrieveUpdateDestroyAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class BucketListViewset(ListCreateAPIView):

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer


class BucketListDetailViewset(RetrieveUpdateDestroyAPIView):

    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer


class ListItemsViewset(ListCreateAPIView):

    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer


class ListItemsDetailViewset(RetrieveUpdateDestroyAPIView):

    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer

