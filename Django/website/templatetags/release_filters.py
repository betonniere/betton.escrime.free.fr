from django import template

register = template.Library()


@register.filter(name='fix_release')
def fix_release(value):
    out = value.replace('__major__',     '5')
    out = out.replace('__minor__',     '6')
    out = out.replace('__beta__',      '34')
    out = out.replace('__ubuntu__',    '<strong>focal</strong> (20.04), <strong>jammy</strong> (22.04)')
    return out
