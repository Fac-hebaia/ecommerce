
#  Marketplace app

## 1. Crear entorno virtual

```bash
python3 -m venv .venv
```

## 2. Activar entorno virtual

### macOS/Linux
```bash
source .venv/bin/activate
```

### Windows
```powershell
.\.venv\Scripts\activate
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 4. Recomendaciones
- Activa siempre el entorno virtual antes de instalar paquetes o ejecutar scripts.
- Al instalar una dependencia nueva ejecutar:
```bash 
pip freeze > requirements.txt 
```

