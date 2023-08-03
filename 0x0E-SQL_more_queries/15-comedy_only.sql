-- list only comedies
SELECT ts.title as title
FROM tv_shows as ts
INNER JOIN tv_show_genres as tgs
ON ts.id = tgs.show_id
INNER JOIN tv_genres as tg
ON tgs.genre_id = tg.id
WHERE name = 'Comedy'
ORDER BY title;
