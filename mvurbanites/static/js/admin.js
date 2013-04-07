jQuery(function($) {
    $('div.inline-group').sortable({
        items: 'div.inline-related',
        handle: 'h3:first',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                $(this).find('input[id$=order]').val(i+1);
            });
        }
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('input[id$=order]').parent().parent('div').hide();

    $('div.inline-related').find('textarea').each(function() {
        if ($(this).val() != '' && $(this).attr('id') != 'id_component_set-__prefix__-text') {
            $(this).parent().parent().parent().parent().find('input[type=radio]').filter('[value="text"]').click();
        } else if ($(this).val() == '' && $(this).attr('id') != 'id_component_set-__prefix__-text') {
            $(this).parent().parent().parent().parent().find('input[type=radio]').filter('[value="image"]').click();
        }
    });
});

/*
 * Use the Django admin jQuery name space. It is running
 * jQuery 1.4 still, so there is no on() function, instead
 * we must drop back to live()
 * */
(function($) {
    $(document).ready(function() {
        $(".image").parent().parent().hide();
        $(".text").parent().parent().hide();
        $("input[type=radio]").live('change', function(e) {
            if ($(this).attr('value') == 'text') {
                $(this).closest('.inline-related').find('.text').each(function() {
                    $(this).parent().parent().show();
                });
                $(this).closest('.inline-related').find('.image').each(function() {
                    $(this).parent().parent().hide();
                });
            } else {
                $(this).closest('.inline-related').find('.text').each(function() {
                    $(this).parent().parent().hide();
                });
                $(this).closest('.inline-related').find('.image').each(function() {
                    $(this).parent().parent().show();
                });
            }
        });
    });
}(django.jQuery));
