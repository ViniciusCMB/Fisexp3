import matplotlib.pyplot as plt

# Pontos amostrais
x = [10,20,30,40,50,60,70,80,90]
y = [420,365,285,220,176,117,69,34,5]
plt.plot(x, y, 'r.', label='Pontos amostrais')

# Regressão linear (a*x + b)
n = len(x)

sumx = round(sum(x),2)
sumy = round(sum(y),2)

x2 = [i**2 for i in x]
sumx2 = round(sum(x2),2)

xy = [x[i]*y[i] for i in range(n)]
sumxy = round(sum(xy),2)

a = round((-(sumx*sumy)+(n*sumxy))/((n*sumx2)-(sumx**2)),2)

b = round((sumy-(a*sumx))/n,2)

fy = [a*i+b for i in range(10,90)]
fx = [i for i in range(10,90)]

plt.plot(fx, fy, 'k',label=f'Ajuste linear $y={a:.2f}*x+{b:.2f}$')

# Vida média a 36.5°C
t = 36.5
vm = round((a*t)+b,2)
plt.plot(t, vm, 'g.', label=f'Vida média à ${t:.1f}°C = {vm:.2f}$')

# Danificado instantâno
vm2 = 0
xvm2 = round((vm2-b)/a,2)
plt.plot(xvm2, vm2, 'b.', label=f'Dano instantâneo em $T = {xvm2:.2f}°C$')


# Configura o Grafico
plt.grid()
plt.legend()
plt.savefig('q1.png')
