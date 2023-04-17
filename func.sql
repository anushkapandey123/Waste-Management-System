DELIMITER $$
CREATE FUNCTION resolved_date(res_date DATE)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE req_value VARCHAR(50);
IF res_date = "0000/00/00" THEN
SET req_value = 'Complaint Being Resolved';
ELSE IF CURRENT_DATE() > res_date THEN
SET req_value = 'Complaint Resolved';
ELSE 
SET req_value= 'Complaint Being Resolved';
END IF;
END IF;
RETURN req_value;

END; $$
DELIMITER ;

