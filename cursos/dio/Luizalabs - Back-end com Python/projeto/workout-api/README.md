# Workout API

API REST desenvolvida como **projeto de estudo do curso** *[Luizalabs — Back-end com Python](https://github.com/alanliveira/courses)*, com foco no aprendizado do **FastAPI**.

O objetivo é praticar os conceitos essenciais de um backend moderno em Python: rotas e controllers, validação com Pydantic, injeção de dependência, persistência com SQLAlchemy (async) e versionamento de banco com Alembic.

> **Status:** projeto em construção — feito durante o curso, alguns endpoints ainda estão sendo implementados.

---

## Stack Tecnológica

| Camada | Tecnologia |
|--------|-----------|
| Framework web | **FastAPI** |
| Validação / schemas | **Pydantic v2** |
| ORM | **SQLAlchemy 2.0** (modo async) |
| Banco de dados | **SQLite** (via `aiosqlite`) |
| Migrations | **Alembic** |
| Servidor | **Uvicorn** |
| Gerenciamento de pacotes | **uv** |
| Linguagem | **Python 3.14** |

---

## Conceitos do FastAPI praticados neste projeto

- **Separation of Concerns:** `models` (ORM / banco) separados de `schemas` (entrada e saída da API).
- **Dependency Injection:** o `DatabaseDependency` injeta uma `AsyncSession` nos endpoints automaticamente.
- **Response models:** cada rota declara `response_model`, e o FastAPI valida/serializa a resposta.
- **Async de ponta a ponta:** endpoints `async` + driver assíncrono (`aiosqlite`) + `AsyncSession`.
- **Documentação automática:** Swagger (`/docs`) e ReDoc (`/redoc`) gerados a partir dos schemas.
- **Configuração por variáveis de ambiente:** usando `pydantic-settings`.

---

## Entidades

O domínio modela uma academia/centro de treinamento:

- **Athlete (Atleta):** `name`, `cpf` (único), `age`, `weight`, `height`, `gender`, `created_at`.
  Possui chaves estrangeiras para `Category` e `TrainingCenter`.
- **Category (Categoria):** `name` (único).
- **Training Center (Centro de Treinamento):** `name`, `address`, `owner` (único).

Relacionamentos:

```
Category (1) ──────< (N) Athlete
TrainingCenter (1) ──< (N) Athlete
```

> Cada tabela possui um `pk_id` (inteiro, chave primária) e um `id` (UUID) herdado do `BaseModel` compartilhado — abordagem usada no curso para expor identificadores não sequenciais na API.

---

## Estrutura do Projeto

| Caminho | Responsabilidade |
|---------|------------------|
| `src/api/configs/` | App, rotas, banco, settings e dependências |
| `src/api/controllers/` | Endpoints da API (athletes, categories, training_center) |
| `src/api/models/` | Models SQLAlchemy — camada de persistência (banco) |
| `src/api/schemas/` | Schemas Pydantic — contrato de entrada/saída (request/response) |
| `src/api/repositories/` | (em breve) abstração de acesso a dados |
| `src/api/shared/` | `BaseModel` e `BaseSchema` compartilhados |
| `alembic/` | Configuração do Alembic (migrations) |
| `alembic/versions/` | Arquivos de migration gerados |
| `alembic.ini` | Arquivo de configuração do Alembic |
| `pyproject.toml` | Metadados e dependências do projeto (gerenciado pelo `uv`) |
| `workout.db` | Banco SQLite local (gerado na execução, ignorado pelo git) |

> **Por que `models` e `schemas` separados?** Os `models` representam as **tabelas do banco** (SQLAlchemy) e os `schemas` definem o **contrato da API** (Pydantic). Essa separação evita expor a estrutura interna do banco e permite validar entrada e saída de forma independente — um dos conceitos centrais praticados no curso.

---

## Setup do Projeto (uv)

Todo o setup é feito com o [uv](https://docs.astral.sh/uv/), que cuida de criar o ambiente virtual e instalar as dependências automaticamente.

### 1. Instalar o `uv`

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# ou via pip (qualquer plataforma)
pip install uv
```

Confirme a instalação:

```bash
uv --version
```

### 2. Entrar no diretório do projeto

```bash
cd "cursos/dio/Luizalabs - Back-end com Python/projeto/workout-api"
```

### 3. Sincronizar as dependências

```bash
uv sync
```

Esse comando, a partir do `pyproject.toml` e do `.python-version`:

- Cria o ambiente virtual em `.venv`
- Instala todas as dependências (FastAPI, SQLAlchemy, Alembic, etc.)
- Usa a versão correta do Python (3.14) automaticamente

### 4. Verificar a instalação

```bash
uv run python --version
uv run fastapi --version
```

Ambiente pronto. Agora siga para **Executar a API**.

---

## Executar a API

### Subir o servidor de desenvolvimento

```bash
uv run fastapi dev
```

A API sobe em `http://localhost:8000` com **reload automático** a cada alteração de código.

- Documentação (Swagger): <http://localhost:8000/docs>
- Documentação (ReDoc): <http://localhost:8000/redoc>

### Aplicar as migrations do banco

```bash
uv run alembic upgrade head
```

Para gerar uma nova migration após alterar os models:

```bash
uv run alembic revision --autogenerate -m "descricao da mudanca"
```

---

## Configuração

As configurações são lidas de variáveis de ambiente (ou de um arquivo `.env`), via `pydantic-settings` (`src/api/configs/settings.py`):

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DATABASE_URL` | URL de conexão do banco (driver async) | `sqlite+aiosqlite:///./workout.db` |

> O mesmo arquivo `workout.db` é usado tanto pela aplicação (driver async `aiosqlite`) quanto pelo Alembic (driver síncrono `pysqlite`).

---

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/athletes/` | Criar um novo atleta |
| `GET` | `/categories/` | Criar uma categoria |
| `GET` | `/training_center/` | Listar centros de treinamento |
| `GET` | `/training_center/{id}` | Detalhar um centro de treinamento |
| `POST` | `/training_center/` | Criar um centro de treinamento |

> Os detalhes de cada rota (corpo, respostas e códigos de status) podem ser consultados interativamente no Swagger em `/docs`.

---

## Licença

Projeto acadêmico/estudo. Consulte o repositório do curso para mais detalhes.
