from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTest(TestCase):
    def test_new_superuser(self):
        
        db = get_user_model()
        super_user = db.objects.create_superuser( #type: ignore
            user_name='test_super',
            email='test@exmaple.com',
            password='test1234',
            first_name='first',
            last_name='last',
        )
        
        self.assertEqual(super_user.user_name, 'test_super')
        self.assertEqual(super_user.email, 'test@exmaple.com')
        self.assertEqual(super_user.first_name, 'first')
        self.assertEqual(super_user.last_name, 'last')
        self.assertEqual(str(super_user), 'test_super')

    def test_super_otherfields(self):
        return
        
        db = get_user_model()
        with self.assertRaises(ValueError):
            super_user = db.objects.create_superuser(
                        username='test_super',
                        email='test@exmaple.com',
                        password='test1234',
                        first_name='first',
                        last_name='last',
                        is_staff=False,
                    )
        
        #Testing not super
        with self.assertRaises(ValueError):
            super_user = db.objects.create_superuser(
                        username='test_super',
                        email='test@exmaple.com',
                        password='test1234',
                        first_name='first',
                        last_name='last',
                        is_super=False,
                    )
            