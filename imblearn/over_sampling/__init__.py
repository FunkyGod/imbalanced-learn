"""
The :mod:`imblearn.over_sampling` provides a set of method to
perform over-sampling.
"""

from .adasyn import ADASYN
from .random_over_sampler import RandomOverSampler
from .smote import SMOTE
from .smote import BorderlineSMOTE
from .smote import SVMSMOTE

__all__ = ['ADASYN', 'RandomOverSampler',
           'SMOTE', 'BorderlineSMOTE', 'SVMSMOTE']
