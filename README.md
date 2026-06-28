# 🤖 XONIBOT 2026 - Bot de WhatsApp con DeepSeek

**Desarrollado por: Darian Alberto Camacho Salas**  
**SOMOS XONIDU**

---

## ⚠️ ADVERTENCIA

> Solo para fines educativos y automatización personal. Úsalo en tus propias cuentas y con responsabilidad. No uses para spam o actividades maliciosas. El uso indebido puede resultar en la suspensión de tu cuenta de WhatsApp.

---

## 📦 INSTALACIÓN

### Arch Linux (AUR)
```bash
yay -S xonibot
```

### Windows (Instalador)
```bash
# Descarga el ZIP desde GitHub
# Extrae y ejecuta INICIAR_XONIBOT.bat como Administrador
```

### Otros sistemas (Windows, macOS, Linux)
```bash
git clone https://github.com/XONIDU/xonibot.git
cd xonibot
python start.py
```

o

```bash
git clone https://github.com/XONIDU/xonibot.git
cd xonibot
python3 start.py
```

---

### Opción 2 – Comando `xoninstall` (recomendado para futuras herramientas XONI)

Agrega la siguiente función a tu `~/.bashrc` con un solo comando:

```bash
echo 'xoninstall() { if [ -z "$1" ]; then echo "Uso: xoninstall <repo>"; echo "Ej: xoninstall xoniran"; else git clone "https://github.com/XONIDU/$1.git"; fi; }' >> ~/.bashrc && source ~/.bashrc && echo "✅ Listo. Usa: xoninstall xonicli"
```

Luego simplemente escribe:

```bash
xoninstall xonibot
cd xonibot
python start.py
```

> **Nota:** Esta función te servirá para instalar cualquier otra herramienta futura de XONIDU.

---

### Opción 3 – Instalación manual (sin Git)

1. **Descarga el ZIP** desde: https://github.com/XONIDU/xonibot/archive/main.zip
2. **Extrae** el contenido en una carpeta
3. **Ejecuta**:
   - Windows: `INICIAR_XONIBOT.bat` (como Administrador)
   - Linux/macOS: `python start.py`

---

## 📁 SOLO NECESITAS ESTOS 4 ARCHIVOS

```
xonibot/
├── INICIAR_XONIBOT.bat   # 🟢 Windows - Ejecuta con permisos admin
├── start.py              # 🟢 Instalador/ejecutor (Linux/macOS/Windows)
├── xonibot.py            # 🔵 El programa principal
└── requisitos.txt        # 📦 Lista de dependencias
```

---

## 🚀 ASÍ DE FÁCIL: SOLO EJECUTA start.py

El archivo start.py hace TODO automáticamente:

| # | Acción |
|:-:|--------|
| 1 | Detecta Windows, Linux o Mac |
| 2 | Verifica Python instalado |
| 3 | Revisa qué librerías faltan |
| 4 | Las instala automáticamente |
| 5 | Ejecuta el bot |

---

## 🎯 REQUISITOS PREVIOS

Antes de ejecutar XONIBOT, asegúrate de tener:

1. **WhatsApp Web** abierto en una pestaña del navegador
2. **DeepSeek** abierto en otra pestaña
3. **Terminal** abierta en otra pestaña/ventana

**Orden de pestañas recomendado:**
- Pestaña 1: WhatsApp Web (chat abierto)
- Pestaña 2: DeepSeek (conversación abierta)
- Pestaña 3: Terminal (ejecutando el bot)

---

## 🎮 CÓMO FUNCIONA

### Flujo del bot:

```
1. Espera mensaje nuevo en WhatsApp
   ↓
2. Copia el mensaje del usuario
   ↓
3. Cambia a DeepSeek y pega el mensaje con contexto
   ↓
4. Espera 3 segundos para respuesta
   ↓
5. Copia la respuesta de DeepSeek
   ↓
6. Vuelve a WhatsApp y envía la respuesta
   ↓
7. Guarda las últimas 3 respuestas para NO repetirse
   ↓
8. Vuelve al paso 1
```

### Características principales:

- ✅ **Contexto de 3 mensajes** - La IA sabe de qué se habla
- ✅ **No se repite** - Guarda las últimas 3 respuestas del bot
- ✅ **Movimiento automático** - Sube/baja 100 píxeles para evitar detección
- ✅ **Solo responde a mensajes del usuario** - Ignora sus propias respuestas
- ✅ **Multiplataforma** - Windows, Linux y macOS
- ✅ **Instalación automática** - start.py instala todo lo necesario
- ✅ **Permisos de administrador en Windows** - INICIAR_XONIBOT.bat

---

## 🪟🐧🍎 COMANDOS (para todos los sistemas)

### Windows
```cmd
# Con permisos de administrador (recomendado)
INICIAR_XONIBOT.bat

# Sin permisos de administrador
python start.py
python xonibot.py
```

### Linux/macOS
```bash
# Con instalación automática
python start.py

# Directo
python xonibot.py
```

### Ver ayuda
```bash
python start.py --help
```

---

## 🪟 ESPECIAL PARA WINDOWS: INICIAR_XONIBOT.bat

El archivo `INICIAR_XONIBOT.bat` en Windows:

1. **Solicita permisos de administrador** (UAC)
2. **Instala dependencias** automáticamente
3. **Ejecuta el bot** con todos los permisos necesarios

### ¿Cómo usar?

1. **Doble clic** en `INICIAR_XONIBOT.bat`
2. Acepta el mensaje de Control de Cuentas de Usuario (UAC)
3. El script instalará automáticamente todas las dependencias
4. XONIBOT se iniciará con permisos completos

---

## 🔧 DEPENDENCIAS (requisitos.txt)

