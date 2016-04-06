# StochasticProcesses

This folder contains various chapters explaining topics in stochastic calculus both analytically and computationally using Monte Carlo techniques. The emphasis is on developing a physical understanding using concepts and examples from physics and finance.

As of writing this readme the **following chapters are in reasonable shape**:

### 1 [Random Walk and Weiner Process](RandomWalkAndWeinerProcess.ipynb)

This chapter starts with describing and simulating the binomial random walk. Then for a large number of steps the process is approximated by a normal distribution and the differences in processes that are fundamentally binomial and fundamentally Gaussian are shown by "zooming in". The process fundamentally Gaussian is continuous in time and is known as the Weiner process. We end by exploring its properties using physical reasoning and simulations. 

### 2 [Brownian Motion](BrownianMotion.ipynb)

This chapter discusses the Langevin equation and its solution. We also simulate the solution and compare with the analytic expressions. We end by plotting some representative trajectories.

### 3 [Brownian Motion of Harmonic Oscillator](StochasticHarmonicOscillator.ipynb)

This chapter discusses Brownian motion in a quadratic potential by adding the said potenital to the Langevin equation. We solve the system analytically and by simulation.

### 4 [Geometric Brownian Motion and Black-Scholes-Merton model for option pricing](GeometricBrownianMotion_and_EuropeanOptions.ipynb)

In this chapter we introduce geometric Brownian motion that leads to log-normal distribution instead of normal distribution. This is the model for stock price fluctuations adopted by Black, Scholes and Metron. We then show how simple vanilla options can be priced in this model using risk neutral pricing using both analytical and Monte Carlo methods. As something not usually seen in quant finance books we also numerically solve the fluctuation in the option price itself demonstrating its correlation with the stock price.

The **following are incomplete**:

### 5 [Barrier Crossing](BarrierCrossing.ipynb)


Things to do in the near future include:

1. American Options and other exotic options
2. Interest rate models
3. Comparison of real stock returns with geometric Brownian motion
4. Levy flights

