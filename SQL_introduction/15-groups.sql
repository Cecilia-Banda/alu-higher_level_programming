-- script that lists the number of records with the same score --
-- in the second_table table of the hbtn_0c_0 database on your MySQL server --
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
