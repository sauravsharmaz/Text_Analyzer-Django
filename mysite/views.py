from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,"index.html")

def ProcessText(request):
	# Get the Text
	InpTxt= request.POST.get('textarea','default')

	# Get the CheckBox Values
	fullcaps=request.POST.get('upper','off')
	puncRem = request.POST.get('removepunc','off')

	if fullcaps=='on':
		tmpStr=""
		for char in InpTxt:
			tmpStr+= char.upper()
		InpTxt= tmpStr
		
	if puncRem=='on':
		punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
		tmpStr=""
		for char in InpTxt:
			if char not in punctuations:
				tmpStr+= char
		InpTxt=tmpStr
	
	if(fullcaps!='on' and puncRem != 'on'):
		return HttpResponse("Please choose a checkbox")

	params={'purpose':'Analyzed','result':tmpStr}
	return render(request,"al.html",params)