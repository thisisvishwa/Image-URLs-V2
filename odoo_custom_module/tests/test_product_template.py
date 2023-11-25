```python
from odoo.tests import common
from odoo.exceptions import ValidationError

class TestProductTemplate(common.TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        self.ProductTemplate = self.env['product.template']

    def test_main_image_url_field(self):
        product = self.ProductTemplate.create({
            'name': 'Test Product',
            'main_image_url': 'https://example.com/main_image.jpg',
        })
        self.assertEqual(product.main_image_url, 'https://example.com/main_image.jpg')

    def test_extra_media_urls_field(self):
        product = self.ProductTemplate.create({
            'name': 'Test Product',
            'extra_media_urls': ['https://example.com/extra_image1.jpg', 'https://example.com/extra_image2.jpg'],
        })
        self.assertEqual(product.extra_media_urls, ['https://example.com/extra_image1.jpg', 'https://example.com/extra_image2.jpg'])

    def test_invalid_main_image_url(self):
        with self.assertRaises(ValidationError):
            self.ProductTemplate.create({
                'name': 'Test Product',
                'main_image_url': 'invalid_url',
            })

    def test_invalid_extra_media_urls(self):
        with self.assertRaises(ValidationError):
            self.ProductTemplate.create({
                'name': 'Test Product',
                'extra_media_urls': ['invalid_url'],
            })
```