import pygal

bar_chart = pygal.Bar()
bar_chart.add('Control', [3829, 7093])
bar_chart.add('100 uM Forskolin', [8541, 16841])
bar_chart.add('10 uM Forskolin', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.add('1 uM Forskolin', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.add('0.1 uM Forskolin', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
bar_chart.render_to_file("test.svg")