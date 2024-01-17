-- tv_genres table contains only one record where name = Comedy (but the id can be different)
SELECT title FROM tv_shows WHERE title NOT IN (
SELECT t.title FROM tv_genres g, tv_show_genres h, tv_shows t
WHERE g.id = h.genre_id
    AND h.show_id = t.id
    AND g.name = "Comedy"
) ORDER BY title ASC;
; 
