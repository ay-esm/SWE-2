from .models import *
from django import forms
from .models import *
from django.core.validators import RegexValidator
from django.forms import formset_factory
class Repair_item_From(forms.Form):
    type1_option = [
        ('-', '-'),
        (' 1/2طقم', ' 1/2طقم'),
        ('اسورة احجار', 'اسورة احجار'),
        ('اسورة عجلة', 'اسورة عجلة'),
        (' اسورة مفرودة', 'اسورة مفرودة'),
        ('بورتكلية','بورتكلية'),
        ('تعليقة','تعليقةر'),
        ('توينز','توينز'),
        ('حرف','حرف'),
        ('حلق','حلق'),
        ('حلق احجار','حلق احجار'),
        ('حلق بطن','حلق بطن'),
        ('خاتم حريمي','خاتم حريمي'),
        ('خاتم رجالي','خاتم رجالي'),
        ('خاتم عقلة','خاتم عقلة'),
        ('خلخال','خلخال'),
        ('دبلة','دبلة'),
        ('زرار قميص','زرار قميص'),
        ('زمام  دهب','زمام  دهب'),
        ('زمام استنلس','زمام استنلس'),
        ('زمام فضة','زمام فضة'),
        ('ساعة','ساعة'),
        ('سبحة احجار','سبحة احجار'),
        ('سبحة فضة','سبحة فضة'),
        ('سلسلة حريمي','سلسلة حريمي'),
        ('سلسلة رجالي','سلسلة رجالي'),
        ('شرابة سبحة','شرابة سبحة'),
        ('طوق فضة','طوق فضة'),
        ('عقد احجار','عقد احجار'),
        ('غويشة','غويشة'),
        ('كولية','كولية'),
        ('محبس كامل','محبس كامل'),
        ('ميدالية','ميدالية'),
        ('طقم كامل','طقم كامل'),
        ('اخري','اخري'),
    ]
    type2_option = [
        ('-','-'),
        ('مصري','مصري'),
        ('ايطالي','ايطالي'),
        ('تركي','تركي'),
        ('هاند','هاند'),
        ('متنوع','متنوع'),
        ('استنليس','استنليس'),
        ('تنجستين','تنجستين'),
        ('ذهب','ذهب'),
        ('اخري','اخري')
                    ]
    type3_option=[
        ('-','-'),
        ('مرمات خارجية','مرمات خارجية'),
        ('مرمات داخلية','مرمات داخلية'),
        ('صيانة','صيانة'),
        ('ضمان','ضمان'),
        ('طلب خاص','طلب خاص'),
        ('اخري','اخري')
    ]
    repair_option = [
        ('-','-'),
        ('توسيع','توسيع'),
        ('تصغير','تصغير'),
        ('لحام','لحام'),
        ('عمل دبلة','عمل دبلة'),
        ('طلاء ذهب','طلاء ذهب'),
        ('تركيب','تركيب'),
        ('طلاء بلاتين','طلاء بلاتين'),
        ('تلميع','تلميع'),
        ('طلاء فضة','طلاء فضة'),
        ('طلاء نيكل','طلاء نيكل'),
        ('لضم','لضم'),
        ('كتابة','كتابة'),
        ('عمل خرطوش','عمل خرطوش'),
        ('عمل رقبة','عمل رقبة'),
        ('عمل حجر','عمل حجر'),
        ('مطلوب حجر','مطلوب حجر'),
        ('اخري','اخري'),
    ]

    numeric = RegexValidator(r'^[1-9]*$', 'Only numeric characters are allowed.')

    type1 =forms.CharField(required=True,label="البيان",widget=forms.Select(choices=type1_option))

    type2 =forms.CharField(required=True,label="الصنف",widget=forms.Select(choices=type2_option))

    type3 =forms.CharField(required=True,label="النوع",widget=forms.Select(choices=type3_option))

    price =forms.DecimalField(required=True,validators=[numeric],label="السعر",decimal_places=2,widget=forms.TextInput(attrs={
                                'class': 'form-control ta-r',
                                'placeholder': '0',
                            }))
    summary = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Repair_item

        fields=['type1','type2','type3','price','summary',]


repair_form_set = formset_factory(Repair_item_From, extra=1)