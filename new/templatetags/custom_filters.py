from django import template

register = template.Library()
BAN_WORD = ['редиска']


@register.filter
def censure_text(value):
    result = value
    for word in BAN_WORD:
        if word in value:
            result = value.replace(word, f'{word[0]}{(len(word) - 1) * '*'}')

    return result
