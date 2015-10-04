<!-- this highlights current tab in navegation bar -->
$(document).ready(function() {
    $('html, body').animate({
            scrollTop: $(".highlight").offset().top - 300
        }, 1000);
});
