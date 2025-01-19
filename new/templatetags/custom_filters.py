from django import template

register = template.Library()
BAN_WORD = ['редиска']


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()


@register.filter
def censure_text(value):
    result = value
    for word in BAN_WORD:
        if word in value:
            result = value.replace(word, f'{word[0]}{(len(word) - 1) * '*'}')

    return result
