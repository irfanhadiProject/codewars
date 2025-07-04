--# write your SQL statement here: 
-- you are given a table 'participants' with column 'n' (number of handshakes).
-- return a table with this column and your result in a column named 'res'.
SELECT n,
(
  SELECT MIN(p)
  FROM generate_series(0, 1000) AS p
  WHERE p * (p - 1) / 2 >= participants.n
) AS res
FROM participants;