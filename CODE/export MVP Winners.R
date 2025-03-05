library(tidyverse)
library(nbastatR)



x <- bref_awards_votes(seasons=2000:2024)
write.csv(dataMVPVotes, "./DATA/MVPWinners_2000-2024.csv")
