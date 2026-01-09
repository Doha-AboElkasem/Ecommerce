# E-Commerce Backend API

A robust Django REST Framework backend API for an e-commerce platform. This project provides a complete solution for managing products, shopping carts, orders, reviews, and customer interactions.

## Project Description

This is a full-featured e-commerce backend built with Django 6.0 and Django REST Framework. The API supports product catalog management, shopping cart functionality, order processing, coupon/discount system, product reviews, and customer contact features. The backend is designed to work seamlessly with frontend applications and includes CORS support for cross-origin requests.

## Features

- **Product Management**: Complete product catalog with categories, images, stock management, and product details
- **Shopping Cart**: Session-based shopping cart with add, update, and remove functionality
- **Order Processing**: Secure order creation with address management and order items tracking
- **Coupon System**: Discount coupon management with validation and expiration handling
- **Product Reviews**: Customer reviews and ratings system with testimonials
- **Category Management**: Organized product categorization with images
- **Contact Form**: Customer contact message handling
- **Product Sorting & Filtering**: Sort products by popularity, price, latest, and ratings
- **Home Page Data**: API endpoint for homepage with trending and popular products
- **Shop Page**: Browse products with various sorting options

## Installation Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd ecommerce/back-end/ecommerce
```

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Database Migrations

```bash
cd src
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

This allows you to access the Django admin panel at `http://localhost:8000/admin/`

## Environment Variables

The project uses Django's default settings. For production, you should set the following environment variables:

- `SECRET_KEY`: Django secret key (currently set in settings.py - **change this for production**)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Add your domain(s) for production
- `DATABASE_URL`: If using a different database (PostgreSQL, MySQL, etc.)

You can create a `.env` file in the project root and use `python-decouple` or `django-environ` to manage environment variables.

**Note**: The current `SECRET_KEY` in `settings.py` is for development only. **Never use this in production!**

## Running the Project

1. Navigate to the `src` directory:

   ```bash
   cd src
   ```

2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

3. The API will be available at:

   ```
   http://localhost:8000/
   ```

4. Access the Django admin panel at:
   ```
   http://localhost:8000/admin/
   ```

## API Endpoints

### Home Page

**GET** `/api/home/`

Returns homepage data including categories, trending products, popular products, and customer reviews.

**Response Example:**

```json
{
  "trending_products": [
    {
      "id": 1,
      "name": "Product Name",
      "price": "29.99",
      "image": "/media/products/2024/01/15/product.jpg",
      "slug": "product-name",
      "category": 1
    }
  ],
  "categories": [
    {
      "id": 1,
      "name": "Category Name",
      "image": "/media/categories/2024/01/15/category.jpg",
      "slug": "category-name"
    }
  ],
  "popular_products": [...],
  "customers_reviews": [...]
}
```

### Shop Page

**GET** `/api/shop/`

Returns a list of available products with optional sorting.

**Query Parameters:**

- `sort_by` (optional): Sort products by:
  - `popularity` - Sort by sales count
  - `average_rating` - Sort by average rating
  - `latest` - Sort by creation date (newest first)
  - `price_low_to_high` - Sort by price (ascending)
  - `price_high_to_low` - Sort by price (descending)

**Response Example:**

```json
{
  "products": [
    {
      "id": 1,
      "name": "Product Name",
      "price": "29.99",
      "image": "/media/products/2024/01/15/product.jpg",
      "slug": "product-name",
      "category": 1
    }
  ]
}
```

### Product Detail

**GET** `/api/product/<slug>/`

Returns detailed information about a specific product including reviews count and average rating.

**Parameters:**

- `slug` (path parameter): Product slug identifier

**Response Example:**

```json
{
  "product": {
    "id": 1,
    "name": "Product Name",
    "category": 1,
    "description": "Product description",
    "image": "/media/products/2024/01/15/product.jpg",
    "price": "29.99",
    "stock": 100,
    "available": true,
    "slug": "product-name",
    "reviews_count": 15,
    "average_rating": 4.5
  },
  "related_products": [...]
}
```

### Shopping Cart

**GET** `/api/cart/`

Retrieves the current shopping cart contents.

