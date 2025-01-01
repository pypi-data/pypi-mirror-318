# streamlit-custom-component

Streamlit component that allows you to do X

## Installation instructions

```sh
pip install streamlit-browser-transcribe
```

## Usage instructions
```python
import streamlit as st

from browser_transcribe import browser_transcribe

value = browser_transcribe()

st.write(value) # this value is the transcribed string
```