import random

from django.contrib.auth import get_user_model
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
from datetime import date
from datetime import datetime

from django.views.generic import ListView

#from djapp01.models import Books, ChartTest
from apps.djapp01.models import DataAs

import json
'''
book = Books(
     name="Sword Come",
     price = 33,
     hire_date = date(2020,11,2),
     author = "Princes of Fenghuo Opera",
     num = 22,
     publish = "Start",
     type = "Fantasy",
     sales_volume = 2
)
book. save()

'''




#@login_required
'''
def v_book_create(request):

     Books.objects.create(
          tb_book_name="Sun",
          tb_book_price=1800,
          tb_book_hire_date=date(2020, 11, 2),
          tb_book_author="Princes of Fenghuo Opera",
          tb_book_num=22,
          tb_book_publish="Start",
          tb_book_type="Fantasy",
          tb_book_sales_volume=2
     )

     Books.objects.create(
          tb_book_name="Star",
          tb_book_price=381,
          tb_book_hire_date=date(2021, 11, 2),
          tb_book_author="Princes of Fenghuo Opera",
          tb_book_num=22,
          tb_book_publish="Start",
          tb_book_type="Fantasy",
          tb_book_sales_volume=2
     )


     book = Books(
          tb_book_name="Sword Come",
          tb_book_price=33,
          tb_book_hire_date=date(2020, 11, 2),
          tb_book_author="Princes of Fenghuo Opera",
          tb_book_num=22,
          tb_book_publish="Start",
          tb_book_type="Fantasy",
          tb_book_sales_volume=2
     )
     book.save()
     
     
     #return JsonResponse('Completed!', safe=False)
     return render(request, "home.html")
'''

def v_home(request):
     return render(request, "home.html")

def v_data_analysis_create_form(request):
     return render(request, "dacrform.html")
'''
def v_book_del(request):
     book = Books.objects.get(id=8)
     book. delete()
     return render(request, "home.html")

def v_book_save(request):
     book = Books.objects.get(id = 6)
     book.publish = "Fun"
     book.save()
     return render(request, "home.html")

def v_book_qry(request):
     books=Books.objects.filter(id=1).values()
     #books = Books.objects.all()
     return render(request, "home.html")

class BooksListView(ListView):
    model = Books
    template_name = 'list.html'

'''

def v_data_analysis_create_auto(request):
     current_time=datetime.now()
     str_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")
     DataAs.objects.create(
          tb_data_analysis_name="CRC Risk Assessment"+str_time,
          tb_data_analysis_date=current_time,
          tb_data_analysis_mh01="10",
          tb_data_analysis_mh02="0", #0,1,2
          tb_data_analysis_mh03="2", #0,1,2
          tb_data_analysis_bf01="0", #0,1,2
          tb_data_analysis_bf02="1", #0,1,2
          tb_data_analysis_bf03="2",
          tb_data_analysis_bf04 = "2",
          tb_data_analysis_bf05 = "1",
          tb_data_analysis_fd01 = "0",
          tb_data_analysis_fd02 = "1",
          tb_data_analysis_fd03 = "2"

     )

     return render(request, "home.html")


def v_data_analysis_create_post(request):
     current_time=datetime.now()

     #data_json = json.load(request.body)
     #tb_data_analysis_mh02 = data_json.get('mh02')
     #print(tb_data_analysis_mh02)
     str_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")

     DataAs.objects.create(

          tb_data_analysis_name="CRC Risk Assessment"+str_time,
          tb_data_analysis_date=current_time,
          tb_data_analysis_mh01=request.POST.get('mh_01', 0),
          tb_data_analysis_mh02=request.POST.get('mh_02', 0),
          tb_data_analysis_mh03=request.POST.get('mh_03', 0),
          tb_data_analysis_bf01=request.POST.get('bf_01', 0),
          tb_data_analysis_bf02=request.POST.get('bf_02', 0),
          tb_data_analysis_bf03=request.POST.get('bf_03', 0),
          tb_data_analysis_bf04=request.POST.get('bf_04', 0),
          tb_data_analysis_bf05=request.POST.get('bf_05', 0),
          tb_data_analysis_fd01=request.POST.get('fd_01', 0),
          tb_data_analysis_fd02=request.POST.get('fd_02', 0),
          tb_data_analysis_fd03=request.POST.get('fd_03', 0)

     )



     return render(request, "home.html")

def v_data_analysis_del(request):
     book = DataAs.objects.get(id=8)
     book. delete()
     return render(request, "home.html")

