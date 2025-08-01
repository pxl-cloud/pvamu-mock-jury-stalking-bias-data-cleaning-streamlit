import os
import toml
import streamlit as st

def load_config() -> dict:
    """
    Loads the main Streamlit configuration file from the project root.

    This function automatically looks for the '.streamlit/config.toml' file
    at the root of the project, regardless of where this module is imported.

    Returns:
        dict: The parsed TOML configuration as a dictionary, or an
              empty dictionary if the file is not found or an error occurs.
    """
    # The path to the config file is hardcoded to be in the .streamlit folder
    # at the root of the project from which the Streamlit app is run.
    config_path = os.path.join(os.getcwd(), ".streamlit", "config.toml")
    
    if not os.path.exists(config_path):
        st.error(f"Configuration file not found: `{config_path}`. Please ensure it exists.")
        return {}
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = toml.load(f)
        return config
    except toml.TomlDecodeError as e:
        st.error(f"Error parsing TOML file `{config_path}`: {e}")
        return {}
    except Exception as e:
        st.error(f"An unexpected error occurred while loading `{config_path}`: {e}")
        return {}

# The function is available at the module level for direct import
# from slutils import load_config
