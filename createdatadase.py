import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="basimehsan"
)

mycursor = mydb.cursor()

createdb="create database cs_220;"
usedb=" use cs_220;"
createlawyer = """
    create table lawyer(
	lawyer_id int,
	fname varchar(10),
	lname varchar(10),
	specialization varchar(10),
	years_of_experience INT,
	phone VARCHAR(15),
	email varchar(20),
	PRIMARY KEY (lawyer_id)
);"""

createjudge = """
    create table judge(
	judge_id int,
	fname varchar(10),
	lname varchar(10),
	years_of_experience INT,
	phone VARCHAR(15),
	email varchar(20),
	PRIMARY KEY (judge_id)
);"""

createplaintiff="""create table plaintiff(
	plaintiff_id int,
	name varchar(10),
	phone VARCHAR(15),
	email varchar(20),
	PRIMARY KEY (plaintiff_id)
);"""

createdefendant="""create table defendant(
	defendant_id int,
	name varchar(10),
	phone VARCHAR(15),
	email varchar(20),
	PRIMARY KEY (defendant_id)
);"""
createcourt="""
    create table court(
	court_id int,
	name VARCHAR(20),
	addr_city VARCHAR(10),
	addr_district VARCHAR(10),
	addr_street VARCHAR(25),
	status varchar(10),
	PRIMARY KEY (court_id)
);"""

createcase="""
    create table kase(
	case_id int,
    year int,
    type VARCHAR(20),
    description varchar(45),
    plaintiff_id int ,
    defendant_id int ,
    judge_id int,
    prosecution_id int,
    court_id int,
    verdict VARCHAR(45),
	PRIMARY KEY (case_id),
    FOREIGN KEY (judge_id) REFERENCES judge(judge_id),
    FOREIGN KEY (court_id) REFERENCES court(court_id),
    FOREIGN KEY (prosecution_id) REFERENCES lawyer(lawyer_id),
	FOREIGN KEY (plaintiff_id) REFERENCES plaintiff(plaintiff_id),
    FOREIGN KEY (defendant_id) REFERENCES defendant(defendant_id)
);"""


mycursor.execute(createdb)
mycursor.execute(usedb)
mycursor.execute(createlawyer)
mycursor.execute(usedb)
mycursor.execute(createjudge)
mycursor.execute(usedb)
mycursor.execute(createplaintiff)
mycursor.execute(usedb)
mycursor.execute(createdefendant)
mycursor.execute(usedb)
mycursor.execute(createcourt)
mycursor.execute(usedb)
mycursor.execute(createcase)

mydb.commit()

