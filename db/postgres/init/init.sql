--ユーザーの作成
CREATE USER docker;
--DBの作成
CREATE DATABASE docker;
--ユーザーにDBの権限をまとめて付与
GRANT ALL PRIVILEGES ON DATABASE docker TO docker;

-- GRANT ALL PRIVILEGES ON my_db.* TO 'admin'@'%';
-- GRANT ALL PRIVILEGES ON test_docker.* TO 'user'@'%';

-- postgresではFLUSH PRIVILEGESは不要だが、他のdbでは必須の場合が多い。念のため記載しておく。
FLUSH PRIVILEGES;

--ユーザーを切り替え
\c docker
--テーブルを作成
CREATE TABLE book (
  id integer, 
  name varchar(30)
);
--テーブルにデータを挿入
INSERT INTO book VALUES (1,'The Very Hungry Caterpillar');