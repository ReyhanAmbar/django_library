from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.template.loader import get_template
from django.template import Context
from .models import Library, RequestedBook, Contact, Student
from django.contrib import admin
from .forms import StudentLoginForm, LibraryForm, AdminLoginForm, LibraryFormExtra, LibraryAddBookForm, ContactForm, \
    ChoiceFilterForm, StudentRegisterForm, StudentSearchForm
from django.db.models import Q
from datetime import date, datetime



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Setup
if not firebase_admin._apps:cred = credentials.Certificate("serviceAccountKey.json")
default_app =firebase_admin.initialize_app(cred)
db = firestore.client()




# Templates


def index(request):
    print(request.GET)
    gelen_deger = request.GET.get('id', None)
    print(gelen_deger)
    home = Library.objects.all()
    if gelen_deger:
        home = home.filter(id=gelen_deger)
    context = {'home': home}
    return render(request, 'homepage.html', context)


def library(request):
    return render(request, 'library.html')


def login_page(request):
    return render(request, 'login_page.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def news(request):
    return render(request, 'news.html')


def book(request):
    books = Library.objects.all()
    form = ChoiceFilterForm(data=request.GET or None)
    if form.is_valid():
        filter_choice = form.cleaned_data['filter_choice']
        books = books.filter(category=filter_choice)
        if filter_choice == 'null':
            books = Library.objects.all()
    context = {'books': books, 'form': form}
    return render(request, 'book.html', context)


def get_book(request):
    form = ChoiceFilterForm()
    query = request.GET.get('search')
    books = Library.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query) |
        Q(year__icontains=query)
    )
    context = {'books': books, 'form': form}
    return render(request, 'book.html', context)


def get_book_admin(request):
    form = ChoiceFilterForm()
    query = request.GET.get('search')
    books = Library.objects.filter(
        Q(title__icontains=query) |
        Q(author__icontains=query) |
        Q(year__icontains=query)
    )
    context = {'books': books, 'form': form}
    return render(request, 'adminbook.html', context)


def get_student(request):
    form = StudentSearchForm()
    query = request.GET.get('search')
    student_list = Student.objects.filter(
        Q(student_name__icontains=query) |
        Q(student_surname__icontains=query) |
        Q(student_no__icontains=query) |
        Q(student_tc__icontains=query)
    )
    context = {'student_list': student_list, 'form': form}
    return render(request, 'student_list.html', context)


def adminbook(request):
    books = Library.objects.all()
    form = ChoiceFilterForm(data=request.GET or None)
    if form.is_valid():
        filter_choice = form.cleaned_data['filter_choice']
        books = books.filter(category=filter_choice)
        if filter_choice == 'null':
            books = Library.objects.all()
    context = {'books': books, 'form': form}
    return render(request, 'adminbook.html', context)


def student_login(request):
    return render(request, 'student_login.html')


messages = []


def StudentLogin(request):
    form = StudentLoginForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        data = {'username': username, 'password': password}
        messages.append(data)
        return render(request, 'studentlogin.html', context={'form': form})
    return render(request, 'studentlogin.html', context={'form': form})


def student_register(request):
    form = StudentRegisterForm()
    if request.method == "POST":
        form = StudentRegisterForm(data=request.POST)
        if form.is_valid():
            student_name = form.cleaned_data.get('student_name')
            student_surname = form.cleaned_data.get('student_surname')
            student_no = form.cleaned_data.get('student_no')
            student_contact = form.cleaned_data.get('student_contact')
            student_email = form.cleaned_data.get('student_email')
            student_tc = form.cleaned_data.get('student_tc')
            student_gender = form.cleaned_data.get('student_gender')
            student_branch = form.cleaned_data.get('student_branch')
            student_password = form.cleaned_data.get('student_password')
            data = {'student_name': student_name, 'student_surname': student_surname, 'student_no': student_no,
                    'student_contact': student_contact, 'student_email': student_email, 'student_tc': student_tc,
                    'student_gender': student_gender, 'student_branch0': student_branch,
                    'student_password': student_password}
            messages.append(data)
            form.save()
            db.collection('Student List').document(student_no).set(data)
            return render(request, 'student_registered.html')
    return render(request, 'student_register.html', context={'form': form})


def student_registered(request):
    return render(request, 'student_registered.html')


