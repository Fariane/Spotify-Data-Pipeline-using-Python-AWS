#  🎵 Spotify Data Pipeline (ETL) Project Using Python & AWS

## Overview
This project involves building an ETL (Extract, Transform, Load) pipeline using AWS services to collect and process data from Spotify playlists. The goal is to automate the extraction of music data, transform it into structured formats, and store it in AWS for further analysis and insights. The data is organized into separate tables for albums, artists, and tracks.

## Architecture
![Architecture Diagram](spotify_pipeline_architecture_dgrm.png)

## Key Components

### Data Extraction
- **Spotify API:** Retrieve music data, including track details, artist information, and albums, using the Spotify API.
- **Authentication:** Implement OAuth 2.0 for secure access to the Spotify API.
- **Scheduling:** Use Amazon CloudWatch to trigger the pipeline on a daily basis to automatically extract the latest data using Cron syntax
  
### Data Transformation
- **Data Cleaning:** Cleanse the raw data by handling missing values, duplicates, and inconsistencies.
- **Data Formatting:** Transform the data into structured formats (e.g., JSON or CSV) for compatibility with downstream processes.
- **Enrichment:** Add additional attributes or aggregate information to enhance the data for analysis.

### Data Loading
- **AWS S3:** Store both raw and processed data in AWS S3 for scalable and cost-effective storage.
- **AWS Glue:** Use AWS Glue and Crawler to infer schemas and create tables within the database.
- **AWS Athena:** Perform SQL analytics on the processed data stored in S3.
- **Data Partitioning:** Organize data into partitions based on attributes like date or category to optimize query performance.

## Project Execution Flow
1. **Data Extraction:** AWS Lambda function is triggered daily via Amazon CloudWatch to extract data from the Spotify API. Extracted data is stored in Amazon S3 (raw data).

2. **Data Transformation:** Another Lambda function is triggered by S3 object put event. It transforms the raw data and stores it in another Amazon S3 bucket (transformed data).

3. **Data Cataloging:** AWS Glue infers schema of the transformed data stored in S3, creating a data catalog.

4. **Querying:** Amazon Athena is used to query the data directly in S3 using standard SQL queries.


## Tools and Technologies

### AWS Services:
- **AWS Lambda:** For data extraction and transformation.
- **Amazon CloudWatch:** To trigger Lambda functions on a scheduled basis.
- **Amazon S3:** For storing raw and transformed data.
- **AWS Glue:** For inferring schema and creating a data catalog.
- **Amazon Athena:** For querying the data stored in S3.

### Programming Languages :
- **Python** for API interactions and ETL scripting

### Libraries:
- `spotipy` for Spotify API interactions, 
- `pandas` for data manipulation,
- `boto3` for interacting with AWS services

## Benefits
- **Automation:** The ETL pipeline automates the entire data processing workflow, reducing manual effort and ensuring up-to-date data.
- **Scalability:** Using AWS services ensures the solution can scale to handle large volumes of data efficiently.
- **Flexibility:** The modular design allows for easy integration with other data sources and analytics tools.

## Future Enhancements
- **Advanced Analytics:** Implement machine learning models to predict song popularity or detect trends in music genres.
- **Real-Time Streaming:** Consider transitioning to a real-time streaming solution to process live data from Spotify.
