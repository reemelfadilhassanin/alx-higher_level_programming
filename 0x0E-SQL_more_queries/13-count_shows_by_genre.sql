-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
    AND t.show_id = s.id
    AND s.title = "Dexter"
ORDER BY g.name ASC;
; 
