$(document).ready(function () {
    $('#year').click(function(){
        get_ordo_as_html();
    }).trigger('click');

    $('#calendars').change(function(){
        get_ordo_as_html();
    }).trigger('change');
});

function get_ordo_as_html(){
    const calendar = $('#calendars option:selected').val();
    const year = $('#year').val();
    console.log(calendar, year);
    $.get(
        '/ordomatic/get_ordo_as_html/' + calendar + '/' + year + '/',
        function(back){
            $('#ordo_block').html(back);
        },
        'html',
    );
}
