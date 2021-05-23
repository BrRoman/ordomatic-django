$(document).ready(function () {
    $('#year').click(function(){
        const year = $(this).val();
        $.get(
            '/ordomatic/get_ordo_as_html/' + year,
            function(back){
                $('#ordo_block').html(back);
            },
            'html',
        );
    }).trigger('click');
});
