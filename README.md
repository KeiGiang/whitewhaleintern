# Intern challenge for White Whale

**Code Challenge: Gibberish Algorithm**
---------------------------------------

Challenge Overview
------------------

We are exticed taht you are intsereted in joiinng Wihte Wahle for the smumer.  Weoclme to yuor fsrit prommarging chanellge.  Yuor chnellage is to courtsnct a prrgoam taht tekas an Enilgsh txet snirtg as iupnt and rerutns rebadale giirebbsh lkie tihs.  It dseno’t mtaetr in waht oerdr the ltteres in a wrod are, but an iproamtnt tihng is taht the frsit and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it whotuit a pboerlm.  Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe.

**The Basics:**

  - You may use *almost any* programming language... it's your choice.  See the supported options [here](http://ideone.com/).
  - Your program should leave the first and last letter of each word in place and scramble the rest.
  - Your program should not scamble punctuation (.,-'...etc.), numbers, or upper-case abbreviations.
  - See the [/text_files] folder for sample text files.

**Input/Output:**

  - Name your program as follows: `gibgen.xx` (where xx is variable based on the language you choose)
  - Your program should be able to read text input from a string passed into STDIN
      - `gibgen.xx "This is a String"`
      - `cat mystringfile.txt | gibgen.xx`
  - Your program should output to the console.

_Note: This challenge is based on a popular word gibberish meme. You can improve the readability by looking at a [researcher's take](http://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/) on the truths/myths of this meme, but this is not required._

What to do
----------
1. [Download](http://git-scm.com/downloads) & install Git on your machine

2. <a href="https://github.com/trentgillham/whitewhaleintern#fork-destination-box" class="btn grouped" data-method="POST" rel="nofollow" title="Fork">Fork</a> this project - Go [here](https://github.com/trentgillham/whitewhaleintern) and click the "Fork" button (located on the upper-right side of the screen)

2. Clone your new fork'd repository to your local machine - `git clone https://github.com/trentgillham/whitewhaleintern.git`
3. Complete the code challenge and fill out the Quick Start & Questions in the the README (see below)
4. `git add` and `git commit` your local repository as you go
4. Push your code and README back to Github occasionally - `git push origin master`
5. Email [gillham@whitewhaleanalytics.com](mailto:gillham@whitewhaleanalytics.com) with the Commit URL to your fork'd repository that you want reviewed. It should include at least 2 files: (1) your updated README with Coding Questions answered, and (2) your program (gibgen.xx)
   - Copy and paste the URL into the email along with your name... it should look something like this:
       - https://github.com/YOUR_USERNAME_HERE/whitewhaleintern.git

_Note: If you have any questions, email [gillham@whitewhaleanalytics.com](mailto:gillham@whitewhaleanalytics.com)._

Judging Criteria
----------------

Your responses to the **Coding Questions** at the bottom of this README are the *Most Important* part of this challenge. A working, fully fault-tolerant program that we just can't break, albeit awesome, is the least important.  Why is that?  Remember, we don't expect you to be expert programmers (just yet)... We want to see how you think through a problem.  


For completion by applicant
===========================

Quick Start
-----------

* This program can be run by using the command "python ./gibgen.py __textfiledirectory__". Where __textfiledirectory__ is a directory to a .txt file in your local system. For example, "text_files/sample.txt" would be a valid directory to run.
* Program was written for Python 2.7
* Given the conditions set above, abbreviations and numbers are not scrambled. Due to probability, 3 character words will remain the same and 4 character words will have a 50% chance of returning the original word.


Coding Questions
----------------

Question 1: "How did you approach the problem?" (500 words or less)
    I started by trying to break the challenge down into smaller subproblems. Some of the subproblems I created include: "How do I breakup a string based on special characters?", "How would I re-introduce the special characters when I am done randomizing?", and "How can I randomize a word while keeping the initial and final letters in their respective places?". Through these subproblems, I could create even smaller subproblems and the solution to the challenge would be the collection of answers to all the subproblems. By creating subproblems, I could view the challenge as a layered problem. With the outer layer being the initial challenge, and each subsequent layer down being a set of subproblems of their immediate upper layer, I could identify and plan how each subproblem in a lower layer would need to interact with each other.
    For example, the first layer of subproblems I created were: "How do I breakup a string based on special characters?" and "How would I re-introduce the special characters when I am done randomizing?". With these questions, I would theory craft possible solutions and attempt to break them. One possible solution I created was to parse through the string until I find a special character and randomize the characters that parsed up to that point. This method proved to be a more complicated solution than necessary and was eventually discarded to try a new solution. The solution I went with involved storing the location and value of special characters into a list and re-inserting after all the words have been scrambled.


Question 2: "What was the most difficult aspect of the solution?" (500 words or less)
    Personally, I think most difficult aspect of this solution was trying to decide which language to program in. Although I think each language has strengths and weaknesses, I have rarely ever had to compare the languages for implementation. Eventually I went with Python because of the procedural programming capabilities which allowed me to start programming without having to worry about semicolons and the object oriented nature of my other choices. Python is also one of the languages used in machine learning at White Whale, which also played a big factor in my decision. Since I was switching programming languages from mainly C# type to Python, there was a small learning curve involved to relearn the language.
    For the past year, I have been programming mainly in C# with some Java and JavaScript on the side. The syntax and grammar of these languages varies from Python and, as a result, slowed my progress. Another issue I ran into involved the Python libraries. Again, this can relate back to my unfamiliarity with the Python language and contributed to the learning curve. Python's data types do not have built in methods to retrieve the lengths of arrays or split by the newline character (\n), which was quite crucial to some parts of my implementation. These functionalities were a stylistic difference of the language itself and added to the overall learning curve. Thus, I think the biggest difficulty was adjusting myself to the language and the learning curve involved.
