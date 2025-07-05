Data source: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
Information from data source website:
This research aimed at the case of customers' default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel Sorting Smoothing Method to estimate the real probability of default. With the real probability of default as the response variable (Y), and the predictive probability of default as the independent variable (X), the simple linear regression result (Y = A + BX) shows that the forecasting model produced by artificial neural network has the highest coefficient of determination; its regression intercept (A) is close to zero, and regression coefficient (B) to one. Therefore, among the six data mining techniques, artificial neural network is the only one that can accurately estimate the real probability of default.

**UCI Credit Card Default Dataset Features**

**Demographic Features**
- `ID`: Unique client ID (not used for modeling)
- `LIMIT_BAL`: Credit limit (in NT dollars)
- `SEX`: Gender (1 = male, 2 = female)
- `EDUCATION`: Education level (1 = graduate, 2 = university, 3 = high school, 4 = others)
- `MARRIAGE`: Marital status (1 = married, 2 = single, 3 = others)
- `AGE`: Age in years

**Past Monthly Repayment Status**
- `PAY_0`: Repayment status in September (2005)
- `PAY_2`: August
- `PAY_3`: July
- `PAY_4`: June
- `PAY_5`: May
- `PAY_6`: April
- **Values**:  
    - `-1` = paid early  
    - `0` = paid in full  
    - `1~9` = months delayed

**Monthly Bill Amounts**
- `BILL_AMT1`: September bill
- `BILL_AMT2`: August bill
- `BILL_AMT3`: July bill
- `BILL_AMT4`: June bill
- `BILL_AMT5`: May bill
- `BILL_AMT6`: April bill

**Monthly Payment Amounts**
- `PAY_AMT1`: September payment
- `PAY_AMT2`: August
- `PAY_AMT3`: July
- `PAY_AMT4`: June
- `PAY_AMT5`: May
- `PAY_AMT6`: April

**Target**
- `default.payment.next.month`: 1 = default, 0 = no default
