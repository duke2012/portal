from .models import *
from django.forms import modelformset_factory
from django.forms import Textarea

LightningReceptorFormSet = modelformset_factory(Lightning_Receptor, exclude=('atmb',), extra=1)
DownLeadLineFormSet=modelformset_factory(Down_Lead_Line, exclude=('atmb',), extra=1)
EarthDeviceFormSet=modelformset_factory(Earth_Device, exclude=('atmb',), extra=1)
ThunderExternalProtectFormSet=modelformset_factory(Thunder_External_Protect, exclude=('atmb',), extra=1,max_num=1,widgets={'memo': Textarea(attrs={'cols': 100, 'rows': 10})})

PowerSpdFormSet=modelformset_factory(Power_SPD, exclude=('atmb',), extra=1)
SignalSpdFormSet=modelformset_factory(Signal_SPD, exclude=('atmb',), extra=1)
FeederLineSpdFormSet=modelformset_factory(Feeder_Line_SPD, exclude=('atmb',), extra=1)
SpdFormSet= modelformset_factory(SPD, exclude=('atmb',), extra=1,max_num=1, widgets={'memo': Textarea(attrs={'cols': 100, 'rows': 10})})