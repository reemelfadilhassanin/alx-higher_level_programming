-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name NOT IN (
SELECT g.name FROM tv_genres g, tv_show_genres v, tv_shows t
WHERE g.id = v.genre_id
    AND v.show_id =t.id
    AND t.title = "Dexter"
) ORDER BY tv_genres.name;
