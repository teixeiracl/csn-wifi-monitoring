# CSN GEO WIFI

## COMO RODAR O DOCKER CONTENDO FRONT, API, BANCO E GEOSERVER
- Instale o docker e docker compose. [Documentação aqui](https://docs.docker.com/compose/install/);
- Clique [aqui](https://drive.google.com/file/d/1n77TidZlFQvViA5-zXF7DgKl2npX_5Og/view?usp=sharing) para baixar a imagem reogeferenciada.|
- Insira a imagem baixada na pasta raiz do projeto com o nome "CONGONHAS_2018_2019.tif";
- No terminal, navegue até este diretório e execute `docker-compose up --build`

- Instâncias:
    - FRONT: http://localhost:3000/
    - API: http://localhost:4011/
    - GEOSERVER: http://localhost:8080/geoserver