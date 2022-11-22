import trees
import group

tree1 = trees.to_tree('a(bc)')
tree2 = trees.to_tree('(ab)c')
subdiv1 = tree1.get_interval_subdivision()
subdiv2 = tree2.get_interval_subdivision()
z = zip(subdiv1, subdiv2)
element = group.FGroupElement(z)

print(element.vertices)
print(element.dom_subdivision)
print(element.img_subdivision)
print(element.get_slopes())
