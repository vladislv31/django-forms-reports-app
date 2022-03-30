$(document).ready(function() {

    edit_questionnaire();

});

function edit_questionnaire() {

    // delete field button
    $(document).on('click', '.edit-questionnaire__item-field__delete', function() {
        const th = $(this);
        const field = th.closest('.edit-questionnaire__item-field');

        field.remove();
    });

    // delete item button
    $(document).on('click', '.edit-questionnaire__item-delete', function() {
        const th = $(this);
        const item = th.closest('.edit-questionnaire__item');

        item.remove();
    });

    // add field link
    $(document).on('click', '.edit-questionnaire__item-add-field', function(e) {
        e.preventDefault();

        const th = $(this);
        const item = th.closest('.edit-questionnaire__item');
        const fields = $('.edit-questionnaire__item-fields', item);

        const item_id = item.attr('data-item-id');

        const last_field = $('.edit-questionnaire__item-field', fields).last();
        let id = 1;

        if (last_field?.length) id = Number(last_field.attr('data-field-id')) + 1;

        fields.append(`
            <div class="edit-questionnaire__item-field" data-field-id="${id}">
                <div class="edit-questionnaire__item-field__number">
                    <input type="text" class="form-control" name="${item_id}_${id}_number" placeholder="Номер" required>
                </div>
                <div class="edit-questionnaire__item-field__question">
                    <input type="text" class="form-control" name="${item_id}_${id}_question" placeholder="Вопрос" required>
                </div>
                <div class="edit-questionnaire__item-field__delete">
                    <img src="/static/main/images/delete.svg">
                </div>
                <div class="edit-questionnaire__item-field__recommendation">
                    <textarea name="${item_id}_${id}_recommendation" cols="30" placeholder="Рекоммендации" rows="5" class="form-control" required></textarea>
                </div>
            </div>
        `);
    });

    // add item link
    $(document).on('click', '.edit-questionnaire__add-item', function(e) {
        e.preventDefault();
        const items = $('.edit-questionnaire__items');

        const last_item = $('.edit-questionnaire__item', items).last();
        let id = 1;


        if (last_item?.length) id = Number(last_item.attr('data-item-id')) + 1;

        items.append(`
            <div class="edit-questionnaire__item block" data-item-id="${id}">
                <div class="edit-questionnaire__item-delete">
                    <img src="/static/main/images/delete.svg">
                </div>
                <div class="edit-questionnaire__item-title">
                    <label class="form-label">Название меры</label>
                    <input type="text" class="form-control" name="${id}_title" required>
                </div>
                <div class="edit-questionnaire__item-designation">
                    <label class="form-label">Обозначние меры</label>
                    <input type="text" class="form-control" name="${id}_designation" required>
                </div>
                <hr>
                <div class="edit-questionnaire__item-fields">
                    <label class="form-label">Поля меры обеспечения безопасности значимого объекта</label>
                </div>
                <hr>
                <div class="edit-questionnaire__item-add-field">
                    <a class="link-info" href="#">Добавить вопрос</a>
                </div>
            </div>`);
    });

    $('form#edit-questionnaire-form').submit(function(e) {
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
            } else {
                $('.form-alerts .form-alerts__error', th).css('display', 'block');
            }
        });

    });

}