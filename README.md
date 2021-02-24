# How to Run Tests 

## Import Project
 ```Use Pycharm to import the project```

## Install Pipenv
```pip install pipenv```<br />
```pipenv install```

## Install all dependencies from Pipfile
```pipenv install --dev```

## Enter into shell
```pipenv shell```

## Set Project Path
```export PYTHONPATH="${PYTHONPATH}:/path/to/project/directory"```

## Run All Tests
```pytest -v Tests```

## Run test scenarios for Pet API
```Scenario 1: pytest -m Pet_scenario_1```<br />
```Scenario 2: pytest -m Pet_scenario_2```<br />
```Scenario 3: pytest -m Pet_scenario_3```<br />
```Scenario 4: pytest -m Pet_scenario_4```

## Run test scenarios for User API
```Scenario 1: pytest -m User_scenario_1```<br />
```Scenario 2: pytest -m User_scenario_2```<br />
```Scenario 3: pytest -m User_scenario_3```<br />
```Scenario 4: pytest -m User_scenario_4```<br />
```Scenario 5: pytest -m User_scenario_5```

## To Run Report
```pytest --html=report.html```