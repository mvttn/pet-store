# Pet store regression suite

## Dev setup process

### Step 1: Clone the repository
```
git clone <repo_url>
cd <repo_directory>
```
### Step 2: Setup virtual environment using Python venv 
Use `python3 -m venv venv`  
Activate your virtual environment:  
For macOS/Linux:  
`source venv/bin/activate`  
For Windows:  
`.\venv\Scripts\activate`
### Step 3: Install python libraries
```
python -m pip install -r requirements.txt
```
You will need to activate your python environment each time you create a new terminal. To deactivate simply type
`deactivate` in your terminal.  

### Step 4: Running the tests:
Ensure your virtual environment is activated (if not already).  

Run the tests using `unittest`  
```python -m unittest tests/regression/test_pet_api.py``` 