import numpy as np

def solve_ode(start, end, h, max_calls, eps, fs, initial_conditions):
    t = start
    v = np.array(initial_conditions, dtype=float)
    kounter = [0]
    print(f"{t:13.6f}{h:13.6f}{0:13d}{0:13d}", *[f"{x:12.6f}" for x in v])

    def runge_kutta_step(t, v, h, fs, kounter):
        k1 = fs(t, v, kounter)
        k2 = fs(t + h / 2, v + h / 2 * k1, kounter)
        k3 = fs(t + h / 2, v + h / 2 * k2, kounter)
        k4 = fs(t + h, v + h * k3, kounter)
        return v + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    while t < end and kounter[0] < max_calls:
        v_new = runge_kutta_step(t, v, h, fs, kounter)
        v_half = runge_kutta_step(t, v, h / 2, fs, kounter)
        v_double_half = runge_kutta_step(t + h / 2, v_half, h / 2, fs, kounter)

        r = np.linalg.norm(v_double_half - v_new) / 15  # Оценка ошибки по правилу Рунге

        if r > eps:
            h /= 2
        elif r < eps / 64:
            h *= 2

        if r < eps:
            t += h
            v = v_new
            print(f"{t:13.6f}{h:13.6f}{r:13.5e}{kounter[0]:13d}", *[f"{x:12.6f}" for x in v])

t_0 = float(input())
T = float(input())
h_0 = float(input())
N_x = int(input())
eps = float(input())
n = int(input())

function_code = []
for i in range(n + 3):
    line = input()
    function_code.append(line)

# Создание функции
function_definition = "\n".join(function_code)
exec(function_definition)

input_string = input()
initial_conditions = [float(x) for x in input_string.split()]

solve_ode(t_0, T, h_0, N_x, eps, fs, initial_conditions)
