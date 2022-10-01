from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSelializer
from rest_framework.views import APIView




class ProductApi(APIView):
    def get(self, request):
         objs = Product.objects.all()
         serializer = ProductSelializer(objs, many= True)
         return Response(serializer.data)

    def post(self, request):
        data =request.data  
        serializer = ProductSelializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)

    def put(self, request):
        data =request.data  
        #obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    #support partial update when we want to update any 
    # particular field data  
    def patch(self, request):
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data, partial= True)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    def delete(self, request):
        data =request.data 
        obj = Product.objects.get(id=data['id'])
        obj.delete()
        return Response({'person':'delete'})




@api_view(['GET','POST','PUT','DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    elif request.method == 'POST':
        data =request.data  
        print(data)
        return Response({"message": "Hello, world!"})
    elif request.method == 'PUT':
        return Response({"message": "Hello, world!"})
    elif request.method == 'DELETE':
        return Response({"message": "Hello, world!"})
    return Response({"message": "Hello, world!"})


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def product(request):
    if request.method == 'GET':
        objs = Product.objects.all()
        serializer = ProductSelializer(objs, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data =request.data  
        serializer = ProductSelializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    # we can update all the data 
    # and we need to pass all data 
    # weather we want to update or not
    elif request.method == 'PUT':
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    #support partial update when we want to update any 
    # particular field data  
    elif request.method == 'PATCH':
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data, partial= True)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    elif request.method == 'DELETE':
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        obj.delete()
        return Response({'person':'delete'})