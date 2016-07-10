from django.db import models
from django.forms import ModelForm

class Atmb(models.Model):
    name=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    company_address=models.CharField(max_length=100)
    parent_id=models.PositiveIntegerField(blank=True,null=True)
    order_no=models.PositiveIntegerField()
    def __str__(self):
    	return  self.name
 #basic check item
class Site_Check_BasicItem(models.Model):
	check_date=models.DateField()
	weather=models.CharField(max_length=50)
	temperature=models.CharField(max_length=50)
	thunderbolt_day=models.CharField(max_length=50)
	thunderbolt_protect_level=models.CharField(max_length=50)
	power_ground_mode=models.CharField(max_length=50)
	check_engineer=models.CharField(max_length=50)
	site_overview=models.CharField(max_length=50)
	memo=models.CharField(max_length=50)
	report_suggestion=models.CharField(max_length=50)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)
	def __str__(self):
		return  ' baisc check item'  

class Site_Check_SpotPicture(models.Model):
	site_check_basicItem=models.ForeignKey(Site_Check_BasicItem, on_delete=models.CASCADE)
	spot_picture=models.ImageField(upload_to='upload/spotPicture')

class Site_Check_SysTopology(models.Model):
	site_check_basicItem=models.ForeignKey(Site_Check_BasicItem, on_delete=models.CASCADE)
	sys_topology=models.FileField(upload_to='upload/sysTopology')

class Site_Check_ThunderProtectPlan(models.Model):
	site_check_basicItem=models.ForeignKey(Site_Check_BasicItem, on_delete=models.CASCADE)
	thunder_protectPlan=models.FileField(upload_to='upload/thunderProtectPlan')

class Site_Check_ThunderHitEvent(models.Model):
	site_check_basicItem=models.ForeignKey(Site_Check_BasicItem, on_delete=models.CASCADE)
	thunder_hitDate=models.DateField()
	thunder_hitAnalysis=models.FileField(upload_to='upload/thunderHitAnalysis',blank=True,null=True)
	thunder_rectifyAction=models.FileField(upload_to='upload/thunderRectifyAction',blank=True,null=True)
#wireShield
EQUIPOTENTIAL_MODE=(('S','S'),('M','M'),('Ss','Ss'),('Mm','Mm'))
COMMENT_START=((0,'一星'),(1,'二星'),(2,'三星'),(3,'四星'),(4,'五星'))
class WireShield(models.Model):
	equipotential_mode=models.CharField(verbose_name="等电位形式",max_length=2,choices=EQUIPOTENTIAL_MODE,blank=True,null=True)
	meb_des=models.CharField(verbose_name="MEB描述",max_length=50,blank=True,null=True)
	meb_value=models.PositiveIntegerField(verbose_name="MEB值",blank=True,null=True)
	leb_des=models.CharField(verbose_name="LEB描述",max_length=50,blank=True,null=True)
	leb_value=models.PositiveIntegerField(verbose_name="LEB描述",blank=True,null=True)
	has_antistatic_floor=models.BooleanField(verbose_name="抗静电地板",default=False)
	is_bracket_under_ground=models.BooleanField(default=False)
	equipment_ground_star=models.PositiveIntegerField(verbose_name="设备接地",choices=COMMENT_START,blank=True,null=True)
	shelf_ground_start=models.PositiveIntegerField(verbose_name="机柜接地",choices=COMMENT_START,blank=True,null=True)
	earth_wire_star=models.PositiveIntegerField(verbose_name="地线长度/颜色/线径综合评定",choices=COMMENT_START,blank=True,null=True)
	misc_star=models.PositiveIntegerField(verbose_name="铠(屏蔽)层/光缆钢芯、冗余线、金属管道、消防柜、电池柜",choices=COMMENT_START,blank=True,null=True)
	equipotential_memo=models.CharField(verbose_name="备注（待确认后，自动同去步到常规项的备注中）:",max_length=50,blank=True,null=True)
	has_idc_shield=models.BooleanField(verbose_name="机房屏蔽",default=False)
	idc_shield_des=models.CharField(max_length=50,blank=True,null=True)
	has_shelf_shield=models.BooleanField(verbose_name="机柜屏蔽",default=False)
	shelf_shield_des=models.CharField(max_length=50,blank=True,null=True)
	has_line_shield=models.BooleanField(verbose_name="线缆屏蔽",default=False)
	line_shield_des=models.CharField(max_length=50,blank=True,null=True)
	shield_memo=models.CharField(verbose_name="备注（待确认后，自动同去步到常规项的备注中）:",max_length=50,blank=True,null=True)
	has_wire=models.BooleanField(verbose_name="弱电电缆-金属线线槽/管道",default=False)
	is_wire1_proper=models.BooleanField(verbose_name="电磁感应环路面积合理",default=False)
	is_wire2_proper=models.BooleanField(verbose_name="与避雷引下线距离合理",default=False)
	is_wire3_proper=models.BooleanField(verbose_name="强弱电电缆敷设距离合理",default=False)
	wire_memo=models.CharField(verbose_name="备注（待确认后，自动同去步到常规项的备注中）:",max_length=50,blank=True,null=True)
	atmb=models.OneToOneField(Atmb, on_delete=models.CASCADE)
	def __str__(self):
		return  ' WireShield' 

