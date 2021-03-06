from django.conf.urls import include, url

from .views import ListStore, StoreView, StoreDetailView, ProductListView

urlpatterns = [
    url(r'^list/store$', ListStore.as_view(), name='list-store'),
    url(r'^store$', StoreView.as_view(), name='store-list'),
    url(r'^store/(?P<token>[0-9a-z]+)$', StoreView.as_view(), name='store-detail'),
    url(r'^product$', ProductListView.as_view(), name='product-list'),
]
