from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.conf import settings

from .openapi3 import get_docs
from .constants import DJANGO_APIS_OPENAPI_LOGIN_URL_KEY
from .constants import DJANGO_APIS_SWAGGER_LOGIN_REQUIRED_KEY

DJANGO_APIS_OPENAPI_LOGIN_URL = getattr(
    settings,
    DJANGO_APIS_OPENAPI_LOGIN_URL_KEY,
    reverse_lazy("admin:index"),
)
DJANGO_APIS_SWAGGER_LOGIN_REQUIRED = getattr(
    settings,
    DJANGO_APIS_SWAGGER_LOGIN_REQUIRED_KEY,
    True,
)
DJANGO_APIS_OPENAPI_SITES = getattr(
    settings,
    "DJANGO_APIS_OPENAPI_SITES",
    ["default"],
)


def swagger_ui_view(request):
    """SWAGGER-UI管理界面。"""
    return render(
        request,
        "django_apis/swagger_ui.html",
        {},
    )


def swagger_ui_data(request):
    """SWAGGER-UI数据接口。"""
    site = request.GET.get("site", "default")
    docs = get_docs(site=site)
    return JsonResponse(
        docs,
        json_dumps_params={
            "ensure_ascii": False,
        },
    )


def swagger_ui_init_js(request):
    """SWAGGER-UI JS脚本。"""
    return render(
        request,
        "django_apis/swagger_ui_init.js",
        {
            "sites": DJANGO_APIS_OPENAPI_SITES,
        },
        content_type="application/javascript",
    )


if DJANGO_APIS_SWAGGER_LOGIN_REQUIRED:
    swagger_ui_view = login_required(login_url=DJANGO_APIS_OPENAPI_LOGIN_URL)(
        swagger_ui_view
    )
    swagger_ui_data = login_required(login_url=DJANGO_APIS_OPENAPI_LOGIN_URL)(
        swagger_ui_data
    )
    swagger_ui_init_js = login_required(login_url=DJANGO_APIS_OPENAPI_LOGIN_URL)(
        swagger_ui_init_js
    )