def v_data_analysis_save(request):
     book = DataAs.objects.get(id = 6)
     book.publish = "Fun"
     book.save()
     return render(request, "home.html")

def v_data_analysis_qry(request):
     books=DataAs.objects.filter(id=1).values()
     #books = Books.objects.all()
     return render(request, "home.html")


def v_data_analysis_charts_bf01(request):
    i=1
    # books = Books.objects.all()
    return render(request, "charts-bf01.html")


def v_data_analysis_charts_mh01(request):
    i=1
    # books = Books.objects.all()
    return render(request, "charts-mh01.html")


def v_data_analysis_charts_mh01_bf01(request):
    i=1
    # books = Books.objects.all()
    return render(request, "charts-mh01-bf01.html")


class DataAnalysisListView(ListView):
    model = DataAs
    template_name = 'listda.html'

# Create your views here.
'''
def get_all_data(request):
    data = ChartTest.objects.all()
    if len(data) == 0:
        random_gen_data()
        data = ChartTest.objects.all()
    response = {
        'msg': 'success',
        'data': json.loads(serializers.serialize('json', data))
    }
    return JsonResponse(response)

DATA_VOLUME_SIZE = 100
TIME_DELTA = timedelta(minutes=1)
def random_gen_data():
    start_time = datetime.datetime(year=2023, month=5, day=10, hour=8, minute=0, second=0)

    data = []
    for i in range(DATA_VOLUME_SIZE):
        cur_time = start_time + i * TIME_DELTA
        cur_value = round(random.uniform(20.00, 30.00), 2)
        temp = ChartTest(time=cur_time, value=cur_value)
        data.append(temp)


'''

def chat_data_jason(request, *args, **kwargs):

    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


def chat_data_jason(request, *args, **kwargs):

    data = {
        "name": "Behavior Factor Alcohol ",
        "values": ">3 drinks",
    }
    return JsonResponse(data) # http response

class ChartData_BF01(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = 1 #User.objects.all().count()


        #labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        #default_items = [qs_count, 23, 2, 3, 12, 2]
        datalist0 = DataAs.objects.filter(tb_data_analysis_bf01="<2 drinks").count()
        datalist1 = DataAs.objects.filter(tb_data_analysis_bf01="2-3 drinks").count()
        datalist2 = DataAs.objects.filter(tb_data_analysis_bf01=">3 drinks").count()

        labels = ["<2 drinks", "2-3 drinks", ">3 drinks"]
        default_items=[datalist0,datalist1,datalist2]

        data = {
                "labels": labels,
                "default": default_items,
        }


        return Response(data)


class ChartData_MH01(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = 1 #User.objects.all().count()


        datalist0 = DataAs.objects.filter(tb_data_analysis_mh01="0").count()
        datalist1 = DataAs.objects.filter(tb_data_analysis_mh01="1").count()
        datalist2 = DataAs.objects.filter(tb_data_analysis_mh01="2").count()
        datalist3 = DataAs.objects.filter(tb_data_analysis_mh01="3").count()
        datalist4 = DataAs.objects.all().count()-datalist0-datalist1-datalist2-datalist3


        labels = ["count 0", "count 1", "count 2", "count 3", "count >3"]
        default_items=[datalist0,datalist1,datalist2,datalist3,datalist4]

        data = {
                "labels": labels,
                "default": default_items,
        }


        return Response(data)


class ChartData_MH01_BF01(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        #qs_count = 1 #User.objects.all().count()

        datalist0 = DataAs.objects.filter(tb_data_analysis_mh01="0" , tb_data_analysis_bf01="<2 drinks").count()
        datalist1 = DataAs.objects.filter(tb_data_analysis_mh01="1", tb_data_analysis_bf01="<2 drinks").count()
        datalist2 = DataAs.objects.filter(tb_data_analysis_mh01="2", tb_data_analysis_bf01="<2 drinks").count()
        datalist3 = DataAs.objects.filter(tb_data_analysis_mh01="3", tb_data_analysis_bf01="<2 drinks").count()
        datalist4 = DataAs.objects.all().count()-datalist0-datalist1-datalist2-datalist3

        labels = ["count 0 <2 drinks ", "count 1 && <2 drinks", "count 2 && <2 drinks", "count 3 && <2 drinks", "other"]
        default_items=[datalist0,datalist1,datalist2,datalist3,datalist4]

        data = {
                "labels": labels,
                "default": default_items,
        }


        return Response(data)
