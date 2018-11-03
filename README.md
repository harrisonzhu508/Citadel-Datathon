# Citadel Datathon

`src` contains the source code used for this challenge
`report` contains the source code used for the $\Latex$ report

https://v2.overleaf.com/6183192336bcqknxjpwgmt

https://drive.google.com/drive/folders/1epKW_AnAU4EOmpiUduaFQqO1_DC5cc2s?usp=sharing


```r
library(MASS)

# Backward selection
backward_model <- MASS::stepAIC( lm(Prob~., data = dataset1) )

# Forward selection
MASS::stepAIC( lm(Prob~1, data = dataset1), 
               direction = "forward", 
               scope=list(
                upper=lm(Prob~., data = dataset1), 
                lower=lm(Prob~1, data = dataset1)) 
)
```
