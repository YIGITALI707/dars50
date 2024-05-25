-- create table files_documents(
-- 	id integer,
-- 	original_name varchar(255),
-- 	filename varchar(255),
-- 	extensions varchar(10),
-- 	language_id integer,
-- 	files_id integer references product_files(id)
-- );
-- create table product_files(
-- 	id integer,
-- 	file_id integer,
-- 	product_id integer,
-- 	positions integer
-- );



-- create table files_images(
-- 	id integer,
-- 	original_name varchar(255),
-- 	filename varchar(255),
-- 	extensions varchar(10),
-- 	products_id integer references product_images(id)
-- );
-- create table product_images(
-- 	id integer,
-- 	image_id integer,
-- 	product_id integer,
-- 	positions integer
-- 	categories_id integer references products(id)
-- );
-- create table products(
-- 	id integer,
-- 	name varchar(45),
-- 	date_added int(10),
-- 	date_updated int(10),
-- 	display int(1),
-- 	category_id int(5),
-- 	deleted int(1)
-- );




create table product_videos(
	id integer,
	video_id integer,
	source_id integer,
	url_code varchar(255)
	product_id integer references files_videos(id)
);
create table files_videos(
	id integer,
	original_name varchar(255),
	filename varchar(255),
	extensions varchar(10)
);










