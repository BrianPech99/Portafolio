# Función para imprimir la tabla de multiplicar de un número
function tabla_multiplicar(n)
    println("Tabla de multiplicar del ", n, ":")
    for i in 1:10
        println("$n x $i = $(n*i)")
    end
end

# Ejecutamos
tabla_multiplicar(5)
