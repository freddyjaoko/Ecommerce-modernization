from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import (
    Category, Item, OrderItem, Order,
    Coupon, BillingAddress, Payment, Refund
)
from django.utils import timezone

User = get_user_model()

class ModelTestCase(TestCase):
    def setUp(self):
        # User
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Category
        self.category = Category.objects.create(
            title='T-Shirts',
            slug='t-shirts',
            description='Cool T-Shirts',
            image='test.jpg'
        )

        # Item
        self.item = Item.objects.create(
            title='Cool Shirt',
            price=100,
            discount_price=80,
            category=self.category,
            label='N',
            slug='cool-shirt',
            stock_no='A123',
            description_short='Short desc',
            description_long='Long desc',
            image='shirt.jpg'
        )

        # OrderItem
        self.order_item = OrderItem.objects.create(
            user=self.user,
            ordered=False,
            item=self.item,
            quantity=2
        )

        # Coupon
        self.coupon = Coupon.objects.create(
            code='DISCOUNT10',
            amount=10
        )

        # Billing Address
        self.billing_address = BillingAddress.objects.create(
            user=self.user,
            street_address='123 Main St',
            apartment_address='Apt 1',
            country='KE',
            zip='00100',
            address_type='B'
        )

        # Payment
        self.payment = Payment.objects.create(
            stripe_charge_id='abc123',
            user=self.user,
            amount=160
        )

        # Order
        self.order = Order.objects.create(
            user=self.user,
            ref_code='XYZ123',
            ordered_date=timezone.now(),
            ordered=False,
            billing_address=self.billing_address,
            shipping_address=self.billing_address,
            payment=self.payment,
            coupon=self.coupon
        )
        self.order.items.add(self.order_item)

        # Refund
        self.refund = Refund.objects.create(
            order=self.order,
            reason="Not satisfied",
            accepted=False,
            email="user@example.com"
        )

    def test_item_string(self):
        self.assertEqual(str(self.item), "Cool Shirt")

    def test_order_item_total_price(self):
        self.assertEqual(self.order_item.get_total_item_price(), 200)

    def test_order_item_discount_price(self):
        self.assertEqual(self.order_item.get_total_discount_item_price(), 160)

    def test_order_item_amount_saved(self):
        self.assertEqual(self.order_item.get_amount_saved(), 40)

    def test_order_item_final_price(self):
        self.assertEqual(self.order_item.get_final_price(), 160)

    def test_order_total_with_coupon(self):
        self.assertEqual(self.order.get_total(), 150)

    def test_order_string(self):
        self.assertEqual(str(self.order), self.user.username)

    def test_coupon_string(self):
        self.assertEqual(str(self.coupon), 'DISCOUNT10')

    def test_payment_string(self):
        self.assertEqual(str(self.payment), self.user.username)

    def test_billing_address_string(self):
        self.assertEqual(str(self.billing_address), self.user.username)

    def test_refund_string(self):
        self.assertEqual(str(self.refund), str(self.refund.pk))
