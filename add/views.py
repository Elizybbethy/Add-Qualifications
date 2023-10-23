from django.shortcuts import get_object_or_404, render, redirect
from .models import Education, Document
from .forms import EducationForm, DocumentForm
from django.contrib.auth.decorators import login_required
from django.views import View

def success(request):
    return render(request, 'success.html')

class EducationView(View):
    def get(self, request):
        form =EducationForm()
        qualifications = Education.objects.all()
        return render(request, 'educ_form.html', {'qualifications':qualifications, 'form':form})
    
    def post(self, request):
        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'qualifications.html',{'form':form})


class QualificationView(View):
    def get(self, request, pk):
        qualification = Education.objects.get(pk=pk)
        return render(request, 'qualifications.html', {'qualification':qualification})
    
# def edit_qualification(request, qualification_id):
#     qualification =get_object_or_404(Education, id=qualification_id)
    
#     if request.method == 'POST':
#         form = EducationForm(request.POST, instance=qualification)
#         if form.is_valid():
#             form.save()
#             return redirect('edit_qualifications',)
        
#     else:
#         form = EducationForm(instance=qualification)
#     return render(request, 'edit_qualifications.html')

class EditEducationView(View):
    
    def get(self, request, pk):
        qualification = get_object_or_404(Education, pk=pk)
        form =EducationForm(instance=qualification)
        
        return render(request, 'edit_qualification.html', {'qualification':qualification, 'form':form, })
    
    def post(self, request, pk):
        qualification = get_object_or_404(Education, pk=pk)
        form = EducationForm(request.POST, request.FILES,instance=qualification)
        if form.is_valid():
            form.save()
            return redirect('qualification', pk=pk)

        else:
            return render(request, 'edit_qualification.html', {'qualification': qualification, 'form':form, })


class DocumentView(View):
    def get(self, request):
        form =DocumentForm()
        documents = Document.objects.all()
        return render(request, 'professional_docs.html', {'documents':documents, 'form':form})
    
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'documents.html',{'form':form})
        
        
class DocumentDetailsView(View):
    def get(self, request, pk):
        documents = Education.objects.get(pk=pk)
        return render(request, 'qualifications.html', {'documents':documents})