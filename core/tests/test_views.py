import pytest
from unittest.mock import patch
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Order, BillingAddress, Payment
from django.utils import timezone

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username='testuser', password='12345')
    return user

@pytest.fixture
def create_order(create_user):
    order = Order.objects.create(
        user=create_user,
        ordered=False,
        ordered_date=timezone.now()
    )
    return order

@pytest.fixture
def create_billing_address(create_user):
    billing_address = BillingAddress.objects.create(
        user=create_user,
        street_address="123 Test St",
        apartment_address="Apt 1",
        country="US",
        zip="12345",
        address_type="B"
    )
    return billing_address

@pytest.mark.django_db
def test_payment_view_get_with_billing_address(client, create_user, create_order, create_billing_address):
    client.login(username='testuser', password='12345')
    create_order.billing_address = create_billing_address
    create_order.save()

    response = client.get(reverse('core:payment', kwargs={'payment_option': 'stripe'}))
    assert response.status_code == 200
    assert 'order' in response.context
    assert "payment.html" in [t.name for t in response.templates]

@pytest.mark.django_db
def test_payment_view_get_without_billing_address(client, create_user, create_order):
    client.login(username='testuser', password='12345')

    response = client.get(reverse('core:payment', kwargs={'payment_option': 'stripe'}))
    assert response.status_code == 302
    assert response.url == reverse('core:checkout')

