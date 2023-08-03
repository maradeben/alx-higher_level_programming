-- list all shows
SELECT ts.title, tgs.genre_id
FROM tv_shows as ts
LEFT JOIN tv_show_genres as tgs
ON ts.id = tgs.show_id
WHERE tgs.genre_id IS NULL
ORDER BY ts.title, tgs.genre_id;
