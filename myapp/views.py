from django.shortcuts import render
from myapp.models import Start, AddSuggestion
from django_pandas.io import read_frame
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


def home(request):
    try:
        a = Start.objects.all()
        if request.method=="GET":
            b = read_frame(a)
            return render(request,'myapp/home.html',{'b':b})
        c = request.POST['resname']
        m = request.POST['addSuggestion']
        if(m == "0"):
            q = Start.objects.values("coupon").filter(name=c)
            qq = read_frame(q)
            print(q)
            # qqq = qq.coupon
            # return HttpResponse(q)
            return render(request,'myapp/coupon.html',{'cou':qq})
        else:
            b = read_frame(a)  
            suggestion = AddSuggestion.objects.create(suggestion=c)
            return render(request,'myapp/home.html',{'b':b}) 

    except MultiValueDictKeyError:
        return render(request,'myapp/home.html')     
    
    