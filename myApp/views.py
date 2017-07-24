from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import MyModel

# Create your views here.
def myView(request):
	# return HttpResponse ('<h1> Test Page myView </h1>')
	my_object = MyModel.objects.all()
	context= {
	'title': 'list',
	'user': request.user,
	'my_object': my_object,


	}
	return render (request,'MyView.html',context)

def mySecondView(request):
	# return HttpResponse ('<h1> Test Page mySecondView </h1>')
	context = {


	}
	return render (request,'MySecondView.html',context)

def MyList (request):
	ObjList = MyModel.objects.all()

	context = {
	'MyList': ObjList,

	}

	return render (request, 'MyList.html', context)

def MyDetail (request, MyModel_id):
	ObjDetail = MyModel.objects.get(id=MyModel_id)
	context = {
	'MyDetail':ObjDetail,

	}
	return render (request, 'MyDetail.html', context)