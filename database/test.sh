docker exec -it <db container id> bash
mysql -u root -p <root password>

USE titanic_db;
select * from passengers;