# Installation

1. Install [Pipenv](http://docs.pipenv.org/en/latest/)
2. `pipenv install --dev`
3. `nameko run temperature`
4. `nameko run humidity`
5. `hug run -f main.py`

And obtain http://127.0.0.1:8000/hello, you should see message like following:
"Temperature is 17, Humidity is 39"
