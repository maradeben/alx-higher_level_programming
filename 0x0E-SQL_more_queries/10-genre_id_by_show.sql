-- list all shows that have at least one genre linked
SELECT ts.title, tgs.genre_id
FROM tv_shows as ts
RIGHT JOIN tv_show_genres as tgs
ON ts.id = tgs.show_id
ORDER BY ts.title, tgs.genre_id;
