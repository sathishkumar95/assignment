from django.shortcuts import render
import os
import pandas as pd


def index(request):
    my_dir = "/media/mrrobot/ACADEMIC/pycharm Projects/assignment/assignment/myfiles"
    lst = reader(my_dir)
    fields = ['no','name','last name','pay','size','age','some','idk','Storage & Organization','someother']
    context = {
        'file_lst': lst,
        'fields':fields,
            }
    return render(request,'myfiles/index.html',context)


def reader(my_dir):
    lst = []
    for file in os.listdir(my_dir):
        if file.endswith(".csv"):
            lst.append(file)

    return lst


def read_csv(file,field):
    df = pd.read_csv(file)
    var = df[field]
    mydata = []
    for i in var:
        mydata.append(i)
    return mydata


def data(request):
    file_id = request.POST.get('test')
    field_id = request.POST.get('field')
    if not file_id or not field_id:
        return render(request,'myfiles/filenotfount.html')
    else :
        return render(request,'myfiles/filefound.html',{'field_id':field_id,'file_id':file_id})
    my_data = read_csv(file_id,field_id)
    my_dir = "/media/mrrobot/ACADEMIC/pycharm Projects/assignment/assignment/myfiles"
    lst = reader(my_dir)
    fields = ['no', 'name', 'last name', 'pay', 'size', 'age', 'some', 'idk', 'Storage & Organization', 'someother']
    context = {
        'file_lst': lst,
        'fields': fields,
        'data': my_data,
        'favourite':'yes',
    }
    return render(request, 'myfiles/index.html', context)