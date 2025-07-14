### Features:
1. Create an event
an event has the following optional fields. Note: at least 1 is required.
Attendees
Theme
Time
Place
confirmed? Y/N

The event hits an agent, which first builds current state of structured data based on client input. It's mission is to then populate the missing parameters. Once all are filled, it will reply back to the user with the proposal. If accepted, it will be booked.

### To Do:

- [ ] bootstrap an orchestrator agent with langGraph and A2A
    * invokes agents, if needed, to fill in missing state

- [ ] bootstrap a people agent
    * friend graph which includes friend's interests and location
- [ ] bootstrap a booking agent
    * requires friends agent to be run first
    * search friends calendar for optimal slot
    * can book invitation once accepted by user.