### Python (se instalan automáticamente)
```txt
# XONIBOT 2026 - Dependencias
# Bot de WhatsApp con DeepSeek

# Automatización de GUI (mouse, teclado, pantalla)
pyautogui>=0.9.54

# Procesamiento de imágenes (opcional, para capturas)
Pillow>=10.0.0
```

### Sistema (instalación manual si falla)

**Linux:**
```bash
# Arch/Manjaro
sudo pacman -S xclip python-pip

# Debian/Ubuntu/Mint
sudo apt install xclip python3-pip

# Fedora
sudo dnf install xclip python3-pip
```

**Windows:** No necesita xclip (usa portapapeles nativo)

**macOS:**
```bash
brew install xclip
# o usa pbpaste/pbcopy nativo
```

---

## 💡 EJEMPLO DE USO

### Ejecutar el bot:
```bash
python start.py
```

### Salida en terminal:
```
==================================================
   WHATSBOT - WhatsApp + DeepSeek
==================================================

[INICIANDO] Mouse en campo texto WhatsApp
[INFO] 5 segundos...
[ACTIVO] Esperando mensajes del USUARIO...

[ESPERA] Esperando mensaje nuevo...

[NUEVO USUARIO] Hola, ¿cómo estás?
[Usuario] Hola, ¿cómo estás?
[DeepSeek] Esperando 3 segundos...
[DeepSeek] Bien, ¿y tú?
[Enviado] Bien, ¿y tú?
```

### Ejemplo de conversación real:

**Usuario:** Hola  
**Bot:** Hola, ¿cómo estás?  
**Usuario:** Bien, ¿y tú?  
**Bot:** Bien, gracias por preguntar.  
**Usuario:** ¿Qué haces?  
**Bot:** Descansando un rato.  

---

## 🔧 PROBLEMAS COMUNES

### ❌ "Python no está instalado"
```bash
# Descarga desde:
https://www.python.org/downloads/
```

### ❌ "externally-managed-environment" en Linux
```bash
# start.py ya lo soluciona automáticamente
# Si quieres manual:
pip install --break-system-packages -r requisitos.txt
```

### ❌ "xclip: command not found" (Linux)
```bash
# Arch/Manjaro
sudo pacman -S xclip

# Debian/Ubuntu
sudo apt install xclip

# Fedora
sudo dnf install xclip
```

### ❌ "No module named 'pyautogui'"
```bash
pip install pyautogui
# En Linux con external management:
pip install --break-system-packages pyautogui
```

### ❌ El bot responde a sus propios mensajes
```bash
# Asegúrate de tener la última versión
git pull
# start.py guarda automáticamente las últimas 3 respuestas
```

### ❌ El bot no pega en DeepSeek
```bash
# Verifica que las pestañas estén en el orden correcto:
# Pestaña 1: WhatsApp
# Pestaña 2: DeepSeek
# Pestaña 3: Terminal
```

### ❌ "Permisos denegados en Windows"
```bash
# Ejecuta INICIAR_XONIBOT.bat como administrador
# O haz clic derecho > "Ejecutar como administrador"
```

---

## ✅ LO QUE PUEDES HACER (Y LO QUE NO)

| ✅ **SÍ** | ❌ **NO** |
|-----------|-----------|
| Automatizar tus propias conversaciones | Usar para spam |
| Aprender sobre automatización | Acosar a otros usuarios |
| Practicar con IA | Usar con fines maliciosos |
| Modificar el código para uso personal | Vender el software |
| Compartir el código con créditos | Quitar los créditos |

---

## 📊 EJEMPLO DE CONVERSACIÓN

```
Usuario: Hola
Bot: Hola, ¿cómo estás?

Usuario: Bien, ¿y tú?
Bot: Bien, gracias. ¿Qué haces?

Usuario: Nada, solo probando el bot
Bot: Interesante, ¿cómo funciona?

Usuario: Automatiza respuestas con IA
Bot: Genial, parece muy útil.
```

---

## 📋 REQUISITOS DEL SISTEMA

- **Python**: 3.8 o superior
- **RAM**: 512 MB mínimo (1 GB recomendado)
- **Espacio**: 100 MB para dependencias
- **Navegador**: Chrome/Firefox con WhatsApp Web y DeepSeek abiertos

---

## 🛠️ TECNOLOGÍAS UTILIZADAS

- Python 3
- PyAutoGUI (Automatización GUI)
- xclip/portapapeles (Copiar/Pegar)
- Navegador web (WhatsApp Web + DeepSeek)

---

## 📞 CONTACTO

| Red | Usuario |
|-----|---------|
| 📸 **Instagram** | @xonidu |
| 📧 **Email** | xonidu@gmail.com |
| 💻 **GitHub** | XONIDU/xonibot |

---

## 📜 LICENCIA

MIT License - Copyright (c) 2026 Darian Alberto Camacho Salas

Ver archivo `Legal` para más detalles.

---

## ⭐ CRÉDITOS

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           XONIBOT 2026 - Bot de WhatsApp                 ║
║                                                           ║
║         Hecho con ❤️ por Darian Alberto Camacho Salas     ║
║                                                           ║
║         "Automatización inteligente para todos"          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 📂 ESTRUCTURA COMPLETA DEL PROYECTO

```
xonibot/
├── INICIAR_XONIBOT.bat   # 🟢 Windows - Ejecuta con permisos admin
├── start.py              # 🟢 Instalador/ejecutor universal
├── xonibot.py            # 🔵 El programa principal
├── requisitos.txt        # 📦 Dependencias Python
├── README.md             # 📖 Documentación
└── Legal                 # 📜 Licencia y términos
```

---

**XONIDU - Enseñando automatización, construyendo conocimiento**

