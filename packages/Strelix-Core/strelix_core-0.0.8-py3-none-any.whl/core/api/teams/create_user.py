from django.contrib import messages
from django.shortcuts import render

from core.decorators import web_require_scopes
from core.models import Organization
from core.service.permissions.scopes import get_permissions_from_request
from core.service.teams.create_user import create_user_service
from core.types.requests import WebRequest


@web_require_scopes("team:invite", True, True)
def create_user_endpoint(request: WebRequest):
    team_id = request.POST.get("team_id", "")

    team: Organization | None = Organization.objects.filter(id=team_id).first()

    if not team:
        messages.error(request, "This team does not exist")
        return render(request, "core/base/toast.html")

    if not team.is_owner(request.user):
        messages.error(request, "Only the team owner can create users")
        return render(request, "core/base/toast.html")

    first_name = request.POST.get("first_name", "")
    last_name = request.POST.get("last_name", "")
    email = request.POST.get("email", "")
    permissions: list = get_permissions_from_request(request)

    created_user = create_user_service(request, email, team, first_name, last_name, permissions)

    if created_user.failed:
        messages.error(request, created_user.error)
        return render(request, "core/base/toast.html")
    else:
        messages.success(request, f"The account for {first_name} was created successfully. They have been emailed instructions.")
    return render(request, "core/base/toast.html")
