# Distiluse Transformer
Given a list of paragraphs we need to calculate their embeddings with the chosen model 'distiluse-base-multilingual-cased-v1', save those embeddings to disk and be able to retrieve them every time the application is restarted, this way we avoid the loading time.

Things to keep in mind:

* The list of paragraphs is in the attached file, each row of the file is a paragraph.
* Paragraphs cannot exceed 512 tokens, so if they exceed 512 we must apply some logic to truncate them into 2 paragraphs. The logic to be applied is up to the candidate's choice, it is not advisable to cut off abruptly when reaching 512 tokens. You could go backwards until you find a '.' or ',', capital '... These are options, you can use one of these or any other of your choice.
* We filter out paragraphs with less than 50 tokens as we consider them irrelevant to our semantic search.
* We must sanitise the paragraphs to ensure that they do not contain extraneous parameters.
* Assuming that the library to calculate the tokens of each paragraph is expensive and we don't want to call it every time we run local tests, we should mock that call in the tests so that we don't make the call to the library and the expected value is automatically returned.

# Project Structure
    ├── README.md
    ├── requirements.txt
    ├── src
    │   ├── app
    │   │   ├── checkers.py
    │   │   ├── data
    │   │   ├── model
    │   │   ├── processing.py
    │   │   └── wrangling.py
    │   ├── main.py
    │   
    ├── tests
    │   ├── test_checkers.py
    │   ├── test_processing.py
    │   └── test_wrangling.py

# Installation
- Install python

        sudo apt update

        sudo apt install python3.9.7

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAl/distiluse-transformer.git

- Install virtual enviroment: 

        sudo apt-get install python3-pip

        sudo pip3 install virtualenv

        virtualenv venv

        source venv/bin/activate

- Install requirements

        pip install -r requirements.txt

- Run Tests

        python3 -m unittest discover tests/

# Output

At the end of the training, the model is automatically saved `/src/app`
