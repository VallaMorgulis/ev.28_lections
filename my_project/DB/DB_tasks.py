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

# SELECT c.charname, c.speechcount, w.title FROM character AS c LEFT JOIN character_work AS cw ON c.charid = cw.charid LEFT JOIN work AS w ON cw.workid = w.workid

# task 7

# SELECT ROUND(avg(speechcount)), w.title FROM character AS c LEFT JOIN character_work AS cw ON c.charid = cw.charid LEFT JOIN work AS w ON cw.workid = w.workid WHERE title = 'Romeo and Juliet' GROUP BY w.title;;

# task 8

# SELECT section, SUM(wordcount) AS sum FROM paragraph GROUP BY section;

# task 9

# SELECT charname, speechcount FROM character WHERE speechcount > 14 AND speechcount < 31;

# task 10

# SELECT title, year FROM work WHERE year > 1600 AND year < 1700;

# task 11

# SELECT longtitle FROM work WHERE longtitle LIKE '%the%';

# task 12

# SELECT DISTINCT section FROM paragraph;

# task 13

# SELECT c.chapterid, c.description, w.title FROM chapter AS c JOIN work AS w ON c.workid = w.workid

# task 14

# SELECT p.paragraphnum, c.charname, c.speechcount FROM character AS c JOIN paragraph AS p ON c.charid = p.charid;

# task 15

# SELECT p.paragraphnum, w.title, w.year FROM work AS w JOIN paragraph AS p ON w.workid = p.workid


# 1. Вытащить все произведения в котрых sourse = Moby и кол-во параграфов меньше 100
# SELECT source, totalparagraphs FROM work WHERE source = 'Moby' AND totalparagraphs < 100; 



# 2. Найти кол-во глав в каждом произведении
# select count(*), work.title from chapter join work on work.workid = chapter.workid group by work.title order by count(*) desc;

# 3. Найти сколько произведений относятся к каждому 
# select count(*), genretype from work group by genretype;

# 4. Найти кол-во параграфов в каждом произведении и вытащить названия произведений
# select count(*), work.title from paragraph join work on work.workid = paragraph.workid group by work.title;


# 5. Вытащить имена героев, чьи реплики состовляют больше 200 слов, также произведения в которых они встречаються, жанр, год выхода произдведения в порядке убывания
# select character.charname, work.title, work.genretype, work.year from character_work join character on character.charid = character_work.charid join work on work.workid = character_work.workid where character.speechcount > 200 order by work.year desc;


# 6. Вытащить героя, который чаще всех появляется в произведениях
# SELECT character.charname, COUNT(*) AS works_count FROM character_work JOIN character
# ON character.charid = character_work.charid JOIN work ON character_work.workid = work.workid
# GROUP BY character.charname ORDER BY works_count DESC LIMIT 1;
