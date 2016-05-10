USE [master]
GO

/****** Object:  Schema [SQL Drill 1]    Script Date: 3/4/2016 12:15:16 PM ******/
CREATE SCHEMA [SQL Drill 1]
GO


CREATE TABLE Book
(BookId int PRIMARY KEY,
Title varchar(30) NOT NULL,
Publisher_Name varchar(30) NULL
)

SELECT * FROM Book

INSERT INTO Book
VALUES (1, 'The Lost Tribe', 'Pocket Books')

INSERT INTO Book
VALUES (2, 'I am America', 'Grand Central Publishing'),
(3, 'I Still Miss My Man But..', 'Pocket Books')

INSERT INTO Book
VALUES (4, 'The Grapes of Wrath', 'Penguin Books'),
(5,'Brave New World', 'Harper Perennial'),
(6, 'The Catcher in the Rye', 'Back Bay Books'),
(7, 'Of Mice and Men', 'Penguin Books')

INSERT INTO Book
VALUES (8, 'To Kill a Mockingbird', 'Harper Perennial'),
(9, 'The Unbearable Lightness...', 'Penguin Books'),
(10, 'The Perks of Being...', 'MTV Books'),
(11, 'Me Talk Pretty One Day', 'Little, Brown, and Co'),
(12, 'The Devil Wears Prada', 'Anchor Books'),
(13, 'Catch 22', 'Simon & Schuster'),
(14, 'Even God is Single', 'Workman Publishing')

INSERT INTO Book
VALUES (15, 'A Streetcar Named Desire', 'Dramatists Play Services'),
(16, 'The Heart is a Lonely Hunter', 'Mariner Books'),
(17, 'Atlas Shrugged', 'Berkley'),
(18, 'Girl Interrupted', 'Vintage'),
(19, 'The Lovely Bones', 'Random House'),
(20, 'Carrie', 'Random House')

CREATE TABLE Publisher
(Name varchar(30) PRIMARY KEY,
[Address] varchar(50) NOT NULL,
Phone varchar(30) NULL
)

SELECT * FROM Publisher

INSERT INTO Publisher
VALUES ('Pocket Books', '456 First Ave, New York, NY 10001', '(123) 456-8795'),
('Grand Central Publishing', '789 Grand Ave, New York, NY 10001', '(789) 156-7896'),
('Penguin Books', '859 Penguin Ave, New York, NY 10005', '(785) 569-8952'),
('Harper Prennial', '8890 Harper Ave, New York, NY 15987', '(125) 895-8964'),
('Back Bay Books', '483 Back Ave, New York, NY 10004', '(888) 859-9874'),
('MTV Books', '493 MTV Ave, New York, NY 45687', '(458) 895-7894'),
('Little, Brown and Co', '4568 Brown Ave, Boston, MA 78941', '(458) 521-2587'),
('Anchor Books', '8741 Anchor Ave, New York, NY 99512', '(452) 562-8963'),
('Simon & Schuster', '888 Simon Ave, New York, NY 10005', '(478) 859-8025'),
('Workman Publishing', '483 Workman Rd, New York, NY 47852', '(458) 456-2017'),
('Dramatists Play Service', '4567 Play Ave, New York, NY 10005', '(852) 569-4895'),
('Mariner Books', '472 Mariner Ave, Boston, MA 10007', '(777) 429-9058'),
('Berkley', '954 Berkley Rd, Berkley, CA 97458', '(798) 415-7896'),
('Vintage', '7898 Vintage Ave, Boston, MA 58912', '(456) 562-8256'),
('Random House', '789 Random Rd., New York, NY 10008', '(789) 589-8952')

CREATE TABLE Book_Authors
(BookID int NOT NULL,
AuthorName varchar(50) NOT NULL
)

SELECT * FROM Book_Authors

INSERT INTO Book_Authors
VALUES (1, 'Edward Marriott'),
(2, 'Stephen Colbert'),
(3, 'Sarah Shankman'),
(4, 'John Steinbeck'),
(5, 'Aldous Huxley'),
(6, 'J.D. Salinger'),
(7, 'John Steinbeck'),
(8, 'Harper Lee'),
(9, 'Milan Kundera'),
(10, 'Stephen Chbosky'),
(11, 'David Sedaris'),
(12, 'Lauren Weisberger'),
(13, 'Joseph Heller'),
(14, 'Karen Salmansohn'),
(15, 'Tennessee Williams'),
(16, 'Carson McCullers'),
(17, 'Ayn Rand'),
(18, 'Susanna Kaysen'),
(19, 'Alice Sebold'),
(20, 'Stephen King')

