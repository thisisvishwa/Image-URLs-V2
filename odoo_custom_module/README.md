# Odoo Custom Module for Displaying External Product Images

## Introduction

This module integrates external URLs for displaying product images in Odoo. It facilitates the management and display of product images from external sources in both the main product image and additional product media sections.

## Objectives

- Facilitate the management of product images from external sources without storing them locally in Odoo.
- Improve Odoo eCommerce site performance by offloading image storage.
- Provide a scalable and efficient method for managing large product catalogs.

## Scope

The development includes extending the Odoo product model, updating the product template view, and implementing dynamic image rendering.

## Installation

1. Download the module and add it to your Odoo addons folder.
2. Restart the Odoo server.
3. Go to Apps menu and click on 'Update Modules List'.
4. Remove the 'Apps' filter and search for this module.
5. Click on 'Install' to install the module.

## Usage

After installation, you can add external URLs for product images in the product template form view. The module will automatically render these images in the product view.

## Development Environment

- Platform: Odoo 17 Community Edition.
- Languages and Tools: Python, XML, JavaScript (if needed for dynamic rendering).

## Technical Requirements

- Efficient handling of external URLs and dynamic image loading.
- Implement robust error handling for invalid or unreachable URLs.
- Ensure compatibility with existing Odoo modules and customizations.
- Provide comprehensive documentation including setup, usage, and troubleshooting guides.

## Testing

Perform unit and integration testing in a controlled environment. The module includes a test suite located in `odoo_custom_module/tests/test_product_template.py`.

## Acceptance Criteria

- All features work as intended.
- Module meets predefined performance criteria.
- Conduct testing with end-users for feedback and refinements.

## Support

If you encounter any problems or have suggestions for improvements, please create an issue in the issue tracker.

## License

This module is licensed under the MIT License. See the LICENSE file for more details.