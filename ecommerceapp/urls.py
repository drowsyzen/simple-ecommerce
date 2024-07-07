from django.urls import path
from . import views

urlpatterns = [
     path("",views.example_view),
     path("getallproducts/",views.getAllProducts),
     path("getproductsdetial/<int:product_id>/",views.getProductDetail),
     path("createnewproduct/",views.createNewProduct),
     path("editproduct/<int:product_id>/",views.editProduct),
     path("deleteproduct/<int:product_id>/",views.deleteProduct),
]
