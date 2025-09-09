from django.http import HttpResponseForbidden
import jwt
 
WHITELISTED_URLS = [
    "/api/users/login",
    "/api/users/register",
    "/api/users/roles",
    "/docs/",
    "/redocs/",
]

""" Middleware that allows you to validate whether a user has an active session using a token. """
def validate_role(get_response):

    def middleware(request):
        if request.path not in WHITELISTED_URLS:
            # Validate whether the token has been sent.
            if 'token' not in request.headers:
                return HttpResponseForbidden("The token must be sent in the service.")
            
            token = request.headers['token']
            try:
                decoded_data = jwt.decode(jwt=token, key='secret', algorithms=["HS256"])

                if request.method == 'POST' and decoded_data["rol"]["id"] != 1:
                    return HttpResponseForbidden("The user must be a 'Operador logístico'")
                else:
                    if request.method == 'GET' and (decoded_data["rol"]["id"] != 1 and decoded_data["rol"]["id"] != 2):
                        return HttpResponseForbidden("The user must be a 'Operador logístico' or a 'Pasajero'")
            except Exception as e:
                return HttpResponseForbidden("You must send a valid token.")
            
        response = get_response(request)
        return response
    
    return middleware