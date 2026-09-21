# Lab-5
In this lab, we'll continue our practice with all of the structures we've seen so far, including while loops, booleans, and strings.  On this lab, we will also practice a coding technique of pair programming.  For more information see https://martinfowler.com/articles/on-pair-programming.html.

# Directions for completing the lab
For this lab we will be pair programming which is a collaborative method of programming featuring two roles, a driver and a navigator, and only one computer.  The driver is the person at the keyboard.  She is focused on completing the individual steps of the problem, ignoring any larger structural issues.  She should always talk through what she is doing while she is doing it.  The navigator is the observer, watching while the driver is typing.  She reviews what is written, gives directions and thoughts.  She worries about the bigger issues and makes note of potential next steps or issues.  There should be constant conversation between the driver and the navigator as code is being developed.  We will alternate roles for every other problem in this lab.  Find a partner and then choose amongst yourselves who should be the first driver.  You will use the first driver's computer to complete this assignment.  That student will be the driver for all of the odd numbered problems.  The other student will be the driver for all even numbered problems.

# Directions for submission
Create a github repo called "XX-YY-Lab-5," where XX are the initials of the first driver (this will also be the student responsible for submitting the lab) and YY are the initials of the first navigator.  Invite me as a collaborator to your repo.  Download the repo files here as a zip file.  Unzip the files and add them to your repo.  Modify the files as appropriate according to the instructions.  Do not change names.  Commit and push changes to your repo.

# Directions for solutions
Do not change any of the code given to you (other than the comments which should absolutely be removed).  I will run your code with the expected structure.  You are welcome to add any additional lines of code or functions you find necessary.  If you make changes in which your solutions do not run, you will receive no credit for that problem.  All solutions should include a docstring with doctests.  Unless otherwise specified, all functions should end with a return of the appropriate type and not a print statement.

# Problem 1
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.  Design a function ugly_number which, given an integer n, returns True if n is an ugly number and False otherwise.

# Problem 2
Design a function bologna_latin which consumes a string and returns a string with the first letter moved to the end of the string together with an "ay."  For example, "computer" would become "omputercay" and "example" would become "xamplecay."  (Proper pig latin has quite a few rules which we will ignore for now and return to again at a later assignment.)

# Problem 3
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.  The values are I=1, V=5, X=10, L=50, C=100, D=500, M=1000.  Roman numerals are usually written from largest to smallest from left to right.  However, the numeral for four is not IIII.  Instead, the number four is written as IV.  The one before the five means to subtract, making it four.  The same principle applied to nine, which is written IX.  In fact, there are six cases in which subtraction is used.  Look up the rules and then write a function roman_to_decimal which takes in a string as a Roman numeral and returns the whole number it corresponds to.

# Problem 4
Design a function power_of_three which takes in an integer and returns True if it is a power of three and False otherwise.
