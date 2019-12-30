from logs import Logger


def recipes_creation(recipeRequest):
    # 1. Comprobar si los datos de la receta son validos (hay que crear un facade)
    #   1.1 El nombre de receta debe de estar informado
    #   1.2 Debe de tener al menos un igrediente
    #   1.3 Los pasos de la receta deben de estar informados
    #   1.4 La foto debe de estar informada
    # 2. Hay que comprobar la coherencia de las relaciones en base de datos
    #   2.1 Si la receta tiene recetas relacionadas hay que comprobar que dichas recetas existen ya
    # 3. Hay que dar de alta los ingredientes
    #   3.1 Comprobar si los ingredientes existen en base de datos y si no existen crearlos
    # 4. Hay que salvar la receta en base de datos
    # 5. Hay que salvar la relación entre los ingredientes y la receta mediante el modelo
    #    IngredientsRecipesModel añadiendo la cantidad de cada ingrediente
    pass
