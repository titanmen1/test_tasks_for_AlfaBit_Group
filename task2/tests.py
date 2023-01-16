import django_fsm
from django.test import TestCase
from django_fsm import can_proceed

from task2.models import Lead, LeadState


class TestsLeadFSM(TestCase):
    def setUp(self):
        LeadState.objects.create(name="NEW", pk=LeadState.STATE_NEW)
        LeadState.objects.create(name="IN_PROGRESS", pk=LeadState.STATE_IN_PROGRESS)
        LeadState.objects.create(name="POSTPONED", pk=LeadState.STATE_POSTPONED)
        LeadState.objects.create(name="DONE", pk=LeadState.STATE_DONE)
        self.model = Lead.objects.create(name="test")

    def test_state_in_progress(self):
        self.assertEqual(self.model.state, 1)
        self.assertTrue(can_proceed(self.model.state_in_progress))
        self.model.state_in_progress()
        self.assertEqual(self.model.state, 2)

    def test_state_postponed(self):
        self.assertEqual(self.model.state, 1)
        self.model.state_in_progress()
        self.assertEqual(self.model.state, 2)

        self.assertTrue(can_proceed(self.model.state_postponed))
        self.model.state_postponed()
        self.assertEqual(self.model.state, 3)

    def test_state_done(self):
        self.assertEqual(self.model.state, 1)
        self.model.state_in_progress()
        self.assertEqual(self.model.state, 2)

        self.assertTrue(can_proceed(self.model.state_done))
        self.model.state_done()
        self.assertEqual(self.model.state, 4)

    def test_state_in_progress_from_state_postponed(self):
        self.assertEqual(self.model.state, 1)
        self.model.state_in_progress()
        self.model.state_postponed()
        self.assertEqual(self.model.state, 3)

        self.assertTrue(can_proceed(self.model.state_in_progress))
        self.model.state_in_progress()
        self.assertEqual(self.model.state, 2)

    def test_state_done_from_state_postponed(self):
        self.assertEqual(self.model.state, 1)
        self.model.state_in_progress()
        self.model.state_postponed()
        self.assertEqual(self.model.state, 3)

        self.assertTrue(can_proceed(self.model.state_done))
        self.model.state_done()
        self.assertEqual(self.model.state, 4)

    def test_wrong_way_for_changing_state(self):
        self.assertEqual(self.model.state, 1)
        self.assertFalse(can_proceed(self.model.state_done))
        self.assertFalse(can_proceed(self.model.state_postponed))

        with self.assertRaises(django_fsm.TransitionNotAllowed):
            self.model.state_done()
            self.model.state_postponed()

        self.model.state_in_progress()
        self.assertFalse(can_proceed(self.model.state_in_progress))

        with self.assertRaises(django_fsm.TransitionNotAllowed):
            self.model.state_in_progress()

        self.model.state_done()
        self.assertFalse(can_proceed(self.model.state_in_progress))
        self.assertFalse(can_proceed(self.model.state_postponed))
        self.assertFalse(can_proceed(self.model.state_done))

        with self.assertRaises(django_fsm.TransitionNotAllowed):
            self.model.state_in_progress()
            self.model.state_postponed()
            self.model.state_done()
