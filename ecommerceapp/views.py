from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from ecommerceapp.services import *

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)



@csrf_exempt
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllProducts(request):

    # user = request.user    
    output_json = get_all_products()

    return Response(output_json)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProductDetail(request,product_id):

    output_json = get_product_detail(product_id)

    return Response(output_json)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNewProduct(request):

    user = request.user
    data = request.data

    output_json = get_product_detail(data,user)

    return Response(output_json)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editProduct(request,product_id):

    data = request.data

    output_json = edit_product(product_id,data)

    return Response(output_json)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProduct(request,product_id):

    output_json = edit_product(product_id)

    return Response(output_json)


@csrf_exempt
@api_view(['POST'])
def registerUser(request):

    user_data = request.data

    output_json = register_user(user_data)

    return Response(output_json)


