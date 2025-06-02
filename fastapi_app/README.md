# FastAPI App - Trabalho Faculdade

## Como rodar

1. Instale as dependências (de preferência em um ambiente virtual):

    ```bash
    pip install -r requirements.txt
    ```

2. Rode o servidor FastAPI:

    ```bash
    uvicorn main:app --reload
    ```

3. Acesse a documentação interativa em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints implementados

- `GET /user/{user_id}`: Path Parameter
- `GET /color/{color}`: Path Parameter com Enum
- `GET /product/{product_id}`: Path Parameter com Path (validação)
- `GET /optional/{item_id}`: Path Parameter opcional
- `GET /search/`: Múltiplos Query Parameters
- `GET /products/`: Múltiplos Query Parameters
- `POST /user/`: Recebe Body e valida com User (Pydantic)
- `POST /product/`: Recebe Body e valida com Product (Pydantic)

Todos os requisitos do trabalho estão contemplados.

4. Para rodas a FAST API
//Chegar até a pagina da API
- `cd fastapi_app`
//Para instalar as dependências
- `pip install -r requirements.txt`

//Para iniciar a API
- `uvicorn main:app --reload`
