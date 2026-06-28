#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WHATSBOT - WhatsApp + DeepSeek
Guarda ultimas 3 respuestas del bot para NO repetirse
Espera 3 segundos en DeepSeek
Delay de 1 seg entre Alt+Tab y click
"""

import os
import sys
import time
import re
import pyautogui

class WhatsAppBot:
    def __init__(self):
        self.ultimo_mensaje_usuario = ""
        self.ultimas_respuestas_bot = []
        self.y_offset = 100
        self.historial_mensajes = []
        
    def mover_mouse_relativo(self, dy):
        x, y = pyautogui.position()
        pyautogui.moveTo(x, y + dy, duration=0.3)
        
    def extraer_ultima_respuesta(self, texto):
        if not texto:
            return None
        
        patron = r'=respuesta\s*(.*?)='
        matches = re.findall(patron, texto, re.DOTALL)
        
        if matches:
            ultima = matches[-1].strip()
            if ultima and ultima not in ["TU_RESPUESTA_BREVE", "TU_RESPUESTA"]:
                return ultima
        
        patron2 = r'=(.*?)='
        matches2 = re.findall(patron2, texto, re.DOTALL)
        if matches2:
            ultima = matches2[-1].strip()
            ultima = re.sub(r'^respuesta\s*', '', ultima)
            if ultima and ultima not in ["TU_RESPUESTA_BREVE", "TU_RESPUESTA"]:
                return ultima
        
        return None
    
    def obtener_portapapeles(self):
        try:
            texto = os.popen('xclip -selection clipboard -o 2>/dev/null').read()
            if texto:
                return texto.encode('utf-8', 'ignore').decode('utf-8').strip()
        except:
            pass
        return ""
    
    def guardar_respuesta_bot(self, respuesta):
        self.ultimas_respuestas_bot.append(respuesta)
        if len(self.ultimas_respuestas_bot) > 3:
            self.ultimas_respuestas_bot.pop(0)
        print(f"[DEBUG] Respuestas bot guardadas: {self.ultimas_respuestas_bot}")
    
    def es_respuesta_del_bot(self, mensaje):
        if not mensaje:
            return False
        for resp in self.ultimas_respuestas_bot:
            if mensaje == resp:
                print(f"[DEBUG] '{mensaje}' es respuesta del bot")
                return True
        return False
    
    def limpiar_texto_whatsapp(self, texto):
        if not texto:
            return []
        
        lineas = texto.split('\n')
        mensajes_validos = []
        
        for linea in lineas:
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            
            if re.match(r'^\d{1,2}:\d{2}\s*(?:a\.m\.|p\.m\.)?$', linea_limpia, re.IGNORECASE):
                continue
            if re.match(r'^\d{1,2}:\d{2}$', linea_limpia):
                continue
            if re.match(r'^\d{1,2}/\d{1,2}/\d{2,4}$', linea_limpia):
                continue
            
            palabras_ignorar = ['archivados', 'notificaciones', 'borrador:', 'editado', 'ult. vez', 
                               'ayer', 'hoy', 'manana', 'lunes', 'martes', 'miercoles', 'jueves', 
                               'viernes', 'sabado', 'domingo', 'Envia mensajes', 'cifrados', 'Zoom', 
                               'https://', 'Reenviado', 'Únase', 'líder', 'llamadas', 'en línea']
            if any(palabra in linea_limpia.lower() for palabra in palabras_ignorar):
                continue
            
            if self.es_respuesta_del_bot(linea_limpia):
                continue
            
            if len(linea_limpia) > 1 and not linea_limpia.startswith('='):
                mensajes_validos.append(linea_limpia)
        
        return mensajes_validos
    
    def obtener_contexto(self, mensajes):
        if not mensajes:
            return ""
        
        ultimos = mensajes[-3:]
        
        contexto = "Contexto de la conversacion:\n"
        for i, msg in enumerate(ultimos, 1):
            contexto += f"{i}. {msg}\n"
        
        return contexto
    
    def esperar_mensaje_nuevo(self):
        print("[ESPERA] Esperando mensaje del usuario...")
        
        while True:
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(1)
            
            texto_raw = self.obtener_portapapeles()
            mensajes_validos = self.limpiar_texto_whatsapp(texto_raw)
            
            if mensajes_validos:
                mensaje_actual = mensajes_validos[-1]
                
                if not self.es_respuesta_del_bot(mensaje_actual):
                    if mensaje_actual != self.ultimo_mensaje_usuario:
                        print(f"\n[NUEVO USUARIO] {mensaje_actual}")
                        self.ultimo_mensaje_usuario = mensaje_actual
                        self.historial_mensajes = mensajes_validos
                        return mensaje_actual
            
            time.sleep(3)
    
    def ejecutar(self):
        os.system('clear')
        print("=" * 50)
        print("   WHATSBOT - WhatsApp + DeepSeek")
        print("     (Guarda ultimas 3 respuestas del bot)")
        print("     (Espera 3 segundos en DeepSeek)")
        print("=" * 50)
        
        print("\n[INICIANDO] Mouse en campo texto WhatsApp")
        print("[INFO] 5 segundos...")
        time.sleep(5)
        
        print("[ACTIVO] Esperando mensajes del USUARIO...\n")
        
        try:
            while True:
                mensaje = self.esperar_mensaje_nuevo()
                
                if mensaje:
                    print(f"[Usuario] {mensaje}")
                    
                    contexto = self.obtener_contexto(self.historial_mensajes[:-1] if len(self.historial_mensajes) > 1 else [])
                    
                    # Ir a DeepSeek
                    pyautogui.hotkey('alt', 'tab')
                    time.sleep(1)  # Delay 1 seg despues de Alt+Tab
                    
                    pyautogui.click()
                    time.sleep(1)  # Delay 1 seg despues de click
                    
                    # Limpiar campo de texto
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(0.5)
                    pyautogui.press('delete')
                    time.sleep(0.5)
                    
                    # Prompt con contexto
                    prompt = f"Contexto:\n{contexto}\nResponde breve y natural a: {mensaje}\nFormato: =respuesta TU_RESPUESTA="
                    
                    os.system(f'echo "{prompt}" | xclip -selection clipboard')
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)
                    pyautogui.press('enter')
                    time.sleep(1)
                    
                    print("[DeepSeek] Esperando 3 segundos...")
                    time.sleep(3)
                    
                    # Subir 100 pixeles
                    self.mover_mouse_relativo(-100)
                    time.sleep(1)
                    
                    # Copiar respuesta
                    pyautogui.click()
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(1)
                    
                    respuesta_raw = self.obtener_portapapeles()
                    respuesta = self.extraer_ultima_respuesta(respuesta_raw)
                    
                    if not respuesta or len(respuesta) < 2:
                        respuesta = "👍"
                    
                    print(f"[DeepSeek] {respuesta}")
                    
                    self.guardar_respuesta_bot(respuesta)
                    
                    # Volver a WhatsApp
                    pyautogui.hotkey('alt', 'tab')
                    time.sleep(1)  # Delay 1 seg despues de Alt+Tab
                    
                    pyautogui.click()
                    time.sleep(1)  # Delay 1 seg despues de click
                    
                    # Bajar 100 pixeles
                    self.mover_mouse_relativo(100)
                    time.sleep(1)
                    
                    # Pegar respuesta
                    os.system(f'echo "{respuesta}" | xclip -selection clipboard')
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)
                    
                    # Enter para enviar
                    pyautogui.press('enter')
                    time.sleep(1)
                    
                    print(f"[Enviado] {respuesta}\n")
                    
                    time.sleep(3)
                    
        except KeyboardInterrupt:
            print("\n[FINALIZADO]")
            sys.exit(0)

if __name__ == "__main__":
    try:
        import pyautogui
    except ImportError:
        os.system("pip3 install pyautogui --break-system-packages")
    
    if os.system("which xclip > /dev/null 2>&1") != 0:
        os.system("sudo pacman -S xclip")
    
    bot = WhatsAppBot()
    bot.ejecutar()
