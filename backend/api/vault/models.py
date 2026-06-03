from django.db import models

class Vault(models.Model):
    owner = models.ForeignKey()


class VaultMember(models.Model):
    class Role(models.TextChoices):
        VIEWER = 'viewer'
        EDITOR = 'editor'
        ADMIN = 'admin'
    
    vault = models.ForeignKey()
    user = models.ForeignKey()
    role = models.CharField(max_length=5, choices=Role.choices)
    
    class Meta:
        unique_together = ['vault', 'user']