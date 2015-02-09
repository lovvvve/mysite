from django.db import models

# Create your models here.

class Ip_address(models.Model):
    ip_address = models.CharField(max_length=15, unique=True)

    def __unicode__(self):
        return self.ip_address


class Contacts(models.Model):
    name = models.CharField(max_length=10, unique=True)
    mobile_phone = models.CharField(max_length=11)
    phone_ext = models.CharField(max_length=5)
    email = models.EmailField(verbose_name='e-mail')

    def __unicode__(self):
        return u'%s mobile phone is %s e-mail is %s' % (self.name, self.mobile_phone, self.email)


class Application(models.Model):
    name = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(Contacts)
    department = models.CharField(max_length=30)
    project = models.CharField(max_length=30,default='peoject')

    def __unicode__(self):
        return self.name


class Server(models.Model):
    is_hypervisor = models.BooleanField(default=False)
    Ip_address = models.ForeignKey(Ip_address)
    device_model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=30, unique=True)
    UUID = models.CharField(max_length=30)

    def __unicode__(self):
        return self.serial_number


class Hypervisor(models.Model):
    hypervisor_hostname = models.CharField(max_length=30)
    hypervisor_ip = models.ForeignKey(Ip_address)
    serial_number = models.ForeignKey(Server, default=2)
    vm_number = models.SmallIntegerField()

    def __unicode__(self):
        return u'%s (%s) have %s VMs.' % (self.hypervisor_hostname, self.hypervisor_ip, self.vm_number)


class VM(models.Model):
    vm_ip = models.ForeignKey(Ip_address)
    hypervisor_ip = models.ForeignKey(Hypervisor)
    UUID = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s in hypervisor %s' % (self.vm_ip, self.hypervisor_ip)


class Host(models.Model):
    private_ip = models.ForeignKey(Ip_address)
    appname = models.ForeignKey(Application)
    hostname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'%s: %s' % (self.appname, self.private_ip)
