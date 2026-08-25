from django.contrib import admin
from vault.models import Vault, VaultMember

class VaultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )
    
class VaultMemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'member_id',
        'vault_id',
        'role'
    )
    
admin.site.register(Vault, VaultAdmin)
admin.site.register(VaultMember, VaultMemberAdmin)