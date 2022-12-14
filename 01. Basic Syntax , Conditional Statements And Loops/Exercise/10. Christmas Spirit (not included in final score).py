quantity = int(input())
days = int(input())

christmas_spirit = 0
total_cost = 0

condition_5th_day = False
for day in range(1, days + 1):
    condition_5th_day = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        christmas_spirit += 5
        total_cost += 2 * quantity

    if day % 3 == 0:
        christmas_spirit += 13
        total_cost += (5 * quantity) + (3 * quantity)
        condition_5th_day = True

    if day % 5 == 0:
        christmas_spirit += 17
        total_cost += quantity * 15

        if condition_5th_day:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += 23

        if day == days:
            christmas_spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {christmas_spirit}')




# quantity = int(input())
# days_count = int(input())

# ornament_sets = 2
# tree_skirts = 5
# tree_garlands = 3
# tree_lights = 15
#
# total_cost = 0
# christmas_spirit = 0
#
# for day in range(1, days_count+1):
#     if day % 11 == 0:
#         quantity += 2
#     if day % 2 == 0:
#         total_cost += quantity * ornament_sets
#         christmas_spirit += 5
#     if day % 3 == 0:
#         total_cost += quantity * (tree_skirts + tree_garlands)
#         christmas_spirit += 13
#     if day % 5 == 0:
#         total_cost += quantity * tree_lights
#         christmas_spirit += 17
#         if day % 3 == 0:
#             christmas_spirit += 30
#     if day % 10 == 0:
#         total_cost += tree_skirts + tree_garlands + tree_lights
#         christmas_spirit -= 20
#         if day == days_count:
#             christmas_spirit -= 30
#
# print(f'Total cost: {total_cost}\nTotal spirit: {christmas_spirit}')
