from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .utils import  tools
from .models import *
from .forms import *
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
def  thunderExternalProtect(request):
	return render(request, 'atmb/thunderExternalProtect.html', context)
def  thunderBoltPulse(request):
	return render(request, 'atmb/thunderBoltPulse.html', context)
def  wireShield(request,site_id):
	form=WireShieldForm()
	
	try:
		item=WireShield.objects.get(atmb=site_id)
	except:
		item=None
	context={'wireShield':item,'siteId':site_id};
	return render(request, 'atmb/wireShield.html', context)

def postWireShield(request,site_id):
	if request.method=='POST':
		siteCheckId=request.POST.get('siteCheckId')
		try:
			wireShield=WireShield.objects.get(atmb=site_id)
		except:
			wireShield=WireShield()
		wireShield.equipotential_mode=request.POST.get('equipotentialMode',None)
		wireShield.meb_des=request.POST.get('mebDes',None)
		wireShield.meb_value=request.POST.get('mebValue',None)
		wireShield.leb_des=request.POST.get('lebDes',None)
		wireShield.leb_value=request.POST.get('lebValue',None)
		wireShield.has_antistatic_floor=request.POST.get('hasAntistaticFloor',None)
		wireShield.is_bracket_under_ground=request.POST.get('isBracketUnderGround',None)
		wireShield.equipment_ground_star=request.POST.get('equipmentGroundStar',None)
		wireShield.shelf_ground_start=request.POST.get('shelfGroundStart',None)
		wireShield.earth_wire_star=request.POST.get('earthWireStar',None)
		wireShield.misc_star=request.POST.get('miscStar',None)
		wireShield.equipotential_memo=request.POST.get('equipotentialMemo',None)
		wireShield.has_idc_shield=request.POST.get('hasIdcShield',None)
		wireShield.idc_shield_des=request.POST.get('idcShieldDes',None)
		wireShield.has_shelf_shield=request.POST.get('hasShelfShield',None)
		wireShield.shelf_shield_des=request.POST.get('shelfShieldDes',None)
		wireShield.has_line_shield=request.POST.get('hasLineShield',None)
		wireShield.line_shield_des=request.POST.get('lineShieldDes',None)
		wireShield.shield_memo=request.POST.get('shieldMemo',None)
		wireShield.has_wire=request.POST.get('hasWire',None)
		wireShield.is_wire1_proper=request.POST.get('isWire1Proper',None)
		wireShield.is_wire2_proper=request.POST.get('isWire2Proper',None)
		wireShield.is_wire3_proper=request.POST.get('isWire3Proper',None)
		wireShield.wire_memo=request.POST.get('wireMemo',None)
                


        

    