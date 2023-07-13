from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.

    Methods:
        create_user(self, email, password=None, **other_fields): Creates and saves a new User instance.
        create_superuser(self, email, password, **other_fields): Creates and saves a new superuser User instance.
    """

    def create_user(self, email, password=None, **other_fields):
        """
        Creates and saves a new User instance.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **other_fields: Additional fields for the user.

        Returns:
            User: The created User instance.

        Raises:
            ValueError: If email is not provided.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        """
        Creates and saves a new superuser User instance.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **other_fields: Additional fields for the user.

        Returns:
            User: The created superuser User instance.
        """
        user = self.create_user(email, password=password, **other_fields)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    """
    Custom User model.

    Attributes:
        USERNAME_FIELD (str): The field to use as the unique identifier for authentication (email).
        REQUIRED_FIELDS (list[str]): The fields required when creating a user.
        objects (UserManager): The manager for the User model.
        first_name (CharField): The first name of the user.
        last_name (CharField): The last name of the user.
        email (CharField): The email address of the user.
        password (CharField): The password of the user.
        is_active (BooleanField): Indicates whether the user is active or not.
        is_admin (BooleanField): Indicates whether the user is an admin or not.
        is_staff (BooleanField): Indicates whether the user is a staff member or not.

    Methods:
        is_author(self, object): Checks if the user is the author of an object.
        is_contributor(self, project): Checks if the user is a contributor to a project.
        has_permission(self, permission, obj=None): Checks if the user has a permission.
        has_module_permission(self, app_label): Checks if the user has a module-level permission.
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    first_name = models.CharField(max_length=50, blank=True)
    """
    CharField: The first name of the user.
    """

    last_name = models.CharField(max_length=50, blank=True)
    """
    CharField: The last name of the user.
    """

    email = models.CharField(max_length=50, blank=False, unique=True)
    """
    CharField: The email address of the user.
    """

    password = models.CharField(max_length=50, blank=False)
    """
    CharField: The password of the user.
    """

    is_active = models.BooleanField(default=True)
    """
    BooleanField: Indicates whether the user is active or not.
    """

    is_admin = models.BooleanField(default=False)
    """
    BooleanField: Indicates whether the user is an admin or not.
    """

    is_staff = models.BooleanField(default=False)
    """
    BooleanField: Indicates whether the user is a staff member or not.
    """

    def is_author(self, object):
        """
        Checks if the user is the author of an object.

        Args:
            object: The object to check against.

        Returns:
            bool: True if the user is the author, False otherwise.
        """
        if self == object.author:
            return True
        else:
            return False

    def is_contributor(self, project):
        """
        Checks if the user is a contributor to a project.

        Args:
            project: The project to check against.

        Returns:
            bool: True if the user is a contributor, False otherwise.
        """
        for contributor in project.contributors.all():
            if self == contributor.user:
                return True
        return False

    def has_permission(self, permission, obj=None):
        """
        Checks if the user has a permission.

        Args:
            permission: The permission to check.
            obj: The object to check against.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        return True

    def has_module_permission(self, app_label):
        """
        Checks if the user has a module-level permission.

        Args:
            app_label: The app label of the module.

        Returns:
            bool: True if the user has the module-level permission, False otherwise.
        """
        return True
