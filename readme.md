# Train Route Analysis

The goals of this program is to:

1.  Find the top 7 most travelled routes for a Sunday on average, indicate the average of each and rank them in decreasing order
2.  What is the probability that a passenger travelling from Kijauri will take a Shuttle if they depart before 07:30?
3.  The Sequence ‘MK’ appears in a payment reference. Based on the distribution of characters in all the payment references what do you think is the most probable next character (if any)?

---

## Most Travelled Route

1. The general approach taken involves iterating through the data points while updating a frequency table that tracks the route aganist the number of times visted.
2. We sort the frequency table based on the value
3. Return a tuple of the 7 most travelled trips

---

## Probability of taking a Shuttle

The probability of travelling from Kijauri is given by:

- _Let, a = The probability that a passenger travelling from Kijauri will take a shuttle if they depart before 7:30_
- _b = The number of people who travelled from Kijauri and departed before 7:30_
- _c = The number of people who took a shuttle, travelled from Kijauri and departed before 7:30_
- _a = c/b_

---

## MK Sequence

The most probable character to appear after MK is the character that appears after MK the most

### Approach

1. Filter the datapoints with "MK" in their receipt
2. Find the character that comes after "MK" _((Index+2) where index is the location of 'M' in the 'MK' sequence in the receipt)_
3. Update the character found in frequency table
4. Find the largest entry in the frequency table

---

## Tools Used

1. I used Pandas to read the CSV file. Why?

   - Its ability to open the CSV in chunks to save memory
   - Its better performance compared to in-built python arrays
   - Easy filtering

2. I used numpy arrays instead of python lists because of the better performance

---

## Extra

1. I opened the CSV in chunks on 1000 datapoints at a time to save memory
2. In the python file, there are 3 separate methods that implement the tasks given. It would be better to perform all three tasks on chunks simutenously, but I've split the tasks for the sake of presentation.

## Running

#### On Bash

```console
pip install -r requirements.txt
cd src
python3 main.py
```

#### On Windows

```sh
pip install -r requirements.txt
cd src
python3 main.py
```

Enjoy 👍
