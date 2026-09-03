# ==============================================================================
# Pipeline: Exploratory Data Analysis & Advanced Visualizations in R
# Track: Virtual Data Science with R Apprentice (Week 2)
# ==============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(scales)
  library(viridis)
  library(patchwork)
})

# Load Processed Mandi Data
generate_eda_visuals <- function(data) {
  # 1. Price Distribution by Primary Commodity (Box Plot)
  p1 <- ggplot(data, aes(x = commodity, y = modal_price, fill = commodity)) +
    geom_boxplot(outlier.colour = "red", outlier.alpha = 0.3) +
    scale_y_continuous(labels = dollar_format(prefix = "₹")) +
    scale_fill_viridis_d(option = "mako") +
    theme_minimal() +
    theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust = 1)) +
    labs(title = "Modal Price Dispersion Across Key Commodities",
         x = "Commodity", y = "Modal Price (₹/Quintal)")

  # 2. Non-Linear Elasticity Curve (GAM Smoothing)
  p2 <- ggplot(data, aes(x = arrivals_tonnes, y = modal_price)) +
    geom_point(alpha = 0.2, color = "#2c3e50") +
    geom_smooth(method = "gam", formula = y ~ s(x, bs = "cs"), color = "#e74c3c", size = 1.2) +
    scale_x_log10(labels = comma) +
    scale_y_continuous(labels = dollar_format(prefix = "₹")) +
    theme_minimal() +
    labs(title = "Non-Linear Price Elasticity (Supply Saturation Tipping Point)",
         x = "Daily Arrivals (Tonnes, Log Scale)", y = "Modal Price (₹/Quintal)")

  # Multi-Panel Output
  combined_plot <- p1 / p2
  return(combined_plot)
}
