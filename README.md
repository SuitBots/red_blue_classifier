# Suit Bots Red/Blue classification

## Usage:

> `make`

Creates a Java output file `Brain.java` that classifies four inputs -- red, green, blue, and alpha color values -- into two outputs -- 0 for Blue, 1 for Red.

> `make validate`

Runs cross validation (n=10) against the observations file

## Prereqisites

* Python3.5
* Pandas
* scikit-learn
* sklearn_porter

## Input file

output.txt has the following per-row format

> RED_VALUE GREEN_VALUE BLUE_VALUE ALPHA_VALUE LABEL

Labeles must be either 'RED' or 'BLUE'.
