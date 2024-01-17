-- cript that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT t.title, SUM(tv_show_ratings.rate) AS "rating" FROM tv_shows AS t
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = t.id
GROUP BY t.title
ORDER BY SUM(tv_show_ratings.rate) DESC
;
