;; Wumpus Cave Escape Domain Definition
;; This PDDL domain file defines the actions and predicates for the Wumpus Cave Escape assignment

(define (domain wumpus-escape)
  (:requirements :strips :typing)
  
  (:types
    location - object
    agent - object
    direction - object
    crate - object
  )
  
  (:predicates
    ;; Agent predicates
    (at ?a - agent ?l - location)        ; agent is at location
    (has-arrow ?a - agent)               ; agent has arrow
    (arrow-count ?a - agent ?n - number) ; agent has n arrows
    (escaped ?a - agent)                 ; agent has escaped
    
    ;; Environment predicates
    (adjacent ?l1 ?l2 - location ?d - direction)  ; locations are adjacent in direction
    (wall-at ?l - location)             ; wall is at location
    (wumpus-at ?l - location)            ; wumpus is at location
    (arrow-at ?l - location)             ; arrow is at location
    (crate-at ?c - crate ?l - location)  ; crate is at location
    (pit-at ?l - location)               ; pit is at location
    (pit-filled ?l - location)          ; pit is filled
    (horizontal-turntable ?l - location) ; horizontal turntable at location
    (vertical-turntable ?l - location)   ; vertical turntable at location
    (empty ?l - location)                ; location is empty
    
    ;; Direction predicates
    (north ?d - direction)               ; direction is north
    (south ?d - direction)               ; direction is south
    (east ?d - direction)                ; direction is east
    (west ?d - direction)                ; direction is west
    
    ;; Map boundary predicates
    (off-map ?l - location)              ; location is off the map (goal)
  )
  
  ;; Action: Walk to adjacent location or escape off map
  (:action walk
    :parameters (?a - agent ?from ?to - location ?d - direction)
    :precondition (and 
      (at ?a ?from)
      (adjacent ?from ?to ?d)
      (not (wall-at ?to))
      (not (wumpus-at ?to))
      (not (crate-at ?c ?to))  ; cannot walk into crate
      (not (pit-at ?to))       ; cannot walk into unfilled pit
      (or (not (horizontal-turntable ?to)) (or (east ?d) (west ?d)))  ; horizontal turntable only allows east/west
      (or (not (vertical-turntable ?to)) (or (north ?d) (south ?d)))  ; vertical turntable only allows north/south
    )
    :effect (and 
      (not (at ?a ?from))
      (at ?a ?to)
      (when (arrow-at ?to) (and (has-arrow ?a) (not (arrow-at ?to))))  ; pick up arrow automatically
      (when (off-map ?to) (escaped ?a))  ; escape if walking off map
    )
  )
  
  ;; Action: Push crate to adjacent location
  (:action push
    :parameters (?a - agent ?c - crate ?from ?to ?dest - location ?d - direction)
    :precondition (and 
      (at ?a ?from)
      (crate-at ?c ?to)
      (adjacent ?from ?to ?d)
      (adjacent ?to ?dest ?d)
      (not (wall-at ?dest))
      (not (wumpus-at ?dest))
      (or (empty ?dest) (arrow-at ?dest) (pit-at ?dest))  ; can push into empty, arrow, or pit
    )
    :effect (and 
      (not (at ?a ?from))
      (at ?a ?to)
      (not (crate-at ?c ?to))
      (crate-at ?c ?dest)
      (when (arrow-at ?to) (and (has-arrow ?a) (not (arrow-at ?to))))  ; pick up arrow if on crate location
      (when (pit-at ?dest) (and (pit-filled ?dest) (not (pit-at ?dest))))  ; fill pit with crate
    )
  )
  
  ;; Action: Shoot wumpus in adjacent location
  (:action shoot
    :parameters (?a - agent ?from ?to - location ?d - direction)
    :precondition (and 
      (at ?a ?from)
      (adjacent ?from ?to ?d)
      (has-arrow ?a)
      (wumpus-at ?to)
    )
    :effect (and 
      (not (has-arrow ?a))
      (not (wumpus-at ?to))
    )
  )
  
  ;; Action: Turn turntable 90 degrees
  (:action turn
    :parameters (?a - agent ?from ?to - location ?d - direction)
    :precondition (and 
      (at ?a ?from)
      (adjacent ?from ?to ?d)
      (or (horizontal-turntable ?to) (vertical-turntable ?to))
    )
    :effect (and 
      (when (horizontal-turntable ?to) 
        (and (not (horizontal-turntable ?to)) (vertical-turntable ?to)))
      (when (vertical-turntable ?to) 
        (and (not (vertical-turntable ?to)) (horizontal-turntable ?to)))
    )
  )
) 