sqlCode = ["""
CREATE TABLE "gibjohn_user" (
	"user_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_forename" TEXT,
	"user_surname" TEXT,
	"user_name"	TEXT,
	"user_password"	TEXT,
	"user_type" INTEGER,
	"user_points" INTEGER,
	"user_classroomid" INTEGER,
	CONSTRAINT "classroomFK"  FOREIGN KEY("user_classroomid") REFERENCES "gibjohn_classroom"("classroom_id")
);
CREATE TABLE "gibjohn_quiz" (
	"quiz_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"quiz_classroomid" INTEGER,
	"quiz_setdate" TEXT,
	"quiz_duedate" TEXT,
	"quiz_data" TEXT,
	CONSTRAINT "classroomFK"  FOREIGN KEY("quiz_classroomid") REFERENCES "gibjohn_classroom"("classroom_id")
);
CREATE TABLE "gibjohn_results" (
	"results_id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"results_quizid" INTEGER,
	"results_date" TEXT,
	"results_data" TEXT,
	"results_userid" INTEGER,
	CONSTRAINT "quizFK"  FOREIGN KEY("results_quizid") REFERENCES "gibjohn_quiz"("quiz_id")
);
CREATE TABLE "gibjohn_classroom" (
	"classroom_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"classroom_joinrequests" TEXT
);
"""]
