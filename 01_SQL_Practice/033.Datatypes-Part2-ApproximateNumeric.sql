


create table ApproNumericDataTypes(
	price decimal,
	cost numeric

)
--DECIMAL(p, s)
--p = total digits
--s = digits after decimal

create table ApproNumericDataTypes(
	price decimal(38,38),
	cost numeric(38,38)

)
--decimal(p,s) and numeric(p,s) are data types in SQL Server that are used to store fixed-point numbers with a specified precision (p) and scale (s). The precision (p) defines the total number of digits that can be stored, while the scale (s) defines the number of digits that can be stored to the right of the decimal point. In this case, both price and cost columns are defined with a precision of 38 and a scale of 38, which means they can store numbers with up to 38 digits in total, all of which can be after the decimal point. This allows for very high precision in storing decimal values, making it suitable for financial calculations or any scenario where exact decimal representation is required.

insert into ApproNumericDataTypes(price) values(1929.92)