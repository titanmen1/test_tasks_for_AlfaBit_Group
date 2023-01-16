from django.test import TestCase

from task1.models import DeliveryState, LeadState


class TestsDeliveryState(TestCase):
    def setUp(self):
        DeliveryState.objects.create(name='NEW', pk=DeliveryState.STATE_NEW)
        DeliveryState.objects.create(name='ISSUED', pk=DeliveryState.STATE_ISSUED)
        DeliveryState.objects.create(name='DELIVERED', pk=DeliveryState.STATE_DELIVERED)
        DeliveryState.objects.create(name='HANDED', pk=DeliveryState.STATE_HANDED)
        DeliveryState.objects.create(name='REFUSED', pk=DeliveryState.STATE_REFUSED)
        DeliveryState.objects.create(name='PAID_REFUSED', pk=DeliveryState.STATE_PAID_REFUSED)
        DeliveryState.objects.create(name='COMPLETE', pk=DeliveryState.STATE_COMPLETE)
        DeliveryState.objects.create(name='NONE', pk=DeliveryState.STATE_NONE)

    def test_get_new_method(self):
        self.assertEqual(DeliveryState.get_new().pk, 1)
        self.assertEqual(DeliveryState.get_new().name, 'NEW')

    def test_get_issued_method(self):
        self.assertEqual(DeliveryState.get_issued().pk, 2)
        self.assertEqual(DeliveryState.get_issued().name, 'ISSUED')

    def test_get_delivered_method(self):
        self.assertEqual(DeliveryState.get_delivered().pk, 3)
        self.assertEqual(DeliveryState.get_delivered().name, 'DELIVERED')

    def test_get_handed_method(self):
        self.assertEqual(DeliveryState.get_handed().pk, 4)
        self.assertEqual(DeliveryState.get_handed().name, 'HANDED')

    def test_get_refused_method(self):
        self.assertEqual(DeliveryState.get_refused().pk, 5)
        self.assertEqual(DeliveryState.get_refused().name, 'REFUSED')

    def test_get_paid_refused_method(self):
        self.assertEqual(DeliveryState.get_paid_refused().pk, 6)
        self.assertEqual(DeliveryState.get_paid_refused().name, 'PAID_REFUSED')

    def test_get_complete_method(self):
        self.assertEqual(DeliveryState.get_complete().pk, 7)
        self.assertEqual(DeliveryState.get_complete().name, 'COMPLETE')

    def test_get_none_method(self):
        self.assertEqual(DeliveryState.get_none().pk, 8)
        self.assertEqual(DeliveryState.get_none().name, 'NONE')


class TestsLeadState(TestCase):
    def setUp(self):
        LeadState.objects.create(name='NEW', pk=LeadState.STATE_NEW)
        LeadState.objects.create(name='IN_PROGRESS', pk=LeadState.STATE_IN_PROGRESS)
        LeadState.objects.create(name='POSTPONED', pk=LeadState.STATE_POSTPONED)
        LeadState.objects.create(name='DONE', pk=LeadState.STATE_DONE)

    def test_get_new_method(self):
        self.assertEqual(LeadState.get_new().pk, 1)
        self.assertEqual(LeadState.get_new().name, 'NEW')

    def test_get_in_progress_method(self):
        self.assertEqual(LeadState.get_in_progress().pk, 2)
        self.assertEqual(LeadState.get_in_progress().name, 'IN_PROGRESS')

    def test_get_postponed_method(self):
        self.assertEqual(LeadState.get_postponed().pk, 3)
        self.assertEqual(LeadState.get_postponed().name, 'POSTPONED')

    def test_get_done_method(self):
        self.assertEqual(LeadState.get_done().pk, 4)
        self.assertEqual(LeadState.get_done().name, 'DONE')

