## What is Ollama?
 
  Ollama is an open-source tool that allows you to run large language models (LLMs) locally on your machine.

## Install ollama in venv

  ## 1. Create a virtual Environment:

  #### i. For mac/linux:
    ```
    python3 -m venv .venv
    ```

  #### ii. For windows:
    ```
      python -m venv .venv
    ```

  ### 2.Activate the virtual environment:

  #### i. For windows:

    ```bash 
      .venv\Scripts\activate
    ```
    **If this won't work, just go to vscode and click `ctrl+shift+p` and select .venv from `python:select interpreter`.**

  #### ii. For mac/linux
    ```bash 
    source .venv/bin/activate
    ```

  ### 3. Install Ollama within the activated virtual environment:

  ```bash
    pip install ollama3.2:latest
  ```

  ### 4. After installation, you can run Ollama commands within the virtual environment. For example, to pull and run a model:

  ```bash
    ollama run llama3.2:latest
  ```