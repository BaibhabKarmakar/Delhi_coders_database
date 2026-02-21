# Delhi Coders Database

A simple yet practical **Python data analysis project** to strengthen core Python concepts while working with real-world-ish social network data.

This project simulates a mini social platform (like an early Facebook/LinkedIn for coders) focused on **Delhi-based developers**. It includes:

- Data cleaning & restructuring
- Basic insight extraction
- Recommendation features:  
  - **People You May Know** (based on mutual friends/connections)  
  - **Pages You May Like** (based on liked pages & friend interests)

Built **only with Python** (no external frameworks or ML libraries) to practice file handling, lists/dictionaries, sets, functions, loops, and logical thinking.

## Project Structure
``` bash
Delhi_coders_database/
├── raw_data.json                # Original messy input data (users + pages)
├── data.json                    # Intermediate file (after initial processing)
├── cleaned_data.json            # Final cleaned & restructured dataset
│
├── data_cleaning_and_restructure.py    # Cleans data: removes duplicates, empty names, inactive users, etc.
├── extract_insights.py                 # Basic statistics and analysis of the network
├── people_you_may_know.py              # Implements "People You May Know" recommendation logic
└── pages_you_may_like.py               # Implements "Pages You May Like" recommendation logic
```


## Features Implemented

- **Data Cleaning**  
  - Remove users with blank/empty names  
  - Deduplicate friends lists  
  - Filter out inactive users (no friends & no liked pages)  
  - Remove duplicate pages by ID  

- **Insights Extraction**  
  - Count total users, pages, connections  
  - Most popular pages  
  - Most connected users  
  - Basic network statistics  

- **Recommendation Engines** (simple rule-based)  
  - **People You May Know** — suggests users who share mutual friends  
  - **Pages You May Like** — suggests pages liked by your friends but not by you  

## How to Run

1. Make sure you have **Python 3.6+** installed.
2. Clone the repo:

   ```bash
   git clone https://github.com/BaibhabKarmakar/Delhi_coders_database.git
   cd Delhi_coders_database
   ```
3. Run the scripts in this recommended order:
   ``` bash
   # 1. Clean and restructure the raw data
    python data_cleaning_and_restructure.py
    
    # 2. See basic insights
    python extract_insights.py
    
    # 3. Generate recommendations for a specific user (edit user ID inside the file)
    python people_you_may_know.py
    python pages_you_may_like.py
   ```
## Technologies Used:
  Python 3 (only standard library — no pip installs required)
  JSON file handling
  List, dict, set operations
  
  Learning Objectives
  This project was created to practice:
  
  Reading & writing JSON files
  Data validation and cleaning
  Working with nested data structures
  Implementing simple graph-like algorithms (friends network)
  Building basic recommendation logic without libraries
  Modular code organization (separate scripts for different features)

## Contributing
Contributions, bug fixes, and improvements are very welcome!
Just open an issue or submit a pull request.


