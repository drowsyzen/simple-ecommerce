from ecommerceapp.serializers import ProductSerializer,AllProductSerializer,RegisterSerializer
from ecommerceapp.models import ProductMstModel
from rest_framework import status


def get_all_products():
    
    all_instock_products = ProductMstModel.objects.filter(status=1,quantity__gte=1).all()
    if all_instock_products:
        product_srl_obj = AllProductSerializer(all_instock_products,many=True)

        return product_srl_obj,"",""
    else:
        return {},"No Products found",400
    


def get_product_detail(product_id):
    all_instock_products = ProductMstModel.objects.filter(status=1,quantity__gte=1,id=product_id).all()
    if all_instock_products:
        product_srl_obj = ProductSerializer(all_instock_products,many=True)

        return product_srl_obj,"",""
    else:
        return {},"No Product found for this id",400
    

def createNewProduct(data,user):

    data.user = user.id
    new_product_obj = ProductSerializer(data=data)

    if new_product_obj.is_valid():
        new_product_obj.save()
        return new_product_obj.data,status.HTTP_201_CREATED
    else:
        error_data = new_product_obj.errors 
        return error_data,"Invalid details",""
    

def edit_product(product_id,data):

    product_obj = ProductMstModel.objects.filter(status=1,id=product_id)
    updated_obj = ProductSerializer(data= data, instance = product_obj, partial = True)
    if updated_obj.is_valid():
        updated_obj.save()
        return updated_obj.data,status.HTTP_201_CREATED
    else:
        error_data = updated_obj.errors 
        return error_data,"Invalid details",""
    

def delete_product(product_id):

    product_obj = ProductMstModel.objects.filter(status=1,id=product_id)
    
    if product_obj:
        product_obj.delete()
        return product_obj.data,"",status.HTTP_201_CREATED
    else:
        error_data = product_obj.errors 
        return "","Error while deleting Product.",""
    

    
def register_user(data):
    new_user_obj = RegisterSerializer(data=data)
    if new_user_obj.is_valid():
        new_user_obj.save()
        return new_user_obj.data,"",""
    return new_user_obj.errors,"Some error while adding new User","400"


