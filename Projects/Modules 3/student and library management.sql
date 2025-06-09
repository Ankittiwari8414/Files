create database mobile;
use mobile;
create table students (
    student_id int auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    dob varchar(30),
    email varchar(100) unique,
    phone varchar(10),
    enrollment_date date
);

insert into students (first_name, last_name, dob, email, phone, enrollment_date)
values 
('john', 'doe', '2002-05-15', 'john.doe@example.com', '1234567890', '2023-09-01'),
('alice', 'smith', '2001-08-20', 'alice.smith@example.com', '9876543210', '2023-09-01'),
('bob', 'johnson', '2000-12-10', 'bob.johnson@example.com', '5678901234', '2023-09-01');

create table courses (
    course_id int auto_increment primary key,
    course_name varchar(30),
    course_description varchar(100),
    credits int
);

insert into courses (course_name, course_description, credits)
values 
('data structures', 'learn about linked lists, trees, and graphs.', 3),
('database systems', 'introduction to relational databases and sql.', 4),
('operating systems', 'fundamentals of os including processes and memory management.', 3),
('computer networks', 'study of networking concepts, protocols, and security.', 3),
('machine learning', 'introduction to ml algorithms and data science.', 4);

create table enrollments (
    enrollment_id int auto_increment primary key,
    student_id int,
    course_id int,
    enrollment_date date,
    grade varchar(5),
    foreign key (student_id) references students(student_id) on delete cascade,
    foreign key (course_id) references courses(course_id) on delete cascade
);

insert into enrollments (student_id, course_id, enrollment_date, grade)
values
(1, 1, '2023-09-05', 'a'),
(1, 2, '2023-09-06', 'b'),
(2, 2, '2023-09-07', 'a'),
(2, 3, '2023-09-07', 'c'),
(3, 1, '2023-09-08', 'b'),
(3, 4, '2023-09-08', 'a');  

select s.student_id, s.first_name, s.last_name from students s join enrollments e on s.student_id = e.student_id join courses c on e.course_id = c.course_id
where c.course_name = 'data structures';

select s.student_id, s.first_name, s.last_name, 
       avg(case 
            when e.grade = 'a' then 4.0
            when e.grade = 'b' then 3.0
            when e.grade = 'c' then 2.0
            when e.grade = 'd' then 1.0
            when e.grade = 'f' then 0.0
          end) as average_gpa
          
from students s join enrollments e on s.student_id = e.student_id
group by s.student_id;

select c.course_id, c.course_name, count(e.student_id) as total_students
from courses c

left join enrollments e on c.course_id = e.course_id group by c.course_id, c.course_name;

select s.student_id, s.first_name, s.last_name from students s join enrollments e on s.student_id = e.student_id
where e.grade = 'a' group by s.student_id;

select s.student_id, s.first_name, s.last_name from students s left join enrollments e on s.student_id = e.student_id
where e.student_id is null;

select c.course_id, c.course_name, count(e.student_id) as total_students from courses c join enrollments e on c.course_id = e.course_id
group by c.course_id order by total_students desc limit 1;

create index idx_enrollments_student on enrollments(student_id);

create index idx_enrollments_course on enrollments(course_id);

create table books (
    book_id int primary key auto_increment,
    title varchar(255),
    author varchar(255),
    publish_year year,
    genre varchar(100),
    quantity int
);

insert into books (title, author, publish_year, genre, quantity) values
('a game of thrones', 'george r. r. martin', 1996, 'fantasy', 10),
('a clash of kings', 'george r. r. martin', 1998, 'fantasy', 8),
('a storm of swords', 'george r. r. martin', 2000, 'fantasy', 7),
('a feast for crows', 'george r. r. martin', 2005, 'fantasy', 6),
('a dance with dragons', 'george r. r. martin', 2011, 'fantasy', 5),
('the great gatsby', 'f. scott fitzgerald', 1925, 'fiction', 5),
('1984', 'george orwell', 1949, 'dystopian', 3),
('to kill a mockingbird', 'harper lee', 1960, 'fiction', 4),
('the hobbit', 'j.r.r. tolkien', 1937, 'fantasy', 2),
('brave new world', 'aldous huxley', 1932, 'dystopian', 6);

