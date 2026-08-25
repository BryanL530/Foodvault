from rest_framework import views, permissions, generics, response
from vault import permissions as vault_permissions
from vault import services as vault_services
from vault.serializers import VaultSerializers, MemberSerializers
  
class VaultAPI(views.APIView):
    #authentication_classes = []
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        '''
        Creates a new vault with user being the owner in vault member
        '''
        vault_serializer = VaultSerializers(data=request.data)
        vault_serializer.is_valid(raise_exception=True)
        
        # Process data
        data = vault_serializer.validated_data
        vault_serializer.instance = vault_services.create_vault(request.user, data)
        return response.Response({'message': 'Vault created'})
    
    def patch(self, request):
        '''
        Update the vault information name/description
        '''
        return response.Response({'message': 'Not yet implemented'})
    
    def get(self, request):
        '''
        Retrieve single/list of vault the user have the permission to read or more
        '''
        target_vault = request.query_params.get('id', None)
        
        if target_vault:
            # Retrieve target vault data
            pass
        else:
            # Retrieve list of accessible vault
            pass      
        return response.Response({'message': 'Not yet implemented'})
    
    def delete(self, request):
        '''
        Deletes a targeted vault
        '''    
        return response.Response({'message': 'Not yet implemented'})