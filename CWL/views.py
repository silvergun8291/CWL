from django.shortcuts import render
from django.db.models import Q
from .models import Company, Contract, Package, PackageLog


def index(request):
    return render(request, 'index.html')


def why(request):
    return render(request, 'why.html')


def about(request):
    return render(request, 'about.html')


def tracking(request):
    if request.method == 'POST':
        contract_number = request.POST['contract_number']
        contract = Contract.objects.filter(contract_number=contract_number).first()

        package = Package.objects.filter(contract_number=contract_number).first()
        package_number = package.package_number

        package_log = PackageLog.objects.filter(package_number=package_number).first()

        if contract != None:
            return render(request, 'result.html', {'contract': contract, 'package': package, 'package_log': package_log})
        else:
            return render(request, 'result.html', {'error': '해당 계약 번호를 찾을 수 없습니다.'})
    else:
        return render(request, 'tracking.html')


def privacy(request):
    return render(request, 'privacy.html')


def detail(request):
    details = list()
    contract_number = request.GET.get('contract_number')
    contract = Contract.objects.filter(contract_number=contract_number).first()

    packages = Package.objects.filter(contract_number=contract_number)

    for package in packages:
        package_log = PackageLog.objects.filter(package_number=package.package_number).first()
        detail = dict()
        # TODO Fill the required fields in detail element
        detail['contract_number'] = contract.contract_number
        detail['package_name'] = package.package_name
        detail['quantity'] = package.quantity
        detail['departure_address'] = contract.departure_address
        detail['arrival_address'] = contract.arrival_address
        detail['temperature'] = package_log.temperature
        detail['humidity'] = package_log.humidity
        details.append(detail)

    return render(request, 'detail.html', {'details': details})
