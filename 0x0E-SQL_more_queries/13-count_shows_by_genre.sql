-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS v
       ON v.`id` = s.`show_id`
       WHERE v.`title` = "Dexter"
 ORDER BY g.`name`
