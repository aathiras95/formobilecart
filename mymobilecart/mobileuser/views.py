from django.shortcuts import render,redirect
from django.http import HttpResponse
from django .views.generic import View
from mobileuser.forms import LoginForm
from mobileuser.models import Users
from django .contrib import messages
from mobileuser.forms import ProductDetailsAddForm
from mobileuser.models import MobileProducts
from mobileuser.forms import UserRegistrationForm
from django .contrib.auth import authenticate,login,logout


# Create your views here.
class IndexView(View):
    def get(self,request):
        # form=LoginForm()
        return render(request,'index1.html')
# class LoginView(View):
#     form_class = LoginForm
#     template_name='login.html'
#     def get(self,request,*args,**kwargs):
#         form=self.form_class()
#         return render(request,self.template_name,{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             Users.objects.create(
#                 username=form.cleaned_data.get('username'),
#                 password=form.cleaned_data.get('password')
#                         )
#             messages.success(request,'user added')
#             return  redirect('mob-user')
#         else:
#             messages.error(request,'Cannot add user ')
#             return render(request,'login.html',{'form':form})

class ProductAddView(View):

    def get(self,request,*args,**kwargs):
        form = ProductDetailsAddForm()
        return render(request,'padd.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=ProductDetailsAddForm(request.POST,files=request.FILES)
        if form.is_valid():
            # MobileProductss.objects.create(
            #     pro_code=form.cleaned_data.get('ProductCode'),
            #     pro_name=form.cleaned_data.get('ProductName'),
            #     pro_ram=form.cleaned_data.get('ProductRam'),
            #     pro_dis=form.cleaned_data.get('ProductDisplay'),
            #     pro_camera=form.cleaned_data.get('ProductCamera'),
            #     pro_battery=form.cleaned_data.get('ProductBattery'),
            #     pro_price=form.cleaned_data.get('ProductPrice'),
            #     pro_offprice=form.cleaned_data.get('ProductOfferPrice'),
            #     pro_processor=form.cleaned_data.get('ProductProcessor'),
            #     pro_warrenty=form.cleaned_data.get('ProductWarrenty'),
            #     pro_specification=form.cleaned_data.get('ProductSpecification'),
            #
            # )
            form.save()
            messages.success(request,'Product added')
            return redirect('pro-list')
        else:
            messages.error(request,'Some error occured')
            return render(request,'padd.html',{'form':form})


class ProductListView(View):
    def get(self,request,*arg,**kwargs):
        product=MobileProducts.objects.all()
        return render(request,'plist.html',{'products':product})

class SingleProductView(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('p_id')
        data=MobileProducts.objects.get(pro_code=pid)
        return render(request,'psingle.html',{'singleproduct':data})

class ProductEditView(View):
    def get(self,request,*args,**kwargs):
        pid = kwargs.get('p_id')
        data = MobileProducts.objects.get(pro_code=pid)
        form=ProductDetailsAddForm(instance=data)
        return render(request,'pedit.html',{'editproduct':form})
    def post(self,request,*args,**kwargs):
        pid=kwargs.get('p_id')
        data=MobileProducts.objects.get(pro_code=pid)
        form=ProductDetailsAddForm(request.POST,instance=data,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Edited sucessfully')
            return redirect('pro-list')
        else:
            messages.error(request, 'Profile Editing failed Failed')
            return render(request, 'pedit.html', {'editproduct': form})

def remove(request,*args,**kwargs):
    pid=kwargs.get('p_id')
    data=MobileProducts.objects.get(pro_code=pid)
    data.delete()
    messages.success(request,'employeedeleted')
    return redirect('pro-list')


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Success')
            return redirect('mob-user')
        else:
            messages.error(request,'Registration Failed')
            return render(request,'signup.html',{'form':form})

class LoginView(View):
    # form_class = LoginForm
    template_name='logging.html'
    def get(self,request,*args,**kwargs):
        # form=self.form_class()
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            # return render(request, 'index1.html')
            return redirect('pro-list')
        else:
            return render(request,'logging.html')



def SignOut(request,*args,**kwargs):
    logout(request)
    return redirect('login')



