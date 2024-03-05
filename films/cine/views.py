from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from cine.models import Cine
from .forms import Cineform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Cine
from django.urls import reverse_lazy


#
# def home(request):
#     k = Cine.objects.all()
#
#     return render(request, 'home.html', {'c': k})

class MovieList(ListView):
    model=Cine
    template_name="home.html"
    context_object_name="c"


# def filmdetail(request,p):
#     c=Cine.objects.get(id=p)
#     return render(request,'edit.html',{'c':c})



class MovieDetail(DetailView):
    model=Cine
    template_name = "edit.html"
    context_object_name = "c"

# def addfilms(request):
#         if (request.method == "POST"):
#             n = request.POST['n']
#             d = request.POST['d']
#             y = request.POST['y']
#             i = request.FILES['i']
#
#             c = Cine.objects.create(name=n, desc=d, year=y, img=i)
#             c.save()
#             return home(request)
#         return render(request, 'addfilms.html')

# class MovieAdd(CreateView):#create view displays a form for adding new objectand handles form
#     model = Cine
#     template_name = "addfilms.html"
#     fileds='__all__'
#     success_url=reverse_lazy('cine:home')

class MovieAdd(CreateView):
    model = Cine
    template_name = "addfilms.html"
    fields = '__all__'  # Corrected attribute name
    success_url = reverse_lazy('cine:home')







# def filmedit(request,p):
#     c = Cine.objects.get(id=p)
#     if (request.method == "POST"):  # After form submission
#         form = Cineform(request.POST,request.FILES,instance=c)  # Creates form object initialized with values inside request.POST
#         if form.is_valid():
#             form.save()  # saves the form object inside Db table
#         return home(request)
#
#     form=Cineform(instance= c)
#     return render (request,'change.html',{'form':form})


class MovieUpdate(UpdateView):
    model = Cine
    template_name = "change.html"
    fields='__all__'
    success_url = reverse_lazy('cine:home')



# def filmdelete(request,p):
#     c=Cine.objects.get(id=p)
#     c.delete()
#     return home(request)


class MovieDelete(DeleteView):
    model = Cine
    success_url = reverse_lazy('cine:home')
    template_name = "delete.html"
