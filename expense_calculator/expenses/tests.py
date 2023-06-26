from django.test import TestCase

# Import for django rest framework
from rest_framework.test import APITestCase
from .models import Expense

# This is not perfect, some tests are better than none.
class ExpenseTestCase(APITestCase):
    def setup(self):
        Expense.objects.create(name="Expense 1", amount="10", category="ONLINE_SERVICES")
        Expense.objects.create(name="Expense 2", amount="20", category="TRAVEL")
        Expense.objects.create(name="Expense 3", amount="30", category="FOOD")
        Expense.objects.create(name="Expense 4", amount="40", category="OTHER")

    def test_expense_list(self):
        response = self.client.get('/api/expenses/')
        self.assertEqual(response.status_code, 200)

    def test_expense_create(self):
        data = {"name": "Expense 5", "amount": "50", "category": "OTHER"}
        response = self.client.post('/api/expenses/', data)
        self.assertEqual(response.status_code, 201)

    def test_expense_update(self):
        data = {"name": "Expense 5", "amount": "55", "category": "OTHER"}
        response = self.client.put('p', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_expense(self):
        response = self.client.delete('/api/expenses/1/')
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        Expense.objects.all().delete()