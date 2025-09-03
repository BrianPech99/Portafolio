import Pkg
Pkg.add("Plots")
using Plots   # Paquete para graficar

# Rango de valores
x = 0:0.1:2π

# Definimos funciones matemáticas
y1 = sin.(x)
y2 = cos.(x)

# Graficamos
plot(x, y1, label="sin(x)", linewidth=2, color=:blue)
plot!(x, y2, label="cos(x)", linewidth=2, color=:red)

savefig("seno_coseno.png")  # Guarda la gráfica como imagen
display(plot!)  # Muestra la gráfica