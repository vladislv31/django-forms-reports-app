$(document).ready(function() {

    do_questionnaire();

});

function do_questionnaire() {

    $('form#do-questionnaire-form select[name="industry"]').change(function() {
        const th = $(this);
        const val = th.val();
        const form = th.closest('form');

        if (val == 'another') {
            $('input[name="industry-another"]', form).css('display', 'block').attr('required', '');
        } else {
            $('input[name="industry-another"]', form).css('display', 'none').removeAttr('required');
        }
    });

    $('form#do-questionnaire-form select[name="type_used_systems"]').change(function() {
        const th = $(this);
        const val = th.val();
        const form = th.closest('form');

        if (val == 'another') {
            $('input[name="type_used_systems-another"]', form).css('display', 'block').attr('required', '');
        } else {
            $('input[name="type_used_systems-another"]', form).css('display', 'none').removeAttr('required');
        }
    });

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

    $('form#do-determine-questionnaire-form').submit(function(e) {
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

            if (data?.status == 'ok') {
                let category_display;

                if (data.determined_category === 'first') category_display = 'первая категория значимости';
                if (data.determined_category === 'second') category_display = 'вторая категория значимости';
                if (data.determined_category === 'third') category_display = 'третья категория значимости';
                if (data.determined_category === 'non') category_display = 'без категории значимости';

                $('.form-alerts .form-alerts__success span', th).text(category_display);
                $('.form-alerts .form-alerts__success', th).css('display', 'block');
            } else {
                $('.form-alerts .form-alerts__error', th).css('display', 'block');
            }
        });
    });

}
