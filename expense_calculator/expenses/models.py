from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # category choice field
    CATEGORY_CHOICES = ("ONLINE_SERVICES", "ONLINE_SERVICES"), ("TRAVEL", "TRAVEL"), ("FOOD", "FOOD"), ("OTHER", "OTHER")
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name