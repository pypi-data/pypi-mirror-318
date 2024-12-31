import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from .utils import deleteFistDotte, dynamicRoute,importModule,convertPathToModulePath
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# 
def FIND_ROUTES(base_path):
    routes:list = []
    
    # Verify if the 'app' folder exists
    if os.path.exists(base_path) and os.path.isdir(base_path):
        # Explore the 'app' folder and its subfolders
        for root, dirs, files in os.walk(base_path):
            #supprimers des _folder
            dirs[:] = [d for d in dirs if not d.startswith("_")]

            route = {
                "pathname": f"{'/' if os.path.basename(root) == base_path else '/' +  deleteFistDotte(os.path.relpath(root, base_path).replace("\\","/"))}",
                "dirName": root
            }
            controller = os.path.join(root, 'controller.py')

            # Check for files and add to dictionary
            if os.path.exists(controller):
                route["module"] = convertPathToModulePath(f"{root}/controller")    

            routes.append(route)

    return routes



def Router(app: FastAPI):
    """
    Charge dynamiquement les routes à partir du répertoire 'app'.
    """
    # Parcours des répertoires dans 'app'
    routes = FIND_ROUTES(base_path="app")
    HTTP_METHODES:tuple = ["DELETE","GET","OPTIONS","PATCH","POST","PUT"]
    for route in routes:

        pathname = dynamicRoute(route_in=route["pathname"])

        if "module" in route:

            module = importModule(path=route["module"])
            for function_name in dir(module):
                function = getattr(module, function_name)
                
                # Vérifie que l'attribut est une fonction utilisable par FastAPI
                if callable(function) and hasattr(function, "__annotations__"):
                    params = getattr(function, "params", {})
                    
                    
                    # Ajout de la route pour chaque méthode HTTP
                    if function_name in HTTP_METHODES:

                        app.add_api_route(
                            path=pathname,
                            endpoint=function,
                            methods=[function_name],
                            **{key: value for key, value in params.items() if key != "tags"}, 
                            tags=params.get("tags") if params.get("tags") else [pathname]
                        )


                    # Ajout d'une route WebSocket si la méthode 'Socket' existe
                    elif function_name == "SOCKET":
                        app.websocket(path=f"{pathname}/ws")(function)


