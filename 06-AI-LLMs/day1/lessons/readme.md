# AI - LLM
## Setup
- create a virtual environment
- python -m venv .venv
- source .venv/bin/activate
- which python3 (shows you the env youre curr using, can paste the path in the search bar if the venv you want to use doesn't appear)
- pip install --upgrade pip

## Specify version of python within the venv (pytorch supports 3.9-3.12)
- brew install python@3.9 ->mac
- sudo apt install python3.9 ->wsl

- python3.9 -m venv env39 (created venv using 3.9)

## Set up for pytorch(linux-cpu)
- https://pytorch.org/get-started/locally/
- pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### didnt need but written here for note purposes
- pip install torchvision
- pip install torch torchvision torchaudio
- python -c "import torch; print(torch.__version__)"

## Set up for Jupyter Notebook
- https://jupyter.org/install 
- Install Jupyter Notebook Extension through vsc extensions
- pip install jupyter
- pip install ipykernel
- touch main.ipynb (creates a Jupyter Notebook file)

## Selecting a kernal/creating one if venv doesnt show
- Asks you to install a kernal so you need to map it in the searchbar topmid
- select the venv you want to use
(if it doesn't show up you can add it using > select > python interpretor > Enter Interpreter path, run "which python" in the terminal while in the env and copy and paste the path up until the env/ and before the /bin, and then the interpretor should show up to be selected.)

## Test if the file is working correctly write this code
import torch
print(torch.__version__)

## Data from Kaggle
- https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability