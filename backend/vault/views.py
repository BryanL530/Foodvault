from rest_framework import views, permissions, generics, response, status
from vault import permissions as vault_permissions
from vault import services as vault_services
from vault.serializers import VaultSerializers, MemberSerializers
from user.authentication import CustomUserAuthentication
from user.models import User
  
class VaultAPI(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        '''
        Creates a new vault with user being the owner in vault member
        '''
        vault_serializer = VaultSerializers(data=request.data)
        vault_serializer.is_valid(raise_exception=True)
        
        # Process data
        try:
            data = vault_serializer.validated_data
            vault_serializer.instance = vault_services.create_vault(request.user, data)
        except:
            return response.Response({'message':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'message': 'Vault created'})
    
    def patch(self, request):
        '''
        Update the vault information name/description
        '''
        return response.Response({'message': 'Not yet implemented put method'})
    
    def get(self, request):
        '''
        Retrieve single/list of vault the user have the permission to read or more
        '''
        
        target_vault = request.query_params.get('id', None)
        user_vaults = request.user.get_vaults()
        resp = response.Response()
        
        if target_vault:
            # Returns target vault
            pass
        else:
            # Returns all user accessible vaults
            pass
        
        resp.data = {'message': 'Not yet implemented get method'}
        return resp
    
    def delete(self, request):
        '''
        Deletes a targeted vault
        '''    
        return response.Response({'message': 'Not yet implemented delete method'})