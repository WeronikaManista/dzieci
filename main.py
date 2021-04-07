# 52 weeks = 2 cans * 52

# potrzeba 500 cans,    ile to zajmie?

# def spaceship_building(cans):
#     total_cans = 0
#     for week in range(1, 53):
#         total_cans = total_cans + cans

cans = 0
week = 0

def spacebuilding(cans, week):
    while cans < 500:
        cans = cans + 2
        week = week + 1
        print(f'week {week} = {cans}')
    print(f'we need: {cans}. Its {week} weeks in total')
spacebuilding(cans, week)
