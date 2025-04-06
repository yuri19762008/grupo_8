from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin, Permission

#No se identifica lógica para roles y permisos en el código (aunque aparece mencionada en las historias).

class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, last_name, profile_type, password, **extra_fields):

        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        if isinstance(profile_type, int):
            profile_type = ProfileType.objects.get(id=profile_type)
        else:
            profile_type = None

        if profile_type and profile_type.type == 'administrador':
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            profile_type=profile_type,
            **extra_fields #Deberían venir los is_staf y is_superuser
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, profile_type=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self._create_user(email, first_name, last_name, profile_type, password, **extra_fields)

#Tipo de Perfil  (funcionario sectorial (y - Reporta al Analista), analista SMA (y - Fiscalizador) y  administrador SMA)

#MMA puede ver informes de avance
#SNIFA puede ver informes tecnicos
#SMA, Organismo Sectorial

class ProfileType(models.Model): 
    type = models.CharField(verbose_name="Tipo",max_length=30,unique=True)
    name = models.CharField(verbose_name="Nombre",max_length=30)
    permissions = models.ManyToManyField(Permission,blank=True)
    def __str__(self):
        return self.type

class User(AbstractBaseUser,PermissionsMixin):
    email =  models.CharField(verbose_name='Correo Electrónico',max_length = 255,unique=True)
    first_name=models.CharField(verbose_name='Nombres',max_length = 255, blank=True, null = True)
    last_name=models.CharField(verbose_name='Apellidos',max_length = 255, blank=True, null = True)
    profile_type = models.ForeignKey(ProfileType,on_delete=models.PROTECT,null=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name'] #python manage.py createsuperuser (vee el save)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    