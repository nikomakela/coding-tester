from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.templatetags.static import static
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.forms.models import model_to_dict


from .models import Submission
from .testing import run_tests_against, FailedTest

jinja_context = dict(
    assignment="sananmuunnos",
    url=reverse,
    static=static,
)


def submission_form(request, assignment=jinja_context["assignment"], **kw):
    if request.GET.get("format") == "json":
        explanation_template = f"tester/explanations/{assignment}.jinja"
        content = render_to_string(explanation_template, jinja_context)
        return JsonResponse({"content": content}, safe=True)
    return render(
        request,
        "tester/submission_form.jinja",
        {**jinja_context, **kw, **{"assignment": assignment}},
    )


def save_test_results(assignment, endpoint, results):
    sub = Submission(
        submission_endpoint_address=endpoint,
        assignment_name=assignment,
        submission_time=timezone.now(),
    )
    sub.save()
    for inp, result in results:
        sub.passedtest_set.create(test_input=inp, test_output=result)
    return sub


def run_tests(request, **kw):
    assignment = kw["assignment"]
    try:
        endpoint = request.POST["endpoint_url"]
    except KeyError:
        return HttpResponseBadRequest("Missing parameter: endpoint_url")
    try:
        results = run_tests_against(assignment, endpoint)
    except FailedTest as e:
        if request.POST.get("format") == "json":
            return JsonResponse(e.content, safe=True)

        return render(
            request,
            "tester/failed_test.jinja",
            {**jinja_context, **{"assignment": assignment}, **e.content},
        )
    submission = save_test_results(assignment, endpoint, results)
    redirect_url = "{path}{params}".format(
        path=reverse(
            "tester:results",
            args=(
                assignment,
                submission.id,
            ),
        ),
        params="?format=json" if request.POST.get("format") == "json" else "",
    )
    return HttpResponseRedirect(redirect_url)


def show_results(request, **kw):
    submission = get_object_or_404(
        Submission,
        id=kw["submission"],
        applicant_address="",
        submission_code_address="",
    )
    if request.GET.get("format") == "json":
        return JsonResponse({"results": model_to_dict(submission)}, safe=True)

    return render(
        request,
        "tester/result_report.jinja",
        {**jinja_context, **kw, "results": submission},
    )


def save_submission(request, **kw):
    submission = get_object_or_404(
        Submission,
        id=kw["submission"],
        assignment_name=kw["assignment"],
        submission_endpoint_address=request.POST["endpoint_url"],
    )
    submission.applicant_name = request.POST["applicant_name"]
    submission.applicant_phone = request.POST["applicant_phone"]
    submission.applicant_address = request.POST["applicant_address"]
    submission.submission_code_address = request.POST["source_code_url"]
    submission.own_tech_competence = request.POST["own_tech_competence"]
    submission.work_experience = request.POST["work_experience"]
    submission.save()

    if request.POST.get("format") == "json":
        return JsonResponse({"results": model_to_dict(submission)}, safe=True)

    return render(
        request,
        "tester/submission_accepted.jinja",
        {**jinja_context, **kw, "results": submission},
    )
