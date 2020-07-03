from rest_framework.throttling import SimpleRateThrottle

class Mythrottle(SimpleRateThrottle):
    scope = 'user'
    def get_cache_key(self, request, view):
        phone=request.query_params['phone']
        if not phone:
            return None
        # return 'throttle_%(scope)s_%(ident)s' %{'scope':self.scope,'ident':phone}
        return True

