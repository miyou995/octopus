from core.models import Invoice
from django.shortcuts import redirect

def user_created_order(view_func):
    def wrap(request, *args, **kwargs):
        order_id = kwargs["order_id"]
        try:
            order = Invoice.objects.get(id=order_id, user=request.user)
        except Invoice.DoesNotExist:
            return redirect('admin:index')
        return view_func(request, *args, **kwargs)
    return wrap