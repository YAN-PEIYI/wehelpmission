(function(){
    $('.openR').click(function () {
        $('.right-menu').toggleClass('active');
    });
    $(".layer").click(function (e) {
        if ($('.right-menu').hasClass("active")) {
            $('.right-menu').removeClass("active");
        }
    });
})();