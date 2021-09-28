from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from library import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('book/', include('library.urls')),
                  path('', views.index, name='index'),
                  path('login_page/', views.login_page, name='login_page'),
                  path('about/', views.about, name='about'),
                  path('contact/', views.contact, name='contact'),
                  path('news/', views.news, name='news'),
                  path('student_login', views.student_login, name='student_login'),
                  path('library/', views.library, name='library'),
                  path('book/', views.book, name='book'),
                  path('studentlogin/', views.StudentLogin, name='StudentLogin'),
                  path('adminlogin/', views.adminlogin, name='adminlogin'),
                  path('adminpage/', views.adminpage, name='adminpage'),
                  path('studentpage/', views.studentpage, name='studentpage'),
                  path('adminbook/', views.adminbook, name='adminbook'),
                  path('get_book', views.get_book, name='get_book'),
                  path('get_book_admin', views.get_book_admin, name='get_book_admin'),
                  path('get_student', views.get_student, name='get_student')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
