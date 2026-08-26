from django.db import models
class Service(models.Model):
    name=models.CharField(max_length=120); short_description=models.CharField(max_length=255); description=models.TextField(blank=True); active=models.BooleanField(default=True)
    def __str__(self): return self.name
class QuoteRequest(models.Model):
    STATUS=[('new','Nouveau'),('contacted','Contacté'),('quoted','Devis envoyé'),('accepted','Accepté'),('closed','Clôturé')]
    name=models.CharField(max_length=120); email=models.EmailField(); phone=models.CharField(max_length=40); service=models.ForeignKey(Service,on_delete=models.SET_NULL,null=True,blank=True); address=models.CharField(max_length=255,blank=True); preferred_date=models.DateField(null=True,blank=True); message=models.TextField(blank=True); status=models.CharField(max_length=20,choices=STATUS,default='new'); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.name} – {self.created_at:%d/%m/%Y}'
class ContactMessage(models.Model):
    name=models.CharField(max_length=120); email=models.EmailField(); phone=models.CharField(max_length=40,blank=True); message=models.TextField(); created_at=models.DateTimeField(auto_now_add=True); handled=models.BooleanField(default=False)
    def __str__(self): return f'{self.name} – {self.created_at:%d/%m/%Y}'
