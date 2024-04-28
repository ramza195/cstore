from category.models import Category


def get_all_categories(request):
    get_categories = Category.objects.all()
    return {'categories': get_categories}