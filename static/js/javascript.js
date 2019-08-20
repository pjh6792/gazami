// navbar.html 
$('#search-text').hide();
$('#search-button').hide();
$('#deactivate-search').hide();
$('#asking-gazami').hide();

$('#activate-search').on('click', function(){
    var milliseconds = 100;
        $('#search-text').fadeIn(milliseconds), $('#search-button').fadeIn(milliseconds), $('#activate-search').hide(), $('#deactivate-search').show(),
        $('#logo').fadeOut(milliseconds), $('#asking-gazami').fadeIn(milliseconds), $('#navbar-my').fadeOut(milliseconds);
});

$('#deactivate-search').on('click', function(){
    var milliseconds = 100;
        $('#search-text').fadeOut(milliseconds), $('#search-button').fadeOut(milliseconds), $('#activate-search').show(),
        $('#deactivate-search').hide(), $('#logo').fadeIn(milliseconds), $('#asking-gazami').fadeOut(milliseconds), $('#navbar-my').fadeIn(milliseconds);
});


// main.html
// function compare()
// {
//     var startDt = document.getElementById("main-start-date").value;
//     var today = document.getElementById("main-today").value;
//     var endDate = document.getElementById("main-end-date").value;
//     alert(endDate)

//     if( (new Date(startDt).getTime() <= new Date(today).getTime()) && (new Date(today).getTime() <= new Date(endDate).getTime()))
//     {
//     }
//     else{
//     }
// }


