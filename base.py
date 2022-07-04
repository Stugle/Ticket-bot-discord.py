from peewee import *

db = SqliteDatabase('ticket.db')

class Ticket(Model):
    nomer = PrimaryKeyField(unique=True)
    ticket_cnl = IntegerField()
    ticket_aut = IntegerField()
    ticket_type = IntegerField()
    ticket_question = BooleanField(default=False)
    msg_sotr = IntegerField(default=0)
    ticket_status_sotr = BooleanField(default=False)
    ticket_sotr = IntegerField(default=0)
    ticket_close = BooleanField(default=False)

    class Meta:
        database = db
        order_by = "nomer"

class Channel(Model):
    nomer = PrimaryKeyField(unique=True)
    channel = IntegerField()
    work = BooleanField(default=False)

    class Meta:
        database = db
        order_by = "nomer"

class Аdvertising(Model):
    nomer = PrimaryKeyField(unique=True)
    text = CharField()

    class Meta:
        database = db
        order_by = "nomer"
    

