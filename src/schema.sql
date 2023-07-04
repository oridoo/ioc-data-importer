CREATE TABLE IF NOT EXISTS sources
(
  id smallserial NOT NULL CONSTRAINT sources_pkey PRIMARY KEY,
  url text,
  name text
);

CREATE TABLE IF NOT EXISTS ip_addresses
(
  id serial NOT NULL CONSTRAINT ip_addresses_pkey PRIMARY KEY,
  source smallint NOT NULL CONSTRAINT ip_addresses_source_fkey REFERENCES sources (id),
  address varchar(16) NOT NULL
);

CREATE TABLE IF NOT EXISTS urls
(
  id serial NOT NULL CONSTRAINT urls_pkey PRIMARY KEY,
  source smallint NOT NULL CONSTRAINT urls_source_fkey REFERENCES sources (id),
  url text NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS urls_url_idx
  on urls (source, url);

CREATE UNIQUE INDEX IF NOT EXISTS ip_addresses_address_idx
  on ip_addresses (source, address);