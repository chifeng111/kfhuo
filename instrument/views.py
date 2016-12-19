from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Instruments, Order
from .forms import Logi_form, Register_form, Add_form
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    instruments = Instruments.objects.all()
    content = {
        'instruments': instruments,
    }
    return render(request, 'list.html', content)

def logi(request):
    form = Logi_form()
    if request.method == 'GET':
        return render(request, 'logi.html', {'form': form})
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = authenticate(username=username, password=password)
        if u and u.is_active:
            login(request, u)
            return redirect('index')
        else:
            messages.error(request,'用户名或密码输入错误哦！')
            return render(request, 'logi.html', {'form': form})

def logo(request):
    if request.user.is_active:
        logout(request)
        return redirect('index')

def register(request):
    form = Register_form(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user.username = username
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('index')

    content = {
        'form': form
    }
    return render(request, 'register.html', content)

def order(request, instrument_id):
    instrument = get_object_or_404(Instruments, id=instrument_id)
    d = datetime.date.today()
    order = Order.objects.filter(instrument=instrument, time__gte=d).order_by('time')
    content = {
        'order': order,
        'instrument': instrument
    }
    return render(request, 'order.html', content)

def add(request, instrument_id):
    if not request.user.is_active:
        messages.error(request, '请先登录')
        return redirect('instrument:logi')
    form = Add_form(request.POST)
    if form.is_valid():
        order_ = form.save(commit=False)
        order_.instrument = Instruments.objects.get(id=instrument_id)
        order_.user = request.user
        order_list = Order.objects.filter(instrument=instrument_id)
        time_list = []
        for o in order_list:
            time_list.append(o.time)
        if order_.time not in time_list:
            if date_is_valid(order_.time):
                order_.save()
                messages.success(request, '预约成功')
                return redirect('/instrument/%s' %instrument_id)
            else:
                messages.error(request, '超出预约范围')
                return redirect('/instrument/%s' % instrument_id)
        else:
            messages.error(request, '该时间已被预约')
            return redirect('/instrument/%s' % instrument_id)
    return render(request, 'add.html', {'form': form})

def delete(request, instrument_id, order_id):
    order = get_object_or_404(Order,id=order_id)
    if order.user != request.user:
        raise Http404
    order.delete()
    messages.success(request, '删除成功！')
    return redirect('/instrument/%s' % instrument_id)


#设置预约范围，判断是否合法
def date_is_valid(date):
    d1 = datetime.date.today()
    d2 = d1 + datetime.timedelta(days=15)
    if date >= d1 and date < d2:
        return True
    else:
        return False