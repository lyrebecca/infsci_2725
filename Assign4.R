install.packages('ggplot2')
library(ggplot2)

Titanic = read.csv("~/Documents/Academics/INFSCI 2725/Assignment 4/train.csv")

p <- ggplot(Titanic, aes(Age, Fare)) + geom_point()
p + facet_grid(vs ~ am)
