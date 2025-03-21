library(tidyverse)
library(nbastatR)
library(rvest)

test <- hoops_hype_salary_summary(return_wide = T,return_message = T)


# URL of the Wikipedia page
url <- "https://en.wikipedia.org/wiki/Forbes_list_of_the_most_valuable_NBA_teams"

# Read the HTML content of the page
webpage <- read_html(url)

# Extract the table with the class "wikitable"
table <- webpage %>%
  html_element("table.wikitable") %>%
  html_table(fill = TRUE)

# The table is stored as a list of data frames, so access the first element
nba_valuations <- table[[1]]

# View the extracted table
print(nba_valuations)
