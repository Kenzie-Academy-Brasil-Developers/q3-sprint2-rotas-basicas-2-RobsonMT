from datetime import datetime

def get_current_date_time():

    current_hour = datetime.now().hour

    message = 'Boa noite!'

    if current_hour < 12:
        message = 'Bom dia!'
        
    elif current_hour < 18:
        message = 'Boa tarde!'

    return {"current_datetime": datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"), "message": message}