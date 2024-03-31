from django.shortcuts import render

# Create your views here.
def calculator(request):
    result = None

    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'addition':
            result = num1 + num2
        elif operation == 'subtraction':
            result = num1 - num2
        elif operation == 'multiplication':
            result = num1 * num2
        elif operation == 'division':
            result = num1 / num2
    return render(request, 'calculator.html', {'result': result})