$(function() {
    /*
     * These are the words that will cycle on the home page.
     * */
    var words = [
        'Explore',
        'Improve',
        'Support',
        'Discover',
        'Inform'
    ];

    $("#slides").slidesjs({
        width: 960,
        height: 400,
        play: {
            auto: true,
            pauseOnHover: true,
        },
        navigation: {
            active: false,
            effect: 'slide'
        },
        callback: {
            start: function(index) {
                // Index is 1 based, array 0 based
                $("#focus").html(words[index - 1]);
            }
        }
    })
});
