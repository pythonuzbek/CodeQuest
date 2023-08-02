import itertools

from django.shortcuts import render, get_list_or_404, get_object_or_404

from apps.models import Category, Problems
from apps.services import run_python_code, get_actual_type


def home(request):
    return render(request, 'index.html')


def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)


def problems(request, id):
    problems = get_list_or_404(Problems, category_id=id)
    context = {
        'problems': problems
    }
    return render(request, 'problems.html', context)


def problem(request, id):
    problem = get_object_or_404(Problems, id=id)
    if request.method == 'POST':
        code_input = request.POST['code']
        python_output, execution_time, memory_usage = run_python_code(code_input, 5)
        value, actual_type = get_actual_type(python_output)
        problem_value, problem_type = get_actual_type(problem.output)
        if value == problem_value:
            context = {
                'result': 'access',
                'value': value,
                'time': execution_time,
                'memory': memory_usage
            }
        else:
            context = {
                'result': 'error',
                'value': value
            }
        return render(request, 'solution.html',
                      {'problem': problem, 'result': context, 'value': value, 'time': execution_time,
                       'memory': memory_usage})
    # context = {
    #     'problem': problem,
    #
    # }
    examples = dict(itertools.islice(problem.input.items(), 3))
    return render(request, 'solution.html', {"problem": problem, "examples": examples})


def submission(request, id):
    return render(request, 'submission.html')


