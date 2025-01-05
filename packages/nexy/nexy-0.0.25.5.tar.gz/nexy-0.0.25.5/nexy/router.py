import os
from fastapi import FastAPI, WebSocket
from inspect import isclass, getmembers, isfunction
from types import ModuleType
from typing import Callable
from .utils import deleteFistDotte, dynamicRoute, importModule, convertPathToModulePath


# Trouver les routes dans le dossier 'app'
def FIND_ROUTES(base_path: str):
    routes = []

    if os.path.exists(base_path) and os.path.isdir(base_path):
        for root, dirs, files in os.walk(base_path):
            # Filtrer les dossiers commençant par '_'
            dirs[:] = [d for d in dirs if not d.startswith("_")]

            route = {
                "pathname": f"{'/' if os.path.basename(root) == base_path else '/' + deleteFistDotte(os.path.relpath(root, base_path).replace('\\', '/'))}",
                "dirName": root,
            }
            controller = os.path.join(root, "controller.py")

            if os.path.exists(controller):
                route["module"] = convertPathToModulePath(f"{root}/controller")

            routes.append(route)

    return routes


# Validation du type de contrôleur (classe ou fonctions)
def validate_controller_style(module: ModuleType, pathname: str):
    has_class = hasattr(module, "default") and isclass(module.default)
    has_functions = any(isfunction(func) for _, func in getmembers(module))

    if has_class and has_functions:
        raise ValueError(
            f"Le contrôleur {pathname} contient à la fois une classe et des fonctions HTTP/SOCKET. "
            "Choisissez l'un des deux styles."
        )

    return "class" if has_class else "function"


# Gestion des contrôleurs de classe
def handle_class_controller(app: FastAPI, Controller: type, pathname: str, HTTP_METHODS: tuple):
    controller_instance = Controller()
    for name, method in getmembers(Controller, isfunction):
        if name.upper() in HTTP_METHODS:
            app.add_api_route(
                path=pathname,
                endpoint=getattr(controller_instance, name),
                methods=[name.upper()],
            )
            print(f"✅ Ajouté la route {name.upper()} : {pathname}")

        elif name == "SOCKET":
            app.add_api_websocket_route(
                path=f"{pathname}/ws",
                endpoint=getattr(controller_instance, name),
            )
            print(f"✅ Ajouté la route WebSocket : {pathname}/ws")


# Gestion des fonctions dans un module
def handle_function_controller(app: FastAPI, module: ModuleType, pathname: str, HTTP_METHODS: tuple):
    for name, function in getmembers(module, isfunction):
        if name.upper() in HTTP_METHODS:
            app.add_api_route(
                path=pathname,
                endpoint=function,
                methods=[name.upper()],
            )
            print(f"✅ Ajouté la route {name.upper()} : {pathname}")

        elif name == "SOCKET":
            app.add_api_websocket_route(
                path=f"{pathname}/ws",
                endpoint=function,
            )
            print(f"✅ Ajouté la route WebSocket : {pathname}/ws")


# Routeur principal
def Router(app: FastAPI):
    """
    Charge dynamiquement les routes à partir du répertoire 'app'.
    """
    routes = FIND_ROUTES(base_path="app")
    HTTP_METHODS = ("DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT")

    for route in routes:
        pathname = dynamicRoute(route_in=route["pathname"])

        if "module" in route:
            try:
                module = importModule(path=route["module"])

                # Valider le style du contrôleur
                style = validate_controller_style(module, pathname)
                print(f"📝 Style du contrôleur pour {pathname} : {style}")

                if style == "class":
                    Controller = getattr(module, "default", None)
                    handle_class_controller(app, Controller, pathname, HTTP_METHODS)
                else:
                    handle_function_controller(app, module, pathname, HTTP_METHODS)

            except ValueError as e:
                print(f"❌ {e}")
                app.add_api_route(
                    path=pathname,
                    endpoint=lambda: {"error": str(e)},
                    methods=["GET"],
                    status_code=500,
                )
            except Exception as e:
                print(f"❌ Erreur lors du chargement du module {route['module']}: {e}")
                app.add_api_route(
                    path=pathname,
                    endpoint=lambda: {"error": f"Erreur : {str(e)}"},
                    methods=["GET"],
                    status_code=500,
                )
