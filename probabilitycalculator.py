import copy
import random

class Hat:
    def __init__(self, **hatcolors):
        self.hatcolors = hatcolors
        self.contents = []
        for k, v in hatcolors.items():
          for i in range(v):
            self.contents.append(k)

    def draw(self, numberofballs):
        self.numberofballs = numberofballs
        # Below requires wider margin of error
        random.shuffle(self.contents)
        poppedcolors = []
        if numberofballs > len(self.contents):
          return self.contents
        x = 0
        while x < self.numberofballs:
            poppedcolors.append(self.contents[-1])
            self.contents.pop(-1)
            x += 1
        return poppedcolors

def experiment(hat, expected_balls = None, num_balls_drawn = 0, num_experiments = 0):
    count = 0
    copiedexpected = copy.deepcopy(expected_balls)

    expectednumbers = []
    for key in copiedexpected:
        expectednumbers.append(copiedexpected[key])
    
    for i in range(num_experiments):
        copiedhat = copy.deepcopy(hat)
        drawnballs = copiedhat.draw(num_balls_drawn)

        listdrawnballs = []
        for key in copiedexpected:
            listdrawnballs.append(drawnballs.count(key))

        if listdrawnballs >= expectednumbers:
            count += 1

    return count / num_experiments

    # copiedhat = copy.deepcopy(hat)
    # converttolist = copiedhat.contents()
    # nested = []
    # wantedcolors = []
    # if expected_balls == None:
    #     expected_balls = {}
    
    # if expected_balls:
    #     for k, v in expected_balls.items():
    #         expectedcolors = (k + ' ') * v
    #         splitexpectedcolors = expectedcolors.split()
    #         nested.append(splitexpectedcolors)
    #     for elements in nested:
    #         for element in elements:
    #             wantedcolors.append(element)
    # drawnballs = hat.draw(num_balls_drawn)
    # print(wantedcolors)
    # print(drawnballs)
    
    # for element in drawnballs:
    #     for item in wantedcolors:
    #         if element == item:
    #             wantedcolors.remove(item)
    #             drawnballs.remove(element)
                    

    # print(drawnballs)
    # print(wantedcolors)
    # count = 0
    # if len(wantedcolors) <= 0:
    #     count += 1
    # return count
    # counterdictlist = {}
    # counterwantlist = {}
    # for number in drawnballs:
    #     counterdrawn = {number: drawnballs.count(number)}
    #     counterdictlist.update(counterdrawn)
    # print(counterdictlist)
    # for counts in set(wantedcolors):
    #     counterwanted = {counts: wantedcolors.count(counts)}
    #     counterwantlist.update(counterwanted)

    # print(counterwantlist)    
    # print(counterdictlist)
    # print(drawnballs)
    # count = 0
    

    # way too slow
    # x = 0
    # count = 0
    # while x < 10:  
    #     if drawnballs.count('blue') == 2 and drawnballs.count('green'):
    #         count += 1
    #         x += 1
    # return count

        
hat1 = Hat(blue=3, red=2, green=6)
# print(hat1)
# print(hat1.contents())
print(experiment(hat = Hat(blue=3,red=2,green=6), expected_balls = {'blue':2, 'green':1}, num_balls_drawn = 4, num_experiments = 1000))