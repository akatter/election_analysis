# election_analysis
Module 3 Bootcamp

# Election Analysis - Module 3 Challenge

## Overview of Project

The purpose of this project is to complete an election audit of a recent congressional election with data provided from the Colorado Board of Elections. The audit is comprised of the following goals:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who recieved votes
3. Calculate the total number of votes each candidate recieved
4. Calculate the percentage of votes each candidate won 
5. Determing the winner of the election based on popular vote
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout

## Resources Used
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.63.2

## Analysis and Results

### Analysis of Refractored Changes
 
An example of the code is shown below.

```
    tickerVolumes(tickerIndex) = tickerVolumes(tickerIndex) + Cells(i, 8).Value
    
    If Cells(i - 1, 1).Value <> tickers(tickerIndex) And Cells(i, 1).Value = tickers(tickerIndex) Then
       tickerStartingPrices(tickerIndex) = Cells(i, 6).Value
    End If
    
    If Cells(i + 1, 1).Value <> tickers(tickerIndex) And Cells(i, 1).Value = tickers(tickerIndex) Then
        tickerEndingPrices(tickerIndex) = Cells(i, 6).Value
        tickerIndex = tickerIndex + 1
    End If
```

### Results of Refractored Changes using Timer


The original code produced these results for 2017 and 2018.
![2017 Timer Results Using Original Code](Resources/OriginalCode_2017.png)
![2018 Timer Results Using Original Code](Resources/OriginalCode_2018.png)

The refactored code produced these results for 2017 and 2018.
![2017 Timer Results Using Refactored Code](Resources/VBA_Challenge_2017.png)
![2018 Timer Results Using Refactored Code](Resources/VBA_Challenge_2018.png)

Comparing the results, it is shown that the refactored code was in fact faster then the original code.


## Summary

