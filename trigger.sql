DELIMITER $$
CREATE TRIGGER waste_wt_less_than_0  
BEFORE INSERT ON waste FOR EACH ROW 
BEGIN  
    DECLARE error_msg VARCHAR(255);
    SET error_msg = ('THIS IS A TRIGGER - The weight cannot be less than 0');
    IF NEW.non_bio_wt < 0 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
END IF;
END; $$
DELIMITER ;