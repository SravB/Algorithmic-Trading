# Algorithmic-Trading

This machine learning algorithm was built using Python 3 and scikit-learn with a Decision Tree Classifier. 

![Screenshot](stock.png)

In this specific example, the algorithm is used on a stock that changes price randomly. The red lines illustrate the stock price movements when we are not holding the stock while the green lines show these movements when we are holding the stock. The blue lines illustrate cash levels over time, where we start with $100 (so in this case, we can also interpret this as the percentage return on the stock). The expected cash value is the return we would have received if we simply held onto the stock for the entire period. The performance is the ratio between the cash value over the expected cash value and is expressed as a percentage.

Below is a screenshot of the algorithm's results on a large sample of stocks where changes in price are generated randomly:

![Screenshot](results.jpg)

Overall, this algorithm predicts whether the stock price will rise or fall with approximately a 75% accuracy. This is far better than the 50% produced when randomly guessing. 
