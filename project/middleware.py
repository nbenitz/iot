
import pytz

from django.utils import timezone
#import requests


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('user_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)


class UserTimezoneMiddleware:
    """ Middleware to check user timezone. """

    def process_request(self, request):
        user_time_zone = request.session.get('user_time_zone', None)
        try:
            if user_time_zone is None:
                freegeoip_response = requests.get(
                    'http://freegeoip.net/json/{0}'.format(ip))
                freegeoip_response_json = freegeoip_response.json()
                user_time_zone = freegeoip_response_json['time_zone']
                if user_time_zone:
                    request.session['user_time_zone'] = user_time_zone
            timezone.activate(pytz.timezone(user_time_zone))
        except:
            pass
        return None


class TimezoneMiddleware2(object):
    """
    Middleware to properly handle the users timezone
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # make sure they are authenticated so we know we have their tz info.
        if request.user.is_authenticated:
            # we are getting the users timezone that in this case is stored in
            # a user's profile
            tz_str = request.user.profile.timezone
            timezone.activate(pytz.timezone(tz_str))
        # otherwise deactivate and the default time zone will be used anyway
        else:
            timezone.deactivate()

        response = self.get_response(request)
        return response
