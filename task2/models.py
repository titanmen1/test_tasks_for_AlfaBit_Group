from django.db import models
from django_fsm import transition, FSMKeyField


class LeadState(models.Model):
    # pk экземпляров модели

    STATE_NEW = 1  # Новый
    STATE_IN_PROGRESS = 2  # В работе
    STATE_POSTPONED = 3  # Приостановлен
    STATE_DONE = 4  # Завершен

    STATE_ENUM = (
        (STATE_NEW, "new"),
        (STATE_IN_PROGRESS, "in_progres"),
        (STATE_POSTPONED, "postponed"),
        (STATE_DONE, "done"),
    )

    name = models.CharField(
        u"Название",
        max_length=50,
        unique=True,
    )


class Lead(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name=u"Имя",
    )

    # Здесь я использую библиотеку django_fsm, которая отвечает за строгие переходы между статусами и так же есть
    # возможность добавлять различную логику при смене статуса
    state = FSMKeyField(
        LeadState,
        on_delete=models.PROTECT,
        default=LeadState.STATE_NEW,
        verbose_name=u"Состояние",
        protected=True
    )

    @transition(
        field=state,
        source=[LeadState.STATE_NEW, LeadState.STATE_POSTPONED],
        target=LeadState.STATE_IN_PROGRESS
    )
    def state_in_progress(self) -> None:
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
        pass

    @transition(field=state, source=LeadState.STATE_IN_PROGRESS, target=LeadState.STATE_POSTPONED)
    def state_postponed(self) -> None:
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
        pass

    @transition(
        field=state,
        source=[LeadState.STATE_IN_PROGRESS, LeadState.STATE_POSTPONED],
        target=LeadState.STATE_DONE
    )
    def state_done(self) -> None:
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
        pass
