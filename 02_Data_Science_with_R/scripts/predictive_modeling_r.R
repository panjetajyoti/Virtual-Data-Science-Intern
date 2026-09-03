# ==============================================================================
# Pipeline: Predictive Regime Classification & Model Evaluation in R
# Track: Virtual Data Science with R Apprentice (Week 4)
# ==============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(caret)
  library(randomForest)
  library(pROC)
})

set.seed(42)

run_predictive_pipeline <- function(data) {
  # Chronological Feature Construction
  model_data <- data %>%
    arrange(arrival_date) %>%
    group_by(market, commodity) %>%
    mutate(
      target = as.factor(if_else(lead(modal_price) > modal_price, "Up", "Down_Flat")),
      price_lag1 = lag(modal_price, 1),
      price_sma7 = zoo::rollmean(modal_price, k = 7, fill = NA, align = "right")
    ) %>%
    ungroup() %>%
    filter(!is.na(target), !is.na(price_lag1), !is.na(price_sma7)) %>%
    select(target, price_lag1, price_sma7, log_arrivals, normalized_spread)

  # 80/20 Time-Series Train/Test Split
  train_idx <- 1:floor(0.80 * nrow(model_data))
  train_set <- model_data[train_idx, ]
  test_set  <- model_data[-train_idx, ]

  # Model Training: Random Forest
  rf_model <- randomForest(target ~ ., data = train_set, ntree = 200, mtry = 2, importance = TRUE)
  
  # Evaluation
  rf_preds <- predict(rf_model, newdata = test_set)
  rf_probs <- predict(rf_model, newdata = test_set, type = "prob")[, "Up"]
  
  conf_matrix <- confusionMatrix(rf_preds, test_set$target, positive = "Up")
  roc_curve <- roc(test_set$target, rf_probs, levels = c("Down_Flat", "Up"))
  
  print(conf_matrix)
  cat("ROC-AUC Score:", auc(roc_curve), "\n")
  
  return(list(model = rf_model, auc = auc(roc_curve)))
}
