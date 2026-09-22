from rest_framework import views, permissions, generics, status
from rest_framework.response import Response
from vault import permissions as vault_permissions
from vault import services as vault_services
from vault.serializers import VaultSerializers, MemberSerializers
from user.authentication import CustomUserAuthentication
from user.models import User



class VaultAPI(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        '''
        Retrieve single/list of vault the user have the permission to read or more
        '''
        #TODO: NOT YET IMPLEMENTED
        target_vault = request.query_params.get('id', None)
        user_vaults = request.user.get_vaults()
        resp = Response()
        
        resp.data = {'message': 'Not yet implemented get method'}
        return resp
    
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
            return Response({'message':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Vault created'})
    
    def patch(self, request):
        '''
        Update the vault information name/description
        '''
        return Response({'message': 'Not yet implemented put method'})
       
    
    def delete(self, request):
        '''
        Deletes a targeted vault
        '''    
        return Response({'message': 'Not yet implemented delete method'})
    
class ItemApi(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    def get(self, request):
        vault_id = request.query_params.get('vault_id', None)
        item_id = request.query_params.get('item_id', None)
        if not vault_id and not item_id:
            return Response({'message': 'Empty query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response('Item Api get')
    def post(self, request):
        return Response('Item Api post')
    def patch(self, request):
        return Response('Item Api patch')
    def delete(self, request):
        return Response('Item Api delete')
    
class MemberApi(views.APIView):
    authentication_classes = [CustomUserAuthentication]
    def get(self, request):
        return Response('Member Api get')
    def post(self, request):
        return Response('Member Api post')
    def patch(self, request):
        return Response('Member Api patch')
    def delete(self, request):
        return Response('Member Api delete')