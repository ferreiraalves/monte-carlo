import random
import matplotlib.pyplot as plt

stories = 15
story_upper_limit = 5
iterations = 5

def work_work():
    days = random.randint(1, story_upper_limit)
    return days

def develop(total_days, total_stories):

    final_days = []
    story_num = []
    days = []
    story = 1
    story_num.append(0)
    days.append(total_days)
    while story < total_stories:
        total_days = total_days + work_work()
        story_num.append(story)
        days.append(total_days)
        story = story + 1
    plt.plot(story_num, days)

    final_days.append(days[-1])
    return (final_days)


x = 1
results = []
while x <= iterations:
    ending_fund = develop(0, stories)
    results.append(ending_fund[0])
    x = x+1


plt.ylabel('Days')
plt.xlabel('Total stories')
print("Numero de dias necessários para conclusão do projeto: " + str(sum(ending_fund)/len(ending_fund)))
plt.show()

