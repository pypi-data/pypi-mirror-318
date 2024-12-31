# Dynamic Router Example

This example demonstrates how to use the FastAPI Dynamic Router extension.

## Directory Structure

```
📦 routes
├── 📂 root
│   └── 📄 __init__.py          ➜  🌐 /
├── 📂 users
│   ├── 📄 __init__.py          ➜  🌐 /users
│   └── 📂 [user_id]
│       └── 📄 __init__.py      ➜  🌐 /users/{user_id}
└── 📂 products
    ├── 📄 __init__.py          ➜  🌐 /products
    └── 📂 [product_id]
        └── 📂 reviews
            └── 📄 __init__.py   ➜  🌐 /products/{product_id}/reviews
```

## Running the Example

```bash
python main.py
```

Visit http://localhost:8000/docs to see the API documentation.