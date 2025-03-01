Criar DATABASE e TABLE:

-- Verificar se o banco de dados já existe e criar se não existir
CREATE DATABASE IF NOT EXISTS rack_management;

-- Usar o banco de dados rack_management
USE rack_management;

-- Verificar se a tabela connections já existe e criar se não existir
CREATE TABLE IF NOT EXISTS connections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    switch_port VARCHAR(50) NOT NULL,
    patch_panel_port VARCHAR(50) NOT NULL
);


-------------------------------------------
COMANDOS EM TERMINAL:

pip install Flask mysql-connector-python

python app.py
-------------------------------------------