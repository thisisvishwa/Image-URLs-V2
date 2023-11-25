{
    "name": "Odoo Custom Module for Displaying External Product Images",
    "version": "1.1",
    "author": "Vishwa G",
    "website": "https://www.yourwebsite.com",
    "category": "Product",
    "summary": "Custom module to display product images from external URLs",
    "description": """
    This module facilitates the management and display of product images from external sources in both the main product image and additional product media sections.
    """,
    "depends": ["base", "product"],
    "data": [
        "views/product_template_form_view.xml",
    ],
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
}