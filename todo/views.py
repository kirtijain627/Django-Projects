from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer

from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# @method_decorator(csrf_exempt, name ='dispatch')
# class StudentAPI(View):

#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu) 
#             return JsonResponse(data=serializer.data)
        
#         stu = StudentSerializer.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return JsonResponse(data = serializer.data)
    

#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Inserted'}
#             return JsonResponse(data=res)
#         # json_data = JSONRenderer().render(serializer.errors)
#         return JsonResponse(data = serializer.errors)

#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         print('json_data = ', json_data)
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         print('pythondata = ', pythondata)
#         id = pythondata.get('id')
#         print(id)
#         stu = Student.objects.get(id = id)
#         print(stu)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         print('serializer = ', serializer)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated'}
#             return JsonResponse(data = res)
#         return JsonResponse(data = serializer.errors)

#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg': 'Data Deleted'}
#         return JsonResponse(res)
 

# #for single set
# def student_detail(request, pk):
#     stu = Student.objects.get(id=pk)
#     # print(stu)
#     serializer = StudentSerializer(stu)
#     # # print(serializer)
#     # # print(serializer.data)
#     # json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
#     # return HttpResponse(json_data, content_type = 'application/json')
#     return JsonResponse(serializer.data)

# #for query set
# def student_list(request):
#     stu = Student.objects.all()
#     # print(stu)
#     serializer = StudentSerializer(stu, many=True)
#     print(serializer)
#     print(serializer.data)
#     return JsonResponse(serializer.data, safe = False)
    

# @csrf_exempt
# def student_create(request):
#     if request.method == 'POST':
#         json_data = request.body
#         # print(json_data)
#         stream = io.BytesIO(json_data)
#         # print(stream)
#         pythondata = JSONParser().parse(stream)
#         # print(pythondata)
#         serializer = StudentSerializer(data = pythondata)
#         # print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Inserted'}
#             return JsonResponse(data=res)
#         # json_data = JSONRenderer().render(serializer.errors)
#         return JsonResponse(data = serializer.errors)

# @csrf_exempt
# def student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu) 
#             return JsonResponse(data=serializer.data)
        
#         stu = StudentSerializer.objects.all()
#         serializer = StudentSerializer(stu, many = True)
#         return JsonResponse(data = serializer.data)
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Inserted'}
#             return JsonResponse(data=res)
#         # json_data = JSONRenderer().render(serializer.errors)
#         return JsonResponse(data = serializer.errors)
    
#     if request.method =='PUT':
#         json_data = request.body
#         print('json_data = ', json_data)
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         print('pythondata = ', pythondata)
#         id = pythondata.get('id')
#         print(id)
#         stu = Student.objects.get(id = id)
#         print(stu)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         print('serializer = ', serializer)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated'}
#             return JsonResponse(data = res)
#         return JsonResponse(data = serializer.errors)

#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id = id)
#         stu.delete()
#         res = {'msg': 'Data Deleted'}
#         return JsonResponse(res)



#Function based API View:

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method =='GET':
#         return Response({'msg':'This is GET Request'})
    
#     if request.method == 'POST':
#         print("post data ",request.data)
#         print(type(request.data))
#         return Response({'msg': 'This is POST request', 'data':request.data})



# with third party app

@api_view(['GET','POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=StudentSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated'})
        return Response(serializer.errors)

    if request.method=='DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

#with Browsable API

@api_view(['GET', 'POST', 'PUT', 'Patch', 'DELETE'])
def student_brow_api(request, pk = None):
    
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer=StudentSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors)

    if request.method=='DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors)

#class based views

class StudentAPI(APIView):

    def get(self, request,pk = None, format=None):
    
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer=StudentSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors)

    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    
    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors)





 