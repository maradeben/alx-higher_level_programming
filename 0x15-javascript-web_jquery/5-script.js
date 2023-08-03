// add a <li> when DIV#add_item clicked

$('DIV#add_item').click(function() {
    $('UL.my_list').append("<li>Item</li>");
});