-- Find Customer Referee, solved Nov 5 2024
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL
