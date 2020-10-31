from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.views import View



user = get_user_model()
from .data import *
from django.views.decorators.csrf import csrf_exempt



from rest_framework.response import Response
from rest_framework.views import APIView
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):


        data = {
            "total_cases":total_cases(),
            "total_deaths": total_deaths(),
            "continents_names" : continents_names ,
            "continents_cases": continents_total_cases,
            "continents_active_cases": continents_active_cases,
            "world_dates_day_by_day" : world_dates_day_by_day ,
            "world_cases_day_by_day" : world_cases_day_by_day,
            "world_deaths_day_by_day" : world_deaths_day_by_day,
            "all_countries" : all_countries
        }

        return Response(data)

def country(request,country):

    country_data_day_by_day=[]
    country_cases_day_by_day=[]
    country_dates_day_by_day=[]
    country_deaths_day_by_day=[]
    for cnt in data1 :
        if cnt[0]==country or cnt[2]==country :
            country_data_day_by_day.append(cnt),country_cases_day_by_day.append(cnt[5]),
            country_dates_day_by_day.append(cnt[3]), country_deaths_day_by_day.append(cnt[8])






    country_data = covid.get_status_by_country_name(country)
    country_data.pop("total_tests_per_million", None)
    for k, v in country_data.items():
        if k != "country":
            country_data[k] = format(v, ",")
    total_cases=country_data['confirmed']
    total_deaths = country_data['deaths']
    total_recovered = country_data['recovered']
    active_cases = country_data['active']
    return render(request, 'welcome/country.html',{'country':country,'country_data':country_data,
                                                   'country_cases_day_by_day' :country_cases_day_by_day,
                                                   'country_deaths_day_by_day' :country_deaths_day_by_day,
                                                   'country_dates_day_by_day' :country_dates_day_by_day,

                                                 'total_cases':total_cases,'active_cases':active_cases,'total_recovered' : total_recovered ,'total_deaths':total_deaths  })
class HomeView(View):
    def get(self,request,*args,**kwargs):



        return render(request,'welcome/charts.html',{"customers":10,"total_cases":total_cases(),
                                                     "total_deaths":total_deaths(),"active_cases":active_cases(),
                                                     "total_recovered":total_recovered(),"europe":europe,
                                                     "asia":asia,"oceania":oceania,"africa":africa,
                                                     "north_america":north_america,"south_america":south_america,
                                                     "covid":covid1,"world":world,"europe_all":europe_all,
                                                     "asia_all":asia_all,"oceania_all":oceania_all,"africa_all":africa_all,
                                                     "north_america_all":north_america_all,"south_america_all":south_america_all})

def get_data(request,*args,**kwargs):
    data={
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

@csrf_exempt
def contactus(request):
    if (request.POST):
        login_data = request.POST.dict()
        firstname = login_data.get("firstname")
        laststname = login_data.get("lastname")
        name = firstname + " " + laststname
        areacode =login_data.get("areacode")
        telnum =login_data.get("telnum")
        tel = areacode +" " + telnum
        approve = request.POST.get('approve', "false")
        subject = "Registration to receive daily updates about COVID-19"
        #feedback = login_data.get("feedback")
        emailid = login_data.get("emailid")
        select = request.POST['dropdown']
        contenu="Hi DataViz community, \n My name is : " + name + " . \n My telephone number is : " + tel +" .\n "
        if approve != "false" :
            #contenu+= "Yes , I have no problem if you contact me but via " + select +" , please ! \n"
            if select=="Telephone" :
                contenu= "Hi " + name +",\n Thank you for registration . You will receive daily updates about COVID-19 by message on your Phone "+ tel + " .\n cdt,\n DataViz Community."
            else :
                contenu= "Hi " + name +",\n \n Thank you for registration . You will receive daily updates about COVID-19 by Mail .\n \n cdt,\n DataViz Community."

       # else :
       # contenu += "No , please don\'t disturb me .\n"
        #contenu+="Feedback : "

        send_mail(subject, contenu, 'salem.dhouimir@ieee.org',[emailid])

        return render(request, 'welcome/contactus.html')
    else:
        return render(request, 'welcome/contactus.html')

def news(request):
    return render(request, 'welcome/news.html')
def qa(request):
    return render(request, 'welcome/qa.html')






