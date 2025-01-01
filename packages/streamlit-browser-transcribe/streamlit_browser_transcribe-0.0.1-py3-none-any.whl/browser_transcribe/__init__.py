import os
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend")
_component_func = components.declare_component("browser_transcribe", path=build_dir)

def browser_transcribe():
  value = _component_func()
  return value