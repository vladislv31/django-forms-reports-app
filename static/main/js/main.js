$(document).ready(function() {

    do_questionnaire();

});

function do_questionnaire() {

    $('form#do-questionnaire-form').submit(function(e) {
        e.preventDefault();

        const th = $(this);

        $('.form-alerts .form-alerts__success', th).css('display', 'none');
        $('.form-alerts .form-alerts__error', th).css('display', 'none');

        $.ajax({
            type: 'POST',
            url: location.protocol + '//' + location.host + location.pathname,
            data: th.serialize()
        }).done(function(json) {
            const data = JSON.parse(json);

            console.log(data)

            if (data?.status === 'ok') {
                $('.form-alerts .form-alerts__success', th).css('display', 'block');
                th.trigger('reset');
                setTimeout(function() {
                    window.location = data.redirect;
                }, 1000);
            } else {
                $('.form-alerts .form-alerts__error', th).css('display', 'block');
            }
        });
    });

}