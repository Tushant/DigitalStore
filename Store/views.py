from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import render

#rest_framework specific
from rest_framework import generics
from .serializers import StoreSerializer, ProductSerializer

from .forms import StoreForm
from .models import Store, Product

class StoreListView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class=StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.all()
        # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class=StoreSerializer
    lookup_url_kwarg = 'token'
    lookup_field = 'token'

    def get_queryset(self):
        queryset = Store.objects.all()
        # Set up eager loading to avoid N+1 selects
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)

def errors_to_json(errors):
    """
    Convert a Form error list to JSON::
    """
    print ('errors', errors)
    return dict(
            (k, map(unicode, v))
            for (k,v) in errors.iteritems()
        )

class ListStore(FormView):
    form_class = StoreForm
    template_name = 'Store/list-store.html'

    def get_initial(self):
        initial = super(ListStore, self).get_initial()
        if self.request.user.is_authenticated():
            initial['email'] = self.request.user.email
            return initial

    def form_invalid(self, form):
        if self.request.is_ajax():
            # self.response = errors_to_json(form.errors)
            # self.success =False
            # response = {
            #     'error': form.errors
            # }
            return JsonResponse(response, status=400)
        else:
            return super(ListStore, self).form_invalid(form.errors)

    def form_valid(self, form):
        store = form.save(merchant=self.request.user)
        success_message = "Thank you for listing your store. We Welcome you."
        # store, created = Store.objects.get_or_create(merchant=self.request.user)
        if self.request.is_ajax():
            response = {
                'result': success_message
            }
            return JsonResponse(response)
        else:
            message.success(self.request, success_message)
            return self.render_to_response(self.get_context_data())
