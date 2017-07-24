from django.shortcuts import render
from app.models import Brainstatus
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from  datetime import datetime
import json,random
from django.views.decorators.csrf import csrf_exempt



def populate_db():
	year = [str(i) for i in range(2010,2017)]
	month = [str(i) for i in range(1,13)]
	day = [str(i) for i in range(1,25)]

	for i in range(2392,2410):
		brainno = str(i)
		seriesid = 'F'
		a = '%s-%s-%s'%(random.choice(year),random.choice(month),random.choice(day))
		dop = datetime.strptime(a,'%Y-%m-%d')
		b = '%s-%s-%s'%(random.choice(year),random.choice(month),random.choice(day))
		doi = datetime.strptime(b,'%Y-%m-%d')
		status = 1
		c = '%s-%s-%s'%(random.choice(year),random.choice(month),random.choice(day))
		lastupdate = datetime.strptime(c,'%Y-%m-%d')
		nextstep = 2
		Brainstatus(brainno = brainno,seriesid = seriesid,dateofperf = dop,dateofimg = doi,status = status , lastupdate = lastupdate , nextstep = nextstep).save()

@csrf_exempt
def brain_status(request):
	
	if request.is_ajax() and request.POST:
		sort_order = json.loads(request.body)	
	else:
		sort_order = {'doi':0,'dop':0,'lu':1}
	
	key_map = {'doi':'-dateofimg','dop':'-dateofperf','lu':'-lastupdate'}	
	#print sort_order	
	for i in sort_order:
		if sort_order[i] == 1:
			orderby = key_map[i]	

	brainnames_ = Brainstatus.objects.all().values_list('brainno')
	brainnames  = [i[0].encode('utf8') for i in brainnames_]	
	#populate_db()
	brain_list = Brainstatus.objects.all().order_by(orderby)
	#brain_list = Brainstatus.objects.all().order_by('-dateofperf')
	#brain_list = Brainstatus.objects.all().order_by('-dateofimg')
	page = request.GET.get('page',1)
	paginator = Paginator(brain_list,10)

	try:
		brainlist = paginator.page(page)
	except PageNotAnInteger:
		brainlist = paginator.page(1)
	except EmptyPage:
		brainlist = paginator.page(paginator.num_pages)
	
	return render(request,'brainlist.html',{'brainlist':brainlist,'brainnames':brainnames})

def eachbrain(request,brno):

	brain_list = Brainstatus.objects.filter(brainno=brno).all()
	#brain_list = Brainstatus.objects.all().order_by('-dateofperf')
	#brain_list = Brainstatus.objects.all().order_by('-dateofimg')
	page = request.GET.get('page',1)
	paginator = Paginator(brain_list,10)

	try:
		brainlist = paginator.page(page)
	except PageNotAnInteger:
		brainlist = paginator.page(1)
	except EmptyPage:
		brainlist = paginator.page(paginator.num_pages)
	
	return render(request,'singlebrain.html',{'brainlist':brainlist})
		
