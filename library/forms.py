from django import forms
from .models import Library, RequestedBook, Contact, Student
from datetime import date

banned_emails = ['gx7600@hotmail.com']


class StudentLoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput, label='Kullanıcı Adı', required=True)
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(StudentLoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control col-lg-5'}  # Bütün form elemanlarına erişir

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_emails:
            raise forms.ValidationError('Hesabınız Blokedir')
        return email



class AdminLoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı', required=True)
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(AdminLoginForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'col-lg-4'}  # Bütün form elemanlarına erişir

    def clean_admin(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username != 'operator' or password != 'operator':
            raise forms.ValidationError('Yanlış Bilgi Girdiniz')
        return username, password


class LibraryForm(forms.ModelForm):
    class Meta:
        model = RequestedBook
        fields = ['title', 'author', 'year']

    def __init__(self, *args, **kwargs):
        super(LibraryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class DateInput(forms.DateInput):
    input_type = 'date'


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


class LibraryFormExtra(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['title', 'author', 'year', 'category', 'availability', 'student_name',
                  'student_surname', 'student_no', 'student_contact', 'student_email',
                  'given_date', 'expiration_date']
        widgets = {'given_date': DateInput(),
                   'expiration_date': DateInput()}

    def __init__(self, *args, **kwargs):
        super(LibraryFormExtra, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class LibraryAddBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['title', 'author', 'year', 'category']

    def __init__(self, *args, **kwargs):
        super(LibraryAddBookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class ChoiceFilterForm(forms.Form):
    filter_choice = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=Library.catchoice,
                                      required=False)
    search = forms.CharField(required=False, max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))


class StudentSearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['reason', 'title', 'content', 'student_name',
                  'student_surname', 'student_no', 'student_contact']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_surname', 'student_tc', 'student_gender', 'student_no', 'student_contact', 'student_email', 'student_branch',
                  'student_password']
        widget = {'student_password': PasswordInput}

    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
