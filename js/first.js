$('#start, #project_page').on('click', function(e){
    e.preventDefault();
    var target= $(this).get(0).id == 'start1' ? $('#start') : $('#project_page');
    $('html, body').stop().animate({
       scrollTop: target.offset().top
    }, 1000);
});