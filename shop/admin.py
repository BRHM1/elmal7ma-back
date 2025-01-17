from django.contrib import admin
from .models import User, Category, Product, Order, OrderItem, Cart, CartItem, Review, Payment, ShippingAddress, Discount

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Payment)
admin.site.register(ShippingAddress)
admin.site.register(Discount)
