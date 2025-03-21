library(tidyverse)
library(nbastatR)


games <- play_by_play(game_ids = c(21700002, 21700003), nest_data = F, return_message = T)
game_logs <- game_logs(seasons = 2019, result_types = c("team", "player"))


