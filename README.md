# Telusko Trac

A modern, full-stack product inventory management system built with FastAPI and React. Streamline your inventory tracking with an intuitive web interface and robust backend API.

## Features

- **Complete CRUD Operations**: Create, read, update, and delete products with ease
- **Advanced Search & Filtering**: Find products quickly by ID, name, or description
- **Dynamic Sorting**: Sort products by any field (ID, name, price, quantity) in ascending or descending order
- **Responsive Design**: Clean, modern UI that works on desktop and mobile devices
- **Real-time Updates**: Instant feedback and automatic data refresh after operations
- **PostgreSQL Integration**: Reliable database storage with SQLAlchemy ORM
- **CORS Enabled**: Seamless frontend-backend communication during development

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- PostgreSQL database

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-backend-prj
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myenv
   # On Windows:
   myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
   ```

4. **Setup PostgreSQL database**
   - Create a database named `mydatabase`
   - Update connection string in `database.py` if needed:
     ```python
     db_url = "postgresql://username:password@localhost:5432/mydatabase"
     ```

5. **Run the backend server**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```
   The application will open at `http://localhost:3000`

### Usage

1. Open your browser and go to `http://localhost:3000`
2. View all products in the table
3. Use the search bar to filter products
4. Click column headers to sort by different fields
5. Add new products using the form on the left
6. Edit existing products by clicking the "Edit" button
7. Delete products with the "Delete" button

### API Endpoints

- `GET /` - Welcome message
- `GET /products/` - Get all products
- `GET /products/{id}` - Get product by ID
- `POST /products/` - Create new product
- `PUT /products/{id}` - Update existing product
- `DELETE /products/{id}` - Delete product

## Support

If you encounter any issues or have questions:

- Check the [Issues](https://github.com/yourusername/yourrepo/issues) page on GitHub
- Review the code comments in the source files
- Ensure all prerequisites are properly installed

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get involved.

## Maintainers

- [Your Name](https://github.com/yourusername) - Project maintainer

---

Built with ❤️ using FastAPI and React</content>
<parameter name="filePath">c:\Users\hp\Documents\FastAPI Backend Prj\README.md