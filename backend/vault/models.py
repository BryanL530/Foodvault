from django.db import models
from django.utils import timezone
#from django.contrib.auth import models as auth_models

class Vault(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    members = models.ManyToManyField('user.User', through='VaultMember', related_name='vaults')
    
    def __str__(self):
        return self.name
        
class VaultMember(models.Model):
    class Role(models.TextChoices):
        OWNER = 'owner', 'Owner'
        EDITOR = 'editor', 'Editor'
        VIEWER = 'viewer', 'Viewer'
        
    vault_id = models.ForeignKey(Vault, on_delete=models.CASCADE)
    member_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=7, choices=Role.choices, default=Role.VIEWER)
    
    class Meta:
        unique_together = ('vault_id', 'member_id')
        
    def __str__(self):
        return f'{self.vault_id}, {self.member_id}, {self.role}'
        
class Item(models.Model):
    vault_id = models.ForeignKey(Vault, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    expiration_date = models.DateField(null=True)
    
    @property
    def has_expiration_date(self) -> bool:
        return self.expiration_date is not None
    
    @property
    def is_expired(self) -> bool:
        if not self.expiration_date:
            return False
        return self.expiration_date < timezone.now().date()
    
    def __str__(self):
        return self.name
            
    
class QuantitiveItem(Item):
    count = models.PositiveIntegerField()
        