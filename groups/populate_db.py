__author__ = 'daniel'
from models import User, Group, Comment

def populate_db():
    get = lambda id: Comment.objects.get(pk=id)
    chad = User.objects.create(username='chad', password='chad', email='chad@chadhall.com')
    brad = User.objects.create(username='brad', password='brad', email='brad@bradhall.com')
    secsi = Group.objects.create(name='SECSI', creator=chad, description='South East Complex Systems Institute')
    secsi.members.add(chad)
    secsi.members.add(brad)
    secsi.save()
    p1 = secsi.pitch_set.create(creator=chad, title='let\'s get a keg.', text="okay bros we " +
                                        "know we can't throw a rager and get all " +
                                        "the tridelts over if we don't have a keg. " +
                                        "let's get a keg.")
    c1 = Comment.add_root(creator=brad, text='fuckkk bro i got so hammered at that ' +
                            'last kegger that i broke my keg tap. im good for the cash '
                            'but since that last dui it\'s hard to get down to liqueur loft.'
                            'can one of you get another tap?', content_object=p1)
    c2 = get(c1.pk).add_child(creator=chad, text='np bro i still have the one from the throwdown at blake\'s.')



if __name__ == '__main__':
    populate_db()