from django import template
from order.models import Order

register=template.Library()

@register.filter(name="cart_total")
def cart_total(user):
    order=Order.objects.filter(user=user,ordered=False) 
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0

@register.filter(name="total_amount")
def total_amount(get_total):
    total=0
    for i in range(int(get_total)):
        total+=i
    return total