create table members (
    member_id int primary key auto_increment,
    first_name varchar(100),
    last_name varchar(100),
    dob date,
    membership_date date,
    email varchar(100) unique,
    phone_number varchar(15) 
);

insert into members (first_name, last_name, dob, membership_date, email, phone_number) values
('sakshi', 'singh', '2004-07-16', '2021-02-20', 'sakshisingh@email.com', '1234567890'),
('saumya', 'singh', '2006-12-20', '2020-03-17', 'saumyasingh@email.com', '0987654321'),
('kiran', 'singh', '2000-06-02', '2022-05-10', 'kiransingh@email.com', '1122334455');

create table transactions (
    transaction_id int primary key auto_increment,
    member_id int,
    book_id int,
    borrow_date date,
    return_date date,
    status enum('borrowed', 'returned'),
    foreign key (member_id) references members(member_id),
    foreign key (book_id) references books(book_id)
);

insert into transactions (member_id, book_id, borrow_date, return_date, status) values
(1, 1, '2025-02-01', '2025-02-10', 'borrowed'),
(1, 3, '2025-02-02', '2025-02-12', 'borrowed'),
(2, 2, '2025-02-05', '2025-02-15', 'borrowed'),
(2, 4, '2025-02-06', '2025-02-16', 'borrowed'),
(3, 5, '2025-02-07', '2025-02-17', 'borrowed'),
(3, 1, '2025-02-07', '2025-02-17', 'borrowed');

select * from books where quantity > 0;

select book_id, count(transaction_id) as borrow_count
from transactions
group by book_id
order by borrow_count desc;

select b.title, b.author, t.borrow_date, t.return_date
from transactions t
join books b on t.book_id = b.book_id
where t.member_id = 1;

select distinct m.first_name, m.last_name, m.email

from transactions t join members m on t.member_id = m.member_id where t.status = 'borrowed' and t.return_date < curdate();

select member_id, count(transaction_id) as total_books_borrowed from transactions group by member_id;

select book_id, count(transaction_id) as borrow_count from transactions group by book_id having borrow_count > 1;

alter table members add phone_number varchar(15);

update books set quantity = quantity - 1 where book_id = 1; 

select b.title, b.author from books b left join transactions t on b.book_id = t.book_id
where t.borrow_date < curdate() - interval 1 year or t.borrow_date is null;

select distinct m.first_name, m.last_name from transactions t join books b on t.book_id = b.book_id join members m on t.member_id = m.member_id
where b.genre = 'science fiction';

select member_id, max(borrow_date) as most_recent_borrow_date from transactions
group by member_id;

select year(borrow_date) as year, month(borrow_date) as month, count(transaction_id) as total_books_borrowed from transactions group by year(borrow_date), month(borrow_date);

delimiter //
create trigger update_book_quantity_after_borrow after insert on transactions for each row

begin
    if new.status = 'borrowed' then
        update books set quantity = quantity - 1 where book_id = new.book_id;
    elseif new.status = 'returned' then
        update books set quantity = quantity + 1 where book_id = new.book_id;
    end if;
end;
//
delimiter ;

select b.title, b.author, m.first_name, m.last_name
from transactions t join books b on t.book_id = b.book_id
join members m on t.member_id = m.member_id where t.status = 'borrowed';

select b.title, b.author, m.first_name, m.last_name, t.return_date from transactions t
join books b on t.book_id = b.book_id join members m on t.member_id = m.member_id where t.return_date = curdate() or t.return_date = curdate() + interval 1 day;

create index idx_book_id on transactions(book_id);

