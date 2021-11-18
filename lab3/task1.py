from Event import Event
from EventsJSON import EventsJSON
from Ticket import *

if __name__ == '__main__':
    json1 = EventsJSON('events')
    json1.add_obj(Event(1, 'Event1', '01.01.2021', 4, 125))
    json1.add_obj(Event(2, 'Event2', '01.02.2021', 125, 1453))
    event3 = Event(3, 'Event3', '02.05.2021', 184, 139)
    json1.add_obj(event3)
    json1.del_obj(event3)
    ticket1 = Ticket.construct_by_id(1)
    print(ticket1)
    ticket2 = AdvanceTicket.construct_by_id(1)
    ticket2.return_ticket()
    print(StudentTicket.construct_by_id(1))
    print(LateTicket.construct_by_id(1))
    print(AdvanceTicket.construct_by_id(2))
