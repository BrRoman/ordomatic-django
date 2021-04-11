$(document).ready(function () {
    $('#get_easter').click(function (e) { 
        const year = $(this).find('#year').val();
        $.get(
            '/ordomatic/get_easter/' + year,
            function(back){
                $('#easter').html(back);
            },
            'html',
        )
    });
});
