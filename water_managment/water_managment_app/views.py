from django.shortcuts import render
from django.views import View
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect


from water_managment_app.form import *
from water_managment_app.models import *


# Create your views here.

class Login_page(View):
    def get (self,request):
        return render(request,"Administration/login.html")
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = LoginTable.objects.get(Username=username, Password=password)
        if login_obj.Type == 'admin':
            request.session['login_id']=login_obj.id
            return HttpResponse('''<script>alert("welcome to admin home"); window.location="/admin_home"</script>''')
        elif login_obj.Type == 'subadmin':
            request.session['login_id']=login_obj.id
            return HttpResponse('''<script>alert("welcome to subadmin home"); window.location="/SubAdminHome"</script>''')
# ////////////////////////////////// ADMIN ///////////////////////////////////

class AdminHome(View):
    def get(self, request):
        return render(request, "Administration/admin_home.html")


class ComplaintPage(View):
    def get(self, request):
        comp_obj = ComplaintTable.objects.all()
        return render(request, "Administration/complaint.html", {'val': comp_obj})
    

class ManageSubAdminPage(View):
    def get(self, request):
         mansub_obj = SubAdminTable.objects.all()
         return render(request, "Administration/manage_sub_admin.html",{'val': mansub_obj})

class Addsubadmin(View):
    def get(self, request):
        return render(request,"Administration/add_subadmin.html")
    def post(self, request):
        form = AddSubAdminForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            c= LoginTable.objects.create(Username=request.POST['username'],Password=request.POST['password'],Type='subadmin')
            c.save()
            obj.LOGIN=c
            obj.save()
            return HttpResponse('''<script>alert("sub admin added successfully"); window.location="/manage_sub_admin"</script>''')


class DelSubAdmin(View): 
     def get(self, request, id):
        obj = LoginTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("sub admin deleted successfully"); window.location="/manage_sub_admin"</script>''')
        

class ConnectionPage(View):
    def get(self, request):
        conn_obj = ConnectionTable.objects.all()
        return render(request, "subadmin/approve_connection.html", {'val': conn_obj})


class Addarea(View):
    def get(self, request):
        return render(request, "Administration/add_area.html")
    def post(self, request):
        form = AddAreaForm(request.POST)
        if form.is_valid():
            obj=form.save()
        return HttpResponse('''<script>alert("area added successfully"); window.location="/connection_page"</script>''')
    
class EditSubAdmin(View):
    def get(self, request,id):
        obj = SubAdminTable.objects.get(id=id)
        print("$$$$$$$$$$", obj)
        return render(request,"Administration/edit_subadmin.html", {'obj':obj})
    def post(self, request, id):
        obj = SubAdminTable.objects.get(id=id)
        form = AddSubAdminForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("sub admin edited successfully"); window.location="/manage_sub_admin"</script>''')
        

# ////////////////////////////// SUBADMIN ///////////////////////////////////
   
class ApproveConnection(View):
    def get(self,request, id):
        obj = ConnectionTable.objects.get(id=id)
        obj.status='approved'
        obj.save()
        return redirect('connection')
    
class RejectConnection(View):
    def get(self,request,id):
        obj = ConnectionTable.objects.get(id=id)
        print("%%%%%%%%%%%%%%%%%%%%%%%")
        obj.status='rejected'
        obj.save()
        return redirect('connection')
    
class SubAdminHome(View):
    def get(self, request):
        return render(request, "subadmin\subadmin_home.html")
    
class Subadminprofile(View):
    def get(self, request):
        id=request.session['login_id']
        obj=SubAdminTable.objects.get(LOGIN=id)
        print(obj)
        return render(request, "subadmin\subadminprofile.html",{'val':obj})
    
class Addmeterreader(View):
    def get(self,request):
        obj=AreaTable.objects.all()
        return render(request,"subadmin/meter_reader.html",{'val':obj})
    def post(self,request):
     form = AddmeterreaderForm(request.POST)
     if form.is_valid():
        c=form.save(commit=False)
        d=LoginTable.objects.create(Username=request.POST['username'],Password=request.POST['password'],Type='pending')
        c.LOGIN=d
        area_id = request.POST.get('area')  # Assuming the area field is named 'area' in the form
        if area_id:
            area = AreaTable.objects.get(id=area_id)  # Get the Area object by the id
            c.Area = area 
            c.save()
        return HttpResponse('''<script>alert("Meter reader added successfully"); window.location="/manage_sub_admin"</script>''')
        
