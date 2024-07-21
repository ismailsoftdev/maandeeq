from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
    group_names = [group.strip() for group in group_names.split(',')]
    return user.groups.filter(name__in=group_names).exists()


@register.filter(name='has_perm')
def has_perm(user, perm_name):
    return user.has_perm(perm_name)