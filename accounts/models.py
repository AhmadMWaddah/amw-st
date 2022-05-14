import pathlib

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def upload_account_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'accounts/{self.username}{ext}'


def default_image():
    return 'defaults/default.png'


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Must Have An E_Mail.')
        if not username:
            raise ValueError('Must Have An UserName.')
        account = self.model(email=self.normalize_email(email), username=username)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_staff_user(self, email, username, password):
        account = self.create_user(email=self.normalize_email(email), username=username, password=password)
        account.is_admin = False
        account.is_staff = True
        account.is_superuser = False
        account.save(using=self._db)
        return account

    def create_superuser(self, email, username, password):
        account = self.create_user(email=self.normalize_email(email), username=username, password=password)
        account.is_admin = True
        account.is_staff = True
        account.is_superuser = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='EMail', max_length=100, unique=True)
    username = models.CharField(verbose_name='UserName', max_length=100, unique=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=255, null=True, blank=True)
    mobile = models.IntegerField(verbose_name='Mobile', null=True, blank=True)
    have_kids = models.BooleanField(verbose_name='Have Kide', default=False)
    kids_count = models.IntegerField(verbose_name='Kids Count', default=0)
    facebook = models.CharField(verbose_name='Facebook', max_length=300)
    instagram = models.CharField(verbose_name='Instagram', max_length=300)
    pinterest = models.CharField(verbose_name='Pinterest', max_length=300)
    snapchat = models.CharField(verbose_name='Snapchat', max_length=300)
    linkedin = models.CharField(verbose_name='LinkedIn', max_length=300)
    twitter = models.CharField(verbose_name='Twitter', max_length=300)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Date Updated', auto_now=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
    is_superuser = models.BooleanField(verbose_name='Is SuperUser', default=False)
    is_admin = models.BooleanField(verbose_name='Is Admin', default=False)
    image = models.ImageField(verbose_name='Image', upload_to=upload_account_image, default=default_image)
    address = models.ForeignKey('Address', verbose_name='Address', on_delete=models.CASCADE, null=True, blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        ordering = ['-date_updated', '-date_joined']

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Address(models.Model):
    address = models.CharField(verbose_name='Address', max_length=255)
    country = models.CharField(verbose_name='Country', max_length=255)
    state = models.CharField(verbose_name='State', max_length=255)
    city = models.CharField(verbose_name='City', max_length=255)
    street = models.CharField(verbose_name='Street', max_length=255)
    building = models.IntegerField(verbose_name='Street No')
    floor = models.IntegerField(verbose_name='Floor No')
    flat = models.IntegerField(verbose_name='Flat No')
    notes = models.TextField(verbose_name='More Info')

    class Meta:
        ordering = ['city']
