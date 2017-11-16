from django.shortcuts import render
from django.http import HttpResponse, Http404  

def sum(request):
    print("i`m sum")
    print(request.GET) 
    sum = 0
    
    for item in request.GET:
        print (item, request.GET[item])
        values=request.GET.getlist(item)
        print(values)
        for value in values:
            try:
                sum+=int(value)
            except ValueError:
                return HttpResponse("error, " + item + " = "+ value + " is not a number", status=400)
    return HttpResponse("sum="+str(sum))


def mult(request):
    print("i`m mult")
    print(request.GET) 
    mult = 1
    
    for item in request.GET:
        print (item, request.GET[item])
        values=request.GET.getlist(item)
        print(values)
        for value in values:
            try:
                mult*=int(value)
            except ValueError:
                return HttpResponse("error, " + item + " = "+ value + " is not a number", status=400)

    return HttpResponse("mult="+str(mult))

def pow(request):
    print("i`m pow")
    count = 0
    for item in request.GET:
        count += 1

    if count == 2:
        arr=[]
        for item in request.GET:
            arr.append(request.GET.getlist(item)[0])
        try:
            a1 = int(arr[0])
            a2 = int(arr[1])
        except ValueError:
            return HttpResponse("error, one parameter is nan", status=400)
        pow = a1**a2               
        return HttpResponse("pow="+str(pow))
    else:
        return HttpResponse("error, power accept 2 parameters", status=400)

# Create your views here.