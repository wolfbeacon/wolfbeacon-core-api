from django.http import JsonResponse
from wolfbeacon.settings import AUTH0
from jose import jwt
from urllib.parse import urlparse

AUTH0_PUBLIC_KEY = AUTH0['PUBLIC_KEY']
AUTH0_DOMAIN = AUTH0['AUTH0_DOMAIN']
API_AUDIENCE = AUTH0['API_AUDIENCE']
ALGORITHMS = AUTH0['ALGORITHM']
BLOCKED_PATHS = AUTH0['BLOCKED_PATHS_REGEX']


class Auth0Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        url = request.build_absolute_uri()
        path = urlparse(url).path

        # Block access to paths that require Auth and verify
        if BLOCKED_PATHS.match(path):

            # GET TOKEN
            auth = request.META.get('HTTP_AUTHORIZATION')

            if not auth:
                return JsonResponse(data={"code": "authorization_header_missing",
                                          "description":
                                              "Authorization header is expected"}, status=401)

            parts = auth.split()

            if parts[0].lower() != "bearer":
                return JsonResponse(data={"code": "invalid_header",
                                          "description":
                                              "Authorization header must start with"
                                              "Bearer"}, status=401)
            elif len(parts) == 1:
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Token not found"}, status=401)
            elif len(parts) > 2:
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Authorization header must be"
                                                         "Bearer token"}, status=401)

            token = parts[1]

            # VALIDATE TOKEN

            jwks = AUTH0_PUBLIC_KEY
            try:
                unverified_header = jwt.get_unverified_header(token)
            except jwt.JWTError:

                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Invalid header. "
                                                         "Use an RS256 signed JWT Access Token"}, status=401)

            if unverified_header["alg"] == "HS256":
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Invalid header. "
                                                         "Use an RS256 signed JWT Access Token"}, status=401)

            rsa_key = {}
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
            if rsa_key:
                try:
                    jwt.decode(
                        token,
                        rsa_key,
                        algorithms=ALGORITHMS,
                        audience=API_AUDIENCE,
                        issuer="https://" + AUTH0_DOMAIN + "/"
                    )

                except jwt.ExpiredSignatureError:
                    return JsonResponse(data={"code": "token_expired",
                                              "description": "token is expired"}, status=401)
                except jwt.JWTClaimsError:
                    return JsonResponse(data={"code": "invalid_claims",
                                              "description": "incorrect claims,"
                                                             " please check the audience and issuer"}, status=401)
                except Exception:
                    return JsonResponse(data={"code": "invalid_header",
                                              "description": "Unable to parse authentication"
                                                             " token."}, status=400)
            else:
                return JsonResponse(data={"code": "invalid_header",
                                          "description": "Unable to find appropriate key"}, status=401)

        response = self.get_response(request)
        return response
