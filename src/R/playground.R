# Citadel UK Datathon challenge
# Authors: Harrison Zhu, Benjamin Hillyard, 
# Source file for code

library(utils)
library(stats)

# Read in the datasets
library(dlm)
data("AirPassengers")
#?"AirPassengers"
#Fit a local level with seasonal dummies
plot(log(AirPassengers), ylab = "log monthly total passengers (in thousands)", 
     main = "Number of international air passengers")
#Keep some observations for forecast validation
y <- as.numeric(log(window(AirPassengers, end = c(1958))))
n <- length(y)
time <- as.vector(time(window(AirPassengers, end = c(1958))))
month <- as.factor(as.integer(time*12) %%12)
#Build the dynamic linear model  - specification with local level + seasonal component (dummies)
#Need to specify initial values for mean m0, otherwise forecasts are diffuse values from zero
#takes a few steps to adjust
build <- function(params) {
  level <- dlmModPoly(order = 2, dV = exp(params[1]), dW = c(exp(params[2:3])))
  seas <- dlmModSeas(frequency = 12, dV = exp(params[1]), dW = c(exp(params[4]), rep(0, 10)))  #stochastic seas.
  mod <- level + seas 
  return(mod)
}
#Initial parameter values - four log-variance, mean and trend, seasonal effect
init <- rep(-5,4)
#Fit the DLM model - numerical optimization
fit <- dlmMLE(y = y, parm = init, build = build, method = "BFGS", control=list(trace = 10, maxit = 1000)) 




