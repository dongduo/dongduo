requirejs.config({
    baseUrl: 'static/scripts/libs',

    shim: {
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            exports: '_'
        },
        'bootstrap': {
            deps: ['jquery']
        }
    },

    paths: {
    }
});

requirejs(['jquery', 'backbone', 'underscore', 'bootstrap'], function ($, Backbone, _) {
    $(function () {
    });
});
