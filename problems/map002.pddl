(define (problem wumpus-cave-escape)
  (:domain wumpus-escape)
  
  (:objects
    loc_-1_-1 - location
    loc_-1_0 - location
    loc_-1_1 - location
    loc_-1_2 - location
    loc_-1_3 - location
    loc_-1_4 - location
    loc_-1_5 - location
    loc_-1_6 - location
    loc_0_-1 - location
    loc_0_0 - location
    loc_0_1 - location
    loc_0_2 - location
    loc_0_3 - location
    loc_0_4 - location
    loc_0_5 - location
    loc_0_6 - location
    loc_1_-1 - location
    loc_1_0 - location
    loc_1_1 - location
    loc_1_2 - location
    loc_1_3 - location
    loc_1_4 - location
    loc_1_5 - location
    loc_1_6 - location
    loc_2_-1 - location
    loc_2_0 - location
    loc_2_1 - location
    loc_2_2 - location
    loc_2_3 - location
    loc_2_4 - location
    loc_2_5 - location
    loc_2_6 - location
    loc_3_-1 - location
    loc_3_0 - location
    loc_3_1 - location
    loc_3_2 - location
    loc_3_3 - location
    loc_3_4 - location
    loc_3_5 - location
    loc_3_6 - location
    loc_4_-1 - location
    loc_4_0 - location
    loc_4_1 - location
    loc_4_2 - location
    loc_4_3 - location
    loc_4_4 - location
    loc_4_5 - location
    loc_4_6 - location
    loc_5_-1 - location
    loc_5_0 - location
    loc_5_1 - location
    loc_5_2 - location
    loc_5_3 - location
    loc_5_4 - location
    loc_5_5 - location
    loc_5_6 - location
    loc_6_-1 - location
    loc_6_0 - location
    loc_6_1 - location
    loc_6_2 - location
    loc_6_3 - location
    loc_6_4 - location
    loc_6_5 - location
    loc_6_6 - location
    agent - agent
    north - direction
    south - direction
    east - direction
    west - direction
  )
  
  (:init
    (at agent loc_3_2)
    (north north)
    (south south)
    (east east)
    (west west)
    (wall-at loc_0_0)
    (wall-at loc_0_1)
    (wall-at loc_0_2)
    (wall-at loc_0_3)
    (wall-at loc_0_4)
    (wall-at loc_0_5)
    (wall-at loc_1_0)
    (wall-at loc_1_5)
    (wall-at loc_2_0)
    (wall-at loc_2_5)
    (wall-at loc_3_0)
    (wall-at loc_3_5)
    (wall-at loc_4_0)
    (wall-at loc_4_5)
    (wall-at loc_5_0)
    (wall-at loc_5_1)
    (wall-at loc_5_2)
    (wall-at loc_5_3)
    (wall-at loc_5_4)
    (wall-at loc_5_5)
    (wumpus-at loc_2_3)
    (arrow-at loc_1_2)
    (empty loc_1_1)
    (empty loc_1_3)
    (empty loc_1_4)
    (empty loc_2_1)
    (empty loc_2_2)
    (empty loc_2_4)
    (empty loc_3_1)
    (empty loc_3_2)
    (empty loc_3_3)
    (empty loc_3_4)
    (empty loc_4_1)
    (empty loc_4_2)
    (empty loc_4_3)
    (empty loc_4_4)
    (empty loc_5_6)
    (off-map loc_-1_-1)
    (off-map loc_-1_0)
    (off-map loc_-1_1)
    (off-map loc_-1_2)
    (off-map loc_-1_3)
    (off-map loc_-1_4)
    (off-map loc_-1_5)
    (off-map loc_-1_6)
    (off-map loc_0_-1)
    (off-map loc_0_6)
    (off-map loc_1_-1)
    (off-map loc_1_6)
    (off-map loc_2_-1)
    (off-map loc_2_6)
    (off-map loc_3_-1)
    (off-map loc_3_6)
    (off-map loc_4_-1)
    (off-map loc_4_6)
    (off-map loc_5_-1)
    (off-map loc_5_6)
    (off-map loc_6_-1)
    (off-map loc_6_0)
    (off-map loc_6_1)
    (off-map loc_6_2)
    (off-map loc_6_3)
    (off-map loc_6_4)
    (off-map loc_6_5)
    (off-map loc_6_6)
    (adjacent loc_-1_-1 loc_0_-1 south)
    (adjacent loc_-1_-1 loc_-1_0 east)
    (adjacent loc_-1_0 loc_0_0 south)
    (adjacent loc_-1_0 loc_-1_-1 west)
    (adjacent loc_-1_0 loc_-1_1 east)
    (adjacent loc_-1_1 loc_0_1 south)
    (adjacent loc_-1_1 loc_-1_0 west)
    (adjacent loc_-1_1 loc_-1_2 east)
    (adjacent loc_-1_2 loc_0_2 south)
    (adjacent loc_-1_2 loc_-1_1 west)
    (adjacent loc_-1_2 loc_-1_3 east)
    (adjacent loc_-1_3 loc_0_3 south)
    (adjacent loc_-1_3 loc_-1_2 west)
    (adjacent loc_-1_3 loc_-1_4 east)
    (adjacent loc_-1_4 loc_0_4 south)
    (adjacent loc_-1_4 loc_-1_3 west)
    (adjacent loc_-1_4 loc_-1_5 east)
    (adjacent loc_-1_5 loc_0_5 south)
    (adjacent loc_-1_5 loc_-1_4 west)
    (adjacent loc_-1_5 loc_-1_6 east)
    (adjacent loc_-1_6 loc_0_6 south)
    (adjacent loc_-1_6 loc_-1_5 west)
    (adjacent loc_0_-1 loc_-1_-1 north)
    (adjacent loc_0_-1 loc_1_-1 south)
    (adjacent loc_0_-1 loc_0_0 east)
    (adjacent loc_0_0 loc_-1_0 north)
    (adjacent loc_0_0 loc_1_0 south)
    (adjacent loc_0_0 loc_0_-1 west)
    (adjacent loc_0_0 loc_0_1 east)
    (adjacent loc_0_1 loc_-1_1 north)
    (adjacent loc_0_1 loc_1_1 south)
    (adjacent loc_0_1 loc_0_0 west)
    (adjacent loc_0_1 loc_0_2 east)
    (adjacent loc_0_2 loc_-1_2 north)
    (adjacent loc_0_2 loc_1_2 south)
    (adjacent loc_0_2 loc_0_1 west)
    (adjacent loc_0_2 loc_0_3 east)
    (adjacent loc_0_3 loc_-1_3 north)
    (adjacent loc_0_3 loc_1_3 south)
    (adjacent loc_0_3 loc_0_2 west)
    (adjacent loc_0_3 loc_0_4 east)
    (adjacent loc_0_4 loc_-1_4 north)
    (adjacent loc_0_4 loc_1_4 south)
    (adjacent loc_0_4 loc_0_3 west)
    (adjacent loc_0_4 loc_0_5 east)
    (adjacent loc_0_5 loc_-1_5 north)
    (adjacent loc_0_5 loc_1_5 south)
    (adjacent loc_0_5 loc_0_4 west)
    (adjacent loc_0_5 loc_0_6 east)
    (adjacent loc_0_6 loc_-1_6 north)
    (adjacent loc_0_6 loc_1_6 south)
    (adjacent loc_0_6 loc_0_5 west)
    (adjacent loc_1_-1 loc_0_-1 north)
    (adjacent loc_1_-1 loc_2_-1 south)
    (adjacent loc_1_-1 loc_1_0 east)
    (adjacent loc_1_0 loc_0_0 north)
    (adjacent loc_1_0 loc_2_0 south)
    (adjacent loc_1_0 loc_1_-1 west)
    (adjacent loc_1_0 loc_1_1 east)
    (adjacent loc_1_1 loc_0_1 north)
    (adjacent loc_1_1 loc_2_1 south)
    (adjacent loc_1_1 loc_1_0 west)
    (adjacent loc_1_1 loc_1_2 east)
    (adjacent loc_1_2 loc_0_2 north)
    (adjacent loc_1_2 loc_2_2 south)
    (adjacent loc_1_2 loc_1_1 west)
    (adjacent loc_1_2 loc_1_3 east)
    (adjacent loc_1_3 loc_0_3 north)
    (adjacent loc_1_3 loc_2_3 south)
    (adjacent loc_1_3 loc_1_2 west)
    (adjacent loc_1_3 loc_1_4 east)
    (adjacent loc_1_4 loc_0_4 north)
    (adjacent loc_1_4 loc_2_4 south)
    (adjacent loc_1_4 loc_1_3 west)
    (adjacent loc_1_4 loc_1_5 east)
    (adjacent loc_1_5 loc_0_5 north)
    (adjacent loc_1_5 loc_2_5 south)
    (adjacent loc_1_5 loc_1_4 west)
    (adjacent loc_1_5 loc_1_6 east)
    (adjacent loc_1_6 loc_0_6 north)
    (adjacent loc_1_6 loc_2_6 south)
    (adjacent loc_1_6 loc_1_5 west)
    (adjacent loc_2_-1 loc_1_-1 north)
    (adjacent loc_2_-1 loc_3_-1 south)
    (adjacent loc_2_-1 loc_2_0 east)
    (adjacent loc_2_0 loc_1_0 north)
    (adjacent loc_2_0 loc_3_0 south)
    (adjacent loc_2_0 loc_2_-1 west)
    (adjacent loc_2_0 loc_2_1 east)
    (adjacent loc_2_1 loc_1_1 north)
    (adjacent loc_2_1 loc_3_1 south)
    (adjacent loc_2_1 loc_2_0 west)
    (adjacent loc_2_1 loc_2_2 east)
    (adjacent loc_2_2 loc_1_2 north)
    (adjacent loc_2_2 loc_3_2 south)
    (adjacent loc_2_2 loc_2_1 west)
    (adjacent loc_2_2 loc_2_3 east)
    (adjacent loc_2_3 loc_1_3 north)
    (adjacent loc_2_3 loc_3_3 south)
    (adjacent loc_2_3 loc_2_2 west)
    (adjacent loc_2_3 loc_2_4 east)
    (adjacent loc_2_4 loc_1_4 north)
    (adjacent loc_2_4 loc_3_4 south)
    (adjacent loc_2_4 loc_2_3 west)
    (adjacent loc_2_4 loc_2_5 east)
    (adjacent loc_2_5 loc_1_5 north)
    (adjacent loc_2_5 loc_3_5 south)
    (adjacent loc_2_5 loc_2_4 west)
    (adjacent loc_2_5 loc_2_6 east)
    (adjacent loc_2_6 loc_1_6 north)
    (adjacent loc_2_6 loc_3_6 south)
    (adjacent loc_2_6 loc_2_5 west)
    (adjacent loc_3_-1 loc_2_-1 north)
    (adjacent loc_3_-1 loc_4_-1 south)
    (adjacent loc_3_-1 loc_3_0 east)
    (adjacent loc_3_0 loc_2_0 north)
    (adjacent loc_3_0 loc_4_0 south)
    (adjacent loc_3_0 loc_3_-1 west)
    (adjacent loc_3_0 loc_3_1 east)
    (adjacent loc_3_1 loc_2_1 north)
    (adjacent loc_3_1 loc_4_1 south)
    (adjacent loc_3_1 loc_3_0 west)
    (adjacent loc_3_1 loc_3_2 east)
    (adjacent loc_3_2 loc_2_2 north)
    (adjacent loc_3_2 loc_4_2 south)
    (adjacent loc_3_2 loc_3_1 west)
    (adjacent loc_3_2 loc_3_3 east)
    (adjacent loc_3_3 loc_2_3 north)
    (adjacent loc_3_3 loc_4_3 south)
    (adjacent loc_3_3 loc_3_2 west)
    (adjacent loc_3_3 loc_3_4 east)
    (adjacent loc_3_4 loc_2_4 north)
    (adjacent loc_3_4 loc_4_4 south)
    (adjacent loc_3_4 loc_3_3 west)
    (adjacent loc_3_4 loc_3_5 east)
    (adjacent loc_3_5 loc_2_5 north)
    (adjacent loc_3_5 loc_4_5 south)
    (adjacent loc_3_5 loc_3_4 west)
    (adjacent loc_3_5 loc_3_6 east)
    (adjacent loc_3_6 loc_2_6 north)
    (adjacent loc_3_6 loc_4_6 south)
    (adjacent loc_3_6 loc_3_5 west)
    (adjacent loc_4_-1 loc_3_-1 north)
    (adjacent loc_4_-1 loc_5_-1 south)
    (adjacent loc_4_-1 loc_4_0 east)
    (adjacent loc_4_0 loc_3_0 north)
    (adjacent loc_4_0 loc_5_0 south)
    (adjacent loc_4_0 loc_4_-1 west)
    (adjacent loc_4_0 loc_4_1 east)
    (adjacent loc_4_1 loc_3_1 north)
    (adjacent loc_4_1 loc_5_1 south)
    (adjacent loc_4_1 loc_4_0 west)
    (adjacent loc_4_1 loc_4_2 east)
    (adjacent loc_4_2 loc_3_2 north)
    (adjacent loc_4_2 loc_5_2 south)
    (adjacent loc_4_2 loc_4_1 west)
    (adjacent loc_4_2 loc_4_3 east)
    (adjacent loc_4_3 loc_3_3 north)
    (adjacent loc_4_3 loc_5_3 south)
    (adjacent loc_4_3 loc_4_2 west)
    (adjacent loc_4_3 loc_4_4 east)
    (adjacent loc_4_4 loc_3_4 north)
    (adjacent loc_4_4 loc_5_4 south)
    (adjacent loc_4_4 loc_4_3 west)
    (adjacent loc_4_4 loc_4_5 east)
    (adjacent loc_4_5 loc_3_5 north)
    (adjacent loc_4_5 loc_5_5 south)
    (adjacent loc_4_5 loc_4_4 west)
    (adjacent loc_4_5 loc_4_6 east)
    (adjacent loc_4_6 loc_3_6 north)
    (adjacent loc_4_6 loc_5_6 south)
    (adjacent loc_4_6 loc_4_5 west)
    (adjacent loc_5_-1 loc_4_-1 north)
    (adjacent loc_5_-1 loc_6_-1 south)
    (adjacent loc_5_-1 loc_5_0 east)
    (adjacent loc_5_0 loc_4_0 north)
    (adjacent loc_5_0 loc_6_0 south)
    (adjacent loc_5_0 loc_5_-1 west)
    (adjacent loc_5_0 loc_5_1 east)
    (adjacent loc_5_1 loc_4_1 north)
    (adjacent loc_5_1 loc_6_1 south)
    (adjacent loc_5_1 loc_5_0 west)
    (adjacent loc_5_1 loc_5_2 east)
    (adjacent loc_5_2 loc_4_2 north)
    (adjacent loc_5_2 loc_6_2 south)
    (adjacent loc_5_2 loc_5_1 west)
    (adjacent loc_5_2 loc_5_3 east)
    (adjacent loc_5_3 loc_4_3 north)
    (adjacent loc_5_3 loc_6_3 south)
    (adjacent loc_5_3 loc_5_2 west)
    (adjacent loc_5_3 loc_5_4 east)
    (adjacent loc_5_4 loc_4_4 north)
    (adjacent loc_5_4 loc_6_4 south)
    (adjacent loc_5_4 loc_5_3 west)
    (adjacent loc_5_4 loc_5_5 east)
    (adjacent loc_5_5 loc_4_5 north)
    (adjacent loc_5_5 loc_6_5 south)
    (adjacent loc_5_5 loc_5_4 west)
    (adjacent loc_5_5 loc_5_6 east)
    (adjacent loc_5_6 loc_4_6 north)
    (adjacent loc_5_6 loc_6_6 south)
    (adjacent loc_5_6 loc_5_5 west)
    (adjacent loc_6_-1 loc_5_-1 north)
    (adjacent loc_6_-1 loc_6_0 east)
    (adjacent loc_6_0 loc_5_0 north)
    (adjacent loc_6_0 loc_6_-1 west)
    (adjacent loc_6_0 loc_6_1 east)
    (adjacent loc_6_1 loc_5_1 north)
    (adjacent loc_6_1 loc_6_0 west)
    (adjacent loc_6_1 loc_6_2 east)
    (adjacent loc_6_2 loc_5_2 north)
    (adjacent loc_6_2 loc_6_1 west)
    (adjacent loc_6_2 loc_6_3 east)
    (adjacent loc_6_3 loc_5_3 north)
    (adjacent loc_6_3 loc_6_2 west)
    (adjacent loc_6_3 loc_6_4 east)
    (adjacent loc_6_4 loc_5_4 north)
    (adjacent loc_6_4 loc_6_3 west)
    (adjacent loc_6_4 loc_6_5 east)
    (adjacent loc_6_5 loc_5_5 north)
    (adjacent loc_6_5 loc_6_4 west)
    (adjacent loc_6_5 loc_6_6 east)
    (adjacent loc_6_6 loc_5_6 north)
    (adjacent loc_6_6 loc_6_5 west)
  )
  
  (:goal
    (escaped agent)
  )
)
