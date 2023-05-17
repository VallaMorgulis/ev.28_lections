# task 1

# SELECT plaintext FROM wordform LIMIT 10;

# task 2

# SELECT plaintext FROM wordform WHERE plaintext LIKE 'a%'

# task 3

# SELECT title, genretype FROM work WHERE genretype = 'p'

# task 4

# SELECT avg(totalparagraphs) FROM work WHERE genretype = 't';

# task 5

# SELECT title FROM work WHERE totalwords > (SELECT AVG(totalwords) FROM work);

# task 6

# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid = character_work.charid LEFT JOIN work ON character_work.workid = work.workid

# task 7

# SELECT ROUND(avg(speechcount)), work.title FROM character JOIN character_work ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid WHERE work.title = 'Romeo and Juliet' GROUP BY work.title;

# task 8