class EditMeterReader(View):
     def get(self, request,id):
        obj = ReaderTable.objects.get(id=id)
        print("$$$$$$$$$$", obj)
        return render(request,"subadmin/meter_reader.html", {'val':obj})
     def post(self, request, id):
        obj = ReaderTable.objects.get(id=id)
        form = AddmeterreaderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("meter reader edited successfully"); window.location="/meter_reader"</script>''')

class DelMeterReader(View): 
     def get(self, request, id):
        obj = ReaderTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("meter reader deleted successfully"); window.location="/meter_reader"</script>''')        

class ViewArea(View):
   def get(self, request):
        obj=AreaTable.objects.all()
        return render(request, "subadmin/view_area.html",{'obj':obj})
class ViewPayment(View):
   def get(self, request):
        obj=PaymentTable.objects.all()
        return render(request, "subadmin/view_payment.html",{'obj':obj})

class AddArea(View):
   def get(self, request):
        return render(request, "subadmin/add_area.html")
   def post(self, request):
        form = AddAreaForm(request.POST)
        if form.is_valid():
            obj=form.save()
        return HttpResponse('''<script>alert("area added successfully"); window.location="/manage_area"</script>''')
  
   
class EditArea(View):
   def get(self, request,id):
        obj=AreaTable.objects.filter(id=id).first()
        print(obj)
        return render(request, "subadmin/edit_area.html",{'obj':obj})
   def post(self, request,id):
        obj=AreaTable.objects.filter(id=id).first()
        form = EditAreaForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save()
        return HttpResponse('''<script>alert("area edited successfully"); window.location="/ViewArea"</script>''')
   
class DelArea(View):
    def get(self, request,id):
        obj=AreaTable.objects.filter(id=id).first()
        obj.delete()
       
        return HttpResponse('''<script>alert("area deleted successfully"); window.location="/ViewArea"</script>''')
class Changepassword(View):
    def get(self,request,id):
        obj=LoginTable.objects.filter(id=id).first()
        return render(request,"subadmin/changepassword.html",{'obj':obj})
    def post(self,request,id):
        obj=LoginTable.objects.filter(id=id).first()
        form=ChangePasswordForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("password changed successfully"); window.location="/ViewSubAdmin"</script>''')

class ViewProfile(View):
    def get(self,request,id):
        obj=ReaderTable.objects.filter(id=id).first()
        return render(request,"subadmin/view_profile.html",{'obj':obj})

class ConnectionPagemeterreader(View):
    def get(self, request):
        conn_obj = ConnectionTable.objects.all()
        return render(request, "meterreader/view_consumer.html", {'val': conn_obj})
class Meterreaderviewnotification(View):
    def get(self,request):
        obj=NotificationTable.objects.all()
        return render(request,"meterreader/")
class NotificationCreateView(View):
    def get(self, request):
        return render(request, 'Administration/notification_create.html', {'form': NotificationForm()})

    def post(self, request):
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification_list')  # Redirect to the list view after successful create
        return render(request, 'Administration/notification_create.html', {'form': form})
class NotificationListView(View):
    def get(self, request):
        notifications = NotificationTable.objects.all()
        return render(request, 'Administration/notification_list.html', {'notifications': notifications})
from django.shortcuts import get_object_or_404

class NotificationUpdateView(View):
    def get(self, request, pk):
        notification = get_object_or_404(NotificationTable, pk=pk)
        return render(request, 'Administration/notification_update.html', {'notification': notification})

    def post(self, request, pk):
        notification = get_object_or_404(NotificationTable, pk=pk)
        notification.Notification = request.POST.get('Notification')
        notification.Date = request.POST.get('Date')
        notification.save()
        return redirect('notification_list')  # Redirect to list view after update
from django.http import HttpResponseRedirect
from django.urls import reverse

class NotificationDeleteView(View):
    def get(self, request, pk):
        notification = get_object_or_404(NotificationTable, pk=pk)
        notification.delete()
        return HttpResponseRedirect(reverse('notification_list'))  # Redirect to list view after delete
