import pathlib

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def upload_account_image(self, filename):
    ext = pathlib.Path(filename).suffix
    return f'accounts/{self.username}{ext}'


def default_image():
    return 'defaults/default.png'


class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Must Have An E_Mail.')
        if not username:
            raise ValueError('Must Have A UserName.')
        account = self.model(email=self.normalize_email(email), username=username)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_staff_user(self, email, username, password):
        account = self.create_user(email=self.normalize_email(email), username=username, password=password)
        account.staff = True
        account.admin = True
        account.save(using=self._db)
        return account

    def create_superuser(self, email, username, password):
        account = self.create_staff_user(email=self.normalize_email(email), username=username, password=password)
        account.superuser = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='EMail', max_length=100, unique=True)
    username = models.CharField(verbose_name='UserName', max_length=100, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=255, null=True, blank=True)
    last_name = models.CharField(verbose_name='last Name', max_length=255, null=True, blank=True)
    kids_count = models.IntegerField(verbose_name='Kids Count', default=0)
    facebook = models.CharField(verbose_name='Facebook', max_length=300, blank=True, null=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=300, blank=True, null=True)
    pinterest = models.CharField(verbose_name='Pinterest', max_length=300, blank=True, null=True)
    snapchat = models.CharField(verbose_name='Snapchat', max_length=300, blank=True, null=True)
    linkedin = models.CharField(verbose_name='LinkedIn', max_length=300, blank=True, null=True)
    twitter = models.CharField(verbose_name='Twitter', max_length=300, blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Date Updated', auto_now=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=True)
    staff = models.BooleanField(verbose_name='Is Staff', default=False)
    admin = models.BooleanField(verbose_name='Is Admin', default=False)
    superuser = models.BooleanField(verbose_name='Is SuperUser', default=False)
    image = models.ImageField(verbose_name='Image', upload_to=upload_account_image, default=default_image)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    class Meta:
        ordering = ['-date_updated', '-date_joined']

    def __str__(self):
        return f'{self.username}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def have_kids(self):
        if self.kids_count > 0:
            return True

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


class ShippingDetail(models.Model):
    address_type = (
        ('Home', 'Home'),
        ('Work', 'Work'),
    )
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    type = models.CharField(choices=address_type, max_length=255)
    mobile = models.IntegerField(verbose_name='Mobile', null=True, blank=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    floor = models.IntegerField()
    flat = models.IntegerField()

    @property
    def address(self):
        address = f'{self.street}, {self.city}, {self.state}, {self.country}, Flat {self.flat}, {self.floor} Floor.'
        return address

    def __str__(self):
        return f'{self.account} - Address'