CHECK_RESULT=((0,'合格'),(1,'不合格'))
class Lightning_Receptor(models.Model):
	light_device=models.CharField(verbose_name='接闪装置',max_length=50,blank=True,null=True)
	position=models.CharField(verbose_name='位置,高度,覆盖',max_length=50,blank=True,null=True)
	resistance=models.PositiveIntegerField(verbose_name='接地电阻',blank=True,null=True)
	quantity=models.PositiveIntegerField(verbose_name='数量',blank=True,null=True)
	install_date=models.DateField(verbose_name='安装时间',blank=True,null=True)
	check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

CABLE_DISTANCE_OPERATOR=((0,'>='),(1,'<'))
class Down_Lead_Line(models.Model):
	mode=models.CharField(verbose_name='形式',max_length=50,blank=True,null=True)
	spec=models.CharField(verbose_name='规格',max_length=50,blank=True,null=True)
	resistance=models.PositiveIntegerField(verbose_name='接地电阻',blank=True,null=True)
	quantity=models.PositiveIntegerField(verbose_name='数量',blank=True,null=True)
	distance_away_cable=models.PositiveIntegerField(verbose_name='与电缆水平距离',choices=CABLE_DISTANCE_OPERATOR,blank=True,null=True)
	cable_quantity=models.PositiveIntegerField(verbose_name='1米',blank=True,null=True)
	check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

EARTH_DEVICE_MODE=((0,'自然接地体'),(1,'人工接地体'),(2,'联合接地装置'))
class Earth_Device(models.Model):
	mode=models.PositiveIntegerField(verbose_name='形式',choices=EARTH_DEVICE_MODE,blank=True,null=True)
	material=models.CharField(verbose_name='主要材料规格',max_length=50,blank=True,null=True)
	resistance=models.PositiveIntegerField(verbose_name='接地电阻',blank=True,null=True)
	position=models.CharField(verbose_name='位置',max_length=50,blank=True,null=True)
	construction_date=models.DateField(verbose_name='建设日期',blank=True,null=True)
	check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

class Thunder_External_Protect(models.Model):
	memo=models.CharField(verbose_name='备注',max_length=50)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

