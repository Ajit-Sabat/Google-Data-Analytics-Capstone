
## Loading Packages and Libraries

install.packages("rmarkdown")
install.packages("tidyverse")
install.packages("lubridate")
install.packages("ggplot2")

library(tidyverse)
library(ggplot2)
library(lubridate)
library(dplyr)
library(skimr)
library(janitor)

## Uploading Divvy datasets

trip_1 <-read_csv("202011-divvy-tripdata.csv")
trip_2 <-read_csv("202012-divvy-tripdata.csv")
trip_3 <-read_csv("202101-divvy-tripdata.csv")
trip_4 <-read_csv("202102-divvy-tripdata.csv")
trip_5 <-read_csv("202103-divvy-tripdata.csv")
trip_6 <-read_csv("202104-divvy-tripdata.csv")
trip_7 <-read_csv("202105-divvy-tripdata.csv")
trip_8 <-read_csv("202106-divvy-tripdata.csv")
trip_9 <-read_csv("202107-divvy-tripdata.csv")
trip_10 <-read_csv("202108-divvy-tripdata.csv")
trip_11 <-read_csv("202109-divvy-tripdata.csv")
trip_12 <-read_csv("202110-divvy-tripdata.csv")

## Comparing the columns of each trip

colnames(trip_1)
colnames(trip_2)
colnames(trip_3)
colnames(trip_4)
colnames(trip_5)
colnames(trip_6)
colnames(trip_7)
colnames(trip_8)
colnames(trip_9)
colnames(trip_10)
colnames(trip_11)
colnames(trip_12)

## Analyzing the Structure of each trip

glimpse(trip_1)
glimpse(trip_2)
glimpse(trip_3)
glimpse(trip_4)
glimpse(trip_5)
glimpse(trip_6)
glimpse(trip_7)
glimpse(trip_8)
glimpse(trip_9)
glimpse(trip_10)
glimpse(trip_11)
glimpse(trip_12)

## Comparing columns of all trips to identify mismatch data type and correcting them

compare_df_cols(trip_1,trip_2,trip_3,trip_4,trip_5,trip_6,trip_7,trip_8,
                trip_9,trip_10,trip_11,trip_12, return = "mismatch")

trip_1 <-mutate(trip_1,end_station_id=as.character(end_station_id),
                start_station_id = as.character(start_station_id))

compare_df_cols(trip_1,trip_2,trip_3,trip_4,trip_5,trip_6,trip_7,trip_8,
                trip_9,trip_10,trip_11,trip_12, return = "mismatch")

## Combining all monthly trips file to a single year trip file

all_trips <-bind_rows(trip_1,trip_2,trip_3,trip_4,trip_5,trip_6,trip_7,trip_8,
                      trip_9,trip_10,trip_11,trip_12)

View(all_trips)
colnames(all_trips)
dim(all_trips)
str(all_trips)
summary(all_trips)

## Removing the unnecessary columns from the dataframe

all_trips<- all_trips %>%
  select(-c(start_lat,start_lng,end_lat,end_lng))



## Renaming the columns

unique(all_trips$member_casual)

all_trips <- all_trips %>% rename(ride_type=rideable_type,user_type=member_casual)


## Data cleaning and preparing data for analysis



## Adding columns that list the date, month, day, and year of each ride

all_trips$date <- as.Date(all_trips$started_at) 
all_trips$month <- format(as.Date(all_trips$date), "%m")
all_trips$day <- format(as.Date(all_trips$date), "%d")
all_trips$year <- format(as.Date(all_trips$date), "%Y")
all_trips$day_of_week <- format(as.Date(all_trips$date), "%A")

### Adding a ride length column for calculating trips in seconds

all_trips$ride_length <- difftime(all_trips$ended_at,all_trips$started_at)
colnames(all_trips)
str(all_trips)

all_trips$ride_length <- as.numeric(as.character(all_trips$ride_length))
is.numeric(all_trips$ride_length)
colnames(all_trips)

### Removing the bad data

all_trips_v2 <- all_trips[!(all_trips$ride_length<0),]
View(all_trips_v2)

  
## Conducting Descriptive Analysis

skim(all_trips_v2)

summary(all_trips_v2$ride_length)

aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type, FUN = mean)
aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type, FUN = median)
aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type, FUN = max)
aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type, FUN = min)

### Analysis average ride time for each day for different user type

aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type + all_trips_v2$day_of_week, FUN = mean)
 
### Re-ordering the weekdays

all_trips_v2$day_of_week <- ordered(all_trips_v2$day_of_week, 
                            levels=c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))

aggregate(all_trips_v2$ride_length ~ all_trips_v2$user_type + all_trips_v2$day_of_week, FUN = mean)
 
## Analyzing ridership data by user_type and weekday.

group_user<-all_trips_v2 %>% 
  mutate(weekday = wday(started_at, label = TRUE)) %>%  #creates weekday field using wday()
  group_by(user_type, weekday) %>%  #groups by usertype and weekday
  summarise(number_of_rides = n()							#calculates the number of rides and average duration 
            ,average_duration = mean(ride_length)) %>% 		# calculates the average duration
  arrange(user_type, weekday)	
group_user

group_ride <-all_trips_v2 %>%
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(ride_type, weekday) %>% 
  summarise(number_of_rides = n()) %>% 
  arrange(ride_type, weekday)
group_ride

## Exporting the clean data.
write.csv(all_trips_v2,"Trips_clean.csv")


## Visualizing the data.

all_trips_v2 %>% 
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(user_type, weekday) %>% 
  summarise(number_of_rides = n()
            ,average_duration = mean(ride_length)) %>% 
  arrange(user_type, weekday)  %>% 
  ggplot(aes(x = weekday, y = number_of_rides, fill = user_type)) +
  geom_col(position = "dodge")

all_trips_v2 %>% 
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(user_type, weekday) %>% 
  summarise(number_of_rides = n()
            ,average_duration = mean(ride_length)) %>% 
  arrange(user_type, weekday)  %>% 
  ggplot(aes(x = weekday, y = average_duration, fill = user_type)) +
  geom_col(position = "dodge")

all_trips_v2 %>%
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(ride_type, weekday) %>% 
  summarise(number_of_rides = n()) %>% 
  arrange(ride_type, weekday)  %>% 
  ggplot(aes(x = ride_type, y = number_of_rides, fill = ride_type)) +
  geom_col(position = "dodge")

all_trips_v2 %>%
  mutate(weekday = wday(started_at, label = TRUE)) %>% 
  group_by(ride_type, weekday) %>% 
  summarise(number_of_rides = n()) %>% 
  arrange(ride_type, weekday)  %>% 
  ggplot(aes(x = weekday, y = number_of_rides, fill = ride_type)) +
  geom_col(position = "dodge")+theme_minimal()