// fetch from url and display the value of hello

$( () => {
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data, status) {
    if (status == 'success') {
        $('DIV#hello').text(data.hello);
    }
});
});
