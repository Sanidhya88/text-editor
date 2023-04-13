# i created this file -sanidhya

from django.http import HttpResponse
from django.shortcuts import render



def home(request):
   
    return render(request,'index2.html')


def analyze(request):
     #get the text 
     name=request.GET.get('text','default')


     #get check box values 
     removepunc=request.GET.get('removepunction','off')
     uppercases=request.GET.get('uppercase','off')
     newlineremover=request.GET.get('newlineremover','off')
     countsvalues=request.GET.get('counts','off')
     
    # check if the checkbox is on 
     if countsvalues=='on':
          pureanaylse= " "
          
          pureanaylse= str(len(name))
                
          params={ 'purpose':'removed punctuation','anaylzed_text':pureanaylse}
          return render(request,'analyze.html',params)
         


     if removepunc == "on":
    
        puncuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        pureanaylse= " "
        for char in name:
            if char not in puncuations:
                pureanaylse=pureanaylse + char
                
        params={ 'purpose':'removed punctuation','anaylzed_text':pureanaylse}
        return render(request,'analyze.html',params)
     #check if upper case is on     
     elif uppercases == "on":
         pureanaylse= " "
         for char in name:
            pureanaylse=pureanaylse + char.upper()

         params={ 'purpose':'uppercase','anaylzed_text':pureanaylse}
         return render(request,'analyze.html',params)
     elif newlineremover=="on":
         pureanaylse=" "

         for char in name:
            if char !="/n":
                pureanaylse=pureanaylse + char

         params={ 'purpose':'new line remover ','anaylzed_text':pureanaylse}
         return render(request,'analyze.html',params)


           

     else:
         
         return HttpResponse( name)


def about(request):
    return HttpResponse("This is a about page ")

def contact(request):
    return HttpResponse(" <h1> welcome to the contact page </h1> <a href='/'> back </a>" )