<!-- this highlights current tab in navegation bar -->
$(document).ready(function() {
    var pathname = window.location.pathname;

    $(".nav a").each(function(index, value) {
        if (pathname == $(this).attr('href'))
            $(this).parent().addClass("active");
    });

    if(pathname == "/") {
        $("#index").addClass("active");
    }
});
