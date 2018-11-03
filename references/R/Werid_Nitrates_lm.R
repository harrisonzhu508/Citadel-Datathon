# Weird lm on Nitrates 

# Predict value of nitrates using size of industry by headcount

nit_data <- read.csv("~/Desktop/Nitratesben_data.csv")

scaled.dat <- scale(nit_data[,c(9,15,17,18)])
lm_data <- nit_data[,c(9,15,17,18)]

summary(nit_data[,c(9,15,17,18)])
lm_data[is.na(lm_data)] <- 0
summary(lm_data)

scaled.dat <- scale(lm_data)

# check that we get mean of 0 and sd of 1
colMeans(scaled.dat)  
apply(scaled.dat, 2, sd)

nit.lm <- lm(value ~  agri_fish_hunt + manufacturing + construction, data = lm_data)

summary(nit.lm)

coef(nit.lm)

# Checking assumptions 

qqnorm(resid(nit.lm))
qqline(resid(nit.lm))

plot(resid(nit.lm) ~ fitted(nit.lm), main = "Residuals vs Fitted values",
     xlab = "Fitted values", ylab = "Residuals")

# Model Comparison 

anova(nit.lm)

# If we want to compare 2 specific models use:

anova(nit.lm0, nit.lm1)