from django.db import connection
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from functools import wraps
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from .models import CustomUser, Merek, Model, Negara, Jumlah, Harga, ManagementWatch

# Custom decorator for admin check
def admin_required(view_func):
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_admin)(view_func))
    return decorated_view_func

# Check if the user is the owner of the object or an admin
def user_is_owner_or_admin(model):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view_func(request, *args, **kwargs):
            obj = get_object_or_404(model, pk=kwargs['id'])
            # Check if the current user is the creator of the object or an admin
            if obj.created_by == request.user or request.user.is_admin:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "You do not have permission to modify this data.")
                return redirect('getmanagementwatch')
        return _wrapped_view_func
    return decorator

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_admin = request.POST.get('is_admin', 'off') == 'on'
        is_user = not is_admin

        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'register.html')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, is_admin=is_admin, is_user=is_user)
            messages.success(request, 'Account registered successfully.')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'register.html')

    return render(request, 'register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('getmanagementwatch')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'messages': messages.get_messages(request)})

    return render(request, 'login.html')

# View Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Views Merek
@login_required
def getMerek(request):
    merek = Merek.objects.all()
    return render(request, 'merek/index.html', {'list_merek': merek})

@login_required
def addMerek(request):
    return render(request, 'merek/add.html')

@login_required
def addMerekValue(request):
    if request.method == "POST":
        nama_merek_field = request.POST['nama_merek']
        nama_pendiri_field = request.POST['nama_pendiri']
        tahun_berdiri_field = request.POST['tahun_berdiri']
        Merek.objects.create(nama_merek=nama_merek_field, nama_pendiri=nama_pendiri_field, tahun_berdiri=tahun_berdiri_field, created_by=request.user)
        messages.success(request, 'Data Merek has been added successfully.')
        return redirect('getmerek')
    return render(request, 'merek/add.html')


@user_is_owner_or_admin(Merek) 
def deleteMerek(request, id):
    merek = get_object_or_404(Merek, id=id)
    merek.delete()
    messages.error(request, 'Data Merek has been deleted successfully.')
    return redirect('getmerek')

@user_is_owner_or_admin(Merek)
def updateMerek(request, id):
    merek = get_object_or_404(Merek, id=id)
    return render(request, 'merek/update.html', {'merek': merek})

@user_is_owner_or_admin(Merek)
def updateMerekValue(request, id):
    if request.method == "POST":
        merek = Merek.objects.get(id=id)
        merek.nama_merek = request.POST['nama_merek']
        merek.nama_pendiri = request.POST['nama_pendiri']
        merek.tahun_berdiri = request.POST['tahun_berdiri']
        merek.save()
        messages.success(request, 'Data Merek has been updated successfully.')
        return redirect('getmerek')

# Views Model
@login_required
def getModel(request):
    model = Model.objects.all()
    return render(request, 'model_watch/index.html', {'list_model': model})

@login_required
def addModel(request):
    return render(request, 'model_watch/add.html')

@login_required
def addModelValue(request):
    if request.method == "POST":
        nama_model_field = request.POST['nama_model']
        nama_pencipta_field = request.POST['nama_pencipta']
        tahun_peluncuran_field = request.POST['tahun_peluncuran']
        Model.objects.create(nama_model=nama_model_field, nama_pencipta=nama_pencipta_field, tahun_peluncuran=tahun_peluncuran_field, created_by=request.user)
        messages.success(request, 'Data Model has been added successfully.')
        return redirect('getmodel')
    return render(request, 'model_watch/add.html')

@user_is_owner_or_admin(Model)
def deleteModel(request, id):
    model = get_object_or_404(Model, id=id)
    model.delete()
    messages.error(request, 'Data Model has been deleted successfully.')
    return redirect('getmodel')

@user_is_owner_or_admin(Model)
def updateModel(request, id):
    model = get_object_or_404(Model, id=id)
    return render(request, 'model_watch/update.html', {'model': model})

@user_is_owner_or_admin(Model)
def updateModelValue(request, id):
    if request.method == "POST":
        model = Model.objects.get(id=id)
        model.nama_model = request.POST['nama_model']
        model.nama_pencipta = request.POST['nama_pencipta']
        model.tahun_peluncuran = request.POST['tahun_peluncuran']
        model.save()
        messages.success(request, 'Data Model has been updated successfully.')
        return redirect('getmodel')

# Views Negara
@login_required
def getNegara(request):
    negara = Negara.objects.all()
    return render(request, 'negara/index.html', {'list_negara': negara})

@login_required
def addNegara(request):
    return render(request, 'negara/add.html')

@login_required
def addNegaraValue(request):
    if request.method == "POST":
        nama_negara_field = request.POST['nama_negara']
        mata_uang_field = request.POST['mata_uang']
        Negara.objects.create(nama_negara=nama_negara_field, mata_uang=mata_uang_field, created_by=request.user)
        messages.success(request, 'Data Negara has been added successfully.')
        return redirect('getnegara')
    return render(request, 'negara/add.html')

@user_is_owner_or_admin(Negara)
def deleteNegara(request, id):
    negara = get_object_or_404(Negara, id=id)
    negara.delete()
    messages.error(request, 'Data Negara has been deleted successfully.')
    return redirect('getnegara')

@user_is_owner_or_admin(Negara)
def updateNegara(request, id):
    negara = get_object_or_404(Negara, id=id)
    return render(request, 'negara/update.html', {'negara': negara})

@user_is_owner_or_admin(Negara)
def updateNegaraValue(request, id):
    if request.method == "POST":
        negara = Negara.objects.get(id=id)
        negara.nama_negara = request.POST['nama_negara']
        negara.mata_uang = request.POST['mata_uang']
        negara.save()
        messages.success(request, 'Data Negara has been updated successfully.')
        return redirect('getnegara')

# Views Jumlah
@login_required
def getJumlah(request):
    jumlah = Jumlah.objects.all()
    return render(request, 'jumlah/index.html', {'list_jumlah': jumlah})

@login_required
def addJumlah(request):
    return render(request, 'jumlah/add.html')

@login_required
def addJumlahValue(request):
    if request.method == "POST":
        jumlah_jam_field = request.POST['jumlah_jam']
        jumlah_baterai_field = request.POST['jumlah_baterai']
        jumlah_tali_field = request.POST['jumlah_tali']
        Jumlah.objects.create(jumlah_jam=jumlah_jam_field, jumlah_baterai=jumlah_baterai_field, jumlah_tali=jumlah_tali_field, created_by=request.user)
        messages.success(request, 'Data Jumlah has been added successfully.')
        return redirect('getjumlah')
    return render(request, 'jumlah/add.html')

@user_is_owner_or_admin(Jumlah)
def deleteJumlah(request, id):
    jumlah = get_object_or_404(Jumlah, id=id)
    jumlah.delete()
    messages.error(request, 'Data Jumlah has been deleted successfully.')
    return redirect('getjumlah')

@user_is_owner_or_admin(Jumlah)
def updateJumlah(request, id):
    jumlah = get_object_or_404(Jumlah, id=id)
    return render(request, 'jumlah/update.html', {'jumlah': jumlah})

@user_is_owner_or_admin(Jumlah)
def updateJumlahValue(request, id):
    if request.method == "POST":
        jumlah = Jumlah.objects.get(id=id)
        jumlah.jumlah_jam = request.POST['jumlah_jam']
        jumlah.jumlah_baterai = request.POST['jumlah_baterai']
        jumlah.jumlah_tali = request.POST['jumlah_tali']
        jumlah.save()
        messages.success(request, 'Data Jumlah has been updated successfully.')
        return redirect('getjumlah')

# Views Harga
@login_required
def getHarga(request):
    harga = Harga.objects.all()
    return render(request, 'harga/index.html', {'list_harga': harga})

@login_required
def addHarga(request):
    return render(request, 'harga/add.html')

@login_required
def addHargaValue(request):
    if request.method == "POST":
        harga_jam_field = request.POST['harga_jam']
        harga_baterai_field = request.POST['harga_baterai']
        harga_tali_field = request.POST['harga_tali']
        Harga.objects.create(harga_jam=harga_jam_field, harga_baterai=harga_baterai_field, harga_tali=harga_tali_field, created_by=request.user)
        messages.success(request, 'Data Harga has been added successfully.')
        return redirect('getharga')
    return render(request, 'harga/add.html')

@user_is_owner_or_admin(Harga)
def deleteHarga(request, id):
    harga = get_object_or_404(Harga, id=id)
    harga.delete()
    messages.error(request, 'Data Harga has been deleted successfully.')
    return redirect('getharga')

@user_is_owner_or_admin(Harga)
def updateHarga(request, id):
    harga = get_object_or_404(Harga, id=id)
    return render(request, 'harga/update.html', {'harga': harga})

@user_is_owner_or_admin(Harga)
def updateHargaValue(request, id):
    if request.method == "POST":
        harga = Harga.objects.get(id=id)
        harga.harga_jam = request.POST['harga_jam']
        harga.harga_baterai = request.POST['harga_baterai']
        harga.harga_tali = request.POST['harga_tali']
        harga.save()
        messages.success(request, 'Data Harga has been updated successfully.')
        return redirect('getharga')

# Views Management Watch
@login_required
def getManagementWatch(request):
    management_watch = ManagementWatch.objects.all()
    return render(request, 'index.html', {'list_management_watch': management_watch})

@login_required
def addManagementWatch(request):
    merek_list = Merek.objects.all()
    model_list = Model.objects.all()
    negara_list = Negara.objects.all()
    jumlah_list = Jumlah.objects.all()
    harga_list = Harga.objects.all()
    return render(request, 'add.html', {'list_merek': merek_list, 'list_model': model_list, 'list_negara': negara_list, 'list_jumlah': jumlah_list, 'list_harga': harga_list})

@login_required
def addManagementWatchValue(request):
    if request.method == "POST":
        keterangan_field = request.POST['keterangan']
        merek_id = int(request.POST['merek_field'])
        model_id = int(request.POST['model_field'])
        negara_id = int(request.POST['negara_field'])
        jumlah_id = int(request.POST['jumlah_field'])
        harga_id = int(request.POST['harga_field'])

        ManagementWatch.objects.create(
            keterangan=keterangan_field, 
            merek_id=merek_id, 
            model_id=model_id, 
            negara_id=negara_id, 
            jumlah_id=jumlah_id, 
            harga_id=harga_id,
            created_by=request.user,
        )
        messages.success(request, 'Data Management Watch has been added successfully.')
        return redirect('getmanagementwatch')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('getmanagementwatch')

@user_is_owner_or_admin(ManagementWatch)
def deleteManagementWatch(request, id):
    management_watch = get_object_or_404(ManagementWatch, id=id)
    management_watch.delete()
    messages.error(request, 'Data Management Watch has been deleted successfully.')
    return redirect('getmanagementwatch')

@user_is_owner_or_admin(ManagementWatch)
def updateManagementWatch(request, id):
    management_watch = get_object_or_404(ManagementWatch, id=id)
    merek_list = Merek.objects.all()
    model_list = Model.objects.all()
    negara_list = Negara.objects.all()
    jumlah_list = Jumlah.objects.all()
    harga_list = Harga.objects.all()
    return render(request, 'update.html', {
        'management_watch': management_watch,
        'list_merek': merek_list,
        'list_model': model_list,
        'list_negara': negara_list,
        'list_jumlah': jumlah_list,
        'list_harga': harga_list,
    })

@user_is_owner_or_admin(ManagementWatch)
def updateManagementWatchValue(request, id):
    if request.method == "POST":
        management_watch = ManagementWatch.objects.get(id=id)
        management_watch.keterangan = request.POST['keterangan']
        management_watch.merek_id = request.POST['merek_field']
        management_watch.model_id = request.POST['model_field']
        management_watch.negara_id = request.POST['negara_field']
        management_watch.jumlah_id = request.POST['jumlah_field']
        management_watch.harga_id = request.POST['harga_field']
        management_watch.save()
        messages.success(request, 'Data Management Watch has been updated successfully.')
        return redirect('getmanagementwatch')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('getmanagementwatch')

# Utility function
def reset_sequence(request, table_name):
    with connection.cursor() as cursor:
        cursor.execute(f"UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='{table_name}'")
    messages.success(request, f'Sequence for {table_name} reset successfully.')
    return redirect('getmanagementwatch')