CREATE TABLE Book_Copies
(BookID int NOT NULL,
BranchID int NOT NULL,
No_of_Copies int NOT NULL
)

SELECT * FROM Book_Copies

INSERT INTO Book_Copies
VALUES (1, 789, 10),
(2, 258, 15),
(3, 123, 14),
(4, 487, 12),
(5, 258, 16),
(6, 123, 18),
(7, 487, 14),
(8, 123, 12),
(9, 789, 6),
(10, 123, 8),
(11, 789, 9),
(12, 258, 13),
(13, 123, 18),
(14, 789, 17),
(15, 487, 15),
(16, 258, 12),
(17, 789, 13),
(18, 789, 19),
(19, 258, 8),
(20, 487, 9)

CREATE TABLE Book_Loans
(BookID int NOT NULL,
BranchID int NOT NULL,
CardNo int NOT NULL,
DateOut date NOT NULL,
DueDate date NOT NULL
)

SELECT * FROM Book_Loans

INSERT INTO Book_Loans
VALUES (5, 789, 1005, '2016-02-07', '2016-03-07')

INSERT INTO Book_Loans
VALUES (8, 258, 1007, '2016-02-09', '2016-03-09'),
(4, 123, 1008, '2016-02-14', '2016-03-14'),
(1, 487, 1009, '2016-02-07', '2016-03-07'),
(2, 258, 1014, '2016-02-17', '2016-03-17'),
(9, 123, 1007, '2016-02-14', '2016-03-14'),
(18, 487, 1007, '2016-02-24', '2016-03-24'),
(14, 123, 1005, '2016-02-17', '2016-03-17'),
(16, 789, 1014, '2016-07-02', '2016-03-02'),
(2, 123, 1009, '2016-02-02', '2016-03-02'),
(8, 789, 1003, '2016-02-01', '2016-03-01'),
(6, 258, 1001, '2016-02-17', '2016-03-17'),
(20, 123, 1009, '2016-02-19', '2016-03-19'),
(17, 789, 1009, '2016-02-07', '2016-03-07'),
(18, 487, 1001, '2016-02-23', '2016-03-23'),
(20, 258, 1014, '2016-02-19', '2016-03-19'),
(1, 789, 1019, '2016-02-14', '2016-03-14'),
(8, 789, 1001, '2016-02-03', '2016-03-03'),
(7, 258, 1014, '2016-02-15', '2016-03-15'),
(2, 487, 1003, '2016-02-18', '2016-03-18'),
(1, 789, 1003, '2016-02-11', '2016-03-11'),
(4, 487, 1003, '2016-02-02', '2016-03-02'),
(7, 258, 1001, '2016-02-17', '2016-03-17'),
(12, 789, 1001, '2016-02-11', '2016-03-11'),
(14, 789, 1003, '2016-02-11', '2016-03-11'),
(3, 258, 1003, '2016-02-14', '2016-03-14'),
(9, 487, 1001, '2016-02-18', '2016-03-18'),
(5, 123, 1001, '2016-02-03', '2016-03-03'),
(13, 487, 1003, '2016-02-17', '2016-03-17'),
(18, 123, 1014, '2016-02-15', '2016-03-15'),
(14, 789, 1005, '2016-02-17', '2016-03-17'),
(20, 123, 1003, '2016-02-7', '2016-03-7'),
(19, 789, 1001, '2016-02-02', '2016-03-02'),
(7, 258, 1009, '2016-02-01', '2016-03-01'),
(4, 123, 1014, '2016-02-17', '2016-03-17'),
(6, 487, 1005, '2016-02-19', '2016-03-19'),
(14, 258, 1001, '2016-02-14', '2016-03-14'),
(15, 789, 1003, '2016-02-23', '2016-03-23'),
(7, 789, 1003, '2016-02-19', '2016-03-19'),
(5, 258, 1009, '2016-02-17', '2016-03-17'),
(2, 487, 1007, '2016-02-05', '2016-03-05'),
(3, 789, 1019, '2016-02-07', '2016-03-07'),
(6, 487, 1018, '2016-02-01', '2016-03-01'),
(12, 258, 1001, '2016-02-17', '2016-03-17'),
(14, 789, 1003, '2016-02-19', '2016-03-19'),
(17, 789, 1005, '2016-02-14', '2016-03-14'),
(18, 258, 1001, '2016-02-23', '2016-03-23'),
(15, 487, 1001, '2016-02-19', '2016-03-19'),
(12, 487, 1003, '2016-02-17', '2016-03-17'),
(1, 258, 1019, '2016-02-19', '2016-03-19')
 
