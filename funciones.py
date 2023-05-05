import datetime
import pytz

import random 

from respuestas import cat_sounds_list

horas_del_te=(15,21,22,23)
horas_de_mimir=(3,4,5)

def sumar_x(expresion):
    try:
        exponente = int(expresion[1:])
    except ValueError:
        raise ValueError('XD')
    exponente += 1
    return f'x{exponente}'

def hora_del_te(zona_horaria):
    hora_actual = datetime.datetime.now(pytz.timezone(zona_horaria))
    hora_actual_str = hora_actual.strftime("%H:%M:%S")
    if hora_actual.hour in horas_del_te:
        mensaje = "Meow 😺 es hora del legendario té! ☕\n"
        ascii_art ="""
```    {
     }   }   {
    {   {  }  }
     }   }{  {
    {  }{  }  }          ___
   ( }{ }{  { )        .'   '.
   .-{   }   }-.      /  .-.  \\
  ( ( } { } { } )    |  /   \  |
  |`-.._____..-'|    | |\_.  | |
  |    EPIC     ;_   \\\|  | / /
  \             /     \\\  '-' /        
    \`.       /    
     `\`-.__ /         
       `._..'       
                     ```
""" 
    elif hora_actual.hour+1 in horas_del_te:
        mensaje = "Falta una hora para la hora del té! ☕\n"
        ascii_art = """
```
 |\\___/\\_\\__//
 |  |      /    |
 |  |wait /     |
 |__|_____|_____|
/             \\```
"""
    elif hora_actual.hour+2 in horas_del_te:
        mensaje = "Faltan dos horas para la hora del té! ☕\n"
        ascii_art = """
``` 
                  
 		                     
                         
     ___                 
 ___| o |___               
/ ~~~~~~~~ \\             
|   wait   |             
 \\________/              
  _|____|_                
 /        \\               
|          |              
 \\        /               
  `------'     ```           
"""
    elif hora_actual.hour+3 in horas_del_te:
        mensaje = "Faltan tres horas para la hora del té! ☕\n"
        ascii_art = """
```    _....._
     .'  UnU  '. 
    /    ___    \\
   |    /  \\    |
   |   |    |   |
    \\   \\__/   /
     '._    _.' 
        `--`    ```
"""
    elif hora_actual.hour in horas_de_mimir:
        mensaje = "no deberías estar durmiendo en vez de preguntar por el té 🤔\n"  
        ascii_art = " // "
    else:
        mensaje = "No es hora del té. Meow!! 😾\n"
        ascii_art = f"La hora actual en {zona_horaria} es {hora_actual_str}.\n"
    return mensaje + ascii_art





#.   Funciones
def is_cat_sound(s):
    for cat_sound in cat_sounds_list:
        if s.lower() == cat_sound.lower() or s.lower() == cat_sound.lower() * len(s):
            return True
    return False



def random_cat_sound_concat():
    # Elige al azar una cantidad de sonidos entre 1 y 5
    num_sounds = random.randint(1, 5)
    
    # Elige al azar los sonidos de gato de la lista cat_sounds_list
    cat_sounds = random.choices(cat_sounds_list, k=num_sounds)
    
    # Concatena los sonidos de gato elegidos y agrega repeticiones aleatorias de las vocales
    new_cat_sound = ""
    for sound in cat_sounds:
        new_sound = ""
        for char in sound:
            if char.lower() in ["a", "e", "i", "o", "u"]:
                # Agrega repeticiones aleatorias de las vocales
                num_repetitions = random.randint(1, 5)
                new_sound += char * num_repetitions
            else:
                new_sound += char
        new_cat_sound += new_sound
    
    return new_cat_sound





def is_new_cat_sound(sound):
    sound_simple = simple_s(sound)
    if is_cat_sound(sound):
        return 0
    else:
        return is_cat_sound(sound_simple)

  
  

def simple_s(palabra):
    # Si la palabra es una cadena vacía, devolver una cadena vacía
    if not palabra:
        return ""
    # Inicializar la palabra simplificada con la primera letra
    palabra_simplificada = palabra[0]
    
    # Recorrer la palabra original, saltando las letras repetidas
    for i in range(1, len(palabra)):
        if palabra[i] != palabra[i-1]:
            palabra_simplificada += palabra[i]
    
    # Devolver la palabra simplificada
    return palabra_simplificada

def get_str(s,i):
    if not s:
        return False
    return s.split()[i].lower()
      