ingreso_mensual = 72000
gasto_mensual = 67000

if ingreso_mensual > 10000:  # SÍ ..
    if ingreso_mensual - gasto_mensual >= 7000:
        print("estas bien en cualquier parte del mundo")
    elif ingreso_mensual - gasto_mensual >= 3000:
        print("puedes ahorrar más")
    else:
        print("gastas demasiado")
    
elif ingreso_mensual >= 1000:  #EN OTRO CASO SÍ ..
    print("estas bien en latinoamerica")
    
elif ingreso_mensual >= 500:  #EN OTRO CASO SÍ ..
    print("estas bien en x")
    
elif ingreso_mensual >= 200:  #EN OTRO CASO SÍ ..
    print("estas bien en ..")
    
else:  # SI NO
    print("ups")