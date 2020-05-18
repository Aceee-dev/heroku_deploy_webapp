import time

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from fib_api.models import FibonacciResults


def fibonacci_calculation(num):
    results=[]
    if num < 2:
        results.append(1)
        res=str(results).strip('[]')
        return res
    else:
        num_seq_1 = 1
        num_seq_2 = 1
        results.append(1)
        results.append(1)
        for i in range(2, num):
            temp = num_seq_1 + num_seq_2
            results.append(temp)
            num_seq_1 = num_seq_2
            num_seq_2 = temp
        res=str(results).strip('[]')
        return res


def fib_number(request):
    num = 0
    result = ''
    time_taken = ''

    if request.GET.get('number'):
        start_time = time.time()
        number = request.GET.get('number')
        num = int(number)
        result = fibonacci_calculation(num)
        end_time = time.time() - start_time
        time_taken = str(end_time)[0:4]

        obj = FibonacciResults.objects.create(
            number=num, result=result, time_taken=time_taken)
        obj.save()

    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
            'time_taken': time_taken
        }
    )
