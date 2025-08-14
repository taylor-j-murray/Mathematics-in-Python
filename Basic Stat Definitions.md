# Basic Stat Definitions

Assumptions/Notations:
* (X,y) will denote a dataset
* y is the target column of (X,y) 
* X is the dataset (X,y) with the target column y removed.

- Homoscedasticity: We say a regression on (X,y) has homoscedasticity if the set of residuals of each of the observations has near constant variance.
A nice way to visual this is that the regressions $h$ is homoscedastic with (X,y) if there exists $\epsilon_1>\epsilon_2>0$ such that 
    1. $\epsilon_1- \epsilon_2$ is smaller than some predetermined threshold and 
    2. all residuals lie in the epsilon band $\{(x,y) \in \mathbb{R}^n~|~ h(x)+ \epsilon_1 > y > h(x)+\epsilon_2\}$.

- Residual: The i-th residual of a regression $h$ on (X,y) is $|h(X_i)-y_i|$.  