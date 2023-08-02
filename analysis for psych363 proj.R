
Data = read.csv(file.choose())

Data$Proficiency_level <- Data$LexTALE_Score * Data$AverageResponseTime

threshold <- 0.5605017

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

#To calculate the Proficiency level and group the participants based on that, we multiplied the score by the 
# average reaction time to create that proficiency level number. Then we took an average of that score and used that 
# average as a threshold for grouping. Those who scored above 0.5605017 would be in the High Proficiency group and those 
# who scored below that threshold would be in the Low Proficiency group 

#What statistical test we ran and why
# Chose to ran a t-test because we had two groups and were trying to compare the mean reaction time between these
# two independent groups to see whether there was a significant difference. So, whether a faster or slower average reaction time had a significant difference 
# on whether one is scored as highly proficient or low proficient. 
