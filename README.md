Dream PC Builder

This program is designed to help you find the best combination of PC components (CPU, GPU, RAM, and SSD)
that you can purchase within a given budget. The program reads component data from CSV files, including
the component name, price, and benchmark score. It then searches for the optimal combination of these
components to maximize the total benchmark score without exceeding the budget.

The program supports two methods for finding the best combination:
1. Branch and Bound: Generates all possible combinations and iteratively finds the optimal one.
2. Backtracking: Uses a recursive approach to explore possible combinations and track the best one.

Progress of the search is tracked and printed periodically for both methods to give an indication of the
number of nodes explored.

CSV Files:
- cpu_data.csv
- gpu_data.csv
- ram_data.csv
- ssd_data.csv

CSV Format:
The CSV files should have the following columns:
Type,Part Number,Brand,Model,Rank,Benchmark,Samples,URL,Component Name,Price

User Input:
- Budget: The maximum amount of money available to spend on the components.
- Method: The search method to use ('branch_and_bound' or 'backtracking').

Output:
- The best combination of components within the budget, including their total price and benchmark score.

Usage:
- Run the app.py

Credits:
- Benchmark scores provided by UserBenchmark (https://www.userbenchmark.com).
