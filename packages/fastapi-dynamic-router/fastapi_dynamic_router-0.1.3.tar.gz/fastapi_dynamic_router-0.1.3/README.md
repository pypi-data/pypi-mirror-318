# FastAPI Dynamic Router

FastAPI extension that provides automatic and dynamic route registration for FastAPI applications, inspired by Next.js's file-system based routing.

## Installation

```bash
pip install fastapi-dynamic-router
```

## How to Use

### Basic Setup

```python
from fastapi import FastAPI
from fastapi_dynamic_router import DynamicRouter

# Create FastAPI app
app = FastAPI()

# Initialize the router
router = DynamicRouter(app)

# Register routes from a directory
router.register_routes('routes')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
```

### Route Examples

1. **Basic Route** (`routes/root/__init__.py`):
```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def index():
    return {'message': 'Welcome to the API'}
```

2. **Dynamic Parameter** (`routes/users/[user_id]/__init__.py`):
```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_user(user_id: str):
    return {'message': f'User details for ID: {user_id}'}
```

3. **Nested Routes** (`routes/products/[productID]/reviews/__init__.py`):
```python
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def get_reviews(product_id: str):
    return {'message': f'Reviews for product ID: {product_id}'}
```

### Configuration Options

```python
# Make routes case-insensitive
app.state.dynamic_router_config['case_sensitive'] = False

# Add a global prefix to all routes
app.state.dynamic_router_config['prefix'] = '/api/v1'
```

## Directory Structure

The router follows a convention-based approach where your directory structure maps directly to URL routes:

```
📦 routes
├── 📂 Root
│   ├── 📄 __init__.py          ➜  🌐 /
│   ├── 📂 version
│   │   └── 📄 __init__.py      ➜  🌐 /version
│   └── 📂 about
│       └── 📄 __init__.py      ➜  🌐 /about
│
├── 📂 users
│   ├── 📄 __init__.py          ➜  🌐 /users
│   ├── 📂 [userID]             ➜  💫 Dynamic Parameter
│   │   ├── 📄 __init__.py      ➜  🌐 /users/{user_id}
│   │   └── 📂 profile
│   │       └── 📄 __init__.py  ➜  🌐 /users/{user_id}/profile
│   └── 📂 settings
│       └── 📄 __init__.py      ➜  🌐 /users/settings
│
└── 📂 products
    ├── 📄 __init__.py          ➜  🌐 /products
    └── 📂 [productID]          ➜  💫 Dynamic Parameter
        └── 📄 __init__.py      ➜  🌐 /products/{product_id}
```

## Route Mapping Examples

| Directory Structure | Generated Route | Type |
|--------------------|-----------------|------|
| `Root/__init__.py` | `/` | Static Route |
| `users/__init__.py` | `/users` | Static Route |
| `users/[userID]/__init__.py` | `/users/{user_id}` | Dynamic Route |
| `Products/[productID]/__init__.py` | `/products/{product_id}` | Dynamic Route |

## Dynamic Parameters

Dynamic parameters are defined using square brackets in directory names:
- 📂 `[userID]` ➜ `{user_id}`
- 📂 `[productID]` ➜ `{product_id}`
- 📂 `[categoryName]` ➜ `{category_name}`

## License

This project is licensed under the MIT License - see the LICENSE file for details.