CREATE TABLE Library_Branch
(BranchID int PRIMARY KEY,
BranchName varchar(30) NOT NULL,
BranchAddress varchar(50) NOT NULL
)
SELECT * FROM Library_Branch

INSERT INTO Library_Branch
VALUES (789, 'Sharpstown', '124 Front St, Portland, OR 97225'),
(258, 'Central', '4878 Central St., Portland, OR 97225'),
(123, 'Plaza', '7894 Plaza Ave., Portland, OR 97225'),
(487, 'North', '489 North Ave, Portland, OR 97458')

CREATE TABLE Borrower
(CardNo int PRIMARY KEY,
Name varchar(30) NOT NULL,
BorrowerAddress varchar(50) NOT NULL,
Phone varchar(20) NOT NULL
)

SELECT * FROM Borrower

INSERT INTO Borrower
VALUES (1005, 'Tina Fey', '1589 2nd Ave., Portland, OR 97254', '(503) 222-1212'),
(1007, 'Bobbie Joe', '1874 SE 82nd Ave, Portland, OR 97458', '(503) 478-8951'),
(1008, 'Tori Amos', '1478 NE 22nd Ave, Portland, OR 97858', '(503) 487-7894'),
(1009, 'Richard Hansen', '888 Front St., Portland, OR 97858', '(503) 874-4125'),
(1014, 'Amy Johnson', '147 51st Place, Portland, OR 97458', '(503) 898-1258'),
(1003, 'Dina Abdula', '1478 Central St., Portland OR 97858', '(503) 747-8974'),
(1001, 'Lana Banana', '3849 Dogwood St., Portland, OR 97225', '(503) 747-4574'),
(1019, 'Jimmy John', '1474 Madison St., Portland, OR 97414', '(503) 858-8958'),
(1018, 'Carl Carlson', '652 Evergreen Way, Portland, OR 97858', '(503) 414-8974')

/*To show how many copies of The Lost Tribe are owned by Sharpstown*/
SELECT * FROM 
Book AS B INNER JOIN Book_Copies AS BC
ON B.BookID = BC.BookID 
WHERE Title = 'The Lost Tribe' AND
BranchID = 789

/*To show how many copies of The Lost Tribe are owned by each library branch*/
SELECT * FROM
Book AS B INNER JOIN Book_Copies AS BC
ON B.BookID = BC.BookID
WHERE Title = 'The Lost Tribe'

/*To retrieve the names of all borrowers who do not have any books checked out*/
SELECT * FROM
Borrower AS BW INNER JOIN Book_Loans AS BL
ON BW.CardNo = BL.CardNo
WHERE DateOut = NULL

/*To retrieve the borrower info for books that are due today at the Sharpstown branch*/
SELECT * FROM
Borrower AS BW INNER JOIN Book_Loans AS BL
ON BW.CardNo = BL.CardNo
WHERE DueDate = '2016-03-07' AND
BranchID = 789

/*To retrieve the name and total number of books loaned out from each library branch*/
SELECT BranchName, COUNT (DateOut) AS NumberofBooksLoaned
FROM Book_Loans INNER JOIN Library_Branch
ON Book_Loans.BranchID = Library_Branch.BranchID
GROUP BY BranchName


/*Retrieve names, addresses, and number of books checked out for all borrowers who have more than five books checked out*/
SELECT Borrower.Name, Borrower.BorrowerAddress, COUNT (Book_Loans.CardNo) AS BooksCheckedOut FROM Book_Loans
LEFT JOIN Borrower
ON Borrower.CardNo = Book_Loans.CardNo
GROUP BY Borrower.Name, Borrower.BorrowerAddress
HAVING COUNT (Book_Loans.CardNo) > 5


/*For each book authored by Stephen King, retrieve the title and number of copies owned by the Central branch*/
SELECT * 
FROM Book_Copies AS BC INNER JOIN Library_Branch AS LB
ON BC.BranchID = LB.BranchID
CROSS JOIN Book 
WHERE Title = 'Carrie' AND BranchName = 'Central'

/*Stored procedure for books due March 7, 2016*/
CREATE PROCEDURE GetBooksDue
AS
	SELECT * FROM
	Borrower AS B INNER JOIN Book_Loans AS BL
	ON B.CardNo = BL.CardNo
	WHERE DueDate = '2016-03-07'




