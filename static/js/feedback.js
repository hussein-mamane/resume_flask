$(document).ready(function() {
    $("#full_name").focus(function() {
        $(this).css("background-color", "#fff");
    });

    $("#full_name").blur(function() {
        $(this).css("background-color", "");
    });

    $("#feedback").focus(function() {
        $(this).css("background-color", "#fff");
    });

    $("#feedback").blur(function() {
        $(this).css("background-color", "");
    });
});