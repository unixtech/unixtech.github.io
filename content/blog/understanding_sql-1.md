Title: Relational Algebra - SQL
Date: 2015-12-06 10:20
Modified: 2015-12-07 19:30
Category: Server    
Tags: Essentials
Authors: Unixer
Slug: understanding-sql-1
Summary: Understanding SQL SELECT and Relational algebra
Latex: 
Status: published



In the age of ORMs so many developers today doesn't know about very fundamental and basic algorithms that runs SQL. Despite being one of easiest and much useful language many people run away from using SQL directly and take shelter in using some 'wrapper' tool which is not always as good as `raw` SQL.

Let's start by defining very basic relation in SQL.

1. Database as Collection of relations ( Tables or Schemas )
2. Being first class predicate - State of database is final state of all relations
3. By *joining*, *aggregating* data from different relations one can filter out data as desired.

#### Relation

Relation in SQL language is defined by several terms.

|           |                         |
| --        | --                      |
| Tuple     | One Row in SQL Relation |
| Attribute | Column in Relation      |
| Unknown   | `Null` in Domain        |

> **Note:-** Tuple is represented by (a, b), Attribute(Column) here will have unique domain(name - Relation name) within relation.   


### Relational Algebra
Relational algebra is superset of *set* algebra which defines formal language of relations in Database domain.  
Each operation done here on relations will return new valid Relation.

This algebra has mainly two groups of operations, One it shares with *set* theory and other one is specific to *Relational* model.

|  | SET operations                    | Relation specific operations |
|     | --------                          | ------------                 |
| 1   | UNION                             | SELECT                       |
| 2   | INTERSECTION                      | PROJECT                      |
| 3   | SET DIFFERENCE                    |                              |
| 4   | CARTESIAN PRODUCT \ CROSS PRODUCT |                              |

Any operations in Relational algebra can be classified mathematically as binary and unary, this fundamental operators have all the power needed to construct complex queries as needed.  
The main operators are:  

- SELECT ( $\sigma$ ) <span class="fa fa-arrow-right"> </span> Can be described as below
    $$ \sigma_\psi RO $$

Where:

|     |                                            |
| ------- | -----------                                     |
| R       | Tupels sets in SQL                              |
| $\psi$  | Predicate in selection retries from Tuples in R |

- PROJECT ( $\pi$ ) <span class="fa fa-arrow-right"> </span> Operation which returns columnar structure in vertical dimention, If you remember this is slicing by attributes can be described as

$$ \pi_{a1,a2...an} RO $$ 

> $_{a1,a2..an}$ are set of attributes names.  

- CARTESIAN\CROSS PRODUCT ( $\times$ ) <span class="fa fa-arrow-right"> </span> This is binary operation as oppose to unary like previous two, Can be used to generate complex relations by joining each tuple operands together. 

$R \times S = {r1, r2...rn,s1,s2...sn}$

- UNION ($\cup$) <span class="fa fa-arrow-right"> </span> Appends two relations together.

> To be successful in this binary operations both relation needs to have same set of attributes.  


$$ R \cup S = (_{r1, r2...rn}) \cup (_{s1, s2...sn}) $$

> Assuming, $S \, \Sigma \, (_{s1,s2...sn}) \quad and \quad R \, \Sigma \, (_{r1,r2...rn})$  

- DIFFERENCE ( $\setminus or \, -$ ) <span class="fa fa-arrow-right"> </span>  A binary operation, as you may have guessed - $\cup$ only but in reverse.  
Set difference can be described as 

$$ R\setminus S = (_{r1,r2...rn}) \quad where \quad (_{r1,r2...rn}) \, \Sigma\, R \quad but \quad  (_{r1,r2...rn}) \, \notin \, S $$


- REMAME($\rho$) <span class="fa fa-arrow-right"> </span> A unary operation that works on attributes and returns new value of attribute, This is mainly used for JOIN operations to differantiate the attributes, can be expressed as

$$ \rho_{a\setminus b}R$$

With this essential building blocks in place we can now move forward and take a look at more complex queries such as mixing many of these premitives to perform *left joins*, *right-joins* etc. In addition to these we can also add few more such as *sum*, *multiplication* to these operations on set of tuples or attributes.  
These algebric math provides fundamental building block of any SQL algorithm which guarantess ACID standards are followed hence understanding them all the more important.




