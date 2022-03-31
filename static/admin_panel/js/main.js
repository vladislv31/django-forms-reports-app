$(document).ready(function() {

    edit_questionnaire();
    edit_determine_questionnaire();

});

function edit_determine_questionnaire() {

    // delete item button
    $(document).on('click', '.edit-determine-questionnaire__delete-item', function(e) {
        e.preventDefault();

        const th = $(this);
        const item = th.closest('.edit-determine-questionnaire__item');

        item.remove();
    });

    // delete subitem button
    $(document).on('click', '.edit-determine-questionnaire__delete-subitem', function(e) {
        e.preventDefault();

        const th = $(this);
        const subitem = th.closest('.edit-determine-questionnaire__item-question');

        subitem.remove();
    });

    // delete question button
    $(document).on('click', '.edit-determine-questionnaire__delete-question', function(e) {
        e.preventDefault();

        const th = $(this);
        const ques = th.closest('.edit-determine-questionnaire__item-ques');

        ques.remove();
    });

    // add item link
    $(document).on('click', '.edit-determine-questionnaire__add-item', function(e) {
        e.preventDefault();
        const items = $('.edit-determine-questionnaire__items');

        const last_item = $('.edit-determine-questionnaire__item', items).last();
        let id = 1;

        if (last_item?.length) id = Number(last_item.attr('data-item-id')) + 1;

        items.append(`
            <div class="edit-determine-questionnaire__item" data-item-id="${id}">
                <p><label>Название значимости</label></p>
                <p><input type="text" class="form-control" name="${id}_significance" required></p>
                <a href="#" class="link link-danger edit-determine-questionnaire__delete-item">Удалить значимость</a>
                <hr>
                <div class="edit-determine-questionnaire__item-questions"></div>
                <a href="#" class="link edit-determine-questionnaire__add-question">Добавить вопрос</a>
            </div>`);
    });

    // add question link
    $(document).on('click', '.edit-determine-questionnaire__add-question', function(e) {
        e.preventDefault();

        const th = $(this);
        const item = th.closest('.edit-determine-questionnaire__item');
        const item_questions = $('.edit-determine-questionnaire__item-questions', item);

        const last_item = $('.edit-determine-questionnaire__item-ques', item_questions).last();
        let id = 1;

        if (last_item?.length) id = Number(last_item.attr('data-subitem-id')) + 1;

        const item_id = item.attr('data-item-id');

        item_questions.append(`
            <div class="edit-determine-questionnaire__item-ques" data-subitem-id="${id}">
                <p><textarea class="form-control" name="${item_id}_${id}_indicator" placeholder="Показатель" required></textarea></p>
                <a href="#" class="link-danger edit-determine-questionnaire__delete-question">Удалить вопрос</a>
                <p>Подвопросы:</p>
                <div class="edit-determine-questionnaire__item-variants">
                </div>
                <a href="#" class="link edit-determine-questionnaire__add-subitem">Добавить подвопрос</a>
            </div>`);

    });

    // add subitem link
    $(document).on('click', '.edit-determine-questionnaire__add-subitem', function(e) {
        e.preventDefault();

        const th = $(this);
        const ques = th.closest('.edit-determine-questionnaire__item-ques');
        const subitem_variants = $('.edit-determine-questionnaire__item-variants', ques);

        const last_item = $('.edit-determine-questionnaire__item-question', subitem_variants).last();
        let id = 1;

        if (last_item?.length) id = Number(last_item.attr('data-question-id')) + 1;

        const subitem_id = ques.attr('data-subitem-id');
        const item_id = ques.closest('.edit-determine-questionnaire__item').attr('data-item-id');

        subitem_variants.append(`
            <div class="block edit-determine-questionnaire__item-question" data-question-id="${id}">
                <label>Название вопроса:</label>
                <textarea class="form-control" name="${item_id}_${subitem_id}_${id}_title"></textarea>
                <label>Для первой категории:</label>
                <textarea class="form-control" name="${item_id}_${subitem_id}_${id}_first_cat_question" required></textarea>
                <label>Для второй категории:</label>
                <textarea class="form-control" name="${item_id}_${subitem_id}_${id}_second_cat_question" required></textarea>
                <label>Для третьей категории:</label>
                <textarea class="form-control" name="${item_id}_${subitem_id}_${id}_third_cat_question" required></textarea>
                <label>Для без категории:</label>
                <textarea class="form-control" name="${item_id}_${subitem_id}_${id}_no_cat_question" required></textarea>
                <a href="#" class="link link-danger edit-determine-questionnaire__delete-subitem">Удалить подвопрос</a>
            </div>`);

    });

    $('form#edit-determine-questionnaire-form').submit(function(e) {
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