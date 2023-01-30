# Data Analytics Migration to Tableau

## 1 - Set up the environment
The repository was setup on both desktop and GitHub

## 2 - Data wrangling and cleaning.
The flight data was downloaded. They were stored in different CSV files which the flight data was grouped by year.  

The CSV files were converted to be pandas dataframes. Further analysis was conducted to clean the data. All rows and columns that have all their values as NULL were deleted. 

The cleaned dataframes were then combined into a single dataframe, in preparation to be uploaded as a single file. The initial check indicated the total number of rows and columns. This information is important for later task in verying the total number of rows and columns that have been successfully imported into postgres database.

![number of rows n columns in the dataframe - to CSV](https://user-images.githubusercontent.com/53040471/214305454-ea736714-ea0c-4ae4-aa8c-81992ba8e826.jpg)

Further data cleaning was conducted on the combined dataframes to make sure that the correct data type is assigned to the columns.

The cleaned combined dataframes was later uploaded to the S3 bucket using the AWS CLI S3 cp command.

![upload csv to s3](https://user-images.githubusercontent.com/53040471/214310584-9fb11e0f-1641-4b06-b66a-4556c169cf28.jpg)


## 3 - PostgreSQL RDS data import and reporting

### Connect pgAdmin4 to PostgreSQL RDS
DB instance was successfully created inside AWS RDS console. The endpoint address was used to connect with production_server on local host. 

### Create the flights_analytics database
A new database called flight_db was sucessfully created using pgadmin4.

### Import the combined_data.csv file into the flights table
The combined_data.csv was successfully imported into flight_db database. The total number of columns is 24.

![upon import - 23 columns](https://user-images.githubusercontent.com/53040471/214314025-e9e688b1-2204-45e8-afcc-6db476e903a8.jpg)

### Explore the flights table and calculate some statictics

In order to verify the total number of records in the database, COUNT function was used. The returned number of records match with the total number of rows in the combined pandas dataframes.

![total number of records in db](https://user-images.githubusercontent.com/53040471/214315282-3e90e5d4-76f6-4a99-b4c8-eeebb45e8de0.jpg)

Further analysis uncovred that year 1987 was the year with the most number of flights.

![year wt highest number of flights](https://user-images.githubusercontent.com/53040471/214316295-b6f20732-29f1-40de-a34b-06e6031704bb.jpg)

The most popular destination gathered from the flights data is ORD (Orlando)

![destination wt highest number of flights ii](https://user-images.githubusercontent.com/53040471/214317497-6a194704-48fa-4663-a09e-ce47e610f00f.jpg)


## 4 - Integrate Tableau Desktop with PostgreSQL RDS

### Download and install Tableau Desktop
The download and installation processes were executed successfully.

### Configure the PostgreSQL connector and connect to the flights_analytics database RDS
Tableau was pointed to use database created inside AWS RDS  by using the same end point used to configure the production_server inside pgAdmin4.

## 5 - Create Tableau Reports

### Tableau data exploration
The total number of records reported inside Tableau matched with the postgreSQL database records. There are 24 columns and 42,722,968 rows.

![total number of records in tableau](https://user-images.githubusercontent.com/53040471/214321125-889d6799-3f8a-48f5-afe1-ec26f42b6dcc.jpg)

### Create a Tableau report for the historical flight origins and destinations
The graph below depicts the number of flights for each destination. The user would be able to view the result based year by clicking on the year button on the right hand side. The data has been sorted to be in descending order. 

![Highest flight destinations - filtered by year](https://user-images.githubusercontent.com/53040471/214322149-e69959b6-3975-4e0f-8092-71529eb3c1e4.jpg)

### Create a Tableau report for the average distance travelled
The bar chart below shows the average distance that each operator flew. The data was further filterred to allow users to see the bar graph based on year. The year dail is on the right hand side of the visual.

![Average distance that carriers travelled](https://user-images.githubusercontent.com/53040471/214323038-70d29a7b-90f5-4103-8214-9eb66e22f7e3.jpg)


### Cretae a Tableau report for the most used flight numbers
The line chart below was created by summing the count of both incoming (origin) and outgoing (destination) flights, against the flight numbers. Filters were applied to display only top five most used flight numbers and top most destination.

From the diagram below, the data suggest that the top five most used flight numbers are 711, 505, 456, 440 and 409. For all these most used flight numbers, the top destination and origin for the said flight numbers is ORD (Orlando)

![Most used flight number ii](https://user-images.githubusercontent.com/53040471/215365674-a4fd156a-dcad-4b18-a2bd-d751f404587c.jpg)


### Create a Tableau report for flights delays and cancellations
The dashboard below was created by combining three other worksheets. All the treemaps clearly rank and display the airports with highest number delays and cancellations.

![Delays_and_cancellations](https://user-images.githubusercontent.com/53040471/214324802-b71847e4-abdd-4636-b958-91a6a69f9f97.jpg)
