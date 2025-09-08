from django.http import HttpResponseForbidden
 
WHITELISTED_URLS = [
    "/api/users/login",
    "/api/users/register",
    "/api/users/roles",
    "/api/cities/",

    "/api/routes/",
    "/api/stops/",
    "/api/routes/schedule/2/add-stop/",
    "/api/routes/schedule/2/",
    "/api/routes/schedule/2/stops/",

    "/docs/",
    "/redocs/"
]

def validate_role(get_response):

    def middleware(request):
        if request.path not in WHITELISTED_URLS:
            # Validar si se envia el token
            if 'token' not in request.headers:
                return HttpResponseForbidden("El token debe ser enviado en el servicio")
            
        response = get_response(request)
        return response
    
    return middleware