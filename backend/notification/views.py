from rest_framework import views, response

class NotificationAPI(views.APIView):
    def get(self, request):
        return response.Response('Nofitication API get')
    
