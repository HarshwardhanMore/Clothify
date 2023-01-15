from django.shortcuts import render, redirect
from .models import Database
# Create your views here.


def home(request):
    return render(request, 'index.html')


def seller(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        price = request.POST.get('price')
        description = request.POST.get('description')
        superCategory = request.POST.get('supercategory')

        subCategories = request.POST.get('supercategory')
        subCategories = subCategories.split(' ')

        color = request.POST.get('color')
        brandName = request.POST.get('brandname')

        availableSize = request.POST.get('availablesize')
        availableSize = availableSize.split(' ')

        age = request.POST.get('age')
        season = request.POST.get('season')

        image = request.FILES.get('image')
        imageName = 'default'
        if (image):
            imageName = image.name

        database = Database.objects.create(name=name,
                                           gender=gender,
                                           price=price,
                                           description=description,
                                           superCategory=superCategory,
                                           subCategories=subCategories,
                                           color=color,
                                           brandName=brandName,
                                           availableSize=availableSize,
                                           age=age,
                                           season=season,
                                           image=image,
                                           imageName=imageName
                                           )
        database.save()
        return render(request, 'seller.html')

    return render(request, 'seller.html')


def shop(request):

    objects = Database.objects.all()

    # for i in object:
    #     print(i)
    # print(objects)
    # print(objects[0])
    # print(objects[1])
    print("----")

    # for i in range(len(objects)):
    #     print(objects[i])
    #     print(objects[i])

    products = []
    for i in range(len(objects)):
        products.append(objects[i])

    context = {
        'products': products,
    }

    return render(request, 'shop.html', context=context)
