$(document).ready(function() {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.chips-placeholder').chips({
        placeholder: 'Cuisine',
        secondaryPlaceholder: 'Enter more'
    });
    $('.tooltipped').tooltip();

    $('.add_cuisine').click(function() {

        var last = $(".cuisine:last").attr("id");
        var split_id = last.split("_");
        var next = Number(split_id[1]) + 1;

        $(".cuisine:last").after('<div class="cuisine" id="cuisine_' + next + '"></div>');
        $('#cuisine_' + next).append(
            '<input type="text" name="cuisine_' + next + '" placeholder="Cuisine" minlength="2" maxlength="20" class="col s8" required/>' +
            '<a class="btn waves-effect waves-light red remove_cuisine col s4" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });
    
     $('#cuisines_container').on('click', '.remove_cuisine', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#cuisine_" + deleteindex).remove();

    });

    $('.add_ingredient').click(function() {

        var last = $(".ingredient:last").attr("id");
        var split_id = last.split("_");
        var next = Number(split_id[1]) + 1;

        $(".ingredient:last").after('<div class="ingredient" id="ingredient_' + next + '"></div>');
        $("#ingredient_" + next).append(
            '<input type="text" name="ingredient_' + next + '" placeholder="Ingredient" class="col s6" required/>' +
            '<input type="text" name="unit_' + next + '" placeholder="Unit" class="col s3" required/>' +
            '<a class="btn waves-effect waves-light red col s3 remove_ingredient" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });

    $('#ingredients_container').on('click', '.remove_ingredient', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#ingredient_" + deleteindex).remove();

    });

    $('.add_instruction').click(function() {

        var last = $(".instruction:last").attr("id");
        var split_id = last.split("_");
        var next = Number(split_id[1]) + 1;

        $(".instruction:last").after('<div class="instruction" id="instruction_' + next + '"></div>');
        $("#instruction_" + next).append(
            '<textarea class="materialize-textarea col s10" placeholder="Instruction" name="instruction_' + next + '"></textarea>' +
            '<a class="btn waves-effect waves-light red col s2 remove_instruction" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });

    $('#instructions_container').on('click', '.remove_instruction', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#instruction_" + deleteindex).remove();

    });
    
    $('.collapsible').collapsible();
    $('.modal').modal();
});
