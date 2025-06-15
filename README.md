# Superheroes API - Phase 4 Code Challenge

This is a Flask-based RESTful API that allows users to track **Heroes** and their **Superpowers**. It features full CRUD functionality with model relationships, data validation, and JSON-formatted responses.

---

##  Project Structure

superheroes-api/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── seed.py
│ ├── migrations/
│ └── init.py
├── challenge-2-superheroes.postman_collection.json
├── README.md
├── requirements.txt


### Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Phase-4-Code-Challenge-Superheroes-.git
cd Phase-4-Code-Challenge-Superheroes-/superheroes-api


2. Create and activate a virtual environment
'''bash
python3 -m venv env


3.source env/bin/activate3. Install dependencies
'''bash
pip install -r requirements.txt


4. Set up the database
'''bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
 


5. Seed the database
'''bash
python server/seed.py


6. Run the server
'''bash
flask run

The server will start at http://127.0.0.1:5000.


### API Endpoints
~ GET /heroes

Returns a list of all heroes.
~ GET /heroes/:id

Returns a specific hero with their powers.
~ GET /powers

Returns a list of all powers.
~ GET /powers/:id

Returns details of a specific power.
~ PATCH /powers/:id

Updates the description of a power (with validation).
~ POST /hero_powers

Creates a new HeroPower association with validations.

##### Validations

   * Power.description: Must be present and at least 20 characters.

   * HeroPower.strength: Must be one of ["Strong", "Weak", "Average"].


###  Testing With Postman

Use the provided file:
'''pgsql
challenge-2-superheroes.postman_collection.json

   1. Open Postman

   2. Click Import

   4. Select the file

   4. Run the pre-defined requests


 Author

Shamim Lytton
GitHub: 
https://github.com/Shamimlytton2024





