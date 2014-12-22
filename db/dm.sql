
CREATE SEQUENCE public.rl_dim_num_floors_id_seq_1;

CREATE TABLE public.dim_num_floors (
                id_num_floors INTEGER NOT NULL DEFAULT nextval('public.rl_dim_num_floors_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_num_floors_pk PRIMARY KEY (id_num_floors)
);


ALTER SEQUENCE public.rl_dim_num_floors_id_seq_1 OWNED BY public.dim_num_floors.id_num_floors;

CREATE SEQUENCE public.rm_dim_num_bathrooms_id_seq_1;

CREATE TABLE public.dim_num_bathrooms (
                id_num_bathroom INTEGER NOT NULL DEFAULT nextval('public.rm_dim_num_bathrooms_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_num_bathrooms_pk PRIMARY KEY (id_num_bathroom)
);


ALTER SEQUENCE public.rm_dim_num_bathrooms_id_seq_1 OWNED BY public.dim_num_bathrooms.id_num_bathroom;

CREATE SEQUENCE public.rl_dim_num_bedrooms_id_seq_1;

CREATE TABLE public.dim_num_bedrooms (
                id_num_bedrooms INTEGER NOT NULL DEFAULT nextval('public.rl_dim_num_bedrooms_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_num_bedrooms_pk PRIMARY KEY (id_num_bedrooms)
);


ALTER SEQUENCE public.rl_dim_num_bedrooms_id_seq_1 OWNED BY public.dim_num_bedrooms.id_num_bedrooms;

CREATE SEQUENCE public.rl_dim_agent_name_id_seq_1;

CREATE TABLE public.dim_agent_name (
                id_agent_name INTEGER NOT NULL DEFAULT nextval('public.rl_dim_agent_name_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_agent_name_pk PRIMARY KEY (id_agent_name)
);


ALTER SEQUENCE public.rl_dim_agent_name_id_seq_1 OWNED BY public.dim_agent_name.id_agent_name;

CREATE SEQUENCE public.rl_dim_property_type_id_seq_1;

CREATE TABLE public.dim_property_type (
                id_property_type INTEGER NOT NULL DEFAULT nextval('public.rl_dim_property_type_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_property_type_pk PRIMARY KEY (id_property_type)
);


ALTER SEQUENCE public.rl_dim_property_type_id_seq_1 OWNED BY public.dim_property_type.id_property_type;

CREATE SEQUENCE public.rl_dim_price_range_id_seq_1;

CREATE TABLE public.dim_price_range (
                id_price_range INTEGER NOT NULL DEFAULT nextval('public.rl_dim_price_range_id_seq_1'),
                name VARCHAR NOT NULL,
                CONSTRAINT dim_price_range_pk PRIMARY KEY (id_price_range)
);


ALTER SEQUENCE public.rl_dim_price_range_id_seq_1 OWNED BY public.dim_price_range.id_price_range;

CREATE SEQUENCE public.fact_rent_house_id_seq;

CREATE TABLE public.fact_rent_house (
                id INTEGER NOT NULL DEFAULT nextval('public.fact_rent_house_id_seq'),
                listing_id VARCHAR NOT NULL,
                id_num_floors INTEGER,
                id_num_bathroom INTEGER,
                id_price_range INTEGER,
                id_property_type INTEGER,
                id_agent_name INTEGER,
                id_num_bedrooms INTEGER,
                CONSTRAINT fact_rent_house_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.fact_rent_house_id_seq OWNED BY public.fact_rent_house.id;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rl_dim_num_floors_rl_fact_rent_house_fk
FOREIGN KEY (id_num_floors)
REFERENCES public.dim_num_floors (id_num_floors)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rm_dim_num_bathrooms_rl_fact_rent_house_fk
FOREIGN KEY (id_num_bathroom)
REFERENCES public.dim_num_bathrooms (id_num_bathroom)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rl_dim_num_bedrooms_rl_fact_rent_house_fk
FOREIGN KEY (id_num_bedrooms)
REFERENCES public.dim_num_bedrooms (id_num_bedrooms)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rl_dim_agent_name_rl_fact_rent_house_fk
FOREIGN KEY (id_agent_name)
REFERENCES public.dim_agent_name (id_agent_name)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rl_dim_property_type_rl_fact_rent_house_fk
FOREIGN KEY (id_property_type)
REFERENCES public.dim_property_type (id_property_type)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.fact_rent_house ADD CONSTRAINT rl_dim_price_range_rl_fact_rent_house_fk
FOREIGN KEY (id_price_range)
REFERENCES public.dim_price_range (id_price_range)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
