CREATE TABLE warehouse_distances(
	distance_id bigserial NOT NULL
	  constraint warehouse_distnaces_pkey
	    PRIMARY KEY,
	x1 FLOAT8 NOT NULL,
	y1 FLOAT8 NOT NULL,
	x2 FLOAT8 NOT NULL, 
	y2 FLOAT8 NOT NULL,
	distance_m FLOAT8 NULL,
	warehouses_fk BIGINT NOT NULL,

	FOREIGN KEY (warehouses_fk) REFERENCES warehouses(warehouse_id)
	  ON DELETE CASCADE
);