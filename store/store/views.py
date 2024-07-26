from django.shortcuts import render,redirect
from .forms import DocForm
from stores.models import DocModel
def form(request):
    a = DocForm()
    data = {'key':a}
    return render(request,"form.html",data)

def upload_doc(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            doc = DocModel.objects.all()
            return render(request, 'submit.html', {'doc': doc})
    else:
        form = DocForm()

    return redirect('/')
