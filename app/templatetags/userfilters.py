from django import template
register=template.Library()

def swap(data):
    return data.swapcase()
register.filter('swap',swap)

def remove(data,arg):
    return data.replace(arg,' ')
register.filter('remove',remove)

@register.filter()
def count(data,sub):
    c=0
    for i in range(len(data)):
        if data[i:i+len(sub):]==sub:
            c+=1
    return c

