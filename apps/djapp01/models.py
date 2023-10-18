

from django.db import models
from datetime import datetime


# Create your models here.

'''
class Books(models.Model):
    # There is no need to specify the id field in the model class, it will be automatically generated

    tb_book_name = models.CharField(max_length=20, verbose_name="book title")
    # The variable string type of the database varchar(20)
    # max_length : Specify the maximum length of the variable string

    tb_book_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')
    # The money-related fields of the database decimal(7,2)
    # max_digits: Specify the maximum number of digits, including decimals
    # decimal_places: Specify the number of decimal places

    tb_book_hire_date = models.DateField(verbose_name='published date')
    # The date field of the database date
    # auto_now_add: When the object is added, it is automatically set to the current time, and will not change later
    # auto_now: Every time the object is updated, the time will be set to the time when it was updated
    # Avoid contradictions, `auto_now`, `auto_now_add`, `default` cannot appear at the same time, a field attribute can only have one of them set,
    # When `auto_now` or `auto_now_add` is set, the field will also have the `blank=True` attribute by default (the field can be empty)

    tb_book_author = models.CharField(max_length=200, verbose_name='author')
    tb_book_num = models.IntegerField(verbose_name='stock', default=0)
    tb_book_publish = models.CharField(max_length=200, verbose_name='Publisher')
    tb_book_type = models.CharField(max_length=300, verbose_name="category")
    tb_book_sales_volume = models.IntegerField(verbose_name='sales', default=0)

    def __str__(self):
        # Modify the description information of the object. At this time, when viewing the book object, it is not the default object address information, but the title of the book object
        return self.tb_book_name

    # The meta option must be part of the model class and cannot be used alone
    class Meta:
        db_table = 'tb_book'  # Specify the table name, the default is app name_model class name
        verbose_name = 'Book'  # The name of the table displayed in amdin, in singular form
        verbose_name_plural = verbose_name  # plural form
'''

class DataAs(models.Model):
    # There is no need to specify the id field in the model class, it will be automatically generated
    tb_data_analysis_name = models.CharField(max_length=200, verbose_name="name")

    #current_dateTime = datetime.now()
    #tb_data_analysis_date = models.DateTimeField(verbose_name='query date', default=datetime.now())
    tb_data_analysis_date = models.DateTimeField(verbose_name='query date', default=datetime(2010, 1, 1, 1, 1, 1, 342380))

    tb_data_analysis_username = models.CharField(max_length=200, verbose_name="user name", default='guest')

    # Medical History
    tb_data_analysis_mh01 = models.CharField(max_length=200, verbose_name="How many relative")
    # The variable string type of the database varchar(20)
    # max_length : Specify the maximum length of the variable string

    tb_data_analysis_mh02 = models.CharField(max_length=200, verbose_name="Bowel disease")
    # The money-related fields of the database decimal(7,2)
    # max_digits: Specify the maximum number of digits, including decimals
    # decimal_places: Specify the number of decimal places

    tb_data_analysis_mh03 = models.CharField(max_length=200, verbose_name="Diabetes")
    # The date field of the database date
    # auto_now_add: When the object is added, it is automatically set to the current time, and will not change later
    # auto_now: Every time the object is updated, the time will be set to the time when it was updated
    # Avoid contradictions, `auto_now`, `auto_now_add`, `default` cannot appear at the same time, a field attribute can only have one of them set,
    # When `auto_now` or `auto_now_add` is set, the field will also have the `blank=True` attribute by default (the field can be empty)

    # Behavioral Factor
    tb_data_analysis_bf01 = models.CharField(max_length=200, verbose_name="Alcohol")
    tb_data_analysis_bf02 = models.CharField(max_length=200, verbose_name="Obesity")
    tb_data_analysis_bf03 = models.CharField(max_length=200, verbose_name="Red Meat")
    tb_data_analysis_bf04 = models.CharField(max_length=200, verbose_name="Meat Consumption")
    tb_data_analysis_bf05 = models.CharField(max_length=200, verbose_name="Smoke")

    # Factor Decrease Risk
    tb_data_analysis_fd01 = models.CharField(max_length=200, verbose_name="Physical Activity", default='fd_01_default')
    tb_data_analysis_fd02 = models.CharField(max_length=200, verbose_name="Dairy Consumption", default='fd_01_default')
    tb_data_analysis_fd03 = models.CharField(max_length=200, verbose_name="Milk Consumption", default='fd_01_default')

    def __str__(self):
        # Modify the description information of the object. At this time, when viewing the book object, it is not the default object address information, but the title of the book object
        return self.tb_data_analysis_name

    # The meta option must be part of the model class and cannot be used alone
    class Meta:
        db_table = 'tb_data_analysis'  # Specify the table name, the default is app name_model class name
        verbose_name = 'Data_Analysis'  # The name of the table displayed in amdin, in singular form
        verbose_name_plural = verbose_name  # plural form

'''
class ChartTest(models.Model):
    tb_chart_test_time = models.DateTimeField()
    tb_chart_test_value = models.DecimalField(max_digits=10, decimal_places=2)
'''