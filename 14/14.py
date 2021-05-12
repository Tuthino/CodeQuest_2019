import sys

class Link(object):
    def __init__(self,city_from,city_to):

        self.city_from = city_from
        self.city_to = city_to

class Graph(object):
    def __init__(self,links=[]):
        self.links = links
    def insert_link(self,city_from, city_to):
        new_link = Link(city_from, city_to)
        self.links.append(new_link)
    def find_last_first(self):
        city_from_list = []
        city_to_list =  []
        for link in self.links:
            city_from_list.append(link.city_from)
            city_to_list.append(link.city_to)
        last = list(set(city_to_list) - set(city_from_list))
        first = list(set(city_from_list) - set(city_to_list))
        return str(last)[2:-2], str(first)[2:-2]
    def find_way(self,last):
        for link in self.links:
            if link.city_to == last:
                print(link.city_to)
                self.find_way(link.city_from)



with sys.stdin as i:
    n = int(i.readline().rstrip())
    for _ in range(n):
        cases = int(i.readline().rstrip())
        graph = Graph(links=[])
        for _ in range(cases):
            city_from, city_to = [x for x in i.readline().rstrip().split()]
            graph.insert_link(city_from,city_to)
        last_city,first_city = [x for x in graph.find_last_first()]
        graph.find_way(last_city)
        print(first_city)

