library(stats)

Data = read.csv(file.choose())

Data$Proficiency_level <- Data$LexTALE_Score

threshold <- 0.484375

Data$Group <- ifelse(Data$Proficiency_level <= threshold, "High Proficiency", "Low Proficiency")

mean_high_proficiency <- mean(Data$Proficiency_level[Data$Group == "High Proficiency"], na.rm = TRUE)
mean_low_proficiency <- mean(Data$Proficiency_level[Data$Group == "Low Proficiency"], na.rm = TRUE) 
print(mean_high_proficiency)
print(mean_low_proficiency)  

sd_high_proficiency <- sd(Data$AverageResponseTime[Data$Group == "High Proficiency"])
sd_low_proficiency <- sd(Data$AverageResponseTime[Data$Group == "Low Proficiency"])
print(sd_high_proficiency)
print(sd_low_proficiency)

DescriptiveStatistics <- data.frame(
  Group = c("High Proficiency", "Low Proficiency"),
  StandardDeviation = c(sd_high_proficiency, sd_low_proficiency),
  Mean = c(mean_high_proficiency, mean_low_proficiency)
)
print(DescriptiveStatistics)

high_proficiency_data <- Data$AverageResponseTime[Data$Group == "High Proficiency"]
low_proficiency_data <- Data$AverageResponseTime[Data$Group == "Low Proficiency"]

t_test_result <- t.test(high_proficiency_data, low_proficiency_data)
print(t_test_result)

correlation <- cor(Data$LexTALE_Score, Data$AverageResponseTime, method = "pearson")
print(correlation)
