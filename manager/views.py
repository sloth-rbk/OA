from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import redirect

# 访问限制模块 @login_required
from django.contrib.auth.decorators import login_required, permission_required


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_index(request):
    '''项目经理申请单计算'''
    xmjl_staff_id = request.user.staff_id
    xmsqds = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.all().count()
    xmsqds0 = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.filter(zhuangtai='0').count()
    xmsqds1 = User.objects.get(staff_id=xmjl_staff_id).xmsqd_set.filter(zhuangtai='1').count()
    return render(request, 'xmjl_index.html', {'data': xmsqds, 'data0': xmsqds0, 'data1': xmsqds1})


from .models import Xmsqd
from account.models import User


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_xqadd(request):
    '''需求增加模块'''
    if request.method == 'POST':
        xmname = request.POST['xmname']
        xqid = request.POST['xqid']
        xmdiqu = request.POST['xmdiqu']
        xqry = request.POST['xqry']
        ryjn = request.POST.getlist('ryjn')
        ryjn = (",".join(str(i) for i in ryjn))
        bzxx = request.POST['bzxx']
        kstime = request.POST['kstime']
        jstime = request.POST['jstime']
        xmsqd = Xmsqd()
        # print(xmname,xmdiqu,xqry,ryjn,bzxx,kstime,jstime)
        userid = request.session.get('_auth_user_id')
        '''获取项目组用户名称及工号'''
        xmsqd.xmname = xmname
        xmsqd.xqid = xqid
        xmsqd.xmdiqu = xmdiqu
        xmsqd.xqry = xqry
        xmsqd.ryjn = ryjn
        xmsqd.bzxx = bzxx
        xmsqd.kstime = kstime
        xmsqd.jstime = jstime
        xmsqd.xmjl_id = userid
        xmsqd.save()
        return redirect('项目经理需求增加模块')
    else:
        return render(request, 'xmjl_staff_demands_add.html')


@permission_required('manager.add_xmsqd', login_url='login', raise_exception=True)
def manager_xqhistory(request):
    xmjl_staff_id = request.user.staff_id
    Xmsqds = Xmsqd.objects.filter(xmjl_staff_id=xmjl_staff_id)
    context = {}
    context['Xmsqds'] = Xmsqds
    for i in context:
        print(i)
    return render(request, 'xmjl_staff_demands_history.html', context)
