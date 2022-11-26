salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for f in range(0, months):
    if f < 1: #  В первый месяц повышения цен нет
        delta = spend - salary
        money_capital += delta
    if f >= 1: # Со второго месяца с повышением цен
        spend *= 1 + increase
        delta = spend - salary
        money_capital += delta

print(round(money_capital))
