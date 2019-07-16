from django.shortcuts import render, redirect
from newrequest.models import NewRequest
from .forms import approvalform
from adminprofile.models import items
# Create your views here.
def home(request):
    req = NewRequest.objects.raw('select * from NewRequest')
    return render(request,'adminrequest/home.html',{'req':req})

def delete(request,id):
    req = NewRequest.objects.get(request_id = id)
    req.delete()
    req = NewRequest.objects.raw('select * from NewRequest')
    return redirect('/adminprofile/adminrequest/')

def approve(request,id):
    req = NewRequest.objects.get(request_id=id)
    eid = req.emp_id
    form = approvalform(request.POST)
    if form.is_valid():
        if not items.objects.filter(id = form.cleaned_data['item_no']).exists():
            return redirect('./')
        print("Yes")
        item = items.objects.get(id = form.cleaned_data['item_no'])
        item.Loaned = 1;
        item.In_use = 1;
        item.save()
        if req.qty == 1:
            req.delete()
        else:
            req.qty = req.qty - 1;
            req.save()
        form.save()
        return redirect('/adminprofile/adminrequest/')
    return render(request,'adminrequest/approval.html',{'form':form, 'id':id, 'eid':eid})