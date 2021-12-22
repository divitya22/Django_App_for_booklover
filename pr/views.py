from django.shortcuts import render,redirect
from .models import Trytab
from .forms import TrytabForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator

def book_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment,filename=book.csv'
    # Create csv writer
    writer=csv.writer(response)
    #Designate the model
    book=Trytab.objects.all()
    #Add column heading to csv
    writer.writerow(['book_name','Type_book'])
    for bks in book:
        writer.writerow([bks.book_name,bks.Type_book])
    return response





def delete_book(request,book_id):
    bk=Trytab.objects.get(pk=book_id)
    bk.delete()
    return redirect('book-list')




# generate text file

def book_text(request):
    response=HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment;filename=book.text'
    bkd=Trytab.objects.all()
    lines=[]
    for b in bkd:
        lines.append(f'{b.book_name}--{b.Type_book}\n')
    response.writelines(lines)
    return response


def show_book(request,book_id):
    book=Trytab.objects.get(pk=book_id)
    return render(request,"event/show_book.html",{"book":book})




def book_list(request):
    book_list = Trytab.objects.all()
    return render(request, 'event/book.html',
                  {'book_list': book_list})



def search_book(request):
    if request.method=="POST":
        searched=request.POST['searched']
        srch=Trytab.objects.filter(book_name__contains=searched)
        return render(request,"event/search_book.html",{"searched":searched,"srch":srch})
    else:
        return render(request,"event/search_book.html",{})


def add_data(request):
    submitted = False
    if request.method=="POST":
        form=TrytabForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_data?submitted=True')
    else:
        form = TrytabForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,"event/Trytabnw.html",{"form":form,"submitted":submitted})


def home(request):
    name="Divitya"
    return render(request,"event/home.html",{"name":name})

def home2(request):
    return render(request,"event/home2.html")


def detail(request):
    return render(request,"event/detail.html")




def to_web(request):
    bk_list=Trytab.objects.all()
    return render(request,"event/detail2.html",{"bk_list":bk_list})


