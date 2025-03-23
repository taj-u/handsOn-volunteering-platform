# backend/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):        
    SKILL_CHOICES = (
        ('teaching', 'Teaching'),
        ('medical', 'Medical'),
        ('construction', 'Construction'),
        ('tech', 'Technology'),
    )
    CAUSE_CHOICES = (
        ('environment', 'Environment'),
        ('education', 'Education'),
        ('healthcare', 'Healthcare'),
        ('poverty', 'Poverty Relief'),
    )
    
    bio = models.TextField(_('bio'), blank=True)
    skills = models.CharField(
        _('skills'),
        max_length=20,
        default=list,
        help_text=_("List of user's skills"),
        choices=SKILL_CHOICES,
        # blank=True,
        # null=True
        
    )
    causes = models.CharField(
        _('causes'),
        max_length=20,
        default=list,
        help_text=_("Causes user supports"),
        choices=CAUSE_CHOICES,
        # null=True,
        # blank=True
    )
    
    volunteer_hours = models.PositiveIntegerField(
        _('volunteer hours'),
        default=0
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')