# FrameAPI
Fast and Light Python Web Framework

## Installation
Create and activate virtual env and then install the framework:

``` py
pip install frameapi
```

## Usage
- Create a file `app.py`:

``` py
from frameAPI import FrameAPI

app = FrameAPI()

app.welcome()
```

- Run the server:

``` 
gunicorn app:app --reload
```

- Open your browser at <a href="http://127.0.0.1:8000" class="external-link" target="_blank">http://127.0.0.1:8000</a>.
