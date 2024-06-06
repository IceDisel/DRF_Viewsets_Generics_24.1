from django.core.exceptions import ValidationError
from urllib.parse import urlparse


class YouTubeLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        value = attrs.get(self.field)
        if value:
            parsed_url = urlparse(value)
            if parsed_url.netloc != 'www.youtube.com' and parsed_url.netloc != 'youtube.com':
                raise ValidationError({self.field: 'Допускаются только ссылки на youtube.com'})
