import random

from django.views import View

from django.shortcuts import render

from django.http import HttpResponseNotFound

from data import departures, tours


class MainView(View):
    def get(self, request):
        context = {
            "tours": random.sample(list(tours.items()), 6)
        }

        return render(request, 'tours/index.html', context=context)


class DepartureView(View):
    def get(self, request, departure):
        list_tours = list(filter(lambda tour: departure == tour[1]['departure'], tours.items()))

        context = {
            'tours': list_tours,
            'departure': departures[departure],
            'number_tours': len(list_tours),
            'max_price': get_max_value('price', list_tours),
            'min_price': get_min_value('price', list_tours),
            'max_nights': get_max_value('nights', list_tours),
            'min_nights': get_min_value('nights', list_tours),
        }

        return render(request, 'tours/departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        tour = tours[id]

        context = {
            'tour': tour,
            'stars': show_count_stars(int(tour.get('stars'))),
            'departure': departures[tour['departure']]
        }

        return render(request, 'tours/tour.html', context=context)


def show_count_stars(stars):
    result = ''
    for star in range(stars):
        result += '★'

    return result


def get_max_value(parameter, list_tours):
    max_value = list_tours[0][1][parameter]

    for tour in list_tours:
        if tour[1][parameter] > max_value:
            max_value = tour[1][parameter]

    return max_value


def get_min_value(parameter, list_tours):
    min_value = list_tours[0][1][parameter]

    for tour in list_tours:
        if tour[1][parameter] < min_value:
            min_value = tour[1][parameter]

    return min_value


def custom_handler_404(request, exception):
    return HttpResponseNotFound(request, 'Ой, что то сломалось... Простите извините!')


def custom_handler_500(request):
    return HttpResponseNotFound(request, 'Ой, что то сломалось... Простите извините!')
