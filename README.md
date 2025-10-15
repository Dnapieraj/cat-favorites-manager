
# 🐱 Cat System

Simple system for managing favorite cats using [The Cat API](https://thecatapi.com/).

## 📋 Features

- 🔍 Fetching random cat images
- ❤️ Adding cats to favorites
- 📋 Displaying list of favorite cats
- 🗑️ Removing cats from favorites

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Dnapieraj/catsystem.git
cd catsystem
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4. Install required packages
```bash
pip install -r requirements.txt
```

### 5. Configure API Key

1. Sign up at [The Cat API](https://thecatapi.com/signup)
2. Get your free API key
3. Create `credentials.py` file in the main project folder:

```python
# credentials.py
headers = {
    'x-api-key': 'YOUR_API_KEY_HERE'
}
```


## 🎮 Usage

Run the application:
```bash
python catsystem.py
```

### Example output:
```
Zaloguj się - podaj login i hasło
Witaj Daniel
Twoje ulubione koty to: [...]
Wylosowano kota: https://cdn2.thecatapi.com/images/abc123.jpg
Czy chcesz dodać kota do ulubionych? T/N: T
Czy chcesz usunąć kota z ulubionych? Podaj jego ID (Enter = pomiń): 
```

## 🔧 Requirements

- Python 3.7+
- Python packages:
  - `requests`

## 📝 API Endpoints

The application uses the following The Cat API endpoints:

- `GET /v1/images/search` - Fetching random cats
- `GET /v1/favourites/` - Fetching favorite cats
- `POST /v1/favourites/` - Adding cat to favorites
- `DELETE /v1/favourites/{id}` - Removing cat from favorites

## 🐛 Known Issues

- Lack of advanced network error handling
- No API key format validation
- Possibility to extend with GUI
