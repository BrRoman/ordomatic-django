$(document).ready(function () {
    $('#year').click(function(){
        const year = $(this).val();
        $.get(
            '/ordomatic/get_list_of_days/' + year,
            function(back){
                $('#days_list').html(back);
            },
            'html',
        );
    }).trigger('click');
});