SPD_CATEGORY=((0,'复合型SPD'),(1,'1级SPD'),(2,'2级SPD'),(3,'3级SPD'),(4,'自带SPD'),(5,'直流SPD'))
class Power_SPD(models.Model):
	category=models.PositiveIntegerField(verbose_name='类别',choices=SPD_CATEGORY,blank=True,null=True)
	type=models.CharField(verbose_name='型号',max_length=50,blank=True,null=True)
	Uc=models.DecimalField(verbose_name='Uc', max_digits=5, decimal_places=2,blank=True,null=True)
	In=models.DecimalField(verbose_name='In', max_digits=5, decimal_places=2,blank=True,null=True)
	Up=models.DecimalField(verbose_name='Up', max_digits=5, decimal_places=2,blank=True,null=True)
	main_circuit_a=models.DecimalField(verbose_name='主电路空开', max_digits=5, decimal_places=2,blank=True,null=True)
	main_circuit_p=models.DecimalField(verbose_name='', max_digits=5, decimal_places=2,blank=True,null=True)
	backup_protection_a=models.DecimalField(verbose_name='后备保护', max_digits=5, decimal_places=2,blank=True,null=True)
	backup_protection_p=models.DecimalField(verbose_name='', max_digits=5, decimal_places=2,blank=True,null=True)
	wiring_total_len=models.DecimalField(verbose_name='接线总长', max_digits=5, decimal_places=2,blank=True,null=True)
	payload=models.BooleanField(verbose_name="负载",default=False)
	onsite_test=models.BooleanField(verbose_name="现场测试",default=False)
	pressure_1_v=models.DecimalField(verbose_name='压1', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_1_ua=models.DecimalField(verbose_name='',  max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_2_v=models.DecimalField(verbose_name='压2', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_2_ua=models.DecimalField(verbose_name='', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_3_v=models.DecimalField(verbose_name='压3', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_3_ua=models.DecimalField(verbose_name='', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_4_v=models.DecimalField(verbose_name='压4', max_digits=5, decimal_places=2,blank=True,null=True)
	pressure_4_ua=models.DecimalField(verbose_name='', max_digits=5, decimal_places=2,blank=True,null=True)
	quantity=models.PositiveIntegerField(verbose_name='数量',blank=True,null=True)
	install_date=models.DateField(verbose_name='安装日期',blank=True,null=True)
	install_place=models.CharField(verbose_name='安装位置',max_length=50,blank=True,null=True)
	check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)


class Signal_SPD(models.Model):
	category=models.PositiveIntegerField(verbose_name='类别',choices=SPD_CATEGORY,blank=True,null=True)
	type=models.CharField(verbose_name='型号',max_length=50,blank=True,null=True)
	Uc=models.DecimalField(verbose_name='Uc', max_digits=5, decimal_places=2,blank=True,null=True)
	In=models.DecimalField(verbose_name='In', max_digits=5, decimal_places=2,blank=True,null=True)
	Up=models.DecimalField(verbose_name='Up', max_digits=5, decimal_places=2,blank=True,null=True)
	ground_wire_len=models.DecimalField(verbose_name='地线长度', max_digits=5, decimal_places=2,blank=True,null=True)
	payload=models.BooleanField(verbose_name="负载",default=False)
	quantity=models.PositiveIntegerField(verbose_name='数量',blank=True,null=True)
	install_date=models.DateField(verbose_name='安装日期',blank=True,null=True)
	install_place=models.CharField(verbose_name='安装位置',max_length=50,blank=True,null=True)
	protection_device=models.CharField(verbose_name='保护设备',max_length=50,blank=True,null=True)
	check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
	atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

class Feeder_Line_SPD(models.Model):
    type=models.CharField(verbose_name='型号',max_length=50,blank=True,null=True)
    Uc=models.DecimalField(verbose_name='Uc', max_digits=5, decimal_places=2,blank=True,null=True)
    In=models.DecimalField(verbose_name='In', max_digits=5, decimal_places=2,blank=True,null=True)
    Up=models.DecimalField(verbose_name='Up', max_digits=5, decimal_places=2,blank=True,null=True)
    ground_wire_len=models.DecimalField(verbose_name='地线长度', max_digits=5, decimal_places=2,blank=True,null=True)
    quantity=models.PositiveIntegerField(verbose_name='数量',blank=True,null=True)
    install_date=models.DateField(verbose_name='安装日期',blank=True,null=True)
    install_place=models.CharField(verbose_name='安装位置',max_length=50,blank=True,null=True)
    check_result=models.PositiveIntegerField(verbose_name='检查结论',choices=CHECK_RESULT,blank=True,null=True)
    atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)

class SPD(models.Model):
    memo=models.CharField(verbose_name='备注',max_length=50,blank=True,null=True)
    atmb=models.ForeignKey(Atmb, on_delete=models.CASCADE)
