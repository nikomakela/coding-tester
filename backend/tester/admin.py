from django.contrib import admin
from .models import Submission, PassedTest


class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "submission_time",
        "assignment_name",
        "submission_endpoint_address",
        "applicant_name",
        "applicant_address",
        "applicant_phone",
        "submission_code_address",
    )
    actions = ("download_csv",)
    list_filter = ["assignment_name", "submission_time"]
    search_fields = [
        "submission_endpoint_address",
        "applicant_name",
        "applicant_address",
        "applicant_phone",
        "submission_code_address",
    ]
    date_hierarchy = "submission_time"

    def download_csv(self, request, qset):
        import csv
        import django.http

        res = django.http.HttpResponse(content_type="text/csv")
        res["Content-Disposition"] = "attachment; filename=submissions.csv"
        w = csv.writer(res)
        w.writerow(
            (
                "Time",
                "Assignment",
                "Endpoint",
                "Applicant name",
                "Applicant phone",
                "Applicant email",
                "Source",
                "Competence",
                "Experience",
            )
        )
        for rec in qset:
            w.writerow(
                (
                    rec.submission_time,
                    rec.assignment_name,
                    rec.submission_endpoint_address,
                    rec.applicant_name,
                    rec.applicant_phone,
                    rec.applicant_address,
                    rec.submission_code_address,
                    rec.own_tech_competence,
                    rec.work_experience,
                )
            )
        return res

    download_csv.short_description = "Download selected rows as CSV file"


class PassedTestAdmin(admin.ModelAdmin):
    list_filter = ["submission__assignment_name", "submission__submission_time"]
    search_fields = [
        "submission__submission_endpoint_address",
        "submission__applicant_name",
        "submission__applicant_address",
        "submission__applicant_phone",
        "submission__submission_code_address",
    ]
    date_hierarchy = "submission__submission_time"


admin.site.register(Submission, SubmissionAdmin)
admin.site.register(PassedTest, PassedTestAdmin)
