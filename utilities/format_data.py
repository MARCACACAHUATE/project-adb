from datetime import datetime


def format_date(date: datetime) -> str:
    month_index = date.month
    mes = { 
        1 :"enero",
        2 :"febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }

    return date.strftime(f"%d de {mes[month_index]} del %Y %H:%M")