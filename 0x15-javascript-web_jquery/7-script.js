// fetch name from JSON, and display

// const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data, status) {
    if (status == 'success') {
        $('DIV#character').text(data['name']);
    }
});
