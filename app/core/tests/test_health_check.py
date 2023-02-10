"""
Tests for the health check API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

class HealthCheckApiTests(TestCase):
    """Test the health check API."""

    def test_health_check(self):
        """Test that the health check API returns a 200."""
        self.client = APIClient()
        res = self.client.get(reverse('health-check'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