**Response Example:**

```json
{
  "items": [
    {
      "product": {
        "id": 1,
        "name": "Product Name",
        "price": "29.99",
        "image": "/media/products/2024/01/15/product.jpg",
        "slug": "product-name"
      },
      "quantity": 2,
      "price": 29.99,
      "total_price": 59.98
    }
  ],
  "total_cart_price": 59.98,
  "discount_amount": 0.0,
  "final_price": 59.98,
  "total_items": 1,
  "has_coupon": false,
  "coupon_code": null
}
```

**POST** `/api/cart/`

Adds a product to the cart or applies a coupon.

**Request Body (Add to Cart):**

```json
{
  "action": "add",
  "product_id": 1,
  "quantity": 2
}
```

**Request Body (Apply Coupon):**

```json
{
  "action": "apply_coupon",
  "code": "DISCOUNT10"
}
```

**PATCH** `/api/cart/`

Updates the quantity of a product in the cart.

**Request Body:**

```json
{
  "product_id": 1,
  "quantity": 3
}
```

**DELETE** `/api/cart/`

Removes a product from the cart or removes an applied coupon.

**Request Body (Remove Product):**

```json
{
  "action": "remove_product",
  "product_id": 1
}
```

**Request Body (Remove Coupon):**

```json
{
  "action": "remove_coupon"
}
```

### Coupon Management

**POST** `/api/coupon/apply/`

Applies a discount coupon to the cart.

**Request Body:**

```json
{
  "code": "DISCOUNT10"
}
```

**Response Example:**

```json
{
  "message": "Coupon applied successfully"
}
```

**DELETE** `/api/coupon/apply/`

Removes the applied coupon from the cart.

**Response Example:**

```json
{
  "message": "Coupon removed"
}
```

### Checkout

**POST** `/api/checkout/`

Creates an order from the current cart.

**Request Body:**

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "company_name": "Company Inc.",
  "country": "United States",
  "address_1": "123 Main St",
  "address_2": "Apt 4B",
  "city": "New York",
  "state": "NY",
  "zip_code": "10001",
  "phone": "+1234567890",
  "email": "john.doe@example.com",
  "additional_info": "Please leave at the door"
}
```

**Response Example:**

```json
{
  "message": "Order placed successfully",
  "order_id": 1
}
```

### Contact Form

**POST** `/api/contact/`

Submits a contact message.

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1234567890",
  "message": "Your message here"
}
```

**Response Example:**

```json
{
  "message": "Contact message sent successfully."
}
```

## How the Frontend Can Use the API

### Basic Setup

The API is configured to accept requests from `http://localhost:3000` (CORS enabled). For production, update `CORS_ALLOWED_ORIGINS` in `settings.py`.

### Using Fetch API

#### Fetch Products (Shop Page)

```javascript
// Get all products sorted by price (low to high)
fetch("http://localhost:8000/api/shop/?sort_by=price_low_to_high")
  .then((response) => response.json())
  .then((data) => {
    console.log(data.products);
  })
  .catch((error) => console.error("Error:", error));
```

#### Fetch Product Detail

```javascript
const productSlug = "product-name";
fetch(`http://localhost:8000/api/product/${productSlug}/`)
  .then((response) => response.json())
  .then((data) => {
    console.log(data.product);
    console.log(data.related_products);
  })
  .catch((error) => console.error("Error:", error));
