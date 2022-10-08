'''
    HTTP Request Types:
        * GET         : İstek URL'de gönderilir. Açıktan gönderilen istek.
        * POST        : İstek data olarak gönderilir. Gizliden gönderilen istek. 
        * PUT       : POST gibidir. PrimaryKey (ID) verisi de ister. Güncelleme için kullanılır.
        * PATCH     : POST/PUT gibidir. Farkı: Belirli bir parçayı güncellemek için kullanılır.
        * DELETE    : POST gibidir. PrimaryKey (ID) verisi de ister. Sadece silme için kullanılır.
'''



from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view() ## hazir tempalate sagliyor!
def home(request):
    return Response({'message': 'welcome to HomePage'})


##? 1) Primary key istemeyenler!
##! verileri listele :

from .serializers import StudentSerializer
from .models import Student ## veri tabani ile iletisime gecen kisim modelller kismidir.

@api_view()
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True) ## Jlike convert tuple in list
    return Response(serializer.data) ## show with JSON


##! Veri kaydet:

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully'})
    return Response({'message': 'Not Valid'})

##? ---------------------------------------------------------------------------------------------

##? 2) Primary key isteyenler!

##! Tek ögrencinin listelenmesi

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serilazier = StudentSerializer(student)
    return Response(serilazier.data)

##! VEri Güncelle

@api_view((['PUT']))
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serilazier = StudentSerializer(instance=student, data=request.data) ## ilki eski veri, ikincisi yeni veri.

    if serilazier.is_valid():
        serilazier.save()
        return Response({'message': 'Updated Successfully'})
    return Response(serializer.errors)

##! Veril Silme:

@api_view((['DELETE']))
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({'message': 'DELETED Successfully'})

##? ---------------------------------------------------------------------------------------------

##! Birlestirme islemleri:

@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
    # Listele:
        students = Student.objects.all() # get data from database/table.
        serializer = StudentSerializer(students, many=True) # Like convert to TupleINList (JSON)
        return Response(serializer.data) # Show with JSON
    elif request.method == 'POST':
    # Ekle:
        serializer = StudentSerializer(data=request.data)

        # if valid:
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'Creating Successfully' }, status=status.HTTP_201_CREATED)
        # if not valid:
        # return Response({ 'message': 'Not Valid.' })
        return Response(serializer.errors) # Hata mesajını göster.


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
    # Kayıt Görüntüle:
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
    # Kayıt Güncelle:
        serializer = StudentSerializer(instance=student, data=request.data)

        # if valid:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Yeni datayı göster
        # if not valid:
        return Response(serializer.errors) # Hata mesajını göster.
    elif request.method == 'DELETE':
    # Kayıt Sil:
        student.delete()
        return Response({ 'message': 'Deleting Successfully' })
    
    return Response(serializer.errors) # Hata mesajını göster.
