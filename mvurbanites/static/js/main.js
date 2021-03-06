$(function() {
    $('#promo').carousel();

    $("#meetup-dialog").dialog({
        autoOpen: false,
        modal: true,
        title: 'Event Information',
        closeText: 'Hide',
        width: 600,
        maxHeight: 600,
        buttons: [{
            text: 'Close',
            class: 'btn',
            click: function() {
                $(this).dialog('close');
            }
        }]
    });

    $("#upcoming").datepicker({
        beforeShowDay: function(date) {
            var result = [true, '', null];
            var matching = $.grep(events, function(event) {
                return event.Date.valueOf() === date.valueOf();
            });
            
            if (matching.length) {
                result = [true, 'highlight', null];
            }
            return result;
        },
        onSelect: function(dateText) {
            var date,
                selectedDate = new Date(dateText),
                i = 0,
                event = null;
            
            while (i < events.length && !event) {
                date = events[i].Date;

                if (selectedDate.valueOf() === date.valueOf()) {
                    event = events[i];
                }
                i++;
            }
            if (event) {
                $("#event-title").html(event.Title);
                $("#event-rsvp").attr('href', event.Url);
                $("#event-description").html(event.Description);
                $("#meetup-dialog").dialog('open');
            }
        }
    });

});
