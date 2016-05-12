# StochasticProcesses

This folder contains various chapters explaining topics in stochastic calculus both analytically and computationally using Monte Carlo techniques. The emphasis is on developing a physical understanding using concepts and examples from physics and finance.

## Complete Chapters
**following chapters are in reasonable shape**:

### 1 [Random Walk and Weiner Process](RandomWalkAndWeinerProcess.ipynb)

This chapter starts with describing and simulating the binomial random walk. Then for a large number of steps the process is approximated by a normal distribution and the differences in processes that are fundamentally binomial and fundamentally Gaussian are shown by "zooming in". The process fundamentally Gaussian is continuous in time and is known as the Weiner process. We end by exploring its properties using physical reasoning and simulations. 

### 2 [Stochastic Calculus](StochasticCalculus.ipynb)

Buileing on the previous chapters developement of Weiner process, this chapter discusses how to integrate with respect to the Weiner process, otherwise known as stochastic integration. After discussing how to define the integral as a summation and differences from Riemann integral, we discuss the differences between Ito's prescription and Stratonovich's prescription and end with Ito's lemma.

### 3 [Brownian Motion](BrownianMotion.ipynb)

This chapter discusses the Langevin equation and its solution. We also simulate the solution and compare with the analytic expressions. We end by plotting some representative trajectories.

### 4 [Brownian Motion of Harmonic Oscillator](StochasticHarmonicOscillator.ipynb)

This chapter discusses Brownian motion in a quadratic potential by adding the said potenital to the Langevin equation. We solve the system analytically and by simulation.

### 5 [Geometric Brownian Motion and Black-Scholes-Merton model for option pricing](GeometricBrownianMotion_and_EuropeanOptions.ipynb)

In this chapter we introduce geometric Brownian motion that leads to log-normal distribution instead of normal distribution. This is the model for stock price fluctuations adopted by Black, Scholes and Metron. We then show how simple vanilla options can be priced in this model using risk neutral pricing using both analytical and Monte Carlo methods. As something not usually seen in quant finance books we also numerically solve the fluctuation in the option price itself demonstrating its correlation with the stock price.

## Incomplete Chapters

The **following are incomplete**:

### 6 [Barrier Crossing](BarrierCrossing.ipynb)

In this chapter we discuss how to evaluate probabilities of random paths crossing barriers. We introduce the analytic way using method of reflection as well as Monte Carlo methods.

In addition we also introduce the method to construct paths when the end points are fixed. This is useful in Monte Carlo simlulations when the final point can only be in a small region and use of methods introduced earlier would lead to most paths having to be discarded.


## Things to do in the near future include:

1. American Options and other exotic options
2. Interest rate models
3. Comparison of real stock returns with geometric Brownian motion
4. Levy flights

