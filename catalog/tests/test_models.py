from django.test import TestCase
from ..models import Department


class TestDepartmentModel(TestCase):
    @classmethod
    def sutUpTestData(cls):
        cls.department = Department.objects.create(id=0, name='back-end')

    def test_max_length_name(self):
        max_length = self.department._meta.get_field('name').max_length
        self.assertEqual(max_length, 32)
