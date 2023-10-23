from django import forms
from .models import Document, Education

STATUS_CHOICE =(
    ('junior','junior'),
    ('average','average'),
    ('senior','senior'),
    ('experienced','experienced'),
)
DEGREE_CHOICES =(
    ('Certificate','Certificate'),
    ('Diploma','Diploma'),
    ('Bachelor','Bachelor'),
    ('Master','Master'),
    ('phd','phd'),
)
class EducationForm(forms.ModelForm):
    status =forms.ChoiceField(choices=STATUS_CHOICE, widget=forms.RadioSelect)
    # degree =forms.ChoiceField(choices=DEGREE_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = Education
        fields =['school_name', 'field_of_study','degree', 'status', 'start_date', 'end_date', 'grade', 'activities_and_societies', 'description', 'my_file' ]
        # my_file =forms.FileField(required=False)
        
        widgets ={
            'description': forms.Textarea(attrs={'rows':2, 'cols':40}),
            'school_name':forms.TextInput(attrs={'placeholder': 'Ex: Makerere University'}),
            'degree':forms.TextInput(attrs={'placeholder': "Ex: Bachelor's"}),
            'field_of_study':forms.TextInput(attrs={'placeholder': 'Ex: Medicine'}),
            'start_date': forms.SelectDateWidget(
                empty_label= ("Choose Year", "Choose Month","Choose Day")),
            'end_date': forms.SelectDateWidget(
                empty_label= ("Choose Year", "Choose Month","Choose Day"))
            
        }
        
class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ['name', 'my_doc']
