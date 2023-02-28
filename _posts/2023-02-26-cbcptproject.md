---
title: College Board Create Performance Task
description: Trimester 2 CPT Project Outline
layout: post
comments: true
toc: true
categories: [week24, markdown]
---

# [Video](https://drive.google.com/file/d/10tMGR_cmDiNv0ZHbLQUvvZzilxhlXmcy/view)

# Writeup

Program Purpose

3.a.i

The purpose of the program is to identify the users next ovulation date to inform them of the next time they will be most ovulated.

3.a.ii

The function of this program is that the user will be asked to insert their next period day, period length, and menstrual cycle length. Once the user tracks their data they will get their next ovulation date as well as have their next period day, period length, and menstrual cycle length saved in the database. The table will print all the values that they have now as well as what they inputted previously.

3.a.iii

The input of the program are the dates of their last period, their usual period length, and their usual menstrual cycle length. Their output would show the next date that they will be ovulated (a 6 day period). The table will also output the data that they input (next period day, period length, and menstrual cycle length) because it was added to the database.

Data Abstraction

3.b.i

![list1](https://cdn.discordapp.com/attachments/806618712056528906/1080044141217599558/IMG_6820.jpg)

![list2](https://cdn.discordapp.com/attachments/806618712056528906/1080044164709875752/IMG_1197.jpg)

![list3](https://cdn.discordapp.com/attachments/806618712056528906/1080044175854161920/IMG_5780.jpg)

3.b.ii

![list4](https://cdn.discordapp.com/attachments/806618712056528906/1080052357611659374/IMG_8725.jpg)

3.b.iii

The list that is being used in this case is users. 

Managing Complexity

3.b.iv

The data in this list is the data that each of the users have for their next period day, period length, and menstrual cycle length.

3.b.v

This manages complexity in the program because being able to have all of the users in one list means that there does not have to be an individual function to read for each of the users. This allows for the code to be shortened to go through each value for each individual user. Without this code there then each user would have to have their own function and it would be harder for the database to add new users because each new user would need to create a new segment of code.

Procedural Abstraction

3.c.i

![](https://cdn.discordapp.com/attachments/806618712056528906/1080044135689498684/IMG_6698.jpg)

![](https://cdn.discordapp.com/attachments/806618712056528906/1080059649828606002/IMG_1810.jpg)

3.c.ii

![](https://cdn.discordapp.com/attachments/806618712056528906/1080060699495112764/IMG_9089.jpg)

![](https://cdn.discordapp.com/attachments/806618712056528906/1080075811635335288/IMG_3266.jpg)

3.c.iii

There are three procedures being shown in this program. There is create, read, and delete. First the ovulation function takes in the user period date, period cycle, and menstrual cycle and then stores the parameter in a json dictionary. The data that is in the dictionary is then fetched into each separate function (create, read, delete). The create function is used to have the user input the new data that is then passed to the read function. The read function is used to display all of the data that the user inputs onto the table for them to see. The delete function allows the user to delete all of the data in the database from the ovulation function.

Algorithmic Implementation

3.c.iv

Iteration is used in the for loop that is used for the adding row in the table when reading the data that is in the database. This data that is in the database is read using the for loop until all the data is added to the table and then displayed. The repeat of all of the users in the database is the iteration aspect being shown. 

The program is using sequencing in the validation feature because of the if else statement that is being used. The if else statement creates the user in different orders depending on the requirements that they must meet.

This validation feature also has selection in it because it has to make a decision if the user should be created. The user can only be created if the period length and the menstrual cycle is a number. The function has to select if the user is able to be made with this knowledge.

Testing

3.d.i

First call: The first call that I made is a create and fetch using the _Create and _Read function to save the period date, period length, and menstrual cycle legth from the user. The inputs were "02/15/23", "5", and "30". The data is then appended to the backend database, then displayed on the front end in the table that is shown. 

Second Call: The second call is a create and fetch from the _Create and _Read function that is used to save the period date, period length, and menstrual cycle legth from the user, but in this case the validation function is implemented and they are not able to append to the backend. The inputs are "02/24/2023", "c", "f". Since these last two values are not numbers they are not able to read and add to the table in the frontend.

3.d.ii

First call tested conditions: The first call tests the condition that the period date is a date from the calendar and that period length and menstrual cycle legth are numbers. If this is true, the create_user() function will execute. 

Second call tested conditions: The second call tests the validate function to make sure that the period length and menstrual cycle length are numbers. In this case it failed and the create_user() function did not execute.

3.d.iii

Results of the first call: The result of the first call that the period date, period length, and menstrual cycle legth are inputted into the backend database and shown on the frontend. They are all valid values that can be used.

Results of the second call: The result of the second call is that the error message will display that tells the user to input valid values for the period date, period length, and menstrual cycle legth.