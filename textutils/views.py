# i have created this file--Abhi
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
	return render(request, 'index.html')

def analyze(request):
	djtext=request.POST.get('text','default')
	removepunc=request.POST.get('removepunc','off')
	captilize=request.POST.get('captilize','off')
	NewLineRemover=request.POST.get('NewLineRemover','off')
	ExtraSpaceRemover=request.POST.get('ExtraSpaceRemover','off')
	CharacterCount=request.POST.get('CharacterCount','off')


	if removepunc == "on":
		punctuations = '''!"#$%&'()*+, -./:;<=>?@[]^_`{|}~'''
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char
		params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
		djtext=analyzed
		#return render(request, 'analyze.html',params)

	if(captilize=="on"):
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		params = {'purpose':'converted to uppercase ', 'analyzed_text': analyzed}
		djtext=analyzed
		#return render(request, 'analyze.html',params)

	if(NewLineRemover=="on"):
		analyzed=""
		for char in djtext:
			if char!="\n" and char!="\r":
				analyzed=analyzed+char
		params = {'purpose':'removed new line', 'analyzed_text': analyzed}
		djtext=analyzed
		#return render(request, 'analyze.html',params)

	if(ExtraSpaceRemover=="on"):
		analyzed=""
		for index,char in enumerate(djtext):
			if djtext[index]==" " and djtext[index+1]==" ":
				pass
			else:
				analyzed=analyzed+char
		params = {'purpose':'Extra space removed', 'analyzed_text': analyzed}
		djtext=analyzed
		#return render(request, 'analyze.html',params)

	if(CharacterCount=="on"):
		lst=[]
		for i in range(len(djtext)):
			lst.append(djtext[i])
		count=len(lst)
		params = {'purpose':'number of character', 'analyzed_text': count}
	
	if(removepunc!="on" and NewLineRemover!="on" and captilize!="on" and ExtraSpaceRemover!="on" and CharacterCount!="on"):
		return HttpResponse("please select any opertion")

		

	return render(request, 'analyze.html',params)

def about(request):
	return HttpResponse("<h1>about abhinav</h1>")

