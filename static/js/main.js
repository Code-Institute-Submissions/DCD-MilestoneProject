$(document).ready(function() {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.chips-placeholder').chips({
        placeholder: 'Cuisine',
        secondaryPlaceholder: 'Enter more'
    });
    $('.tooltipped').tooltip();

    $('.add_ingredient').click(function() {

        var last = $(".ingredient:last").attr("id");
        var split_id = last.split("_");
        var next = Number(split_id[1]) + 1;

        $(".ingredient:last").after('<div class="ingredient" id="ingredient_' + next + '"></div>');
        $("#ingredient_" + next).append(
            '<input type="text" name="ingredient_' + next + '" placeholder="Ingredient" class="col s7" required pattern="\S+" title="No preceding and ending white spaces" />' +
            '<input type="text" name="unit_' + next + '" placeholder="Unit" class="col s3" required pattern="\S+" title="No preceding and ending white spaces" />' +
            '<a class="btn waves-effect waves-light red col s2 remove_ingredient" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });

    $('#ingredients_container').on('click', '.remove_ingredient', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#ingredient_" + deleteindex).remove();

    });
});
