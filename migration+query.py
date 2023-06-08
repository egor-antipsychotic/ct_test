import psycopg2

# конфиг нужен рабочий
conn = psycopg2.connect(
    host="host",
    database="database",
    user="user",
    password="password")

table_create_query = """CREATE TABLE article (
                        id        integer CONSTRAINT articlekey PRIMARY KEY,
                        title       varchar(255) NOT NULL,
                        text         text NOT NULL
                    );


                        CREATE TABLE comment (
                        id        integer CONSTRAINT commentkey PRIMARY KEY,
                        article_id integer NOT NULL,
                        text         text NOT NULL
                    );"""

table_fill_query = """INSERT INTO article (id, title, text) VALUES (1, 'Phasellus gravida eu ante et imperdiet', 'Mauris rutrum augue risus, sodales maximus neque vulputate a. Curabitur porttitor, risus eu fermentum hendrerit, urna est dictum est, quis condimentum lectus nisi eget diam.');
                      INSERT INTO article (id, title, text) VALUES (2, 'Maecenas egestas fermentum rutrum', 'Vivamus varius nibh et iaculis mollis. Phasellus eu massa a libero eleifend scelerisque. Nulla molestie justo libero, ac aliquet mi iaculis eget.');
                      INSERT INTO article (id, title, text) VALUES (3, 'Nam vestibulum dignissim volutpat', 'Praesent neque lectus, porttitor et nunc vitae, congue semper felis. Pellentesque convallis facilisis odio id fringilla. Vivamus quis nibh felis.');
                      INSERT INTO article (id, title, text) VALUES (4, 'Phasellus augue ipsum, rutrum a imperdiet', 'Praesent in turpis ac nisl pellentesque volutpat. Maecenas vitae viverra ipsum. Proin accumsan diam vitae nulla tincidunt, a mollis diam luctus.');
                      INSERT INTO article (id, title, text) VALUES (5, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit', 'Integer eget urna porttitor, dictum quam quis, cursus tellus. Pellentesque dictum accumsan mauris a pulvinar.');

                      INSERT INTO comment (id, article_id, text) VALUES (1, 1, 'Nunc ac arcu non lectus bibendum mattis. Suspendisse suscipit, enim sit amet ultrices laoreet, dolor dui rhoncus quam');
                      INSERT INTO comment (id, article_id, text) VALUES (2, 1, 'Aenean cursus a sapien ac malesuada');
                      INSERT INTO comment (id, article_id, text) VALUES (3, 1, 'Fusce sit amet lacus dignissim, tempus massa sed, ultricies dolor');
                      INSERT INTO comment (id, article_id, text) VALUES (4, 4, 'Phasellus non urna commodo, finibus lectus ac, gravida lectus');
                      INSERT INTO comment (id, article_id, text) VALUES (5, 4, 'Suspendisse pretium porttitor iaculis. Nulla in tortor vel est lobortis fermentum');
                      INSERT INTO comment (id, article_id, text) VALUES (6, 4, 'Etiam gravida vehicula massa non condimentum');
                      INSERT INTO comment (id, article_id, text) VALUES (7, 4, 'Etiam rutrum purus a ipsum viverra laoreet. Nunc aliquet ex vitae tincidunt luctus');
                      INSERT INTO comment (id, article_id, text) VALUES (8, 4, 'Sed facilisis fermentum lacus, non semper est sodales sed.');
                      INSERT INTO comment (id, article_id, text) VALUES (9, 5, 'Integer vitae ipsum auctor, interdum leo eu, facilisis dui. Suspendisse ut feugiat dolor, in ultrices leo');"""

# ответ на задачу
answer_query = """SELECT
                  article.id, article.title, article.text
                  FROM article
                  LEFT JOIN comment ON article.id == comment.article_id
                  WHERE comment.article_id IS NULL
                  """


def create():
    with conn.cursor() as cursor:
        cursor.execute(table_create_query)


def fill():
    with conn.cursor() as cursor:
        cursor.execute(table_fill_query)


def answer():
    with conn.cursor() as cursor:
        cursor.execute(answer_query)


if __name__ == '__main__':
    create()
    fill()
    answer()
