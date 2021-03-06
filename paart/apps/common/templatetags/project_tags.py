from django.template import Library
from django.conf import settings

register = Library()


@register.simple_tag
def project_name():
    return settings.PROJECT_TITLE


@register.filter
def percentage(value):
    return '{:.0%}'.format(value)