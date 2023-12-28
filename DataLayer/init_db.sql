-- init_db.sql
CREATE TABLE IF NOT EXISTS Currency (
    Country TEXT,
    Name TEXT,
    Abbreviation TEXT
);

CREATE TABLE IF NOT EXISTS CurrencyPair (
    Pair TEXT,
    MinValue REAL,
    MaxValue REAL
);

INSERT INTO Currency (Country, Name, Abbreviation) VALUES
    ('United States', 'Dollar', 'USD'),
    ('Eurozone', 'Euro', 'EUR'),
    ('Japan', 'Yen', 'JPY'),
    ('Israel', 'Shekel', 'ILS');

INSERT INTO CurrencyPair (Pair, MinValue, MaxValue) VALUES
    ('USD/EUR', 1.1, 1.2),
    ('USD/JPY', 100, 110),
    ('USD/ILS', 3.5, 3.8);
