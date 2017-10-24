from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

class MyUserManager(BaseUserManager):
    """
    The default User Model is too crowd, we use Custom BaseUserManager instead
    """

    def create_user(self, username, password=None):
        """
        create a user
        :param username: username of new User
        :param password: password of new User
        :return: A BaseUser object
        """

        user = self.model(
            username=username,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        create a superuser, this is use for "python manage createsuperuser"
        :param username: name of new superuser
        :param password: password of new superuser
        :return: a BaseUser object with is_admin set to True
        """

        user = self.create_user(username, password)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ()

    class Meta:
        ordering = ('-username',)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def is_superuser(self):
        return self.is_admin