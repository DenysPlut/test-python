from heroofukraine import *

#----------------------main------------------------------------------

hero1 = HeroOfUkraine('Roman',5, 'on Donbass', 12 )
hero2 = HeroOfUkraine('Viktor', 14, 'on Zaporizhzhya', 37)

hero1.show_heroOfUkraine()
hero2.move_up()
hero1.rank_up()
hero1.set_rank(15)
hero2.show_heroOfUkraine()
