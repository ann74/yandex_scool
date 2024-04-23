# Решение на разборе. Идея такая, что рассматриваем одинаково два случая, когда 2 бегуна встречаются
# в одной точке и в разных, для второго случая одного из бегунов делаем как бы зеркальным и рассматриваем
# снова момент нахождения в одной точке. При этом момент нахождения рассчитываем как разность расстояний
# поделить на скорость сближения (расхождения)

L, x1, v1, x2, v2 = map(int, input().split())

ans = 10**30
for rotation in range(2):
    deltax = (x2 - x1 + L) % L # Чтобы было положительным, если (x2 - x1) < 0
    deltav = v1 - v2
    if deltav < 0:
        deltav = -deltav
        deltax = (-deltax + L) % L
    if deltax == 0:
        ans = 0
    if deltav != 0:
        ans = min(ans, deltax / deltav)
    x2 = (-x2 + L) % L
    v2 = -v2

if ans == 10**30:
    print('NO')
else:
    print('YES')
    print(ans)

