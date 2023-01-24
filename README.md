# Data Analytics Migration to Tableau

## Milestone 1 - Set up the environment
The repository was setup on both desktop and GitHub

## Milestone 2 - Data wrangling and cleaning.
The flight data was downloaded. They were stored in different CSV files which the flight data was grouped by year.  

The CSV files were converted to be pandas dataframes. Further analysis was conducted to clean the data. All rows and columns that have all their values as NULL were deleted. 

The cleaned dataframes were then combined into a single dataframe, in preparation to be uploaded as a single file. The initial check indicated the total number of rows and columns. This information is important for later task in verying the total number of rows and columns that have been successfully imported into postgres database.

![number of rows n columns in the dataframe - to CSV](https://user-images.githubusercontent.com/53040471/214304267-d58ae830-5581-4659-8c42-a555a25c0b59.jpg)

Further data cleaning was conducted on the combined dataframes to make sure that the correct data type is assigned to the columns.

The cleaned combined dataframes was later uploaded to the S3 bucket using the AWS CLI S3 cp command.

![AWS S3 CP Command]

## Milestone 3 - PostgreSQL RDS data import and reporting

### Connect pdAdmin4 to PostgreSQL RDS

### Create the flights_analytics database

### Import the combined_data.csv file into the flights table

### Explore the flights table and calculate some statictics



## Milestone 4 - Integrate Tableau Desktop with PostgreSQL RDS

### Download and install Tableau Desktop

### Configure the PostgreSQL connector and connect to the flights_analytics database RDS

## Milestone 5 - Create Tableau Reports

### Tableau data exploration

### Create a Tableau report for the historical flight origins and destinations

### Create a Tableau report for the average distance travelled

### Cretae a Tableau report for the most used flight numbers

### Create a Tableau report for flights delays and cancellations


