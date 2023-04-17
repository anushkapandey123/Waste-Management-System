DELIMITER $$
CREATE TRIGGER waste_wt_more_than_limit  
BEFORE INSERT ON waste FOR EACH ROW 
BEGIN  
    DECLARE error_msg VARCHAR(255);
    SET error_msg = ('THIS IS A TRIGGER - The weight of non-biodegradable is more than the limit');
    IF NEW.non_bio_wt >= (2*NEW.bio_wt) THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
END IF;
END; $$
DELIMITER ;

/*
DELIMITER $$
CREATE TRIGGER waste_wt_morethan_limit  
BEFORE INSERT ON waste FOR EACH ROW 
BEGIN  
    DECLARE error_msg VARCHAR(255);
    SET error_msg = ('THIS IS A TRIGGER - The weight of non-biodegradable is more than the limit');
    IF NEW.non_bio_wt >= 10 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
END IF;
END; $$
DELIMITER ;
*/


























































































