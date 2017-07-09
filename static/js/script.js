$(document).ready(function () {
    $('.navbarcontainer .dropdown').hover(function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown(150);
    }, function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp(105)
    });


    $('.scrollinrollinrollin').scrollbox({
        direction: 'v',
        linear: true,
        step: 1,
        delay: 0,
        speed: 100
    });
});