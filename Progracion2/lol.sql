-- Create a new table called 'champions'
CREATE TABLE champions (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    attack_damage INT,
    ability_power INT
);

-- Insert some sample data into the 'champions' table
INSERT INTO champions (id, name, role, attack_damage, ability_power) VALUES
(1, 'Ahri', 'Mage', 53, 0),
(2, 'Garen', 'Fighter', 66, 0),
(3, 'Ashe', 'Marksman', 61, 0),
(4, 'Lux', 'Mage', 54, 0),
(5, 'Lee Sin', 'Fighter', 70, 0);

-- Select all data from the 'champions' table
SELECT * FROM champions;