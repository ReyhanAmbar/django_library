from django.db import models
from datetime import date


class Library(models.Model):
    issueB = [
        ('Uygun', 'uygun'),
        ('Uygun değil', 'uygun değil')
    ]

    catchoice = [
        ('null', 'Lütfen bir kategori seçiniz'),
        ('Bilim & Mühendislik', 'Bilim & Mühendislik'),
        ('Edebiyat', 'Edebiyat')
    ]

    title = models.CharField(max_length=100,
                             blank=False, null=False,
                             verbose_name='Kitap Adı',
                             help_text='Kitabın adını giriniz.')
    author = models.CharField(max_length=100,
                              blank=False, null=False,
                              verbose_name='Yazar',
                              help_text='Kitabın yazarını giriniz.')
    year = models.IntegerField(verbose_name='Basım Yılı',
                               help_text='Basım yılını giriniz.',
                               blank=True, null=True)
    category = models.CharField(max_length=30,
                                verbose_name='Kategori',
                                choices=catchoice,
                                default='null')
    availability = models.CharField(max_length=30,
                                    verbose_name='Uygunluk',
                                    choices=issueB,
                                    default='Uygun')
    student_name = models.CharField(max_length=100,
                                    verbose_name='Öğrenci Adı',
                                    help_text='Kitabı alacak öğrencinin adı',
                                    blank=True, default='', null=True)
    student_surname = models.CharField(max_length=100,
                                       verbose_name='Öğrenci Soyadı',
                                       help_text='Kitabı Alacak Öğrencinin Soyadı',
                                       blank=True, null=True, default='')
    student_no = models.CharField(max_length=50,
                                  verbose_name='Öğrenci No',
                                  help_text='Öğrenci Numarası',
                                  blank=True, null=True, default='')
    student_contact = models.CharField(max_length=100,
                                       verbose_name='Öğrenci Telefon No',
                                       help_text='Öğrenci telefon numarası',
                                       blank=True, null=True, default='')
    student_email = models.CharField(max_length=150,
                                     verbose_name='Öğrenci Email',
                                     help_text='Öğrenci e-mail',
                                     blank=True, null=True, default='')
    given_date = models.DateField(blank=True, null=True,
                                  verbose_name='Verilen Tarih',
                                  help_text='Veriliş Tarihi')
    expiration_date = models.DateField(blank=True, null=True,
                                       verbose_name='Son Teslim Tarihi',
                                       help_text='Bitiş Tarihi')

    class Meta:
        verbose_name_plural = "Library"
        ordering = ['expiration_date']

    def __str__(self):
        return "%s" % self.title


class RequestedBook(models.Model):
    title = models.CharField(max_length=100,
                             blank=False, null=False,
                             verbose_name='Kitap Adı',
                             help_text='Kitabın adını giriniz.')
    author = models.CharField(max_length=100,
                              blank=False, null=False,
                              verbose_name='Yazar',
                              help_text='Kitabın yazarını giriniz.')
    year = models.IntegerField(verbose_name='Basım Yılı',
                               help_text='Basım yılını giriniz.',
                               blank=True, null=True)

    class Meta:
        verbose_name_plural = "Requested Books"
        ordering = ['id']

    def __str__(self):
        return "%s" % self.title


class Contact(models.Model):
    reason_choice = [
        ('Lütfen Bir Neden Seçiniz', 'Lütfen bir neden seçiniz'),
        ('Kitap Rezerve Et', 'Kitap rezerve et'),
        ('Kitap Kayıp Bildirimi', 'Kitap kayıp bildirimi'),
        ('Şikayet ve Önerileriniz', 'Şikayet ve önerileriniz'),
        ('Diğer', 'Diğer')
    ]
    reason = models.CharField(max_length=70,
                              verbose_name='Nedeniniz',
                              choices=reason_choice,
                              default='Lütfen Bir Neden Seçiniz')
    title = models.CharField(max_length=100,
                             blank=False, null=False,
                             verbose_name='Mesajınızın Konusu',
                             help_text='Lütfen başlığınızı açıklayıcı giriniz. Başlıksız mesajlar okunmaz.')
    content = models.TextField(max_length=1000,
                               verbose_name='Mesajınızın İçeriği',
                               blank=False, null=False,
                               help_text='Mesajınızın içeriğini yazınız.')
    student_name = models.CharField(max_length=100,
                                    verbose_name='Öğrenci Adı',
                                    help_text='Adınız',
                                    blank=True, default='', null=True)
    student_surname = models.CharField(max_length=100,
                                       verbose_name='Öğrenci Soyadı',
                                       help_text='Soyadınız',
                                       blank=True, null=True, default='')
    student_no = models.CharField(max_length=50,
                                  verbose_name='Öğrenci No',
                                  help_text='Öğrenci Numarası',
                                  blank=True, null=True, default='')
    student_contact = models.CharField(max_length=100,
                                       verbose_name='Öğrenci İletişim',
                                       help_text='Geri dönüş için telefon ya da email giriniz',
                                       blank=True, null=True, default='')

    class Meta:
        verbose_name_plural = "Messages From Students"
        ordering = ['id']

    def __str__(self):
        return "%s" % self.title


class Student(models.Model):
    gender = [
        ('', 'Cinsiyet Seçiniz'),
        ('kadın', 'Kadın'),
        ('erkek', 'Erkek')
        ]
    student_name = models.CharField(max_length=100,
                                    verbose_name='Öğrenci Adı',
                                    help_text='Kitabı alacak öğrencinin adı',
                                    blank=False, default='', null=False)
    student_surname = models.CharField(max_length=100,
                                       verbose_name='Öğrenci Soyadı',
                                       help_text='Kitabı Alacak Öğrencinin Soyadı',
                                       blank=False, null=False, default='')
    student_no = models.CharField(max_length=50,
                                  verbose_name='Öğrenci No',
                                  help_text='Öğrenci Numarası',
                                  blank=False, null=False, default='')
    student_contact = models.CharField(max_length=100,
                                       verbose_name='Öğrenci Telefon No',
                                       help_text='Öğrenci telefon numarası',
                                       blank=False, null=False, default='')
    student_email = models.CharField(max_length=150,
                                     verbose_name='Öğrenci Email',
                                     help_text='Öğrenci e-mail',
                                     blank=False, null=False, default='')
    student_password = models.CharField(max_length=20,
                                        verbose_name='Öğrenci Şifre',
                                        help_text='Öğrenci Şifresi',
                                        blank=False, null=False, default='')
    student_tc = models.CharField(max_length=11,
                                  verbose_name='Öğrenci TC',
                                  help_text='Öğrenci TC Giriniz',
                                  blank=False, null=False, default='')
    student_gender = models.CharField(max_length=10,
                                      choices=gender,
                                      default='',
                                      verbose_name='Cinsiyet',
                                      help_text='Cinsiyet Seçiniz')
    student_branch = models.CharField(max_length=100,
                                      verbose_name='Okuduğu Bölüm',
                                      help_text='Öğrencinin okuduğu bölüm',
                                      blank=False, null=False, default='')

    class Meta:
        verbose_name_plural = "Student List"
        ordering = ['id']

    def __str__(self):
        return "%s" % self.student_no
