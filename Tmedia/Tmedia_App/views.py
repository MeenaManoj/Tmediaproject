from django.http import JsonResponse
from django.shortcuts import render


from django.shortcuts import render
from .models import Company_data

def company_data(request):
    data = Company_data.objects.all()
    company_data_list = [{'company_name': item.company_name, 'company_location': item.company_location} for item in data]
    return JsonResponse({'company_data': company_data_list})
    # return render(request, 'Tmedia_App/test.template.html', {'company_data': data})


from rest_framework import generics
from .models import Company_data
from .serializer import CompanyDataSerializer

class CompanyDataList(generics.ListCreateAPIView):
    queryset = Company_data.objects.all()
    serializer_class = CompanyDataSerializer

class CompanyDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company_data.objects.all()
    serializer_class = CompanyDataSerializer


 