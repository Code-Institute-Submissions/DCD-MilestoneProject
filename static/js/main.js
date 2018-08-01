$(document).ready(function() {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.chips').chips();
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();
    $('.modal').modal();

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
            '<textarea class="materialize-textarea col s9 m10 l11" placeholder="Instruction" name="instruction_' + next + '"></textarea>' +
            '<a class="btn waves-effect waves-light red col s3 m2 l1 remove_instruction" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });

    $('#instructions_container').on('click', '.remove_instruction', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#instruction_" + deleteindex).remove();

    });
    
    $('.add_search_ingredient').click(function() {

        var last = $(".ingredient:last").attr("id");
        var split_id = last.split("_");
        var next = Number(split_id[1]) + 1;

        $(".ingredient:last").after('<div class="ingredient" id="search-ingredient_' + next + '"></div>');
        $("#search-ingredient_" + next).append(
            '<input type="text" name="ingredient_' + next + '" placeholder="Ingredient" class="col s9"/>' +
            '<a class="btn waves-effect waves-light red col s3 remove_ingredient" id="remove_' + next + '"><i class="material-icons">remove</i></a>'
        );
    });

    $('#search_ingredients_container').on('click', '.remove_ingredient', function() {
        var id = this.id;
        var split_id = id.split("_");
        var deleteindex = split_id[1];

        $("#search-ingredient_" + deleteindex).remove();

    });    
});
