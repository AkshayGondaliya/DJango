# i have created not by deafault

from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("hello")
#
# def about(request):
#     #f=open("practice.txt","r+")
#     #text=f.read()
#     return HttpResponse('''<h1>akshay</h1> <a href="https://www.youtube.com/watch?v=WFxdxNx8iKE&list=PL1-aSABtP6AB1zZrjGs_evFIM51W_S-Jz&index=3"> odoo play list </a>''')

def index(request):
    #return HttpResponse("hello")
    # params={"name":"akshay"}
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    charcount = request.POST.get('charcount', 'off')
    #params={}
    #print(removepunc)
    if removepunc=='on':

        #anatext=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #params['purpose1']='removepunctuations'
        #params['analyzed_text'] = analyzed

        params={'analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html', params)

    if charcount == "on":
        dic = {}
        for i in djtext:
            if i not in dic.keys():

                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        params = {'analyzed_text': dic}
        #params['purpose2']='char counter'
        #params['counter'] = dic
    if(charcount!="on" and removepunc!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

        # elif charcount=="on":
    #     dic={}
    #     for i in djtext:
    #         if i not in dic.keys():
    #
    #             dic[i] = 1
    #         else:
    #             dic[i] = dic[i] + 1
    #     params={'purpose':'char counter','analyzed_text':dic}
    #     return render(request,'analyze.html', params)


    #else:
        #return HttpResponse("Error")