$(document).ready(function () {
    let value = $("#menu").attr("id");

    $("#menu").click(function () {
        if (value === "menu") {
            $("#nav-close").show();
            $("#nav-open").hide();
            value = "close"
        } else {
            $("#nav-close").hide();
            $("#nav-open").show();
            value = "menu"
        }
    })
});
$("#dropdown").on("click", function (e) {
    e.preventDefault();

    if ($(this).hasClass("open")) {
        $(this).removeClass("open");
        $(this).children("ul").slideUp("fast");
    } else {
        $(this).addClass("open");
        $(this).children("ul").slideDown("fast");
    }
});