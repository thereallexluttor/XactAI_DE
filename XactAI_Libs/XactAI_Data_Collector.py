import pandas as pd
import numba as nb

class CleanDataframe:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    # Este método puede pasar cualquier archivo .csv a dataframe 

    def csv_to_dataframe(self):
    # Lee el archivo CSV y crea un DataFrame de pandas
       self.dataframe = pd.read_csv(self.dataframe)

        # Devuelve el DataFrame
       return self.dataframe
    
    # Este método puede limpiar un dataframe y eliminar datos duplicados y faltantes
    
    def clean_dataframe(self):
        """
        Limpia el dataframe eliminando valores duplicados y faltantes.
        
        Returns:
        - DataFrame: Nuevo dataframe limpio sin valores duplicados ni faltantes.
        """
        # Limpiar valores duplicados
        self.dataframe = self.dataframe.drop_duplicates()
        
        # Limpiar valores nulos
        self.dataframe = self.dataframe.dropna()

        # Limpiar valores NaN en filas completas
        self.dataframe = self.dataframe.dropna(how='all')

        return self.dataframe
    
    # Este método da formato estándar a los nombres de las columnas del dataframe
    
    def name_formater(self):
        """
        Da formato estándar a los nombres de las columnas del dataframe.
        
        Returns:
        - DataFrame: DataFrame con los nombres de las columnas en formato estándar.
        """
        # Limpiar los nombres de las columnas y obtener los mejores
        self.dataframe.columns = [x.lower().replace(" ","_").replace("?","")\
        .replace("-","_").replace(r"/","_").replace("\\","_").replace("%",'')\
        .replace(")","").replace(r"(","").replace("$","") for x in self.dataframe.columns]
        
        return self.dataframe
    # Este método nos brinda los nombres de las columnas para pasar a través de GPT-3    
    
    def get_column_names(self):
        """
        Obtiene los nombres de las columnas del dataframe.
        
        Returns:
        - list: Lista de los nombres de las columnas del dataframe.
        """
        return list(self.dataframe.columns)
    
    def get_columns_info(self):
          # Creamos un diccionario para almacenar la información de cada columna
          column_info = {}

          # Recorremos las columnas del dataframe
          for col in self.dataframe.columns:
            # Obtenemos el tipo de dato de la columna
            col_type = str(self.dataframe[col].dtype)

            # Guardamos el tipo de dato de la columna en la lista 'types'
            #self.dataframe.types.append(col_type)

            # Agregamos la información de la columna al diccionario
            column_info[col] = col_type
          return column_info