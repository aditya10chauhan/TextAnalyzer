#  I have created this file - Aditya
from django.http import HttpResponse
from django.shortcuts import render

#def index (request):
 #return HttpResponse("<h1>hello Aditya</h1>")

#def about (request):
 #return HttpResponse("ut BootScare")

#def webpage (request):
 #return HttpResponse('''<h1> WebPage </h1> <a href = "https://practice.geeksforgeeks.org/problems/friends-pairing-problem5425/1">GFG</a>''')

def index (request):
 #params = { 'name':'Aditya' , 'college':'MNNIT'}
 return render(request , 'index.html')
 #return HttpResponse("HOME")_


def analyze(request):
 # Get the text
 djtext = request.POST.get('text', 'default')

 #check checkboxex values
 removepunc = request.POST.get('removepunc', 'off')
 fullcaps = request.POST.get('fullcaps', 'off')
 newlineremove = request.POST.get('newlineremove' , 'off')
 extraspaceremove = request.POST.get('extraspaceremove' , 'off')
 charcount  = request.POST.get('charcount' , 'off')



#check which checkbox is on
 if removepunc == "on":
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  analyzed = ""
  for char in djtext:
   if char not in punctuations:
    analyzed = analyzed + char
  params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
  #analyze the text
  djtext = analyzed
  #return render(request, 'analyze.html', params)

 if fullcaps == "on":
  analyzed = ""
  for char in djtext:
   analyzed = analyzed + char.upper()
  params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
  djtext = analyzed
 # return render(request, 'analyze.html', params)


 if(newlineremove == "on"):
  analyzed = ""
  for char in djtext:
      if char !="\n" and char !="\r":
            analyzed = analyzed + char

  params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}
  djtext = analyzed
  #return render(request, 'analyze.html', params)

 if(extraspaceremove == "on"):
  analyzed = ""
  for index, char in enumerate(djtext):
      if djtext[index] == " " and djtext[index+1] == " ":
       pass
      else:
            analyzed = analyzed + char
  params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}
  djtext = analyzed


 if charcount == "on":
    analyzed =0
    for char in djtext:
     if char !=" ":
      analyzed+=1
      params = {'purpose': 'Char Count', 'analyzed_text': analyzed}


 if(removepunc !="on" and newlineremove !="on" and fullcaps != "on" and extraspaceremove != "on" and charcount != "on"):
   return HttpResponse("ERROR")



 return render(request, 'analyze.html', params)

# def capfirst(request):
#  return HttpResponse('''<h>capatilize first </h2><a href="http://127.0.0.1:8000/">Back to home </a>''')
#
# def newlineremove(request):
#  return HttpResponse('''<h1>newlineremove</h1> <a href="http://127.0.0.1:8000/">Back to home </a>''')
#
# def spaceremove(request):
#  return HttpResponse('''<h1>space remove</h1> <a href="http://127.0.0.1:8000/">Back to home </a> ''')
#
# def charcount(request):
#  return HttpResponse('''<h1>charcount</h1> <a href="http://127.0.0.1:8000/">Back to home </a>''')


