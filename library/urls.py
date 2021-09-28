from django.urls import path, re_path
from library.views import request_book, book_detail, admin_book_detail, add_book, \
    book_added, book_update, book_updated, book_delete, book_deletion, requested_book, \
    view_requested_book, req_book_deletion, view_issued_book, contact_operator, view_received_message, contacted, \
    message_delete, message_detail, student_register, student_registered, student_list, student_detail, student_update, \
    student_updated, student_deletion

urlpatterns = [
    path('request_book/', request_book, name='request_book'),
    path('requested_book/', requested_book, name='requested_book'),
    path('view_requested_book/', view_requested_book, name='view_requested_book'),
    re_path(r'req_book_deletion/(?P<pk>[0-9]+)/', req_book_deletion, name='req_book_deletion'),
    re_path(r'book_detail/(?P<pk>[0-9]+)/', book_detail, name='book_detail'),
    re_path(r'admin_book_detail/(?P<pk>[0-9]+)/', admin_book_detail, name='admin_book_detail'),
    path('add_book/', add_book, name='add_book'),
    path('book_added/', book_added, name='book_added'),
    re_path(r'book_update/(?P<pk>[0-9]+)/', book_update, name='book_update'),
    path('book_updated/', book_updated, name='book_updated'),
    re_path(r'book_delete/(?P<pk>[0-9]+)/', book_delete, name='book_delete'),
    re_path(r'book_deletion/(?P<pk>[0-9]+)/', book_deletion, name='book_deletion'),
    path('view_issued_book', view_issued_book, name='view_issued_book'),
    path('contact_operator', contact_operator, name='contact_operator'),
    path('view_received_message', view_received_message, name='view_received_message'),
    path('contacted', contacted, name='contacted'),
    re_path(r'message_delete/(?P<pk>[0-9]+)/', message_delete, name='message_delete'),
    re_path(r'message_detail/(?P<pk>[0-9]+)/', message_detail, name='message_detail'),
    path('student_register', student_register, name='student_register'),
    path('student_registered', student_registered, name='student_registered'),
    path('student_list', student_list, name='student_list'),
    re_path(r'student_detail/(?P<pk>[0-9]+)/', student_detail, name='student_detail'),
    re_path(r'student_update/(?P<pk>[0-9]+)/', student_update, name='student_update'),
    path('student_updated', student_updated, name='student_updated'),
    re_path(r'student_deletion/(?P<pk>[0-9]+)/', student_deletion, name='student_deletion'),

]
