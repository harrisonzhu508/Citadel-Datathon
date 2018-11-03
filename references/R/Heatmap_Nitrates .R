



library(RColorBrewer) 
library(gplots)
require(graphics)


data <- nit_data <- read.csv("~/Desktop/Nitratesben_data.csv")

rnames <-data[,1]
m <- as.matrix(data[,2:ncol(data)])  
rnames <-data[,1]
row.names(m) <-rnames


nrow(m)
ncol(m)

png("~/Desktop/Nitrates.png",
    width = 6*300,        # 5 x 300 pixels
    height = 6*300,
    res = 300,            # 300 pixels per inc
    pointsize = 8)        # smaller font size


row_distance = dist(m, method = "euclidean")
row_cluster = hclust(row_distance, method = "complete")

col_distance = dist(t(m), method = "euclidean")
col_cluster = hclust(col_distance, method = "complete")

heatmap.2(m,     # mat_data
          main = "Final, Euclidean, Complete", # heat map title
          density.info = "none",  # turns off density plot inside color legend
          trace = "none",         # turns off trace lines inside the heat map
          margins = c(12,12),     # widens margins around plot
          col = "heat.colors",
          labRow = NA,
          labCol = NA,
          symm = TRUE,
          cutree(row_cluster, k=1),
          Colv = as.dendrogram(col_cluster),
          Rowv = as.dendrogram(row_cluster)) 

dev.off()