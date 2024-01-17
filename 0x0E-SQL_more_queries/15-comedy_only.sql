-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT v.title FROM tv_genres t, tv_show_genres t, tv_shows v
WHERE t.id = t.genre_id
    AND t.show_id = v.id
    AND t.name = "Comedy"
ORDER BY v.title ASC;
; 
