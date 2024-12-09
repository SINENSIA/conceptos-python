from datetime import datetime
def get_dia_semana_for_humans(datetime):
    """
    Esta función recibe una fecha y devuelve el día de la
    semana de la fecha en español-castellano
    return:
        weekday: str
        Una cadena de texto representando el dia de la semana.
        en español-castellano
    Ejemplo:
        get_dia_semana_for_humans(datetime(1879, 3, 14))
        >>> "Martes"
    """
    # Creamos una lista con los días de la semana
    
    weekdays = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    # Obtenemos el día de la semana de la fecha
    weekday = weekdays[datetime.weekday()]
    
    return weekday

mi_fecha = datetime(1879, 3, 14)
print(get_dia_semana_for_humans(mi_fecha))


