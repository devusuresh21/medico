from django.dispatch import Signal

admin_product_request = Signal()
from .models import SupplierRequest

# Define a receiver function to handle admin product requests
def handle_admin_product_request(sender, **kwargs):
    admin_user = kwargs['admin_user']
    product_details = kwargs['product_details']
    
    # Logic to store the admin product request in the database
    # For example:
    SupplierRequest.objects.create(requested_by=admin_user, details=product_details)
    
# Connect the receiver function to the signal
admin_product_request.connect(handle_admin_product_request)
