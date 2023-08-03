// fetch and list title of all movies

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    if (status == 'success') {
        $.each(data.results, function(i, movie) {
            $('UL#list_movies').append('<li>' + movie.title + '</li>');
        });
    }
});
