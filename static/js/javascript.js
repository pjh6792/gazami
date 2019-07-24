$('#search-text').hide();
$('#search-button').hide();
$('#deactivate-search').hide();
$('#asking-gazami').hide();

$('#activate-search').on('click', function(){
    var milliseconds = 100;
        $('#search-text').fadeIn(milliseconds), $('#search-button').fadeIn(milliseconds), $('#activate-search').hide(), $('#deactivate-search').show(),
        $('#logo').fadeOut(milliseconds), $('#asking-gazami').fadeIn(milliseconds);
});

$('#deactivate-search').on('click', function(){
    var milliseconds = 100;
        $('#search-text').fadeOut(milliseconds), $('#search-button').fadeOut(milliseconds), $('#activate-search').show(),
        $('#deactivate-search').hide(), $('#logo').fadeIn(milliseconds), $('#asking-gazami').fadeOut(milliseconds);
});