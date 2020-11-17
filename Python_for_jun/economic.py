# q_analog = 600  # время аналога (человеко-часов)
# n_cp = 1.2  # сложность разрабатываемой программы
# n_kv = 1.0  # коэфф квалификации программиста (от 2 до 3 лет)
#
# q_prog = (q_analog * n_cp) / n_kv  # трудозатраты на программирование (чел.-часов)
# print('Трудозатраты на программирование программы - ', q_prog)
#
# n_a = 0.3  # коэфф  на разработку алгоритма
# n_t = 0.3  # коэфф  на тестирование программы
# n_i = 0.3  # коэфф  на внесение исправлений в программу
# n_doc = 0.35  # коэфф  на написание документации
#
# t_2_prog = q_prog / (n_a + 1 + n_t + n_i + n_doc)
# print('время на написание алгоритма - ', t_2_prog)
#
# t_1_razrab = n_a * t_2_prog
# print('время на разработку алгоритма - ', t_1_razrab)
#
# t_3_doc = t_2_prog * (n_t + n_i + n_doc)
# print('время на документацию - ', t_3_doc)
#
# print('проверка - ', t_1_razrab + t_2_prog + t_3_doc)
#
# # =============================================================
#
# t_p = 8  # продолжительность рабочего дня
# D_k = 366  # общее число дней в году
# D_b_p = 119  # число выходных и праздничных дней в году
#
# T_month = 3  # (q_prog / 24) / 22  # время выполнения проекта в месяцах, 730 - столько часов в 1 месяце
# # print('\n', T_month)
# F_m = (t_p * (D_k - D_b_p)) / 12
# print('\nФонд времени в текущем месяце - ', F_m)
# F = T_month * F_m
# print('Фонд рабочего времени', F)
# N = q_prog / F
# print('Средняя численность исполнителей', N)
#
# t_hours_table = 8 + 88 + 56 + 48 + 48 + 64 + 56 + 8 + 16 + 8 + 16 + 304
# print('\nВремя чаловеко-часов по таблице', t_hours_table)
# t_days_table = 1 + 11 + 7 + 6 + 6 + 8 + 7 + 1 + 2 + 1 + 2 + 38
# print('Время чаловеко-дней по таблице', t_days_table)
#
#
# def salary(t_zan, oklad, name=''):
#     # o_month = oklad * (1 + 13 / 100)
#     # если вдруг надо считать без ндфл:
#     o_month = oklad
#     print('\nМесячный оклад', name, o_month)
#     o_dn = o_month * 8 / F_m
#     print('Дневной оклад', name, o_dn)
#     t_zan = t_zan / 8  # перевели в дни
#     c_zar_isp = t_zan * o_dn
#     print(f'Заработная плата {name} за весь период работы ({t_zan}) равен {c_zar_isp}')
#     print('НАЛОГ:')
#     c_zar_dop = 0.2 * c_zar_isp
#     print('Дополнительный расход на зарплату', name, c_zar_dop)
#     h_social = (
#                        22 + 5.1 + 2.9 + 0.2) / 100  # отчисления работадателя в (ИФНС). Пенсионное 22%, Медицинское 5.1%, Социальное 2.9%, Отчисления в ФСС 0.2%
#     c_zar_nalog = (c_zar_isp + c_zar_dop) * h_social
#     print(f'Отчисления в ИФНС за {name} равны {c_zar_nalog}')
#     return [c_zar_nalog + c_zar_dop + c_zar_isp, c_zar_isp]
#
#
# t_ruc = 8 + 88  # часов
# ruc = salary(t_ruc, 70000, 'Руководитель')
#
# t_prog = q_prog - t_ruc
# prog = salary(t_prog, 50000, "Программист")
#
# C_naklad = (ruc[1] + prog[1]) * 0.5
# print('\nНакладные расходы', C_naklad)
#
# all_salary = ruc[0] + prog[0]
# print('\nОбщие затраты на зарплату', all_salary)
#
# expenses_of_staff = 9000 * 3 + 1200 * 1 + 29000  # комп, принтер, лицуха лабвью
# print('затраты на оборудование', expenses_of_staff)
# expenses_of_office = 20000 * 3
# zatraty_all = all_salary + expenses_of_office + expenses_of_staff + C_naklad
# print('\nОбщие затраты', zatraty_all)
#
# print('\nCметная стоимость проекта', zatraty_all + zatraty_all * 0.2)


marks = [4, 4, 4, 4, 4,
         5, 4, 5, 4, 5,
         4, 4, 4, 4,
         4, 5, 4, 5,
         4, 4, 4, 4,
         5, 4, 4, 4, 4,
         4, 4, 4,
         4, 4, 3, 5,
         4, 5, 4, 4, 5,
         5, 5, 5, 5, 4,
         5, 5, 3,  # это 12 сем
         5, 5, 5, 5, 4,  # это практика
         4, 5, 5, 4, 5,  # это курсачи
         5, 5, 5, 5,  # это нирс
         5]

print(len(marks))

print('\n', marks.count(3) / len(marks))
print(marks.count(4) / len(marks))
print(marks.count(5) / len(marks))

av_mark = sum(marks) / len(marks)
print('\n', av_mark)
