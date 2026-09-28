from cola import Cola
import linecache

def get_value_from_file(filename,index):
    line = linecache.getline(filename, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split


class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0

class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root
    
    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arribo(self.root)
            while cola_tree.tamano() > 0:
                node = cola_tree.atencion()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arribo(node.left)
                if node.right is not None:
                    cola_tree.arribo(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)
        
        __inorden_file(self.root, file_name)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

        __inorden_start_with(self.root, cadena)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)
 
    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)

    # ejercicio 1
    def altura_subarbol_izq(self):
        def __altura_izq(root):
            if root is None:
                return 0
            return 1 + max(__altura_izq(root.left), __altura_izq(root.right))
        return __altura_izq(self.root.left)

    def altura_subarbol_der(self):
        def __altura_der(root):
            if root is None:
                return 0 
            return 1 + max(__altura_der(root.left), __altura_der(root.right))
        return __altura_der(self.root.right)  

    def contar_pares_impares(self):
        def __contar_pares_impares(root):
            par = 0
            impar = 0 
            if root is not None:
                pares_izq, impares_izq = __contar_pares_impares(root.left)
                if root.value % 2 == 0:
                    par = 1 
                else:
                    impar = 1 
                pares_der, impares_der = __contar_pares_impares(root.right)
                
                par += pares_izq + pares_der
                impar += impares_izq + impares_der
            return par, impar
        par, impar = __contar_pares_impares(self.root)
        return par, impar
    
    # ejercicio 4 
    def get_left_child(self,key):
        '''retorna el hijo izquierdo de un nodo'''
        node = self.search(key)
        if node is not None and node.left is not None:
            return node.left.value
        return None

    def get_right_child(self,key):
        '''retorna el hijo derecho de un nodo'''
        node = self.search(key)
        if node is not None and node.right is not None:
            return node.right.value
        return None
    
    # ejercicio 5
    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero) 

    def generar_bosque_s_v(self):
        arbol_superheroes = BinaryTree()
        arbol_villanos = BinaryTree()
        
        def __generar_bosque_s_v(root):
            if root is not None:
                if root.other_values: # si other_values es True
                    arbol_superheroes.insert_node(root.value, True)
                else:
                    arbol_villanos.insert_node(root.value, False)
                __generar_bosque_s_v(root.left)
                __generar_bosque_s_v(root.right)
        
        __generar_bosque_s_v(self.root)
       
        nodos_superheroes = arbol_superheroes.contar_heroes()
        nodos_villanos= arbol_villanos.contar_villanos()
        print('arbol de superheroes: ')
        arbol_superheroes.inorden_super_or_villano(True)
        print('arbol de villanos: ')
        arbol_villanos.inorden_super_or_villano(False)

        return {
                'nodos_superheroes':nodos_superheroes,
                'nodos_villanos':nodos_villanos,
                }

    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
   
    def contar_villanos(self):
        def __contar_villanos(root):
            count = 0
            if root is not None:
                if root.other_values is False:
                    count = 1
                count += __contar_villanos(root.left)
                count += __contar_villanos(root.right)
            return count
        return __contar_villanos(self.root)

    def postorden_superheroe(self, is_hero):
        def __postorden_hereo(root, is_hero):
            if root is not None:
                __postorden_hereo(root.right, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __postorden_hereo(root.left, is_hero)
        __postorden_hereo(self.root, is_hero)

    # ejercicio 6 
    def inorden_jedi_master(self,file_name,rank):
        def __inorden_jedi_master(root,file_name,rank):
            if root is not None:
                __inorden_jedi_master(root.left, file_name, rank)
                value = get_value_from_file(file_name, root.other_values)
                if rank in value[1].split('/'):
                    print(root.value, value[1].split('/'))
                __inorden_jedi_master(root.right, file_name, rank)
            
        __inorden_jedi_master(self.root,file_name, rank)

    def inorden_green_lightsaber(self,file_name,color):
        def __inorden_green_lightsaber(root,file_name,color):
            if root is not None:
                __inorden_green_lightsaber(root.left, file_name, color)
                value = get_value_from_file(file_name, root.other_values)
                if color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_green_lightsaber(root.right, file_name, color)
            
        __inorden_green_lightsaber(self.root,file_name, color)

    def inorden_with_master(self,file_name):
        def __inorden_with_master(root, file_name):
            if root is not None:
                __inorden_with_master(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if '-' not in value[3].split('/'):
                    print(root.value, value[3].split('/'))
                __inorden_with_master(root.right,file_name)

        __inorden_with_master(self.root,file_name)

    def inorden_by_spicie(self,file_name,spicies):
        def __inorden_by_spicie(root, file_name,spicies):
            if root is not None:
                __inorden_by_spicie(root.left, file_name,spicies)
                value = get_value_from_file(file_name, root.other_values)
                for spicie in spicies:
                    if spicie in value[2].split('/'):
                        print(root.value, value[2].split('/'))
                __inorden_by_spicie(root.right,file_name,spicies)

        __inorden_by_spicie(self.root,file_name, spicies)

    def inorden_start_with_jedi(self,cadena):
        def __inorden_start_with_jedi(root,cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right,cadena)
        __inorden_start_with_jedi(self.root, cadena)

    def inorden_contain_hypen(self,cadena):
        def __inorden_contain_hypen(root,cadena):
            if root is not None:
                __inorden_contain_hypen(root.left,cadena)
                if cadena in root.value:
                    print(root.value)
                __inorden_contain_hypen(root.right,cadena)
        __inorden_contain_hypen(self.root, cadena)

    # ejercicio 8
    def find_min(self):
        '''retorna el valor minomo de un nodo en un arbol'''
        def __find_min_node(root):
            if root is None:
                return None
            if root.left is None:
                return root.value
            return __find_min_node(root.left)
        return __find_min_node(self.root)

    def find_max(self):
        '''retorna el valor maximo de un nodo en un arbol'''
        def __find_max_node(root):
            if root is None:
                return None
            if root.right is None:
                return root.value
            return __find_max_node(root.right)
        return __find_max_node(self.root)


    # ejercicio 23
    def inorden_criatura_defeat_by(self):
        def __inorden_criatura_defeat_by(root):
            if root is not None:
                __inorden_criatura_defeat_by(root.left)
                criatura = root.value
                derrotado = root.other_values['derrotado']
                print(f'nombre: {criatura}, derrotado por: {derrotado}')
                __inorden_criatura_defeat_by(root.right)

        __inorden_criatura_defeat_by(self.root)
    
    def inorden_add_field_captured(self):
        def __inorden_add_field_captured(root):
            if root is not None:
                __inorden_add_field_captured(root.left)
                root.other_values['capturada'] = None
                __inorden_add_field_captured(root.right)

        __inorden_add_field_captured(self.root)
    
    def inorden_add_field_description(self):
        def __inorden_add_field_description(root):
            if root is not None:
                __inorden_add_field_description(root.left)
                root.other_values['descripcion'] = None
                __inorden_add_field_description(root.right)
        
        __inorden_add_field_description(self.root)

    def inorden_add_description(self, creature_name, description):
        def __inorden_add_description(root, creature_name, description):
            if root is not None:
                __inorden_add_description(root.left, creature_name, description)
                if creature_name is not None:
                    root.other_values['descripcion'] = description
                __inorden_add_description(root.right,creature_name,description)
            
        __inorden_add_description(self.root,creature_name, description) 

    def inorden_add_capturer(self, capturer_dict):
        def __inorden_add_capturer(root, capturer_dict):
            if root is not None:
                __inorden_add_capturer(root.left, capturer_dict)
                if root.value in capturer_dict:
                    root.other_values['capturada'] = capturer_dict[root.value]
                __inorden_add_capturer(root.right, capturer_dict)
            
        __inorden_add_capturer(self.root, capturer_dict)

    def inorden_defeated_by(self, hero_name):
        def __inorden_defeated_by(root, hero_name):
            if root is not None:
                __inorden_defeated_by(root.left, hero_name)
                if root.other_values['derrotado'] == hero_name:
                    print(root.value)
                __inorden_defeated_by(root.right, hero_name)

        __inorden_defeated_by(self.root, hero_name)

    def inorden_not_defeated(self):
        def __inorden_not_defeated(root):
            if root is not None:
                __inorden_not_defeated(root.left)
                if root.other_values['derrotado'] is None:
                    print(root.value)
                __inorden_not_defeated(root.right)

        __inorden_not_defeated(self.root)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values['derrotado'] is not None:
                    if root.other_values['derrotado'] not in ranking:
                        ranking[root.other_values['derrotado']] = 1
                    else:
                        ranking[root.other_values['derrotado']] += 1 
                __inorden_ranking(root.right, ranking)

        __inorden_ranking(self.root, ranking)

    def inorden_captured_by(self, hero_name):
        def __inorden_captured_by(root, hero_name):
            if root is not None:
                __inorden_captured_by(root.left, hero_name)
                if root.other_values['capturada'] == 'Heracles':
                    print(root.value)
                __inorden_captured_by(root.right, hero_name)

        __inorden_captured_by(self.root, hero_name)
                






