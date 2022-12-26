# Distiluse Transformer
Dada una lista de parrafos necesitamos calcular sus embeddings con el modelo elegido ‘distiluse-base-multilingual-cased-v1’, guardar esos embeddings en disco y poder recuperarlos cada vez que la aplicacion se reinicie, de esta manera evitamos el tiempo de carga.

Cosas a tener en cuenta:

* La lista de parrafos se encuentra en el fichero adjunto, cada fila del fichero es un parrafo.
* Los parrafos no pueden superar los 512 tokens, por lo que si superasen 512 debemos aplicar alguna logica para truncarlos en 2 parrafos. La logica a aplicar es a eleccion del candidato, se desaconseja cortar bruscamente simplemente al llegar a 512 tokens. Se podria retroceder hasta encontrar un ‘.’ o ’,’, mayuscula… Son opciones, se puede usar una de esas o cualquier otra que decida el candidatos.
* Filtramos los parrafos con menos de 50 tokens ya que los consideramos irrelevantes de cara a nuestra busqueda semantica.
* Debemos sanitizar los parrafos para asegurarnos de que no contengan parametros extraños.
* Suponiendo que la libreria para calcular los tokens de cada parrafo fuese costosa y no nos conviene llamarla cada vez que ejecutamos tests en local, mockear esa llamada en los test de manera que no llegue a realizar la llamada a la libreria y que se devuelva automaticamente el valor esperado.

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

# Output

At the end of the training, the model is automatically saved `/src/app`
