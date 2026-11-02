# Pydantic Data Validation & Serialization

A practical Python project demonstrating how to use **Pydantic** for data validation, structured models, custom validators, serialization, and computed fields.

This project uses a sample product model to demonstrate important Pydantic features.

## 🚀 Features

### 1. Nested Models
- Created a separate `Category` model.
- Used `Literal` to restrict category values.
- Integrated the category model into the main product model.

### 2. Field Definitions
- Required fields using `Field(...)`.
- Default values.
- Optional fields using `str | None`.
- Field aliases using `alias="userName"`.
- Email validation using `EmailStr`.

### 3. Model Configuration

Explored Pydantic configuration options:

- `extra="ignore"` – Ignores additional input fields.
- `strict=True` – Enables strict type validation.
- `frozen=True` – Prevents model instances from being modified.
- `validate_assignment=True` – Configures validation during assignment; note that `frozen=True` prevents normal assignment regardless.

### 4. Custom Validators

**Field Validator**
- Used `@field_validator("name")`.
- Automatically converts product names into title case.

**Model Validator**
- Used `@model_validator(mode="after")`.
- Checks that an available product has a price greater than zero.

### 5. Computed Fields
- Used `@computed_field`.
- Created a calculated `price_with_tax` field.
- Demonstrated how to include calculated values in serialized output.

### 6. Serialization

Implemented:

- `model_dump()` – Converts the model into a Python dictionary.
- `model_dump_json()` – Converts the model into JSON.

## 🛠️ Technologies Used

- Python
- Pydantic
- EmailStr

## 📁 Project Structure

```text
Pydantic-Validation/
│
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/MuhammadIbrahim732/Pydantic-Validation.git
```

**2. Navigate to the project directory**

```bash
cd Pydantic-Validation
```

**3. Install dependencies**

```bash
pip install pydantic email-validator
```

**4. Run the project**

```bash
python main.py
```

## 🎯 Learning Outcomes

Through this implementation, I practiced:

- Creating structured data models.
- Validating nested data.
- Defining required, optional, and default fields.
- Applying strict validation and model configuration.
- Implementing field-level and model-level validators.
- Creating computed fields.
- Serializing Python objects into dictionaries and JSON.

## 👨‍💻 Author

**Muhammad Ibrahim**

AI/ML Engineering Learner | Python | Machine Learning | Deep Learning | Generative AI

- GitHub: https://github.com/MuhammadIbrahim732
- LinkedIn: https://www.linkedin.com/in/muhammad-ibrahim-4a8425330/

---

⭐ If you find this project useful, consider giving it a star!
