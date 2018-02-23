from django.conf.urls import url, include
from bucket.views import (UsersDetailViewset, UsersListViewset, BucketListDetailViewset, BucketListViewset,
    ListItemsViewset, ListItemsDetailViewset)


urlpatterns = [
    url(r'^users/$', UsersListViewset.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UsersDetailViewset.as_view(), name='user_detail'),
    url(r'^bucketlist/$', BucketListViewset.as_view(), name='bucket_list'),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$', BucketListDetailViewset.as_view(), name='bucket_list_detail'),
    url(r'^listitems/$', ListItemsViewset.as_view(), name='list_items'),
    url(r'^listitems/(?P<pk>[0-9]+)/$', ListItemsDetailViewset.as_view(), name='list_items_detail'),
]
