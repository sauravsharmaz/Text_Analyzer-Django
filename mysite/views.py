from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,"index.html")

def ProcessText(request):
	# Get the Text
	InpTxt= request.GET.get('textarea','default')

	# Get the CheckBox Values
	fullcaps=request.GET.get('upper','off')
	puncRem = request.GET.get('removepunc','off')

	if fullcaps=='on':
		tmpStr=""
		for char in InpTxt:
			tmpStr+= char.upper()
		params={'purpose':'Converted to upper case','result':tmpStr}
		return render(request,"al.html",params)

	elif puncRem=='on':
		punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
		tmpStr=""
		for char in InpTxt:
			if char not in punctuations:
				tmpStr+= char
		params={'purpose':'Punctuations Removed','result':tmpStr}
		return render(request, 'al.html',params)