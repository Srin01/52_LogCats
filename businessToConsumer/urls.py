from django.urls import path
from .views import (
    HomeView,
    MyAccount,
    InventorySales,
    CheckoutView,
    ProductDetail,
    OrderSummaryView,
    PaymentView,
    CouponView,
    afterAdd,
    addItem,
    payment_complete,
    add_to_cart,
    remove_from_cart,
    remove_single_from_cart,
    customerReg,
    afterReg,
    wholesale_shop,
    nearby_shop
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('addItem/',addItem, name='addItem'),
    path('afterAdd/',afterAdd, name='afterAdd'),
    path('editProfile/', MyAccount.as_view(), name='my_account'),
    path('payment-complete', payment_complete, name="payment_complete"),
    path('add-coupon', CouponView.as_view(), name="add_coupon"),
    path('payment-complete', payment_complete, name="payment_complete"),
    path('stats/',InventorySales,name = "stats/"),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove-single-from-cart/<slug>/',
         remove_single_from_cart, name='remove_single_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('product/<slug>/', ProductDetail.as_view(), name='product'),
    path('wholesale_shop', wholesale_shop, name = 'wholesale_shop'),
    path('nearby_shop',nearby_shop, name = 'nearby_shop'),
    path('customerReg',customerReg, name='reg'),
    path('afterReg',afterReg, name='after_reg')
]
