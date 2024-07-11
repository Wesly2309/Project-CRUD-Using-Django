from django.urls import path
from . import views

urlpatterns = [
    path('', views.getManagementWatch, name='getmanagementwatch'),

    # Views Merek
    path('merek/', views.getMerek, name='getmerek'),
    path('merek/addmerek', views.addMerek, name='addmerek'),
    path('merek/storemerek', views.addMerekValue, name='storemerek'),
    path('merek/editmerek/<int:id>', views.updateMerek, name='editmerek'),
    path('merek/updatemerek/<int:id>', views.updateMerekValue, name='updatemerek'),
    path('merek/deletemerek/<int:id>', views.deleteMerek, name='deletemerek'),

    # Views Model
    path('model_watch/', views.getModel, name='getmodel'),
    path('model_watch/addmodel', views.addModel, name='addmodel'),
    path('model_watch/storemodel', views.addModelValue, name='storemodel'),
    path('model_watch/editmodel/<int:id>', views.updateModel, name='editmodel'),
    path('model_watch/updatemodel/<int:id>', views.updateModelValue, name='updatemodel'),
    path('model_watch/deletemodel/<int:id>', views.deleteModel, name='deletemodel'),

    # Views Negara
    path('negara/', views.getNegara, name='getnegara'),
    path('negara/addnegara', views.addNegara, name='addnegara'),
    path('negara/storenegara', views.addNegaraValue, name='storenegara'),
    path('negara/editnegara/<int:id>', views.updateNegara, name='editnegara'),
    path('negara/updatenegara/<int:id>', views.updateNegaraValue, name='updatenegara'),
    path('negara/deletenegara/<int:id>', views.deleteNegara, name='deletenegara'),

    # Views Jumlah
    path('jumlah/' , views.getJumlah , name='getjumlah'),
    path('jumlah/addjumlah' , views.addJumlah , name='addjumlah'),
    path('jumlah/storejumlah' , views.addJumlahValue , name='storejumlah'),
    path('jumlah/editjumlah/<int:id>' , views.updateJumlah , name='editjumlah'),
    path('jumlah/updatejumlah/<int:id>' , views.updateJumlahValue , name='updatejumlah'),
    path('jumlah/deletejumlah/<int:id>' , views.deleteJumlah , name='deletejumlah'),

    # Views Harga
    path('harga/', views.getHarga, name='getharga'),
    path('harga/addharga', views.addHarga, name='addharga'),
    path('harga/storeharga', views.addHargaValue, name='storeharga'),
    path('harga/editharga/<int:id>', views.updateHarga, name='editharga'),
    path('harga/updateharga/<int:id>', views.updateHargaValue, name='updateharga'),
    path('harga/deleteharga/<int:id>', views.deleteHarga, name='deleteharga'),

    # Views ManagementWatch
    path('managementwatch/', views.getManagementWatch, name='getmanagementwatch'),
    path('managementwatch/addmanagementwatch', views.addManagementWatch, name='addmanagementwatch'),
    path('managementwatch/storemanagementwatch', views.addManagementWatchValue, name='storemanagementwatch'),
    path('managementwatch/editmanagementwatch/<int:id>', views.updateManagementWatch, name='editmanagementwatch'),
    path('managementwatch/updatemanagementwatch/<int:id>', views.updateManagementWatchValue,name='updatemanagementwatch'),
    path('managementwatch/deletemanagementwatch/<int:id>', views.deleteManagementWatch, name='deletemanagementwatch'),

    # Logout path
    path('logout/', views.logout_view, name='logout'),

    # Register and login paths
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),

]

