-- a script that list all shows contained in hbtn_0d_tvshows without a genre
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id is NULL
ORDER BY title, genre_id;
