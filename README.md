[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8jF9KApJ)
# Data Engineering Challenge

An implementation of core data engineering concepts using Python and SQL, with GitHub Codespaces integration.

## Objective
In this challenge, you work as a Data Engineer for a retail banking company. Your task is to build an ETL (Extract, Transform, Load) pipeline that processes the bank’s transaction data. The company collects various transaction types, customer ages, and balances, and they need a system to extract this data from raw files, clean and transform it, and load it into a database for analysis.

You will work with a dataset containing 100 rows of customer IDs, ages, transaction types, and balances, which is provided in the repository as `bank_transactions_dataset.csv`. Your task is to implement the ETL pipeline to process this data.

---

## Getting Started
1. Once you accept the assignment, you will be redirected to your own copy of the repository.
2. The repo is forked, and you only need to commit the changes that you make in the Python files. 
3. **Use GitHub Codespaces**:
   - Click on the green **Code** button in your forked repository.
   - Select **Codespaces** and choose "Create codespace on main" to open your development environment.

4. The repository includes a pre-configured `devcontainer.json` file, which automatically sets up the Python environment in Codespaces.
5. Once the Codespace is ready and the environment is set up, review the code in the Python files to understand the structure.
6. A `requirement.txt` file is added in the repo, which pre-installs the required libraries for the challenge (do not modify; if you do then run pip).
7. `.devcontainer`, `tests`, `.gitignore` and `.github` are protected files and they SHOULD NOT be altered.
8. Implement the missing functions marked with **TODO** comments.
9. Test your implementation by running the `main.py` file inside GitHub Codespaces.
10. Once the Codespace changes are committed, your project will be automatically submitted for review. 

---

## Steps to Follow
1. Accept the assignment to obtain your forked repository and set up your environment using **GitHub Codespaces**.
2. ### Task1: Data Extraction(8 marks)

**`extract.py`**: Implement the logic to extract data from the `bank_transactions_dataset.csv`.
  
3. ### Task2: Data Transformation(20 marks)

 **`transform.py`**: Implement the transformation logic (e.g., handle missing values, data normalisation).

4. ### Task3: Data Loading (12 marks)
    
   **`load.py`**: Implement the loading logic to insert the cleaned data into a SQLite database.

5. Run the codes inside **GitHub Codespaces** to test your implementation.
6. After completing the coding on those three files, examine the ETL pipeline in **main.py**.
7. Run the **`main.py`** to complete the ETL challenge; your final `SQL_database` will be created in the repo.
8. Commit the changes using the COMMIT button (green) available in the codespace.


---

## Tips
- Make sure you handle different data types properly (e.g., strings, integers, floats).
- Use the SQLite library in Python to interact with the database.
- Ensure data quality checks are in place after the transformation step.
- You can Run 'pytest' in the command line to test the python files.

---

## Submission Guidelines
After completing the challenge, commit the changes using the commit button available in the codespace. Make sure the changes have been successfully committed.

---

## Evaluation Criteria
- Correct implementation of the ETL pipeline (extract, transform, load).
- Proper handling of missing or invalid data.
- Accurate data insertion into the SQLite database.
- Clean and readable code with appropriate comments and structure.
- Successful execution of the project within **GitHub Codespaces**.

Good luck, and happy coding!
