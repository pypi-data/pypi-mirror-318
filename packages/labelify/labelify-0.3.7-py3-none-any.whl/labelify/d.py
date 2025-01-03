data = """
    PREFIX ex: <http://exampl.ecom/>
    
    ex:a 
        ex:b ex:c ;
        ex:d ex:e , ex:f ;
    .
    
    ex:x
        ex:b ex:c ;
    .   
    
    ex:x
        ex:h ex:j ;
    .     
    """

from rdflib import Graph

g = Graph().parse(data=data)

print(len(set(g.subjects())))
print(len(set(g.predicates())))
print(len(set(g.objects())))