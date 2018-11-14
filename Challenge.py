import my_module
import SimpleGUICS2Pygame

my_list = my_module.LinkedList()
my_list.append("My first project")
my_list.append("Because I'm smart :)")
my_list.append("Right?")
my_list.append("Oh no? ok :(")
print my_list.length()
my_list.display()
print "Show me my second index here %s" % my_list.get(2)
my_list.erase(3)
print my_list.length()
my_list.display()
my_list.append("Hey guys!")
my_list.append("I love you all!")
print my_list.length()