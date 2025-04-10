# Grade Sorter App

## Description
A Python application that collects, validates, sorts, and analyzes student grades. The program handles grade input validation, sorts grades in descending order, and provides feedback on grade performance.

## Features
- Input validation ensuring grades are between 0-100
- Helpful error messages for invalid inputs
- Automatic grade sorting in descending order
- Removal of lowest two grades
- Display of original and sorted grades
- Final grade analysis with highest grade feedback

## Technical Details
- Input validation using try/except blocks
- Numerical range validation (0-100)
- Dynamic list manipulation using sort() and pop()
- Formatted string output for clear user feedback

## Usage
1. Run the program
2. Enter four numerical grades when prompted
   - Grades must be between 0 and 100
   - Non-numerical inputs will trigger error messages
3. View your original grades
4. See grades sorted from highest to lowest
5. Watch as lowest grades are removed
6. Receive feedback on your highest grade

## Requirements
- Python 3.x