```

#### Add to Cart

```javascript
fetch("http://localhost:8000/api/cart/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  credentials: "include", // Important for session-based cart
  body: JSON.stringify({
    action: "add",
    product_id: 1,
    quantity: 2,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

#### Get Cart Contents

```javascript
fetch("http://localhost:8000/api/cart/", {
  credentials: "include", // Important for session-based cart
})
  .then((response) => response.json())
  .then((data) => {
    console.log(data.items);
    console.log(data.total_cart_price);
    console.log(data.final_price);
  })
  .catch((error) => console.error("Error:", error));
```

#### Update Cart Item Quantity

```javascript
fetch("http://localhost:8000/api/cart/", {
  method: "PATCH",
  headers: {
    "Content-Type": "application/json",
  },
  credentials: "include",
  body: JSON.stringify({
    product_id: 1,
    quantity: 5,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

#### Remove Item from Cart

```javascript
fetch("http://localhost:8000/api/cart/", {
  method: "DELETE",
  headers: {
    "Content-Type": "application/json",
  },
  credentials: "include",
  body: JSON.stringify({
    action: "remove_product",
    product_id: 1,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

#### Apply Coupon

```javascript
fetch("http://localhost:8000/api/coupon/apply/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  credentials: "include",
  body: JSON.stringify({
    code: "DISCOUNT10",
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

#### Create Order (Checkout)

```javascript
fetch("http://localhost:8000/api/checkout/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  credentials: "include",
  body: JSON.stringify({
    first_name: "John",
    last_name: "Doe",
    company_name: "",
    country: "United States",
    address_1: "123 Main St",
    address_2: "",
    city: "New York",
    state: "NY",
    zip_code: "10001",
    phone: "+1234567890",
    email: "john.doe@example.com",
    additional_info: "",
  }),
})
  .then((response) => response.json())
  .then((data) => {
    console.log("Order ID:", data.order_id);
  })
  .catch((error) => console.error("Error:", error));
```

### Using Axios

If you prefer using Axios, here's an example setup:

```javascript
import axios from "axios";

// Configure axios instance
const api = axios.create({
  baseURL: "http://localhost:8000/api",
  withCredentials: true, // Important for session-based cart
  headers: {
    "Content-Type": "application/json",
  },
});

// Fetch products
const getProducts = async (sortBy = "latest") => {
  try {
    const response = await api.get(`/shop/?sort_by=${sortBy}`);
    return response.data.products;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};

// Add to cart
const addToCart = async (productId, quantity = 1) => {
  try {
    const response = await api.post("/cart/", {
      action: "add",
      product_id: productId,
      quantity: quantity,
    });
    return response.data;
  } catch (error) {
    console.error("Error adding to cart:", error);
    throw error;
  }
};

// Get cart
const getCart = async () => {
  try {
    const response = await api.get("/cart/");
    return response.data;
  } catch (error) {
    console.error("Error fetching cart:", error);
    throw error;
  }
};

// Apply coupon
const applyCoupon = async (code) => {
  try {
    const response = await api.post("/coupon/apply/", { code });
    return response.data;
  } catch (error) {
    console.error("Error applying coupon:", error);
    throw error;
  }
};

// Checkout
const checkout = async (orderData) => {
  try {
    const response = await api.post("/checkout/", orderData);
    return response.data;
  } catch (error) {
    console.error("Error during checkout:", error);
    throw error;
  }
};
```

### Important Notes for Frontend Developers

1. **Session-Based Cart**: The cart uses Django sessions, so you must include `credentials: 'include'` in fetch requests or `withCredentials: true` in Axios to maintain the session.

2. **CORS Configuration**: The API currently allows requests from `http://localhost:3000`. Update `CORS_ALLOWED_ORIGINS` in `settings.py` if your frontend runs on a different port or domain.

3. **Error Handling**: Always check the response status and handle errors appropriately. The API returns appropriate HTTP status codes (200, 201, 400, 404, etc.).

4. **Media Files**: Product and category images are served from `/media/` path. Make sure to use the full URL when displaying images: `http://localhost:8000/media/products/...`

5. **Query Parameters**: Use URL query parameters for filtering and sorting (e.g., `?sort_by=price_low_to_high`).

## Contributing Guidelines

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository** and create a new branch for your feature or bugfix
2. **Follow PEP 8** Python style guidelines
3. **Write clear commit messages** describing your changes
4. **Test your changes** before submitting a pull request
5. **Update documentation** if you add new features or change existing behavior
6. **Ensure all tests pass** before submitting

### Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes and test them
3. Commit your changes: `git commit -m "Add: description of changes"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This is a development version. For production deployment, ensure you:

- Set `DEBUG = False`
- Configure a production database (PostgreSQL recommended)
- Set a secure `SECRET_KEY`
- Configure proper `ALLOWED_HOSTS`
- Set up proper static file serving
- Use HTTPS
- Configure proper CORS settings
