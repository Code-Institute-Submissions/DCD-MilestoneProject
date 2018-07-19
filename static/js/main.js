$(document).ready(function() {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.chips-placeholder').chips({
        placeholder: 'Cuisine',
        secondaryPlaceholder: 'Enter more'
    });
    $('.tooltipped').tooltip();
})