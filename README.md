# Sample Python Script for Getting Facebook Posts

## Prerequisites
- Python 3.8 and up. Download here: 
- Facebook Account.

## How to Setup and Run

1. To start, please follow the following instructions to get the `access_token`: [How to use Facebook Graph API and extract data using Python!](https://towardsdatascience.com/how-to-use-facebook-graph-api-and-extract-data-using-python-1839e19d6999)

1. Put that `access_token` inside a `credentials.json` file, like this:  
`credentials.json`
```
{
    "access_token": "<Access Token>"
}
```

1. Create a Virtual Environment by executing the following:  
On Windows Command Prompt:
```
python3 -m venv .venv
.venv/Scripts/Activate.ps1
```
On Linux/Mac Terminal:
```
python3 -m virtualenv .venv
source .venv/bin/activate
```

1. Install the necessary packages inside the Virtual Environment:  
On Windows Command Prompt or Linux/Mac Terminal:
```
pip install -r requirements.txt
```

1. Run the script `sample_fb.py`
On Windows Command Prompt or Linux/Mac Terminal:
```
python sample_fb.py
```