# It depends on

A design though where we can maintain the dependency tree based on the input.

For now, I need to plan how we can have this entier system.

I will be keeping my idea on this read me section with further details.



## Requirements

- it should be able to draw mapping between the depends on tree.
- Should we be having options to create the requrements fields.

- Example: Name of the key-objects.
- On depends field: ("dependency object", "priority max 1- 10", "count") <-- should be able to color of each objects and thikness to represent these multi dimention.

- As from the same objects it should be thinking about, who/what are the downstream consumer of this object... its should be able to generate automatically from this.



### When: 
A depends on B and C; B depends on D

R={(A,B),(A,C),(B,D)}