# Election Analysis

## Project Overview

A recent local congressional election in Colorado took place and we are asked to audit the election results through the use of a python code that can automatically obtain the followig information:
1. Determine the total number of votes cast.
2. Determine each county's voting turnout, by voting count and percentage.
3. Specify the county with the largest turnout.
4. Get a complete list of  candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources
-Data source: election_results.csv (provided by the board of elections).
-Software: Python 3.7.6 and Visual Studio Code 1.63.2

## Results
The analysis of the election shows that:
-The number of total votes cast was: 369,771.
-The total votes follow the distribution described below:
    +Jefferson county: 38,855 votes (10.5%).
    +Denver county: 306,055 votes (82.8%).
    +Araphoe county: 24,801 votes (6.7%).
-The county with the largest turnout was Denver.
-The names of the candidates who received votes were:
    + Charles Casper Stockham
    + Diana DeGette
    + Raymon Anthony Doane
The votes casted per candidate are detailed as follows:
    -Charles Casper Stockham received 23.0% of the votes, with 85,213 votes.
    -Diana DeGette received 73.8% of the votes, with 272,892 votes.
    -Raymon Anthony Doane received 3.1% of the votes with 11,606 votes.
The winner of the election by popular vote was:
    -Diana DeGette (272,892 votes which account for 73.8% of the total votes.)

## Election-audit Summary
This local congressional election provides a perfect example of a real-world situation in which a script that allows automatic analysis provides useful and relevant information.
The code used demonstrates the power of a widely used analytic tool (python), which allows for an automated analysis of large-volume information that must be taken into account individually, as there is no option of analyzing a sample of the votes casted for a democratic election.
Even though  the data provided accounts for votes casted in three counties in the state of Colorado, with minor modifications to the code, as long as the same kind of information is provided (Ballot ID, candidate name and county), it can loop through any number of votes and could be used for a state-wide election, such as a Governor Election. Nevertheless, I must point out that the voting results must be presented in a standardized manner, in order to properly merge the different voting sources (mail in ballots, digital voting machines and manual votes).
The accuracy of the calculations presented also can be adjusted as needed in case of a close count between candidates, so the chance of a draw can be ruled out.