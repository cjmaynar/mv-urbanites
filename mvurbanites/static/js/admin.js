jQuery(function($) {
    $('div.inline-group').sortable({
        items: 'div.inline-related',
        handle: 'h3:first',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('textarea[id$=text]').val()) {
                    $(this).find('input[id$=order]').val(i+1);
                }
            });
        }
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('input[id$=order]').parent().parent('div').hide();
});

/*
 * Use the Django admin jQuery name space. It is running
 * jQuery 1.4 still, so there is no on() function, instead
 * we must drop back to live()
 * */
(function($) {
    $(document).ready(function() {
        $("input[type=radio]").live('change', function(e) {
            if ($(this).attr('value') == 'text') {
                console.log("text");
                // Show text box, hide image fields
            } else {
                console.log("Image");
                // Hide text box, show image fields
            }
        });
    });
}(django.jQuery));
