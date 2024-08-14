# Event Storming
We started to know more about the project by considering that our CTO is the domain expert and we are the team that is going to implement the project. So we started asking questions about the project and the domaing expert concerns.

## Specifying the project

At first we came to these details:
![Initial thoughts](../media/event_storming_1.jpg)

What we came at this step was:
- what operations are needed
- what scenarios exists
- who are the end-users
- what parts of the system already exists and what should be developed

## Event Stormig
Then with the help of the domain expert, domain events extracted:
![Domain Events](../media/event_storming_2.jpg)
![Domain Events](../media/event_storming_3.jpg)

## Project Decomposition
Next the overal project composition shaped out
![Project Decomposition](../media/event_storming_4.jpg)


## Bounded Context Connections
In this stpe the connection of bcs and their types (core, supporting, generic) were elicitated.
![](../media/event_storming_5.jpg)
![](../media/event_storming_6.jpg)
![](../media/event_storming_7.jpg)

## Clean Architeture Mapping
Then a the client aggregate in resource management bc was mapped to clean architecture as an example.
![](../media/event_storming_8.jpg)