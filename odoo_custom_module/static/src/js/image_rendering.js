odoo.define('odoo_custom_module.image_rendering', function (require) {
    'use strict';

    var ajax = require('web.ajax');

    function render_main_image(main_image_url) {
        if (main_image_url) {
            var main_image = document.getElementById('main_image');
            main_image.src = main_image_url;
        }
    }

    function render_extra_media(extra_media_urls) {
        if (extra_media_urls) {
            var extra_media = document.getElementById('extra_media');
            extra_media_urls.forEach(function(url) {
                var img = document.createElement('img');
                img.src = url;
                extra_media.appendChild(img);
            });
        }
    }

    function load_images() {
        ajax.jsonRpc('/web/dataset/call_kw', 'call', {
            model: 'product.template',
            method: 'read',
            args: [[], ['main_image_url', 'extra_media_urls']],
        }).then(function (res) {
            res.forEach(function (product) {
                render_main_image(product.main_image_url);
                render_extra_media(product.extra_media_urls);
            });
        });
    }

    $(document).ready(function () {
        load_images();
    });
});