from django.forms import ModelForm

from water_managment_app.models import AreaTable, LoginTable, NotificationTable, ReaderTable, SubAdminTable


class AddSubAdminForm(ModelForm):
    class Meta:
        model = SubAdminTable
        fields = ['Name', 'Age', 'Gender', 'Email', 'Phone', 'Actions']

class ViewAreaForm(ModelForm):
    class Meta:
        model = AreaTable
        fields = ['Areas', 'Description']


class AddAreaForm(ModelForm):
    class Meta:
        model = AreaTable 
        fields = ['Areas', 'Description']


class EditAreaForm(ModelForm):
    class Meta:
        model = AreaTable
        fields = ['Areas', 'Description']     

class EditSubAdminForm(ModelForm):
    class Meta:
        model = SubAdminTable
        fields = ['Name', 'Age', 'Gender', 'Email', 'Phone', 'Actions']

class AddmeterreaderForm(ModelForm):
    class Meta:
        model = ReaderTable
        fields = ['Name', 'Age', 'Gender', 'Email', 'Phone']

class EditmeterreaderForm(ModelForm):
    class Meta:
        model = ReaderTable
        fields = ['Name', 'Age', 'Gender', 'Email', 'Phone']
        
class DelMeterReaderForm(ModelForm):
    class Meta:
        model = ReaderTable
        fields = ['Name', 'Age', 'Gender', 'Email', 'Phone']
class ChangePasswordForm(ModelForm):
    class Meta:
        model= LoginTable
        fields=['Password']
class NotificationForm(ModelForm):
    class Meta:
        model = NotificationTable
        fields = ['Notification', 'Date']

    