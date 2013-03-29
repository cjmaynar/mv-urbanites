$(function() {
    $('#promo').carousel();

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
                alert(event.Title);
            }
        }
    });

});
