from ResumeUploader.form import ResumeForm
from ResumeUploader.models import resumeModel
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def homepage(request):
    if request.method == 'POST':  # checking that whatever we are sending through the form is Post or Get method
        obj = ResumeForm(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            # user_name = obj.cleaned_data['Full Name']
            # user_surname = obj.cleaned_data['Surname']
            # user_conatact = obj.cleaned_data['Contact No']
            # user_email = obj.cleaned_data['Email ID']
            # user_dob = obj.cleaned_data['Date-of-Birth']
            # user_locality = obj.cleaned_data['locality']
            # user_city = obj.cleaned_data['city']
            # user_state = obj.cleaned_data['state']
            # user_pincode = obj.cleaned_data['pincode']
            # user_image = obj.cleaned_data['Upload Image']
            # user_resume = obj.cleaned_data['Upload Resume']
    
            # userData = resumeModel(userName = user_name, userSurname = user_surname, userContact = user_conatact, userEmail = user_email, DoB = user_dob, locality = user_locality, city = user_city, state = user_state, pincode = user_pincode, profileImage = user_image, resumeHolder = user_resume)    
            # userData.save()
        # return HttpResponse('<h1> Your Data Saved Successfully </h1>')
        return redirect('/')  #returning back to the main page
    form = ResumeForm()
    display_item = resumeModel.objects.all()
    return render(request,'index.html',{'form':form,'display_item':display_item})

def candidateViewer(request,id):
    if request.method == 'POST':
        id_picker = resumeModel.objects.get(pk = id)
        # data_display = resumeModel.objects.all()
        return HttpResponse('candidate.html',{'id_picker':id_picker})
    return render(request,'candidate.html',{})
