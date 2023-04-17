DELIMITER $$
CREATE FUNCTION organic_user(bio FLOAT, non_bio FLOAT)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE req_value VARCHAR(50);
IF bio >= non_bio THEN
SET req_value = 'Good, the citizen generates more bio-degradable waste';
ELSE IF bio < non_bio THEN
SET req_value = 'Bad, the citizen generates more non-biodegradable waste';
END IF;
END IF;
RETURN req_value;

END; $$
DELIMITER ;

