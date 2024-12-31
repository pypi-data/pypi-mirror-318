from documente_shared.domain.base_enum import BaseEnum


class DocumentProcessStatus(BaseEnum):
    PENDING = 'PENDING'
    ENQUEUED = 'ENQUEUED'
    PROCESSING = 'PROCESSING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    DELETED = 'DELETED'
    CANCELLED = 'CANCELLED'


class DocumentProcessCategory(BaseEnum):
    CIRCULAR = 'CIRCULAR'
    DESGRAVAMEN = 'DESGRAVAMEN'

    @property
    def is_circular(self):
        return self == DocumentProcessCategory.CIRCULAR

    @property
    def is_desgravamen(self):
        return self == DocumentProcessCategory.DESGRAVAMEN


class DocumentProcessSubCategory(BaseEnum):
    # Circulares
    CC_COMBINADA = 'CC_COMBINADA'
    CC_NORMATIVA = 'CC_NORMATIVA'
    CC_INFORMATIVA = 'CC_INFORMATIVA'
    CC_RETENCION_SUSPENSION_REMISION = 'CC_RETENCION_SUSPENSION_REMISION'

    # Desgravamenes
    DS_CREDISEGUROS = 'DS_CREDISEGUROS'

