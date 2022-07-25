-- mysql -P 33306 -u editUser -h 127.0.0.1 -p sampledb
SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;
create database sampledb;
-- create user editUser@'%' identified by 'Password';
GRANT all on sampledb.* TO `editUser`@'%' IDENTIFIED BY 'Password';
GRANT all on sampledb.* TO `editUser`@'localhost' IDENTIFIED BY 'Password';
-- SELECT user,host FROM mysql.user;
-- grant all on itms.* to itmsUser;
use sampledb;

-- data
CREATE TABLE t_samplelist (
    id int PRIMARY KEY AUTO_INCREMENT,  -- プライマーキー
    itemName VARCHAR(64) NOT NULL, -- 商品名
    quantity VARCHAR(64) NOT NULL, -- 数量
    flag int NOT NULL -- 削除フラッグ(0:有効,1:削除+パスワード空白)
);
INSERT INTO t_samplelist VALUES (1,'スイカ','1個',0);
INSERT INTO t_samplelist VALUES (2,'トマト','２個',0);
INSERT INTO t_samplelist VALUES (3,'きゅうり','10本',0);
SELECT * FROM t_samplelist;