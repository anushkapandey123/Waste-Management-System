delimiter //
CREATE PROCEDURE totalwaste(IN wid VARCHAR(25), OUT tot_wt FLOAT)
       BEGIN
         SELECT (non_bio_wt+bio_wt) INTO tot_wt FROM waste
         WHERE w_id = wid;
       END//
delimiter ;
