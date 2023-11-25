```python
from odoo import models, fields, api
from urllib.parse import urlparse

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    main_image_url = fields.Char(string='Main Image URL', required=True)
    extra_media_urls = fields.Text(string='Extra Media URLs')

    @api.constrains('main_image_url', 'extra_media_urls')
    def _check_url_validity(self):
        for record in self:
            if not self._validate_url(record.main_image_url):
                raise models.ValidationError('Invalid URL in Main Image URL field')
            if record.extra_media_urls:
                urls = record.extra_media_urls.split('\n')
                for url in urls:
                    if not self._validate_url(url):
                        raise models.ValidationError('Invalid URL in Extra Media URLs field')

    @staticmethod
    def _validate_url(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
```