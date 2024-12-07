# **Sentiment Analysis of Amazon Product Reviews**

 _Mitansh Maheshwari_  
_Date - 12/2/2024_

---

## Project Overview
This project involves performing sentiment analysis on Amazon product reviews from the **CDs & Vinyl** category, using data up to 2023. The goal is to understand customer sentiments towards products in this category, providing insights into the relationship between product ratings, review sentiments, and other features like price, category, and word count.

## Dataset Structure and Source

The dataset used for this project is provided by **McAuley Lab, UCSD**. You can access the dataset and more details on their official site: [McAuley Lab, UCSD](https://amazon-reviews-2023.github.io/).

## Python Packages and Libraries used

- `pandas`
- `datetime`
- `beautifulsoup4`
- `re`
- `nltk`
- `vaderSentiment`
- `numpy`
- `tabulate`
- `prettytable`
- `matplotlib`
- `seaborn`
- `wordcloud`

**NOTE** 
These libraries and packages are required and need to be installed before running the notebook. To install them, simply run:
1. For notebook:
    ```bash
    !pip install <PackageName>
    ```
2. For command line:
    ```bash
    pip install <PackageName>
    ```

## Files Included

- ### Data Files
    - `updated_metadata.jsonl`

- ### Notebook (Main Code)
    - `sentiment.ipynb`
    
    [**NOTE** - The file takes about 1hr 30min to run]

- ### Generated Output Files
    - `sentiment.HTML`
    - `sentiment.pdf`
