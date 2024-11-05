team1_num = 0
team2_num = 0
score_1 = int(input('введите количество решенных задач командой Мастера кода: '))
score_2 = int(input('введите количество решенных задач командой Волшебники данных: '))
team1_time = 1552.512
team2_time = 2153.31451

class Teams:
    def __init__(self, *args):
        self.file_names = args

    def team_count(self):
        for i in self.file_names:

            with open(i, encoding='UTF-8') as f_1:

                if i == 'team_1.txt':
                    line_1 = str(f_1.readlines())
                    team1_num = len(line_1.split(','))
                    print(team1_num)
                elif i == 'team_2.txt':
                    line_2 = str(f_1.readlines())
                    team2_num = len(line_2.split(','))
                    print(team2_num)


        print('В команде Мастера кода участников: %s' % team1_num, "!")
        print('В команде Волшебники данных участников: %s' % team2_num, "!")
        print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num),"!")
        pass



    def tasks(self):

        print('Команда Волшебники данных решила задач: {}'.format(score_2), "!")
        print('Волшебники данных решили задачи за {}'.format(team1_time), "c !")
        pass

    def resalt_all(self):
        print(f'Команды решили', score_1, 'и', score_2, 'задач.')
        if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
            win_1 = 'Победа команды Мастера кода!'
        elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
            win_1 = 'Победа команды Волшебники данных!'
        else:
            win_1 = 'Ничья'

        return win_1

    def total_time(self):
        tasks_total = score_1 + score_2
        time_avg = team1_time + team2_time

        print(f'Сегодня было решено', tasks_total,'задач, в среднем по ', time_avg,'секунды на задачу!.')
        pass


games_1 = Teams('team_1.txt', 'team_2.txt')
print(games_1.team_count())
print(games_1.tasks())
print(games_1.resalt_all())
print(games_1.total_time())