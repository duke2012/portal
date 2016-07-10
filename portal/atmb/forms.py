from .models import *
from django.forms import ModelForm
from django.forms import Textarea

class WireShieldForm(ModelForm):
	class Meta:
		model=WireShield
		exclude = ('atmb',)
		widgets={
                        'wire_memo': Textarea(attrs={'cols': 100, 'rows': 5}),
                        'equipotential_memo': Textarea(attrs={'cols': 100, 'rows': 5}),
                        'shield_memo': Textarea(attrs={'cols': 100, 'rows': 5})
                        }
class LightningReceptorForm(ModelForm):
	class Meta:
		model=Lightning_Receptor
		exclude = ('atmb',)
