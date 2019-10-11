# Create your views here.
from django.shortcuts import render,redirect
from adminside.models import addproductcat
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView



@login_required
def add_product_cat(request):
    return render(request, 'adminlayout/add_product_cat.html')

@login_required
def createpost(request):
        name=request.POST.get('name')
        category=request.POST.get('category')        
        inst = addproductcat(product_name=name,category=category)
        inst.save()
        return redirect('add_product_cat')

@login_required    
def view_product_cat(request):
        aa=addproductcat.objects.all()
        return render(request,"adminlayout/view_product_cat.html",{'aa':aa})

@login_required          
def del_product_cat(request):
        if request.method == 'GET':
            pk=request.GET.get('pk')   
            addproductcat.objects.filter(id=pk).delete()
            return redirect('view_product_cat')
        else:
            print("Error")      

# @login_required
# class update_cat(UpdateView):
#         model = addproductcat
#         template_name = 'adminlayout/update_cat.html'
#         # form_class = OrgProfileForm
#         pk_url_kwarg = 'pk'
#         #url_name = 'update_cat'
#         fields = ('product_name','category')
#         success_url = 'done/'

@login_required
def update_cat_done(request):
        return render(request,"adminlayout/update_cat_done.html")






