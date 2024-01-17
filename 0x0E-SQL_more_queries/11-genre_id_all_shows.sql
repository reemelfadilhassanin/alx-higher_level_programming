-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.title , t.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS t
ON tv_show_genres.show_id = tv_shows.id
    ORDER BY tv_shows.title, tv_show_genres.genre_id;
