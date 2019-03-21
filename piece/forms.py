from django import forms
from .models import Repairpiece,Repairtype

class RepairForm(forms.ModelForm):
    name = forms.CharField(max_length=25 , label='الاسم')


    class Meta:
        model = Repairpiece
        widgets={'types':forms.CheckboxSelectMultiple}
        typeobj=Repairtype.objects.all()

        names=[objt.typename for objt in typeobj]

        #types=forms.ModelMultipleChoiceField(choices=names)
        types=forms.ModelMultipleChoiceField(queryset=Repairtype.objects.all())

        # def __init__(self, *args, **kwargs):
        #     # Only in case we build the form from an instance
        #     # (otherwise, 'toppings' list should be empty)
        #     if kwargs.get('instance'):
        #         # We get the 'initial' keyword argument or initialize it
        #         # as a dict if it didn't exist.
        #         initial = kwargs.setdefault('initial', {})
        #         # The widget for a ModelMultipleChoiceField expects
        #         # a list of primary key for the selected data.
        #
        #         # initial['types'] = [t.typename for t in kwargs['instance'].repairtype_set.all()]
        #
        #     forms.ModelForm.__init__(self, *args, **kwargs)

        #Override Save
        def save(self, commit=True):
            # Get the unsave Pizza instance
            instance = forms.ModelForm.save(self, False)

            # Prepare a 'save_m2m' method for the form,
            old_save_m2m = self.save_m2m

            def save_m2m():
                old_save_m2m()
                # This is where we actually link the pizza with toppings
                instance.repairtype_set.clear()
                instance.repairtype_set.add(*self.cleaned_data['types'])

            self.save_m2m = save_m2m

            # Do we need to save all changes now?
            if commit:
                instance.save()
                self.save_m2m()

            return instance

        fields=['name','phone','types']