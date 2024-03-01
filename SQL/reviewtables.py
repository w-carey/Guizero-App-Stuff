sqlCode = ["""
CREATE TABLE "bnb_user" (
	"user_id"			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_forename"		TEXT,
	"user_surname"		TEXT,
	"user_name"			TEXT,
	"user_password"		TEXT,
	"user_type"			INTEGER,
	"user_created"		TEXT
);
CREATE TABLE "bnb_product" (
	"product_id"		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"product_name"		INTEGER,
    "product_price"		INTEGER,       
    "product_category"	TEXT       
);
CREATE TABLE "bnb_order" (
	"order_id"			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "order_userid"		INTEGER,
    "order_productid"	INTEGER,
	"order_date"		TEXT,
	"order_status"		INTEGER, 
	CONSTRAINT "useridfk"  FOREIGN KEY("order_userid") REFERENCES "bnb_user"("user_id"),
    CONSTRAINT "productidfk"  FOREIGN KEY("order_productid") REFERENCES "bnb_product"("product_id")       
);
CREATE TABLE "bnb_review" (
	"review_id"			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "review_orderid"	INTEGER,
    "review_stars"		INTEGER,
    "review_text"		TEXT,    
	CONSTRAINT "orderidfk"  FOREIGN KEY("review_orderid") REFERENCES "bnb_order"("order_id")
);
"""]
