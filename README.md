# Twitter API

### Author: David Abadi, 2020-02-09

API to read your twitter home feed and transform feed images to text.

### Usage

Copy github repository and set your Twitter API keys in the key.py file and create a key.json file with the Google Cloud API key. Set the GOOGLE_APPLICATION_CREDENTIALS enviroment variable to the json file you just created.

To run and test:

```
python api.py
curl http://127.0.0.1:5000/
```

or on the web browser navigate to http://127.0.0.1:5000/