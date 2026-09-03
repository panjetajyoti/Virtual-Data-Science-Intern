# ==============================================================================
# Pipeline: Data Cleaning, Imputation & Feature Engineering in R
# Track: Virtual Data Science with R Apprentice (Week 3)
# ==============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(lubridate)
  library(stringr)
  library(scales)
})

# Ingestion & Schema Cleaning
clean_mandi_data <- function(file_path) {
  raw_df <- read_csv(file_path, col_types = cols(.default = "c"))
  
  df_stage1 <- raw_df %>%
    rename_all(~ tolower(str_replace_all(., " ", "_"))) %>%
    mutate(
      state = str_to_title(str_trim(state)),
      district = str_to_title(str_trim(district)),
      market = str_to_title(str_trim(market)),
      commodity = str_to_title(str_trim(commodity)),
      arrival_date = parse_date_time(arrival_date, orders = c("dmy", "ymd", "mdy")),
      modal_price = as.numeric(modal_price),
      min_price = as.numeric(min_price),
      max_price = as.numeric(max_price),
      arrivals_tonnes = as.numeric(arrivals_in_tonnes)
    )
  
  # Localized Median Imputation per District-Commodity
  df_imputed <- df_stage1 %>%
    group_by(district, commodity) %>%
    mutate(
      modal_price = if_else(is.na(modal_price), median(modal_price, na.rm = TRUE), modal_price)
    ) %>%
    ungroup() %>%
    filter(!is.na(modal_price), !is.na(arrivals_tonnes))
  
  # IQR Outlier Filtering
  df_filtered <- df_imputed %>%
    group_by(commodity) %>%
    mutate(
      q1 = quantile(modal_price, 0.25, na.rm = TRUE),
      q3 = quantile(modal_price, 0.75, na.rm = TRUE),
      iqr = q3 - q1
    ) %>%
    filter(modal_price >= (q1 - 1.5 * iqr) & modal_price <= (q3 + 1.5 * iqr)) %>%
    ungroup()
  
  # Feature Transformation
  final_df <- df_filtered %>%
    mutate(
      log_arrivals = log1p(arrivals_tonnes),
      day_of_week = wday(arrival_date, label = TRUE, abbr = TRUE),
      normalized_spread = (max_price - min_price) / modal_price
    )
  
  return(final_df)
}
