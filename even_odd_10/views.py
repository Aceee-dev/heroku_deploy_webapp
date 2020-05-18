import time

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from even_odd_10.models import EoResults



def eo_number(request):
    num_a=''
    result1=0
    result2=0

    if request.GET.get('number'):
        num_a = request.GET.get('number') 
        li= num_a.split (",")
        li1= []
        for i in li:
            li1.append(int(i))

        for it in li:
            if (int(it) % 2) == 0:  
                 result1=result1+int(it)
            else:  
                 result2=result2+int(it)

        obj = EoResults.objects.create(
               num_arr=num_a,result1=result1,result2=result2)
        obj.save()

    return render(
        request,
        'index1.html',
        {
            'result1': result1,
            'result2': result2,
        }
    )