def student_list(request):
    student_list = Student.objects.all()
    form = StudentSearchForm()
    context = {'student_list': student_list, 'form': form}
    return render(request, 'student_list.html', context=context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', context={'student': student})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentRegisterForm(instance=student, data=request.POST or None)
    context = {'form': form, 'student': student}
    if form.is_valid():
        student_name = form.cleaned_data.get('student_name')
        student_surname = form.cleaned_data.get('student_surname')
        student_no = form.cleaned_data.get('student_no')
        student_contact = form.cleaned_data['student_contact']
        student_tc = form.cleaned_data['student_tc']
        student_email = form.cleaned_data['student_email']
        student_gender = form.cleaned_data['student_gender']
        student_branch = form.cleaned_data['student_branch']
        student_password = form.cleaned_data['student_password']
        data = {'student_name': student_name, 'student_surname': student_surname, 'student_no': student_no,
                'student_contact': student_contact, 'student_tc': student_tc, 'student_email': student_email,
                'student_gender': student_gender, 'student_branch': student_branch,
                'student_password': student_password}
        db.collection('Student List').document(student_no).update(data)
        messages.append(data)
        form.save()
        return render(request, 'student_updated.html')
    return render(request, 'student_update.html', context=context)


def student_updated(request):
    return render(request, 'student_updated.html')


def student_deletion(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return HttpResponseRedirect(reverse(student_list))


def adminlogin(request):
    form = AdminLoginForm()
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            data = {'username': username, 'password': password}
            messages.append(data)
            if username == 'operator' and password == 'operator':
                return render(request, 'adminpage.html', context={'messages': messages, 'form': form})
            else:
                return render(request, 'adminlogin.html', context={'form': form})
    return render(request, 'adminlogin.html', context={'form': form})


def adminpage(request):
    return render(request, 'adminpage.html')


def studentpage(request):
    return render(request, 'studentpage.html')


def add_book(request):
    form = LibraryAddBookForm()
    if request.method == "POST":
        form = LibraryAddBookForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            year = form.cleaned_data.get('year')
            category = form.cleaned_data['category']
            data = {'title': title, 'author': author, 'year': year, 'category': category}
            db.collection('Library').document(title).set(data)
            messages.append(data)
            form.save()
            return render(request, 'book_added.html')
    return render(request, 'add_book.html', context={'form': form})


def book_added(request):
    return render(request, 'book_added.html')


def book_detail(request, pk):
    book = get_object_or_404(Library, pk=pk)
    return render(request, 'book_detail.html', context={'book': book})


def admin_book_detail(request, pk):
    book = get_object_or_404(Library, pk=pk)
    return render(request, 'admin_book_detail.html', context={'book': book})


def request_book(request):
    form = LibraryForm()
    if request.method == "POST":
        form = LibraryForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            year = form.cleaned_data.get('year')
            data = {'title': title, 'author': author, 'year': year}
            db.collection('Requested Book').document(title).set(data)
            messages.append(data)
            form.save()
            return render(request, 'requested_book.html')
    return render(request, 'request_book.html', context={'form': form})


def requested_book(request):
    return render(request, 'requested_book.html')


def view_requested_book(request):
    req_book = RequestedBook.objects.all()
    context = {'req_book': req_book}
    return render(request, 'view_requested_book.html', context=context)


def book_update(request, pk):
    book = get_object_or_404(Library, pk=pk)
    form = LibraryFormExtra(instance=book, data=request.POST or None)
    context = {'form': form, 'book': book}
    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        year = form.cleaned_data.get('year')
        category = form.cleaned_data['category']
        data = {'title': title, 'author': author, 'year': year, 'category': category}
        db.collection('Library').document(title).update(data)
        messages.append(data)
        form.save()

        return render(request, 'book_updated.html')
    return render(request, 'book_update.html', context=context)


def book_updated(request):
    return render(request, 'book_updated.html')


def book_delete(request, pk):
    book = get_object_or_404(Library, pk=pk)
    return render(request, 'book_delete.html', context={'book': book})


def book_deletion(request, pk):
    book = get_object_or_404(Library, pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse(adminbook))


def req_book_deletion(request, pk):
    req_book = get_object_or_404(RequestedBook, pk=pk)
    req_book.delete()
    return HttpResponseRedirect(reverse(view_requested_book))


def view_issued_book(request):
    student = Library.objects.all().filter(availability='Uygun değil')
    context = {'student': student}
    return render(request, 'view_issued_book.html', context=context)


def contact_operator(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            reason = form.cleaned_data.get('reason')
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            std_name = form.cleaned_data.get('student_name')
            std_surname = form.cleaned_data.get('student_surname')
            contact = form.cleaned_data.get('contact')
            data = {'reason': reason, 'title': title, 'content': content, 'std_name': std_name,
                    'std_surname': std_surname, 'contact': contact}
            db.collection('Messages From Student').document(reason).set(data)
            messages.append(data)
            form.save()
            return render(request, 'contacted.html')
    return render(request, 'contact_operator.html', context={'form': form})


def contacted(request):
    return render(request, 'contacted.html')


def view_received_message(request):
    view_mes = Contact.objects.all()
    context = {'view_mes': view_mes}
    return render(request, 'view_received_message.html', context=context)


def message_delete(request, pk):
    view_mes = get_object_or_404(Contact, pk=pk)
    view_mes.delete()
    return HttpResponseRedirect(reverse(view_received_message))


def message_detail(request, pk):
    mes_det = get_object_or_404(Contact, pk=pk)
    return render(request, 'message_detail.html', context={'mes_det': mes_det})
