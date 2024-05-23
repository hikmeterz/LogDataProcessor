# Log Data Processor

## Project Description
This repository contains Python scripts that process log data by extracting and transforming specific patterns. The provided scripts implement various tasks to clean and format log data, making it easier to analyze. The repository includes detailed implementations of these techniques and provides example usage on sample log files.

## Files
- `task1.py`: Python script for processing log data to extract specific patterns and transform them into a structured format.
- `task2.py`: Python script for another log data processing task, focusing on different patterns and transformations.
- `log_task1.txt`: Sample log file used for testing the script in `task1.py`.
- `output_task1.txt`: Output file generated by `task1.py`.
- `rapor.pdf`: Project report describing the implementation and results of the log data processing tasks.

## Python Script Descriptions

### `task1.py`
This Python script processes log data to extract specific patterns and transform them into a structured format. The script reads from an input log file, applies regular expressions to find matching patterns, and writes the cleaned and transformed data to an output file.

#### Key Features:
- Extracts IP addresses and timestamps from log entries.
- Cleans and transforms the extracted data by removing unnecessary characters and formatting it consistently.
- Writes the cleaned data to an output file.


### 'task2.py' 
This Python script performs another log data processing task. It focuses on extracting and transforming different patterns from the log data.

#### Key Features:
Extracts different patterns from log entries based on specified criteria.
Cleans and transforms the extracted data by applying specific formatting rules.
Writes the cleaned data to an output file.
Example Workflow
Extracting and Transforming Log Data
The script reads a log file, extracts specified patterns, and transforms them into a structured format.
Writes the cleaned and transformed data to an output file.

### task1()
This function extracts IP addresses and timestamps from log entries, cleans them, and writes the structured data to an output file.

Steps:
Read the log file using Python's file handling functions.
Apply regular expressions to find matching patterns.
Clean and transform the extracted data by removing unnecessary characters and formatting it.
Write the cleaned data to an output file.

