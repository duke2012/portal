from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .utils import  tools
from .models import *
from .forms import *
from .formSet import *
import  json

# Create your views here.
def  index(request):
	menus=tools. getIndexMenuList()
	context={'menuList':menus}
	return render(request, 'atmb/base.html', context)
def  basicItem(request,site_id):
	try:
		item=Site_Check_BasicItem.objects.get(atmb=site_id)
	except:
		item=None
	context={'basicItem':item,'siteId':site_id};
	return render(request, 'atmb/basicItem.html', context)
def postBasicItem(request,site_id):
	if request.method=='POST':
		siteCheckId=request.POST.get('siteCheckId')
		try:
			siteCheckBasicItem=Site_Check_BasicItem.objects.get(atmb=site_id)
		except:
			siteCheckBasicItem=Site_Check_BasicItem()
		siteCheckBasicItem.check_date=request.POST.get('checkDate',None)
		siteCheckBasicItem.weather=request.POST.get('weather',None)
		siteCheckBasicItem.temperature=request.POST.get('temperature',None)
		siteCheckBasicItem.thunderbolt_day=request.POST.get('thunderboltDay',None)
		siteCheckBasicItem.thunderbolt_protect_level=request.POST.get('thunderboltProtectLevel',None)
		siteCheckBasicItem.thunderbolt_protect_level=request.POST.get('thunderboltProtectLevel',None)
		siteCheckBasicItem.power_ground_mode=request.POST.get('powerGroundMode',None)
		siteCheckBasicItem.check_engineer=request.POST.get('checkEngineer',None)
		siteCheckBasicItem.site_overview=request.POST.get('siteOverview',None)
		siteCheckBasicItem.memo=request.POST.get('memo',None)
		siteCheckBasicItem.report_suggestion=request.POST.get('reportSuggestion',None)
		siteCheckBasicItem.atmb_id=site_id
		siteCheckBasicItem.save()
		#upload picture;
		spotPicture=Site_Check_SpotPicture()
		spotPicture.site_check_basicItem_id=siteCheckBasicItem.id
		spotPicture.spot_picture=request.FILES.get('spotPicture')
		if spotPicture.spot_picture.name:
			spotPicture.save()
		
		sysTopology=Site_Check_SysTopology()
		sysTopology.site_check_basicItem_id=siteCheckBasicItem.id
		sysTopology.sys_topology=request.FILES.get('sysTopology')
		if sysTopology.sys_topology.name:
			sysTopology.save()
		
		thunderProtectPlan=Site_Check_ThunderProtectPlan()
		thunderProtectPlan.site_check_basicItem_id=siteCheckBasicItem.id
		thunderProtectPlan.thunder_protectPlan=request.FILES.get('thunderProtectPlan')
		if thunderProtectPlan.thunder_protectPlan:
			thunderProtectPlan.save()

		thunderHitEvent=Site_Check_ThunderHitEvent()
		thunderHitEvent.thunder_hitDate=request.POST.get('checkDate',None)
		thunderHitEvent.site_check_basicItem_id=siteCheckBasicItem.id
		thunderHitEvent.thunder_hitAnalysis=request.FILES.get('thunderHitAnalysis',None)
		thunderHitEvent.thunder_rectifyAction=request.FILES.get('thunderRectifyAction',None)
		if thunderHitEvent.thunder_hitDate and (thunderHitEvent.thunder_hitAnalysis or thunderHitEvent.thunder_rectifyAction):
			thunderHitEvent.save()
		return HttpResponseRedirect(reverse('basicItem',kwargs={'site_id': site_id}))	
def  thunderExternalProtect(request,site_id):
	if request.method=='POST':
		form=LightningReceptorForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()

	else:

	    lightningReceptors= LightningReceptorFormSet(queryset=Lightning_Receptor.objects.filter(atmb=site_id))
	    downLeadLines=DownLeadLineFormSet(queryset=Down_Lead_Line.objects.filter(atmb=site_id))
	    earthDevices=Earth_Device.objects.filter(atmb=site_id)
	    memo=Thunder_External_Protect.objects.filter(atmb=site_id)
	    context={'lightningReceptors':lightningReceptors,'downLeadLines':downLeadLines,'earthDevices':earthDevices,'memo':memo,'site_id':site_id}    
	    return render(request, 'atmb/thunderExternalProtect.html', context)
def  thunderBoltPulse(request):
	return render(request, 'atmb/thunderBoltPulse.html', context)
def  wireShield(request,site_id):
	try:
		temp=WireShield.objects.get(atmb=site_id)
	except:
		temp=None	
	form=WireShieldForm(instance=temp)
	if request.method=='POST':
		form=WireShieldForm(request.POST,instance=temp)
		if form.is_valid():
			temp=form.save(commit=False)
			temp.atmb_id=site_id
			temp.save()
			return HttpResponseRedirect(reverse('wireShield',kwargs={'site_id': site_id}))	
	return render(request, 'atmb/WireShield.html', {'form': form,'site_id':site_id})
	




        

    