from django.db import models
from django.contrib.auth.models import User

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, default="Default Company")  # Add default here
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    image = models.FileField(null=True)
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    desc = models.TextField(null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.category.name} -- {self.name}"

class Status(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1) 

class Booking(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    booking_id = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    book_date = models.DateField(null=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.book_date} - {self.profile.user.username}"

class Send_Feedback(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.profile.user.username} - {self.date}"

class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PetProfile(models.Model):
    name = models.CharField(max_length=100, null=True)
    breed = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    image = models.FileField(null=True)
    owner = models.ForeignKey(User, related_name='owned_pets', on_delete=models.CASCADE)
    veterinarian = models.CharField(max_length=100, null=True)
    visit_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class ProductRequest(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='pending')

class AdminRequest(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField(default='', max_length=1000)  # Adjusted max_length

    def __str__(self):
        return f"{self.product_name} - Requested by: {self.requested_by}"

class SupplierRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_requests')
    request_date = models.DateTimeField(auto_now_add=True)
    admin_details = models.TextField()  # Field for admin details
    user_details = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Request by {self.requester.username} at {self.request_date}"

# Register AdminRequest in the admin panel
from django.contrib import admin
from .models import AdminRequest   

class AdminRequestAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'requested_by')  # Specify the fields to display in the list view

admin.site.register(AdminRequest, AdminRequestAdmin)
from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"
