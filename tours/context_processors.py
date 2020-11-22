def statistic(request):
    statistic = {
        'title': "Stepik Travel",
        'subtitle': "Для тех, кого отвлекают дома",
        'description': "Лучшие направления, где никто не будет вам мешать сидеть на берегу \
         и изучать программирование, дизайн, разработку игр и управление продуктами",
    }

    return statistic


def departures(request):
    departures = {
        "msk": "Из Москвы",
        "spb": "Из Петербурга",
        "nsk": "Из Новосибирска",
        "ekb": "Из Екатеринбурга",
        "kazan": "Из Казани",
    }

    return departures
