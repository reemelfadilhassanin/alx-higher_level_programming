-- cript that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT t.title, SUM(tv_show_ratings.rate) AS "rating" FROM t AS t
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tt.id
GROUP BY t.title
ORDER BY SUM(tv_show_ratings.rate) DESC
;
