CREATE DATABASE stock_data;

CREATE TABLE    stock_tickers (
    ticker VARCHAR(10),
    company_name VARCHAR(255),
    market VARCHAR(50),
    locale VARCHAR(10),
    primary_exchange VARCHAR(100),
    type VARCHAR(50),
    active BOOLEAN,
    currency_name VARCHAR(50),
    cik VARCHAR(20),
    composite_figi VARCHAR(20),
    share_class_figi VARCHAR(20),
    last_updated_utc TIMESTAMP
);

/* After executing script.py, the table will be populated with data */
SELECT * FROM stock_tickers;

/* Datasets almost always have a timestamp column to track when the data was last updated */
 ALTER TABLE stock_tickers
    ADD COLUMN ds DATE;