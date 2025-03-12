from heroofukraine import *

#----------------------main------------------------------------------

hero1 = HeroOfUkraine('Roman',5, 'on Donbas', 12 )
hero2 = HeroOfUkraine('Viktor', 34, 'on Zaporizhzhya', 37)

hero1.show_heroOfUkraine()
hero2.move_up()
hero1.level_up()
hero2.show_heroOfUkraine()
hero2.set_rank(5)

