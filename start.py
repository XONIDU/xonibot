#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONIBOT 2026 - Bot de WhatsApp con DeepSeek - Installer
SUPER ROBUSTO - Multiplataforma con múltiples estrategias de instalación
"""

import subprocess
import sys
import os
import platform
import shutil
import importlib.util
import time
import tempfile

# ============================================================================
# Colores para terminal
# ============================================================================
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

# ============================================================================
# Detección del sistema
# ============================================================================
SYSTEM = platform.system().lower()
ARCH = platform.machine().lower()

def es_linux():
    return SYSTEM == 'linux'

def es_arch():
    if not es_linux():
        return False
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                return 'arch' in f.read().lower()
        return shutil.which('pacman') is not None
    except:
        return False

def es_debian():
    if not es_linux():
        return False
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                return 'debian' in content or 'ubuntu' in content or 'mint' in content
        return shutil.which('apt') is not None
    except:
        return False

def es_fedora():
    if not es_linux():
        return False
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                return 'fedora' in f.read().lower()
        return shutil.which('dnf') is not None
    except:
        return False

def es_windows():
    return SYSTEM == 'windows'

def es_mac():
    return SYSTEM == 'darwin'

# ============================================================================
# Comandos Python
# ============================================================================
def obtener_python_comandos():
    """Múltiples comandos Python para probar"""
    comandos = []
    if es_windows():
        comandos.extend([
            ['python'],
            ['py'],
            ['python3'],
        ])
    else:
        comandos.extend([
            ['python3'],
            ['python'],
        ])
    return comandos

def obtener_pip_comandos():
    """Múltiples comandos pip para probar"""
    comandos = []
    if es_windows():
        comandos.extend([
            ['pip'],
            ['pip3'],
            [sys.executable, '-m', 'pip'] if sys.executable else None,
        ])
    else:
        comandos.extend([
            ['pip3'],
            ['pip'],
            [sys.executable, '-m', 'pip'] if sys.executable else None,
            ['python3', '-m', 'pip'],
            ['python', '-m', 'pip'],
        ])
    return [c for c in comandos if c is not None]

def ejecutar_comando(cmd, timeout=60):
    """Ejecuta un comando y devuelve (success, stdout, stderr)"""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=os.environ.copy()
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout"
    except Exception as e:
        return False, "", str(e)

def encontrar_python():
    """Encuentra un comando Python que funcione"""
    for cmd in obtener_python_comandos():
        success, _, _ = ejecutar_comando(cmd + ['--version'])
        if success:
            return cmd
    return None

def encontrar_pip():
    """Encuentra un comando pip que funcione"""
    for cmd in obtener_pip_comandos():
        success, _, _ = ejecutar_comando(cmd + ['--version'])
        if success:
            return cmd
    return None

# ============================================================================
# Instalación de pip
# ============================================================================
def instalar_pip_con_ensurepip():
    """Instala pip usando ensurepip"""
    python_cmd = encontrar_python()
    if not python_cmd:
        return False
    
    # Intentar con diferentes flags
    flags = [
        [],
        ['--upgrade'],
        ['--user'],
        ['--break-system-packages'],
    ]
    
    for flag in flags:
        cmd = python_cmd + ['-m', 'ensurepip'] + flag
        success, _, _ = ejecutar_comando(cmd)
        if success:
            return True
    
    return False

def instalar_pip_con_getpip():
    """Instala pip descargando get-pip.py"""
    try:
        import urllib.request
        import urllib.error
        
        temp_dir = tempfile.mkdtemp()
        get_pip_path = os.path.join(temp_dir, 'get-pip.py')
        
        # Descargar get-pip.py con múltiples intentos
        urls = [
            'https://bootstrap.pypa.io/get-pip.py',
            'https://raw.githubusercontent.com/pypa/get-pip/main/get-pip.py',
        ]
        
        downloaded = False
        for url in urls:
            try:
                urllib.request.urlretrieve(url, get_pip_path)
                downloaded = True
                break
            except:
                continue
        
        if not downloaded:
            return False
        
        # Ejecutar get-pip.py con diferentes flags
        python_cmd = encontrar_python()
        if not python_cmd:
            return False
        
        flags = [
            [],
            ['--user'],
            ['--break-system-packages'],
        ]
        
        for flag in flags:
            cmd = python_cmd + [get_pip_path] + flag
            success, _, _ = ejecutar_comando(cmd, timeout=120)
            if success:
                return True
        
        return False
    except:
        return False

def instalar_pip_sistema_linux():
    """Instala pip usando el gestor de paquetes del sistema"""
    if not es_linux():
        return False
    
    if es_debian():
        # Debian/Ubuntu/Mint
        cmds = [
            ['sudo', 'apt', 'update'],
            ['sudo', 'apt', 'install', '-y', 'python3-pip'],
            ['sudo', 'apt', 'install', '-y', 'python3-pip', '--fix-missing'],
        ]
    elif es_arch():
        # Arch Linux
        cmds = [
            ['sudo', 'pacman', '-S', '--noconfirm', 'python-pip'],
            ['sudo', 'pacman', '-S', '--noconfirm', 'python-pip', '--needed'],
        ]
    elif es_fedora():
        # Fedora
        cmds = [
            ['sudo', 'dnf', 'install', '-y', 'python3-pip'],
            ['sudo', 'dnf', 'install', '-y', 'python3-pip', '--allowerasing'],
        ]
    else:
        # Intento genérico
        cmds = [
            ['sudo', 'apt', 'install', '-y', 'python3-pip'],
            ['sudo', 'pacman', '-S', '--noconfirm', 'python-pip'],
            ['sudo', 'dnf', 'install', '-y', 'python3-pip'],
        ]
    
    for cmd in cmds:
        success, _, _ = ejecutar_comando(cmd, timeout=120)
        if success:
            return True
    
    return False

def instalar_pip_windows():
    """Instala pip en Windows"""
    if not es_windows():
        return False
    
    # Intentar con ensurepip primero
    if instalar_pip_con_ensurepip():
        return True
    
    # Intentar con get-pip.py
    return instalar_pip_con_getpip()

def instalar_pip_mac():
    """Instala pip en macOS"""
    if not es_mac():
        return False
    
    # Intentar con ensurepip
    if instalar_pip_con_ensurepip():
        return True
    
    # Intentar con get-pip.py
    if instalar_pip_con_getpip():
        return True
    
    # Intentar con Homebrew
    if shutil.which('brew'):
        success, _, _ = ejecutar_comando(['brew', 'install', 'python3'], timeout=120)
        if success:
            return True
    
    return False

def instalar_pip():
    """Instala pip en cualquier sistema"""
    print(f"{Colors.YELLOW}Instalando pip...{Colors.END}")
    
    if es_linux():
        if instalar_pip_sistema_linux():
            print(f"{Colors.GREEN}Pip instalado con gestor de paquetes{Colors.END}")
            return True
        if instalar_pip_con_ensurepip():
            print(f"{Colors.GREEN}Pip instalado con ensurepip{Colors.END}")
            return True
        if instalar_pip_con_getpip():
            print(f"{Colors.GREEN}Pip instalado con get-pip.py{Colors.END}")
            return True
    elif es_windows():
        if instalar_pip_windows():
            print(f"{Colors.GREEN}Pip instalado en Windows{Colors.END}")
            return True
    elif es_mac():
        if instalar_pip_mac():
            print(f"{Colors.GREEN}Pip instalado en macOS{Colors.END}")
            return True
    
    print(f"{Colors.RED}No se pudo instalar pip automaticamente{Colors.END}")
    return False

# ============================================================================
# Instalación de paquetes Python - ESTRATEGIAS MÚLTIPLES
# ============================================================================
def obtener_flags_instalacion():
    """Obtiene todos los flags posibles para pip install"""
    flags = [
        [],  # Sin flags
        ['--user'],
        ['--break-system-packages'],  # Arch/Fedora modernos
        ['--system'],  # Debian/Ubuntu
        ['--ignore-installed'],
        ['--no-deps'],
        ['--upgrade'],
        ['--user', '--upgrade'],
        ['--break-system-packages', '--upgrade'],
        ['--no-warn-script-location'],
    ]
    return flags

def instalar_paquete_con_pip(pip_cmd, package, flags):
    """Intenta instalar un paquete con flags específicos"""
    cmd = pip_cmd + ['install'] + flags + [package]
    flag_desc = ' '.join(flags) if flags else 'sin flags'
    print(f"    Intentando: {' '.join(cmd)}")
    
    success, stdout, stderr = ejecutar_comando(cmd, timeout=120)
    if success:
        print(f"{Colors.GREEN}    ✓ Instalado con {flag_desc}{Colors.END}")
        return True
    else:
        error = stderr[:100] if stderr else stdout[:100]
        print(f"{Colors.YELLOW}    ✗ Falló: {error}{Colors.END}")
        return False

def instalar_paquete(package):
    """Instala un paquete con múltiples estrategias"""
    pip_cmd = encontrar_pip()
    if not pip_cmd:
        print(f"{Colors.RED}No se encontró pip para instalar {package}{Colors.END}")
        return False
    
    # Primero intentar con --break-system-packages (Arch/Fedora)
    flags_prioritarias = [
        ['--break-system-packages'],
        ['--user'],
        ['--system'],
        [],
    ]
    
    for flags in flags_prioritarias:
        if instalar_paquete_con_pip(pip_cmd, package, flags):
            return True
    
    # Si falla, intentar con todas las combinaciones
    for flags in obtener_flags_instalacion():
        if instalar_paquete_con_pip(pip_cmd, package, flags):
            return True
    
    return False

def instalar_multiple_pip(packages):
    """Instala múltiples paquetes juntos"""
    if not packages:
        return True
    
    pip_cmd = encontrar_pip()
    if not pip_cmd:
        return False
    
    flags_prioritarias = [
        ['--break-system-packages'],
        ['--user'],
        ['--system'],
        [],
    ]
    
    for flags in flags_prioritarias:
        cmd = pip_cmd + ['install'] + flags + packages
        success, _, _ = ejecutar_comando(cmd, timeout=180)
        if success:
            print(f"{Colors.GREEN}✓ Paquetes instalados: {', '.join(packages)}{Colors.END}")
            return True
    
    return False

# ============================================================================
# Instalación de dependencias del sistema
# ============================================================================
def instalar_xclip():
    """Instala xclip en Linux"""
    if not es_linux():
        return False
    
    print(f"{Colors.YELLOW}Instalando xclip...{Colors.END}")
    
    if es_debian():
        cmds = [
            ['sudo', 'apt', 'update'],
            ['sudo', 'apt', 'install', '-y', 'xclip'],
        ]
    elif es_arch():
        cmds = [
            ['sudo', 'pacman', '-S', '--noconfirm', 'xclip'],
        ]
    elif es_fedora():
        cmds = [
            ['sudo', 'dnf', 'install', '-y', 'xclip'],
        ]
    else:
        cmds = [
            ['sudo', 'apt', 'install', '-y', 'xclip'],
            ['sudo', 'pacman', '-S', '--noconfirm', 'xclip'],
        ]
    
    for cmd in cmds:
        success, _, _ = ejecutar_comando(cmd, timeout=120)
        if success:
            print(f"{Colors.GREEN}✓ xclip instalado{Colors.END}")
            return True
    
    print(f"{Colors.RED}No se pudo instalar xclip{Colors.END}")
    return False

def instalar_ffmpeg():
    """Instala ffmpeg en Linux"""
    if not es_linux():
        return False
    
    print(f"{Colors.YELLOW}Instalando ffmpeg...{Colors.END}")
    
    if es_debian():
        cmds = [
            ['sudo', 'apt', 'update'],
            ['sudo', 'apt', 'install', '-y', 'ffmpeg'],
        ]
    elif es_arch():
        cmds = [
            ['sudo', 'pacman', '-S', '--noconfirm', 'ffmpeg'],
        ]
    elif es_fedora():
        cmds = [
            ['sudo', 'dnf', 'install', '-y', 'ffmpeg'],
        ]
    else:
        cmds = [
            ['sudo', 'apt', 'install', '-y', 'ffmpeg'],
            ['sudo', 'pacman', '-S', '--noconfirm', 'ffmpeg'],
        ]
    
    for cmd in cmds:
        success, _, _ = ejecutar_comando(cmd, timeout=180)
        if success:
            print(f"{Colors.GREEN}✓ ffmpeg instalado{Colors.END}")
            return True
    
    return False

# ============================================================================
# Verificación de dependencias
# ============================================================================
def verificar_paquete_python(module_name):
    """Verifica si un módulo Python está disponible"""
    try:
        if module_name == 'PIL':
            __import__('PIL')
        else:
            __import__(module_name)
        return True
    except ImportError:
        return False

def verificar_xclip():
    """Verifica si xclip está instalado"""
    if not es_linux():
        return True  # No necesario en otros sistemas
    return shutil.which('xclip') is not None

# ============================================================================
# Función principal
# ============================================================================
def main():
    if es_windows():
        os.system('cls')
    else:
        os.system('clear')
    
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}═══════════════════════════════════════════════════════════
                    XONIBOT 2026                    
              Bot de WhatsApp con DeepSeek            
              SUPER ROBUSTO - Multiplataforma          
                                                          
              Sistema: {SYSTEM.upper()} | Arch: {ARCH}           
              Detectado: {'Arch Linux' if es_arch() else 'Debian' if es_debian() else 'Fedora' if es_fedora() else SYSTEM}
                                                          
              Desarrollado por: Darian Alberto            
              Camacho Salas                               
              #Somos XONIDU
═══════════════════════════════════════════════════════════{Colors.END}
"""
    print(banner)
    
    # ===== 1. Verificar Python =====
    print(f"\n{Colors.BOLD}[1/5] Verificando Python...{Colors.END}")
    python_cmd = encontrar_python()
    if not python_cmd:
        print(f"{Colors.RED}Error: No se encontró Python instalado{Colors.END}")
        print("Descarga desde: https://www.python.org/downloads/")
        sys.exit(1)
    
    version = subprocess.run(python_cmd + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.GREEN}✓ Python: {version}{Colors.END}")
    print(f"  Comando: {' '.join(python_cmd)}")
    
    # ===== 2. Verificar/Instalar pip =====
    print(f"\n{Colors.BOLD}[2/5] Verificando pip...{Colors.END}")
    pip_cmd = encontrar_pip()
    if not pip_cmd:
        print(f"{Colors.YELLOW}pip no encontrado. Instalando...{Colors.END}")
        if not instalar_pip():
            print(f"{Colors.RED}No se pudo instalar pip automaticamente{Colors.END}")
            sys.exit(1)
        pip_cmd = encontrar_pip()
        if not pip_cmd:
            print(f"{Colors.RED}Error: No se pudo instalar pip{Colors.END}")
            sys.exit(1)
    
    print(f"{Colors.GREEN}✓ pip disponible: {' '.join(pip_cmd)}{Colors.END}")
    
    # ===== 3. Verificar dependencias Python =====
    print(f"\n{Colors.BOLD}[3/5] Verificando dependencias Python...{Colors.END}")
    
    dependencias = [
        ('pyautogui', 'pyautogui'),
        ('PIL', 'pillow'),
    ]
    
    faltantes = []
    for module, package in dependencias:
        if verificar_paquete_python(module):
            print(f"{Colors.GREEN}  ✓ {package}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}  ✗ {package} (FALTANTE){Colors.END}")
            faltantes.append(package)
    
    if faltantes:
        print(f"\n{Colors.YELLOW}Faltan {len(faltantes)} paquetes: {', '.join(faltantes)}{Colors.END}")
        respuesta = input("Instalar automaticamente? (s/n): ").lower()
        if respuesta == 's':
            if not instalar_multiple_pip(faltantes):
                # Intentar uno por uno
                print(f"{Colors.YELLOW}Intentando instalar uno por uno...{Colors.END}")
                for package in faltantes:
                    if not instalar_paquete(package):
                        print(f"{Colors.RED}Error instalando {package}{Colors.END}")
                        print(f"  Prueba manual: pip install {package}")
                        if es_linux():
                            print(f"  O con: pip install --break-system-packages {package}")
                        print(f"  O con: pip install --user {package}")
    
    # ===== 4. Verificar dependencias del sistema =====
    print(f"\n{Colors.BOLD}[4/5] Verificando dependencias del sistema...{Colors.END}")
    
    # xclip (Linux)
    if es_linux():
        if verificar_xclip():
            print(f"{Colors.GREEN}  ✓ xclip{Colors.END}")
        else:
            print(f"{Colors.YELLOW}  ✗ xclip (FALTANTE - necesario para portapapeles){Colors.END}")
            respuesta = input("Instalar xclip? (s/n): ").lower()
            if respuesta == 's':
                instalar_xclip()
    
    # ffmpeg (opcional)
    if es_linux() and shutil.which('ffmpeg'):
        print(f"{Colors.GREEN}  ✓ ffmpeg (opcional){Colors.END}")
    elif es_linux():
        print(f"{Colors.YELLOW}  ✗ ffmpeg (opcional - para mejor manejo de medios){Colors.END}")
    
    # ===== 5. Buscar xonibot.py =====
    print(f"\n{Colors.BOLD}[5/5] Buscando xonibot.py...{Colors.END}")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rutas = [
        os.path.join(script_dir, 'xonibot.py'),
        os.path.join(script_dir, '..', 'xonibot.py'),
        os.path.join(os.getcwd(), 'xonibot.py'),
        os.path.join(os.path.expanduser("~"), '.xonibot', 'xonibot.py'),
        '/usr/share/xonibot/xonibot.py',
    ]
    
    xonibot_path = None
    for r in rutas:
        if os.path.exists(r):
            xonibot_path = r
            print(f"{Colors.GREEN}✓ Encontrado: {r}{Colors.END}")
            break
    
    if not xonibot_path:
        print(f"{Colors.RED}Error: No se encuentra xonibot.py{Colors.END}")
        print("Coloca xonibot.py en el mismo directorio que start.py")
        sys.exit(1)
    
    # ===== Crear accesos directos =====
    if es_linux():
        with open('XONIBOT.sh', 'w') as f:
            f.write("""#!/bin/bash
echo "========================================"
echo "   XONIBOT 2026 - Bot de WhatsApp"
echo "   #Somos XONIDU"
echo "========================================"
python3 start.py "$@"
read -p "Presiona Enter para salir"
""")
        os.chmod('XONIBOT.sh', 0o755)
        print(f"{Colors.GREEN}✓ Creado XONIBOT.sh{Colors.END}")
    elif es_windows():
        with open('XONIBOT.bat', 'w') as f:
            f.write("""@echo off
title XONIBOT
echo ========================================
echo    XONIBOT 2026 - Bot de WhatsApp
echo    #Somos XONIDU
echo ========================================
python start.py %*
pause
""")
        print(f"{Colors.GREEN}✓ Creado XONIBOT.bat{Colors.END}")
    
    # ===== Ejecutar =====
    print(f"\n{Colors.BOLD}Iniciando XONIBOT...{Colors.END}")
    print(f"{Colors.CYAN}Para salir: Ctrl+C{Colors.END}")
    print("-" * 50)
    
    try:
        cmd = python_cmd + [xonibot_path] + sys.argv[1:]
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Detenido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XONIBOT{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
