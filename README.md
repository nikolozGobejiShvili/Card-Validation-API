# Card Validation API

This Django-based API provides a robust system for validating card information, ensuring cards meet specific numeric standards and perform algorithm-based validation to determine if a card is theoretically valid. 
This API is especially useful for applications needing to preprocess and validate card data before actual transaction processes.

## Features

- **User Authentication**: Securely manage and access card data.
- **Card Creation and Validation**: Add new cards with validation for card numbers and CCVs.
- **Custom Card Validation Logic**: Implements a unique validation algorithm that pairs and processes card number sequences.

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/yourusername/card-validation-api.git
cd card-validation-api
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
