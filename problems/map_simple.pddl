(define (problem wumpus-cave-escape)
  (:domain wumpus-escape)
  
  (:objects
    loc_-1_-1 - location
    loc_-1_0 - location
    loc_-1_1 - location
    loc_-1_2 - location
    loc_-1_3 - location
    loc_0_-1 - location
    loc_0_0 - location
    loc_0_1 - location
    loc_0_2 - location
    loc_0_3 - location
    loc_1_-1 - location
    loc_1_0 - location
    loc_1_1 - location
    loc_1_2 - location
    loc_1_3 - location
    loc_2_-1 - location
    loc_2_0 - location
    loc_2_1 - location
    loc_2_2 - location
    loc_2_3 - location
    loc_3_-1 - location
    loc_3_0 - location
    loc_3_1 - location
    loc_3_2 - location
    loc_3_3 - location
    agent - agent
    north - direction
    south - direction
    east - direction
    west - direction
  )
  
  (:init
    (at agent loc_1_1)
    (north north)
    (south south)
    (east east)
    (west west)
    (wall-at loc_0_0)
    (wall-at loc_0_1)
    (wall-at loc_0_2)
    (wall-at loc_1_0)
    (wall-at loc_2_0)
    (wall-at loc_2_1)
    (wall-at loc_2_2)
    (empty loc_1_1)
    (empty loc_1_2)
    (empty loc_2_3)
    (off-map loc_-1_-1)
    (off-map loc_-1_0)
    (off-map loc_-1_1)
    (off-map loc_-1_2)
    (off-map loc_-1_3)
    (off-map loc_0_-1)
    (off-map loc_0_3)
    (off-map loc_1_-1)
    (off-map loc_1_3)
    (off-map loc_2_-1)
    (off-map loc_2_3)
    (off-map loc_3_-1)
    (off-map loc_3_0)
    (off-map loc_3_1)
    (off-map loc_3_2)
    (off-map loc_3_3)
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
    (adjacent loc_3_-1 loc_2_-1 north)
    (adjacent loc_3_-1 loc_3_0 east)
    (adjacent loc_3_0 loc_2_0 north)
    (adjacent loc_3_0 loc_3_-1 west)
    (adjacent loc_3_0 loc_3_1 east)
    (adjacent loc_3_1 loc_2_1 north)
    (adjacent loc_3_1 loc_3_0 west)
    (adjacent loc_3_1 loc_3_2 east)
    (adjacent loc_3_2 loc_2_2 north)
    (adjacent loc_3_2 loc_3_1 west)
    (adjacent loc_3_2 loc_3_3 east)
    (adjacent loc_3_3 loc_2_3 north)
    (adjacent loc_3_3 loc_3_2 west)
  )
  
  (:goal
    (escaped agent)
  )
)
